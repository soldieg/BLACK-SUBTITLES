# BlackDefinitiveHDPC localization package

This folder collects language data for the [BlackDefinitiveHDPC](https://github.com/euspring1/BlackDefinitiveHDPC) fork. It keeps the port's own menu text separate from the original game's menu catalog and cutscene subtitles.

## Contents

- `localization/port-menu/<locale>.jsonl`: the port's own PC settings/menu strings. English and Brazilian Portuguese come from `loader/src/lang.cpp`; the other six language files are AI translation drafts. Each line contains only `key` and `text`.
- `localization/original-game-menu/<locale>.jsonl`: original-game menu catalog mirrors from this repository's canonical catalogs. Russian contains the ID-based entries from the existing Russian Recomp catalog; it has no port-specific key entries. Rows contain only `id` and `text`.
- `Subtitles/<locale>/`: the nine primary cutscene SRTs for English, Brazilian Portuguese, Spanish, French, German, Italian, Indonesian and Russian. These are copied from `Subtitles/`; experimental ASR and retimed candidates are excluded.

## Runtime support

The inspected BlackDefinitiveHDPC `main` currently activates only English and Brazilian Portuguese for the port UI and original game language. The Spanish, French, German, Italian, Indonesian and Russian catalogs here are reference translations; this package alone does not enable those languages in the executable. The port's SRT loader reads SRTs from enabled mods' `subtitles/` folder and associates them with movie basenames. Enable movie subtitles in the port settings. The SRTs are data only and still need an in-game timing/rendering check in that port.

Use one subtitle-language mod at a time. The current loader gathers subtitle files from enabled mods into a single movie-name map, so two locale packs containing the same movie basename can override one another. Each mod must also include a `game/` folder to be recognized by the current mod scanner.

The nine movie basenames are `03_N`, `05_N`, `07_N`, `09_N`, `11_N`, `13_N`, `15_N`, `17_N` and `18_N`. `AK_N` and `MP5_N` have no spoken dialogue and have no SRT in the canonical set.

## Review status

- English and Brazilian Portuguese port-menu strings are copied from the fork's current source.
- The other port-menu translations and the Russian original-game menu catalog need review in the target port before being treated as final.
- Subtitle review and speaker-attribution limitations are documented in the language READMEs under `Subtitles/`.

