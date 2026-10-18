# BLACK subtitles and localization data

> [!IMPORTANT]
> **Found an error in any translation?** [Open an Issue](https://github.com/soldieg/BLACK-SUBTITLES/issues/new) so it can be reviewed and corrected.

Reusable subtitle and localization source data for **BLACK (2006)**. This repository is not affiliated with Electronic Arts.

## Repository layout

- `Subtitles/`: the 72 primary cutscene SRTs, grouped by locale (`en`, `pt-BR`, `es`, `fr`, `de`, `it`, `id`, `ru`). These are the primary caption tracks, not the experimental audio-sync outputs.
- `Localization/Menu/`: original game menu catalogs and source notes. Translation rows keep only their identifier and text; Indonesian source records are retained without invented IDs.
- `Localization/Fonts/`: runtime font dependencies and their locale-specific layout (`de`, `id`, `pt-BR`, `ru`). PT-BR `Small.bin` and `Big.bin` match the standard game fonts by SHA-256.
- `Launcher/`: 292 keyed launcher strings per available locale.
- `Test/Audio-Sync/`: separate ASR candidate and retimed candidate sets. They are experimental and must not replace primary subtitle files without review.
- `Test/Gameplay-Audio-Transcription/`: current 3,591-row-per-locale analysis and the earlier 3,196-row snapshot. These are research catalogs, not runtime-ready subtitles.
- `GitHubs/BLACK-XBERecomp/`: translations specific to the Recomp menu plus mirrors of the available original game-menu catalogs for that fork.
- `Tools/`: helper scripts.
- `manifest.json`: locale-indexed inventory with file paths, sizes, SHA-256 hashes, and explicit test-only assets.
- `SOURCE-SHA256SUMS.txt`: checksums for source text and subtitle files.

## Language coverage and review state

Primary cutscene subtitles have nine tracks per each of eight locales (72 SRTs total). English tracks are under `Subtitles/en/`. Per-locale READMEs document editorial work and remaining audio/native-speaker review; AI review is not human confirmation.

Original game-menu catalogs are available in English, Portuguese, Spanish, French, German, Italian, and Indonesian. The XBERecomp Russian catalog includes records from `MainUK.bin` in the game’s byte-preserving glyph representation; the mapping is not yet decoded as Unicode prose. Its Russian fonts are included under `Localization/Fonts/`.

Gameplay voice catalogs remain experimental: six locales have 3,591 rows each in the detailed set, and human audio confirmation/native review remain pending per row. PT-BR gameplay is retained for research but intentionally omitted from the locale download entries in `manifest.json`.

## Audio-sync experiments and provenance

`Test/Audio-Sync/asr-candidates-20261011/` contains 44 SRT candidates, generated from language-specific speech-stream WAVs. `Test/Audio-Sync/retimed-candidates-20261011/` contains 54 experimental files. The 44 tracks present in both sets differ in both text and timing; the retimed set also has ten additional files. Neither set is a verified replacement for `Subtitles/`.

The extracted WAVs used for analysis are local work products and are not included here. The experiment READMEs and index CSVs preserve the available stream mapping and processing provenance.

## Manifest behavior

`manifest.json` is an inventory of actual repository assets. Locale `files` list supplemental localization materials; research data is marked `test_only` and remains separate from runtime-ready content. Its presence does not imply that a game or launcher runtime already loads that asset type. The generated `directory_tree` mirrors the repository's nested asset folders and shows each file's SHA-256, size, locale, and catalog status. Files not yet assigned to a locale list appear as `not_in_locale_catalog`; they are indexed for review but are not made downloadable by that status alone.

The GitHub Action **Refresh localization manifest** regenerates the folder tree, asset hashes, sizes, and `SOURCE-SHA256SUMS.txt` after pushes that touch localization data. Pull requests run the same generator in check-only mode and fail if the generated metadata is stale. To update it locally, run `python Tools/update_manifest.py`; use `python Tools/update_manifest.py --check` to verify without writing files. New files are detected and shown in the generated tree, but still need an explicit locale/category entry before they become part of a downloadable locale package.

## Formats

- Cutscene captions: SubRip (`.srt`).
- Menus, launcher, and gameplay catalogs: UTF-8 JSON Lines (`.jsonl`) with identifiers and text. The bilingual launcher source also retains its Portuguese text column.
- Alignment and review data: CSV/JSON.

The repository contains localization text and metadata plus documented font dependencies. It does not contain the game, executable, cutscene videos, or extracted audio.
