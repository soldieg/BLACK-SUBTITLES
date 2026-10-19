# BLACK-XBERecomp menu localization hub

This folder collects the menu text relevant to the `TGP482/BLACK-XBERecomp` fork in two separate groups:

- Each of the eight locale catalogs (`en-US`, `pt-BR`, `es`, `fr`, `de`, `it`, `id`, and `ru`) contains the full 155-string Recomp UI catalog plus 1,724 original game-menu records. Recomp UI rows use `key` and `text`; original menu rows use `id` and `text`. Editorial/source metadata is kept out of these translation rows.
- `original-game-menu/` mirrors the available original game-menu catalogs (`en-US`, `pt-BR`, `es`, `fr`, `de`, `it`, and `id`) from the repository's canonical [`Localization/Menu/`](../../../../Localization/Menu/) data. These mirror the broader original game menu catalogs from the canonical menu data; rows contain only `id` and `text`.

Russian menu records from `MainUK.bin` are included in `ru.jsonl` using the byte-preserving game-glyph representation; they are not yet decoded as Unicode Russian prose. Russian runtime fonts are cataloged separately. The current Recomp runtime reads downloaded Recomp UI overlays for `pt-BR`, `id`, and `ru`; `en-US`, `es`, `fr`, `de`, and `it` use the built-in UI translation table. Original-game menu catalogs and SRTs remain data assets whose in-game use depends on their corresponding runtime readers. Review and source notes remain in the repository documentation.

Language choices in the Recomp menu use each language's endonym across UI locales where the label is readable. The Russian option uses the readable endonym in each Latin-script UI catalog (`RUSSIAN`, `RUSSE`, `RUSSISCH`, `RUSSO`, or `RUSO`). Only the Russian UI catalog uses `РУССКИЙ`, because the Russian UI requests Cyrillic glyphs from installed Windows fonts (Arial, Segoe UI, or Tahoma); if none is available, the UI translation falls back to English. The Portuguese menu text maps unsupported tilde vowels (`Ã/ã/Õ/õ`) to the available diaeresis glyphs (`Ä/ä/Ö/ö`). Update completion messages are deliberately short (for example, `ATUALIZADO` and `EM DIA`). The five catalogs added for `en-US`, `es`, `fr`, `de`, and `it` use the existing Recomp menu translations and the matching original-game menu catalog.


## Language-screen package counts

The number shown after `NOT DOWNLOADED`, `MISSING`, or `DAMAGED` is a count of manifest assets for that locale, not a language version. The launcher catalog is excluded from the game package status. Expected totals are 11 for `en-US`, `pt-BR`, `es`, `fr`, and `it` (two menu catalogs plus nine cutscene SRTs); 13 for `de` and `id` (those 11 plus `Small.bin` and `Big.bin`); and 12 for `ru` (one Recomp menu catalog, nine SRTs, and two font files; no original-game menu catalog is listed for Russian). `READY` means every listed package asset is present and matches its SHA-256; `CURRENT / READY` additionally means that locale is currently selected.
