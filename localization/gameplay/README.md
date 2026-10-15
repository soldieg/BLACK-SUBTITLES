# Gameplay voice caption data

This folder contains two versions of the gameplay dialogue candidate catalogs. The six top-level JSONL files contain 3,196 rows per locale (`en-US`, `pt-BR`, `es`, `fr`, `de`, `it`). The later `large-v3-review-20261011/` set contains 3,591 rows per locale and additional source-language, ASR, and editorial-review evidence.

The later set is the more detailed review corpus, but neither set is a final, synchronized gameplay subtitle package. Text is candidate transcription and AI-assisted translation; audio confirmation, source-language resolution, and native-speaker review remain pending as recorded on each row. The clip-relative timestamps are not mission time. The game does not load these catalogs, and the source audio is not included.
