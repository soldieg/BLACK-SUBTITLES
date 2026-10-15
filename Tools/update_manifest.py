#!/usr/bin/env python3
"""Refresh repository localization inventory metadata and nested path tree."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "manifest.json"
CHECKSUM_PATH = ROOT / "SOURCE-SHA256SUMS.txt"
ASSET_ROOTS = ("GitHubs/", "Launcher/", "Localization/", "Subtitles/", "Test/")
CHECKSUM_EXTENSIONS = {".bin", ".csv", ".json", ".jsonl", ".srt", ".txt"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def repository_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
    )
    paths = result.stdout.decode("utf-8").split("\0")
    return sorted(
        path
        for path in paths
        if path
        and path.startswith(ASSET_ROOTS)
        and PurePosixPath(path).name != ".gitkeep"
        and (ROOT / Path(*PurePosixPath(path).parts)).is_file()
    )


def asset_records(manifest: dict[str, Any]) -> list[tuple[str, str | None, dict[str, Any]]]:
    records: list[tuple[str, str | None, dict[str, Any]]] = []
    for group_name in ("locales", "test_assets_by_locale", "repository_assets_by_locale"):
        group = manifest.get(group_name, {})
        for locale, locale_data in group.items():
            for record in locale_data.get("files", []) if isinstance(locale_data, dict) else locale_data:
                if isinstance(record, dict) and isinstance(record.get("source_path"), str):
                    records.append((record["source_path"], locale, record))

    for group_name in ("test_documents", "excluded_assets"):
        for record in manifest.get(group_name, []):
            if isinstance(record, dict) and isinstance(record.get("source_path"), str):
                records.append((record["source_path"], record.get("locale"), record))
    return records


def make_tree(files: list[str], records: list[tuple[str, str | None, dict[str, Any]]]) -> tuple[dict[str, Any], list[str]]:
    by_path: dict[str, list[tuple[str | None, dict[str, Any]]]] = {}
    for path, locale, record in records:
        by_path.setdefault(path, []).append((locale, record))

    tree: dict[str, Any] = {"type": "directory", "children": {}}
    unregistered: list[str] = []
    for path in files:
        file_path = ROOT / Path(*PurePosixPath(path).parts)
        references = by_path.get(path, [])
        if not references:
            unregistered.append(path)
        leaf: dict[str, Any] = {
            "type": "file",
            "status": "listed" if references else "not_in_locale_catalog",
            "source_path": path,
            "size_bytes": file_path.stat().st_size,
            "sha256": sha256(file_path),
        }
        if references:
            def values(key: str) -> list[Any]:
                return sorted({record[key] for _, record in references if record.get(key) is not None})

            locales = sorted({locale for locale, _ in references if locale})
            for key, value in (
                ("locales", locales),
                ("categories", values("category")),
                ("asset_types", values("asset_type")),
                ("destination_paths", values("destination_path")),
                ("formats", values("format")),
            ):
                if value:
                    leaf[key] = value
            if any(record.get("test_only") for _, record in references):
                leaf["test_only"] = True

        node = tree["children"]
        parts = PurePosixPath(path).parts
        for directory in parts[:-1]:
            child = node.setdefault(directory, {"type": "directory", "children": {}})
            node = child["children"]
        node[parts[-1]] = leaf
    return tree, unregistered


def render_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def expected_outputs() -> tuple[str, str, list[str], int]:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    records = asset_records(manifest)
    files = repository_files()
    known_paths = set(files)
    missing = sorted({path for path, _, _ in records if path not in known_paths})
    if missing:
        raise ValueError("Manifest source_path does not match a repository file (case-sensitive):\n" + "\n".join(missing))

    for path, _, record in records:
        source = ROOT / Path(*PurePosixPath(path).parts)
        record["size_bytes"] = source.stat().st_size
        record["sha256"] = sha256(source)

    tree, unregistered = make_tree(files, records)
    manifest["directory_tree"] = tree

    checksum_lines = []
    for relative in files:
        source = ROOT / Path(*PurePosixPath(relative).parts)
        if source.suffix.lower() in CHECKSUM_EXTENSIONS:
            checksum_lines.append(f"{sha256(source)}  {relative}")
    checksums = "\n".join(checksum_lines) + "\n"
    return render_json(manifest), checksums, unregistered, len(files)


def write_or_check(path: Path, expected: str, check: bool) -> bool:
    actual = path.read_text(encoding="utf-8") if path.exists() else ""
    if actual == expected:
        return False
    if check:
        return True
    path.write_text(expected, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Update the folder-based localization manifest and file checksums.")
    parser.add_argument("--check", action="store_true", help="fail if generated metadata is out of date")
    args = parser.parse_args()

    try:
        manifest_text, checksums_text, unregistered, file_count = expected_outputs()
    except (OSError, ValueError, subprocess.CalledProcessError, json.JSONDecodeError) as error:
        print(f"Manifest update failed: {error}", file=sys.stderr)
        return 1

    manifest_changed = write_or_check(MANIFEST_PATH, manifest_text, args.check)
    checksums_changed = write_or_check(CHECKSUM_PATH, checksums_text, args.check)
    dirty = manifest_changed or checksums_changed

    mode = "out of date" if args.check and dirty else "updated" if dirty else "already current"
    print(f"Manifest/checksums {mode}. Indexed {file_count} files in nested repository folders.")
    if unregistered:
        print(f"Files not yet assigned to a locale download list: {len(unregistered)}")
        for path in unregistered:
            print(f"  - {path}")
    else:
        print("All indexed files are assigned in a locale, test, or repository asset list.")

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with Path(summary_path).open("a", encoding="utf-8") as summary:
            summary.write("## Localization manifest sync\n\n")
            summary.write(f"- Metadata: **{mode}**\n- Files in nested tree: **{file_count}**\n")
            summary.write(f"- Files not assigned to a locale download list: **{len(unregistered)}**\n")
            for path in unregistered:
                summary.write(f"  - `{path}`\n")

    return 1 if args.check and dirty else 0


if __name__ == "__main__":
    raise SystemExit(main())
