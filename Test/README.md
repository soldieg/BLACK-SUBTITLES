# Research and test data

This folder keeps analysis outputs separate from the primary language assets. Files here are not automatically runtime-ready.

- `Audio-Sync/asr-candidates-20261011/`: 44 ASR-derived SRT candidates and stream mapping index.
- `Audio-Sync/retimed-candidates-20261011/`: 54 retimed SRT experiments plus alignment review data.
- `Gameplay-Audio-Transcription/large-v3-review-20261011/`: detailed gameplay voice catalogs with 3,591 records in each of six locales and row-level review states.
- `Gameplay-Audio-Transcription/legacy-candidates/`: earlier 3,196-row locale catalogs retained as historical candidates.

The ASR and retiming sets are different: the 44 matching tracks differ in both text and timing, and the retimed set has ten extra tracks. The extracted WAVs used as source evidence are local work products and are not checked into this repository. See the READMEs and CSVs alongside each dataset for further provenance and limitations.

PT-BR gameplay data remains available here for analysis but is intentionally excluded from the downloadable locale entries in `manifest.json`.
