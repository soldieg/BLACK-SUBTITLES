# Gameplay voice catalog — detailed review set

This set has six locale catalogs (`en-US`, `pt-BR`, `es`, `fr`, `de`, `it`) with 3,591 records each. It contains ASR transcripts, translations, clip/audio identity, timestamps, and AI-assisted editorial corrections. The 2026-10-15 correction log contains 774 records.

## Review state

The row-level `translation_status` and `review_status` fields are authoritative. The set includes onomatopoeia/vocalization and dialogue candidates; entries remain candidates whenever their status says audio or source-language review is pending. AI review is not human listening, native-speaker review, or confirmation against the game. No extracted audio is distributed, and timestamps are clip-relative rather than mission/gameplay timing.

`AUDIT.md`, `HISTORY.md`, `build-summary.json`, and the correction log retain detailed provenance. Some audit history describes earlier snapshots; use the six current JSONL catalogs for current row counts. This data is not wired into the game runtime.
