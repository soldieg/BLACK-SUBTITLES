# Indonesian game menu catalog

`id.jsonl` contains the 1,724 text records exported from the user-provided Indonesian `MainUS.bin`. The original archive copies `indonesia language.rar` and `indonesia language (1).rar` were byte-identical (SHA-256: `0f6d81a3fc54a0d97a094765c8ebbf6f20bb5efe34aeb91de0d80b6876a2256b`). The extracted `MainUS.bin` SHA-256 is `eac02a88e4fff6590dfd98151efcea2aa36cc697d03292208efc23ce6c0e8186`.

The exporter preserves the game string IDs and record order. All 1,724 IDs and their order match the English `en-US.jsonl` catalog; the source bank has 776 indexed records. Each row is marked `provided-indonesian-bank-unreviewed`: this records its source, not a completed editorial or native-speaker review.

Only the editable text catalog is included here; the original binary language bank is not distributed. Indonesian cutscene subtitles and launcher strings are provided separately as AI-reviewed drafts, with native-speaker review still pending. There is no Indonesian gameplay voice-caption catalog in this snapshot.

## Indonesian fonts

The supplied Indonesian language archive includes `language/fonts/Small.bin` (40,448 bytes; SHA-256 `F194F96F9389BA7F4CB126AC02E2F619F27DF0339AB97DF6FE7A740E5A1FCA35`) and `language/fonts/Big.bin` (72,832 bytes; SHA-256 `119EDE7EC211DDEBDE76B46E4DCBEA86E486F1B13549FC1FE58ECB5ED59611C5`). Both are byte-identical to the standard font files in the inspected BLACK builds; they are not Indonesian-specific replacements. The repository does not redistribute these original game assets. From the repository root, run `.\tools\prepare-indonesian-fonts.ps1 -GameRoot "C:\path\to\BLACK\game"` to validate and copy the font files from your own game installation into `dist/indonesian-support/language/fonts/`. Copy the generated `language` folder into the game root. The expected names, sizes, and hashes are also recorded in `id-font-dependencies.json`.

The Indonesian cutscene SRT and launcher text additions are AI-reviewed drafts; see `../../subtitles/id/README.md` and `../launcher/REVIEW-id.md`. Native-speaker review remains pending.
