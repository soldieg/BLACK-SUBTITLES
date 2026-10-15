# Multilingual gameplay speech review set

This is a six-locale candidate corpus for gameplay voice lines. The six JSONL files contain 3,591 rows each and retain clip/bank identifiers, source audio hashes, segment-relative timestamps, ASR evidence, translation text, and review metadata. Target locales are Brazilian Portuguese, Spanish, French, German, and Italian; `en-US` is the English pivot/source catalog.

## Status in this snapshot

Each translated target catalog has 592 assistant-curated rows awaiting native-speaker review, 315 candidates awaiting direct audio confirmation, 734 machine candidates awaiting source-language review, 8 dual-ASR candidates still awaiting audio/language review, and 1,942 machine-ASR drafts. The English catalog has its own distinct status counts (see the top-level repository README). There are 33 onomatopoeia candidates, 138 possible-vocalization rows, and 132 spoken-dialogue candidates in the English dataset; these categories describe classification fields, not human-confirmed transcripts.

ASR agreement, model confidence, and AI-assisted curation do not count as human listening or native-speaker review. Source-language labels and reconstructed words can be wrong. Do not treat these entries as verified dialogue.

Timestamps are relative to extracted source clips, not mission/gameplay time. Clip hashes and bank/index fields are included to help a reviewer match a candidate to their own source files. Audio is not included, and these catalogs are not loaded by the game runtime.

`AUDIT.md` and `HISTORY.md` preserve earlier analysis notes. Some notes reference private temporary reports that are not distributed here and may state earlier counts. `historical-build-summary-20261011.json` is an original historical build summary, not the current row-count source.
