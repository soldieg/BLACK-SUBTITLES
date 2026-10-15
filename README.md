# BLACK subtitles and localization data

> [!IMPORTANT]
> **Found an error in any translation?** [Open an Issue](https://github.com/soldieg/BLACK-SUBTITLES/issues/new) so it can be reviewed and corrected.

An unofficial, reusable collection of subtitle and localization data for **BLACK (2006)**. The files use open formats so they can be adapted to different players, tools, and projects. This repository is not affiliated with Electronic Arts.

## Current snapshot

Updated from the latest local Build Legendas material on 2026-10-15. Six ID-keyed menu catalogs were refreshed from their corresponding original `Main*.bin` language banks (1,724 records each); Indonesian and Russian materials without stable IDs were retained from their existing source files. The current gameplay review set has 3,591 rows in each of six locales, plus a 774-record AI editorial correction log. The primary cutscene set contains 9 tracks for each of eight language directories (English, Portuguese, Spanish, French, German, Italian, Indonesian, and Russian): 72 SRT files total. Existing Indonesian and Russian SRTs were preserved byte-for-byte.

“Reviewed” distinguishes source-backed or AI-editorial work from pending human checks. Gameplay text still has audio and/or native review pending as indicated per row; AI review is not human confirmation. Cutscene text retains uncertainty and review caveats in its language READMEs.

## Languages and contents

| Area | Languages / count | Source and state |
| --- | --- | --- |
| Cutscene subtitles | 9 SRTs each: en, pt-BR, es, fr, de, it, id, ru | Existing tracks; native/audio review status is documented per locale. |
| Game menu | 1,724 IDs each: en-US, pt-BR, es, fr, de, it | Exported from corresponding original `Main*.bin` banks; PT-BR uses corrected ID alignment. |
| Indonesian menu | 1,724 existing records | Preserved source catalog; no IDs are invented. |
| Launcher | en/pt-BR, es, fr, de, it, id | 292 keyed UI entries; Indonesian review state is documented. |
| Gameplay voice candidates | 3,591 rows each: en-US, pt-BR, es, fr, de, it | Detailed ASR and AI editorial set; audio/native checks remain pending as recorded per row. |

## Folder guide

- `subtitles/`: primary cutscene SRTs by locale, plus separate ASR/timing experiments.
- `localization/game/`: ID-keyed menu catalogs, Indonesian no-ID source, source notes, runtime font layout, and prior editorial catalogs for comparison.
- `localization/launcher/`: launcher interface catalogs.
- `localization/gameplay/`: earlier candidate set and detailed 3,591-row review set with row-level provenance.
- `tools/`: helper scripts for local preparation and validation.
- `SOURCE-SHA256SUMS.txt`: checksums for distributed `.srt`, `.csv`, `.jsonl`, and `.json` files. Binary game fonts are identified by hashes in `localization/game/id-font-dependencies.json`.

## Game menu banks and runtime fonts

The six language banks were exported into open JSONL for comparison and editing. See [`localization/game/MAIN-BANK-SOURCES.md`](localization/game/MAIN-BANK-SOURCES.md) for source filenames and the Portuguese alignment note. Indonesian and Russian source materials without stable IDs remain in their existing files; no artificial IDs are assigned. Indonesian `Small.bin` and `Big.bin` runtime fonts are included under `localization/game/runtime/id/language/fonts/` and verified identical to the standard game fonts. Text catalogs remain source data and are not compiled game-ready banks.

## Subtitle notes

The primary cutscene tracks use SubRip (`.srt`) and are organized by locale and video stem. Videos without dialogue intentionally have no track. Translation and speaker labels may have AI/editorial review, while native-speaker review and full cue-by-cue audio verification can remain pending; consult each locale README.

Experimental sets in `subtitles/audio-sync-candidates-20261011/` and `subtitles/audio-sync-retimed-20261011/` contain ASR and timing candidates. They are experiments and should not replace the primary tracks without review. Their READMEs document stream-specific caveats.

## Gameplay review notes

The detailed gameplay catalogs contain clip-relative timestamps, source/audio identifiers, ASR evidence, translations, and row-level review states. They are not synchronized to mission time, are not wired into the game, and do not include extracted audio. A language label or agreement between ASR models is not proof of what was spoken. Read `localization/gameplay/large-v3-review-20261011/README.md` and `AUDIT.md` before treating any candidate as confirmed.

## Formats and reuse

- Cutscene captions: SubRip (`.srt`).
- Menu, launcher, and gameplay catalogs: UTF-8 JSON Lines (`.jsonl`), one record per line.
- Alignment/audit tables: CSV.
- Preserve IDs, ordering, provenance, and review-status fields when adapting catalogs.

The repository contains localization text and metadata plus the explicitly documented Indonesian font files. It does not contain the game, executable, videos, or extracted audio.
