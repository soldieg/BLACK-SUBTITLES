# Cutscene audio-alignment experiments

This folder contains 54 SRT timing candidates (nine stems across six locales) and `alignment-review.csv`, with one report row per cue. Text and speaker labels are copied from the primary curated tracks; the automated pass changes cue timing only.

The alignment compares translated cue words with automatic transcripts from the corresponding localized audio streams. Where lexical matching was weak, it retained English cue timing. Brazilian Portuguese uses English timing because no pt-BR cutscene voice stream was identified. The report flags 19 out-of-order cue rows and records fallback decisions.

These are unverified experiments, not a replacement set. ASR-based timing is not proof of lip sync. Listen to the appropriate stream and review the CSV before promoting any timing. No audio is included.
