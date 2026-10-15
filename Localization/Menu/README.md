# In-game menu text catalogs

The English, Portuguese, Spanish, French, German, and Italian JSONL catalogs each contain 1,724 menu records aligned by stable IDs from their corresponding original `Main*.bin` bank. Indonesian remains the existing no-ID source catalog; Russian source-bank decoding is documented separately. See [MAIN-BANK-SOURCES.md](MAIN-BANK-SOURCES.md). These are editable text exports, not compiled game banks.

`editorial-review-build-legendas/` preserves earlier AI/editorial menu catalogs for comparison; the Main-bank exports are the active keyed source. Menu wording follows the supplied original language banks. This does not imply every string received human/native review.

Font binaries and their dependencies are organized separately in [`../Fonts/`](../Fonts/). Runtime paths there are packaging examples, not compiled game-ready language banks.
