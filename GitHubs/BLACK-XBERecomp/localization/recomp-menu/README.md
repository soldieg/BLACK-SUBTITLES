# BLACK-XBERecomp menu localization hub

This folder collects the menu text relevant to the `TGP482/BLACK-XBERecomp` fork in two separate groups:

- `pt-BR.jsonl`, `id.jsonl`, and `ru.jsonl` are the 90 Recomp-specific UI strings used by that fork. Their keys match the English phrases from `src/common/translations.cpp`.
- `original-game-menu/` mirrors the available original game-menu catalogs (`en-US`, `pt-BR`, `es`, `fr`, `de`, `it`, and `id`) from the repository's canonical [`Localization/Menu/`](../../../../Localization/Menu/) data. These contain the game's broader menu text and are kept separate because their schemas and coverage differ from the Recomp strings.

No verified Russian original-game menu catalog is included: the `MainUK.bin` glyph mapping has not been decoded. The Russian Recomp-specific 90-string catalog is available above. These JSONL files are source data; runtime language switching/loading is separate work. Review states and source provenance remain in the canonical catalog READMEs.
