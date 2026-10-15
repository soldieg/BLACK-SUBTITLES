# BLACK subtitles and localization data

An unofficial, reusable collection of subtitle and localization data prepared for **BLACK (2006)**. The files are kept in open formats so they can be adapted to different players, tools, and projects.

This repository contains text and metadata only. It does not contain the game, executable files, XMV videos, extracted audio, or the game's binary language/font banks. For Indonesian localization, `tools/prepare-indonesian-fonts.ps1` can validate and package the standard font files from a user's own game installation; the original font binaries are not distributed here. It is not affiliated with or endorsed by Electronic Arts.

## Languages

| Language | Catalog code | Cutscene captions | Menu text | Launcher text | Gameplay candidates |
| --- | --- | --- | --- | --- | --- |
| English | `en-US` / `en` | 9 tracks | Source | Source | Source candidates |
| Portuguese | `pt-BR` | 9 tracks | Available | Available | Candidate translations |
| Spanish | `es` | 9 tracks | Available | Available | Candidate translations |
| French | `fr` | 9 tracks | Available | Available | Candidate translations |
| German | `de` | 9 tracks | Available | Available | Candidate translations |
| Italian | `it` | 9 tracks | Available | Available | Candidate translations |
| Indonesian | `id` | 9 tracks | Available | Available | Not available |

The Indonesian menu catalog is a text-only export of the supplied `MainUS.bin`. It preserves source IDs and order but is not independently reviewed. Indonesian cutscene captions and launcher strings are AI-reviewed drafts; native-speaker review remains pending. No Indonesian gameplay caption catalog is included in this snapshot.

## Contents

### `subtitles/` — cutscene SRT files

The primary set has nine spoken video stems in English and six translated languages: `03_N`, `05_N`, `07_N`, `09_N`, `11_N`, `13_N`, `15_N`, `17_N`, and `18_N` (63 SRT files). English files are directly under `subtitles/`; translated files are in locale subfolders:

```text
subtitles/03_N.srt          # English
subtitles/pt-BR/03_N.srt    # Brazilian Portuguese
subtitles/es/03_N.srt       # Spanish
subtitles/fr/03_N.srt       # French
subtitles/de/03_N.srt       # German
subtitles/it/03_N.srt       # Italian
subtitles/id/03_N.srt       # Indonesian
```

The same folder pattern is used for the other eight stems listed above. Videos without dialogue, such as `AK_N` and `MP5_N`, intentionally have no track.

The dialogue tracks include localized speaker labels. Translation and speaker attribution have received AI/editorial review, but native-speaker review and complete cue-by-cue audio verification remain pending. English source passages also contain uncertain wording. The SRTs are usable as editable caption files; inclusion here does not certify official wording or final synchronization.

Two separate experimental sets are retained:

- `subtitles/audio-sync-candidates-20261011/`: 44 SRT candidates transcribed from language-specific audio streams. Text and timing are ASR candidates. The available narrative streams include English, Spanish, French, German, and Italian; no Brazilian Portuguese dub stream was identified. The `17_N` Spanish-stream candidate was identified as Galician, so that directory has no Spanish `17_N.srt`.
- `subtitles/audio-sync-retimed-20261011/`: 54 automatically retimed candidate tracks plus `alignment-review.csv`. The alignment used ASR word matching; many cues fell back to English timing and the report flags out-of-order rows. Treat these files as experiments, not replacements for the primary tracks.

The candidate directories have their own READMEs with their generation and review notes. Files remain separated so a consumer can choose the track set that fits their use.

### `localization/game/` — in-game menu strings

The English, Portuguese, Spanish, French, German, and Italian catalogs each contain 1,724 ID-keyed `MainUS` records. The Indonesian `id.jsonl` catalog adds 1,724 records from the supplied Indonesian bank. `proper-name-invariants.jsonl` records canonical names. These are editable text catalogs, not game-ready `MainUS.bin` files. Indonesian provenance and review status are documented in `localization/game/INDONESIAN.md`; editorial and native-speaker review remain pending.

