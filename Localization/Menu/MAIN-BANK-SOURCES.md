# Menu catalog sources and review status

The six ID-keyed catalogs (`en-US`, `pt-BR`, `es`, `fr`, `de`, `it`) contain 1,724 rows aligned by stable IDs. `en-US`, `es`, `fr`, `de`, and `it` follow their corresponding supplied `Main*.bin` banks. The active `pt-BR.jsonl` now uses the supplied `BLACK v 3/MainUS.bin` file: despite its basename, its 1,724 UTF-8 text records are Portuguese and all IDs are unique. Source SHA-256: `99E5FB9F4C4EC3F53E87C40423BF62EE8E8C753B9C5B63C2D3DFAB0C9DBAD378`. This replaces the earlier active Build Legendas-aligned wording. Prior extraction and editorial comparisons remain preserved in their audit/reference folders.

`id.jsonl` is the existing Indonesian no-ID catalog and is preserved from its supplied source. No IDs are invented. Russian menu text remains documented separately because its source bank uses a special character/font mapping and is not represented as a verified decoded catalog here.

The previous Build Legendas editorial catalogs are retained under `editorial-review-build-legendas/` for comparison. The Main-bank catalogs are the active ID-keyed menu source. These exports are editable text, not compiled game banks; matching a provided bank does not claim human editorial/native review of every string.
