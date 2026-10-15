# Russian menu-language source notes

The user-supplied `language.7z` archive (SHA-256 `1d2b53aae9ae681ee04f99d7e612cc94c5099b9ca21597bc7e426ebc8d157b16`) contains `language/strings/MainUK.bin`, `MainFr.bin`, `MainGe.bin`, `MainIt.bin`, `MainSp.bin`, and `language/fonts/Small.bin` plus `Big.bin`.

Despite the `UK` filename, inspection found Russian text in `MainUK.bin`. One indexed entry corresponds to the English source `Primary objectives only. Lots of Healthpacks. No rewards.` and contains bytes rendered by the current parser as `OCHOBHSE QELN. MHOFO AZTE4EK. HAFPAD HET.` This appears to use the game's special character/font mapping rather than ordinary UTF-8 Cyrillic. It is evidence of Russian menu text, but not yet a validated decoded catalog. The byte-to-glyph mapping and the relationship to the supplied font banks still need to be established before converting or redistributing the strings as normal text.

The supplied font banks differ from the stock fonts and are likely part of that language's display setup:

- `Small.bin` — SHA-256 `de383f6eb7ff2ea80374255e6212d9455cc7c62e6a367accbeecdfed72301c90`
- `Big.bin` — SHA-256 `73d8872cfffc3b2c6026ef89b9b015df70d442548656b28900bfacfbc1cd4ecd`

The archive and original binary assets are not copied into this repository. Russian runtime folders under `runtime/ru/` are placeholders only; no `MainUS.bin` or font file has been generated. Existing locale catalogs remain untouched. For subtitles, use the English SRTs as the primary translation source; the Russian subtitle drafts live separately in `subtitles/ru/` and have not been checked against Russian audio.
