# BLACK subtitles and localization hub

**BLACK-SUBTITLES is a community hub for subtitle and localization files for BLACK (2006).** English is the reference language where an English source exists. The repository keeps each asset separate so players, modders, and other projects can use only what they need.

This is an unofficial community project. It does not include the game, executable files, videos, or extracted audio, and is not affiliated with or endorsed by Electronic Arts.

## Languages and available material

| Language | Code | Included material |
| --- | --- | --- |
| English | `en-US` | Reference menu and launcher text; cutscene subtitles; gameplay transcription candidates |
| Portuguese (Brazil) | `pt-BR` | Menu and launcher text; nine cutscene subtitle tracks; font files listed in the manifest |
| Spanish | `es` | Menu and launcher text; nine cutscene subtitle tracks; gameplay transcription candidates |
| French | `fr` | Menu and launcher text; nine cutscene subtitle tracks; gameplay transcription candidates |
| German | `de` | Menu and launcher text; nine cutscene subtitle tracks; gameplay transcription candidates |
| Italian | `it` | Menu and launcher text; nine cutscene subtitle tracks; gameplay transcription candidates |
| Indonesian | `id` | Menu and launcher text; nine cutscene subtitle tracks; required font files listed in the manifest |
| Russian | `ru` | Russian runtime menu bank and fonts; draft cutscene subtitle tracks |

Included files have different review states. Indonesian and Russian drafts, and gameplay transcription candidates, should be treated as work in progress. Gameplay candidates are not timed to in-game events and are not integrated into the game runtime.

## Find and use files

- `Subtitles/` contains editable `.srt` cutscene tracks, grouped by language when applicable.
- `Localization/Menu/` contains original-game menu catalogs. `GitHubs/` contains menu catalogs specific to supported forks and projects.
- `Launcher/` contains launcher interface text.
- `Localization/Fonts/` contains language font dependencies where needed.
- `Test/Gameplay-Audio-Transcription/` contains candidate voice transcripts and translations; these are reference material, not synchronized gameplay subtitles.
- `Test/` contains experimental subtitle and audio-sync material. Treat it as testing data, not as the approved subtitle set.
- `Tools/` contains repository utilities.
- [`manifest.json`](manifest.json) is the file index. It groups available downloads by language and lists each file's category, repository path, destination path, format, size, and SHA-256. Use it to select the assets you need and verify downloaded files. The manifest describes available files; it does not itself add runtime support to a game or launcher.

The nine cutscene tracks are `03_N`, `05_N`, `07_N`, `09_N`, `11_N`, `13_N`, `15_N`, `17_N`, and `18_N`. Some videos have no dialogue and therefore have no subtitle track.

## Contribute or report an issue

Found a mistranslation, typo, missing line, or timing problem? [Open an Issue](https://github.com/soldieg/BLACK-SUBTITLES/issues/new). Include the language, file, line or cue number, current text, suggested correction, and context or evidence when available.

To contribute files or corrections, open a Pull Request. Keep unrelated languages and assets separate, preserve IDs and subtitle timing unless the change specifically corrects them, and describe the source or reasoning for the change. Community review helps improve the hub; inclusion does not mean a translation has received human or native-speaker approval.

## Português (Brasil)

**O BLACK-SUBTITLES é um hub comunitário de legendas e arquivos de localização para BLACK (2006).** O inglês é o idioma de referência quando existe uma fonte em inglês. Os arquivos ficam separados para que cada pessoa, mod ou projeto possa escolher somente o material de que precisa.

O repositório reúne legendas de cutscenes, textos de menu e launcher, fontes necessárias para alguns idiomas e transcrições candidatas de falas de gameplay. Nem todo conteúdo foi revisado por uma pessoa nativa. As transcrições de gameplay ainda não estão sincronizadas com os eventos do jogo nem integradas ao runtime.

O [`manifest.json`](manifest.json) organiza os arquivos disponíveis por idioma e informa categoria, caminho, destino, formato, tamanho e SHA-256. Ele ajuda a localizar e conferir os arquivos; não implementa, por si só, o suporte a um idioma dentro do jogo.

Encontrou erro, texto estranho, fala ausente ou problema de timing? [Abra uma Issue](https://github.com/soldieg/BLACK-SUBTITLES/issues/new) com idioma, arquivo, linha ou cue, texto atual, sugestão e contexto. Para enviar traduções ou correções, abra uma Pull Request e explique a origem ou o motivo da alteração. A comunidade pode revisar e melhorar o material; estar no repositório não significa que o conteúdo já foi aprovado por uma pessoa ou por um falante nativo.
