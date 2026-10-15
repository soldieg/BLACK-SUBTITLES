# Localized cutscene audio sync candidates (2026-10-11)

These separate SRT candidates were generated from extracted language-specific SSH stream WAVs. Cue text and timestamps come from multilingual ASR on each localized stream; timing is relative to the original stream timeline. The candidate bank-to-video pairing is recorded in `stream-sync-index.csv` and was derived from the English transcript-overlap map in the local Build Legendas work folder (`.work/character-audio-catalog-20261011/subtitle-stream-map.csv`). The same narrative wording in each localized stream and near-matching stream lengths/start times corroborate the pairing. This is a strong mapping candidate, not human-verified lip sync.

Extracted narrative audio languages: English (`en`), Spanish (`es`), French (`fr`), German (`de`), and Italian (`it`). No Brazilian Portuguese dub stream was identified; the primary `Subtitles/pt-BR/` captions are translated text over non-Portuguese audio. In the Level/17_N candidate, the fifth stream was identified as Galician (`gl`, confidence 0.41), so no Spanish SRT was emitted for it.

All SRT text is machine ASR and may contain errors, particularly proper names, military terms, and clipped lines. Review against audio before runtime use. Original English and translated primary tracks were left untouched.

Stream indexes 1-5 correspond to French, German, Italian, English, and Spanish. Duplicate English captures at indexes 6-7 were excluded. The extracted WAVs are local work products and are not included in this repository.