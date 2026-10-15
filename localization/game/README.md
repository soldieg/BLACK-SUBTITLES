# In-game menu text catalogs

These UTF-8 JSONL files export the 1,724 keyed string records from the game's `MainUS` menu/text bank. Each row preserves its record index and stable hexadecimal ID alongside the text. `en-US.jsonl` is the English source, and `pt-BR`, `es`, `fr`, `de`, and `it` are localized catalogs. `proper-name-invariants.jsonl` lists canonical names used during review.

The catalogs are editable source data. They are not the game's binary bank and do not include fonts or other game assets. Preserve IDs and ordering when converting them for a tool or game build. Editorial review is not the same as native-speaker or in-game-context validation.
