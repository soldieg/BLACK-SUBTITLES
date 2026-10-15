# Menu catalog sources and review status

The six ID-keyed catalogs (`en-US`, `pt-BR`, `es`, `fr`, `de`, `it`) contain 1,724 rows aligned by stable IDs from their corresponding original `Main*.bin` banks. The matching original bank for each locale is the source of its menu wording. `pt-BR.jsonl` uses corrected ID alignment already present in Build Legendas because the raw Portuguese bank has a documented shifted/missing tail; the original extraction and comparison are retained in the local translation hub under `revisado/localization/game/source-bank-audit/`.

`id.jsonl` is the existing Indonesian no-ID catalog and is preserved from its supplied source. No IDs are invented. Russian menu text remains documented separately because its source bank uses a special character/font mapping and is not represented as a verified decoded catalog here.

The previous Build Legendas editorial catalogs are retained under `editorial-review-build-legendas/` for comparison. The Main-bank catalogs are the active ID-keyed menu source. These exports are editable text, not compiled game banks; matching a provided bank does not claim human editorial/native review of every string.
