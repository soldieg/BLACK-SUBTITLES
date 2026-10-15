# BLACK-XBERecomp menu localization hub

This folder collects the menu text relevant to the `TGP482/BLACK-XBERecomp` fork in two separate groups:

- `pt-BR.jsonl`, `id.jsonl`, and `ru.jsonl` each contain 93 Recomp-specific UI strings plus 1,724 original game-menu records. Recomp UI rows use `key` and `text`; original menu rows use `id` and `text`. Editorial/source metadata is kept out of these translation rows.
- `original-game-menu/` mirrors the available original game-menu catalogs (`en-US`, `pt-BR`, `es`, `fr`, `de`, `it`, and `id`) from the repository's canonical [`Localization/Menu/`](../../../../Localization/Menu/) data. These mirror the broader original game menu catalogs from the canonical menu data; rows contain only `id` and `text`.

Russian menu records from `MainUK.bin` are included in `ru.jsonl` using the byte-preserving game-glyph representation; they are not yet decoded as Unicode Russian prose. Russian runtime fonts are cataloged separately. These JSONL files are source data; runtime language switching/loading is separate work. Review and source notes remain in the repository documentation.