#### Runtime language file layout

The expected game-relative paths are represented for every catalog locale (`en-US`, `pt-BR`, `es`, `fr`, `de`, `it`, and `id`) under `localization/game/runtime/<locale>/language/`:

```text
localization/game/runtime/<locale>/language/MainUS.bin
localization/game/runtime/<locale>/language/fonts/Small.bin
localization/game/runtime/<locale>/language/fonts/Big.bin
```

GitHub contains only `.gitkeep` placeholders in these folders; it does not contain the game's binary language or font assets. The editable Indonesian menu text is at `localization/game/id.jsonl`; it is not a compiled `MainUS.bin`. For Indonesian, `Small.bin` and `Big.bin` are identical to the standard game fonts. Their expected hashes and the local preparation instructions are in `localization/game/id-font-dependencies.json` and `localization/game/INDONESIAN.md`.

### `localization/launcher/` — launcher interface strings

The English/Portuguese source catalog and Spanish, French, German, Italian, and Indonesian catalogs contain 292 keyed UI entries. Indonesian received an AI editorial pass; native-speaker review remains pending. Locale catalogs are source data for a launcher, not launcher executables.

### `localization/gameplay/` — voice-caption candidates

- The first six catalogs contain 3,196 candidate rows per language.
- `large-v3-review-20261011/` contains the later six-locale review set, with 3,591 rows per locale in this snapshot. Each row retains clip/bank identity, hashes, segment timing, transcript/translation provenance, and review status.
- The review set distinguishes spoken-dialogue candidates, possible vocalizations, and 33 onomatopoeia candidates. ASR output and AI-assisted translations are not human-confirmed transcripts. A language label is evidence attached to a candidate, not proof of the spoken language.
- The catalogs contain clip-relative times, not mission/gameplay synchronization. They are not wired into the game runtime.

In each translated target catalog (`pt-BR`, `es`, `fr`, `de`, `it`), the current statuses are: 592 assistant-curated drafts awaiting native review; 315 assistant-curated candidates awaiting direct audio review; 734 machine candidates awaiting source-language review; 8 dual-ASR candidates awaiting audio or source-language review; and 1,942 machine drafts from English or multilingual ASR. The English source catalog has its own statuses: 538 assistant-curated drafts awaiting review, 332 awaiting direct audio review, 774 awaiting source-language review, 9 dual-ASR review candidates, and 1,938 machine-ASR candidates. These categories describe the `review_status` field and do not mean the text is ready to ship. See the catalog records and `large-v3-review-20261011/AUDIT.md` for provenance and caveats. Historical build summaries and audit notes may reflect an earlier snapshot; the row counts above were recomputed from the files in this repository.

No extracted audio is included. SHA-256 values and source-bank/clip indexes are retained where present so reviewers can match a candidate to their own lawful game files.

## Formats and reuse

- Cutscene captions: standard SubRip (`.srt`).
- Menu, launcher, and gameplay catalogs: UTF-8 JSON Lines (`.jsonl`), one record per line.
- Candidate alignment review: CSV.
- `SOURCE-SHA256SUMS.txt` lists SHA-256 checksums for the distributed SRT, CSV, JSONL, and JSON data files.

You may select or convert individual files for your own player or project. Keep the candidate/review status and provenance fields when reformatting gameplay data so machine suggestions are not mistaken for verified dialogue.

## Snapshot notes

This text-data snapshot was imported from the BLACK Build Legendas work on 2026-10-15. Experimental timing tracks and ASR-derived gameplay content are intentionally included alongside curated material, but in clearly separate folders. Temporary machine-specific work files, local backups, game assets, and audio are not part of this repository. The historical build-summary copy has machine-specific absolute paths removed; its earlier metrics remain historical.
