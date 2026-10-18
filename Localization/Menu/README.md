# In-game menu text catalogs

The six ID-keyed JSONL catalogs (`en-US`, `pt-BR`, `es`, `fr`, `de`, `it`) contain 1,724 menu records aligned by stable IDs. `en-US`, `es`, `fr`, `de`, and `it` follow their corresponding supplied `Main*.bin` banks. The active `pt-BR` catalog follows the supplied `BLACK v 3/MainUS.bin` file, whose 1,724 text records are Portuguese despite the filename (SHA-256: `99E5FB9F4C4EC3F53E87C40423BF62EE8E8C753B9C5B63C2D3DFAB0C9DBAD378`). Indonesian remains the existing no-ID source catalog; Russian source-bank decoding is documented separately. See [MAIN-BANK-SOURCES.md](MAIN-BANK-SOURCES.md). These are editable text exports, not compiled game banks. Each row contains only its stable ID and text.

`editorial-review-build-legendas/` preserves earlier AI/editorial menu catalogs for comparison; the Main-bank exports are the active keyed source. Menu wording follows the supplied original language banks. Editorial review notes are documented separately; a text-only row does not imply human/native review.

Font binaries and their dependencies are organized separately in [`../Fonts/`](../Fonts/). PT-BR `Small.bin` and `Big.bin` are included because the language package needs those runtime files; their hashes match the standard game fonts. Runtime paths there are packaging examples, not compiled game-ready language banks.
