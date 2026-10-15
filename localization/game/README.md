# In-game menu text catalogs

The English, Portuguese, Spanish, French, German, and Italian JSONL catalogs each contain 1,724 menu records aligned by stable IDs from their corresponding original `Main*.bin` bank. Indonesian remains the existing no-ID catalog from the supplied source; Russian source-bank decoding is documented separately. See [MAIN-BANK-SOURCES.md](MAIN-BANK-SOURCES.md). These are editable text exports, not compiled game banks.

`editorial-review-build-legendas/` preserves the previous AI/editorial menu catalogs for comparison; the Main-bank exports are the active keyed source. Menu wording follows the supplied original language banks. This does not imply every string received human/native review.

The Indonesian runtime font files are included at `runtime/id/language/fonts/Small.bin` and `Big.bin`. Both are byte-identical to the standard game fonts; their sizes and SHA-256 values are recorded in `id-font-dependencies.json`. Runtime paths are examples for packaging, not a compiled Indonesian `MainUS.bin`.
