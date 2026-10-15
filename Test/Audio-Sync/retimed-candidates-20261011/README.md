# Cutscene audio alignment candidates — 2026-10-11

These 54 SRT files are experimental timing candidates generated from the extracted localized cutscene voice streams. They are kept separate from the runtime tracks in the parent `Subtitles/` folders. The report is `alignment-review.csv` and has one row per cue, including the chosen audio language, match score, and whether the cue was aligned or fell back to another timing.

The existing game assets contain speech streams associated with English, Spanish, French, German, and Italian. The script aligned translated SRT words against automatic word transcripts for each available language; where the lexical match was weak, it retained the corresponding English cue timing. The Brazilian Portuguese track uses English audio timing because no pt-BR cutscene voice stream was identified.

The automated pass completed 44 audio-stream/language combinations and emitted 1,079 cues. This is not a verified synchronization pass: matches are ASR-based, and the review report shows many fallbacks, especially for French, German, and Italian. Listen to the localized stream and review `alignment-review.csv` before promoting any candidate to the runtime subtitle folders. Cue wording and speaker labels are copied from the curated tracks; only timestamps differ.

A structural audit found 19 out-of-order cue rows across the candidate tracks (including cues 20/22 in `09_N`, cue 7 in `15_N`, and one cue in German `03_N`). These are explicitly marked `out-of-order` in the report. This confirms the candidates are not ready to replace runtime tracks; use the report to manually inspect/re-time those lines.
