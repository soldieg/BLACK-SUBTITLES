# Cutscene subtitle tracks

The primary runtime-style SRT collection is organized by video stem and locale. English tracks are at this directory's root; translated tracks are in locale folders. The nine spoken stems are `03_N`, `05_N`, `07_N`, `09_N`, `11_N`, `13_N`, `15_N`, `17_N`, and `18_N`. `AK_N` and `MP5_N` have no dialogue track in this set.

English and six translated languages are present for the nine spoken cutscenes. The non-English tracks include translated speaker labels. Some speaker assignments were inferred from scene context; see `SPEAKER_ATTRIBUTION_REVIEW.csv`. Native-speaker review and complete direct-audio verification remain pending. The English source also has uncertain passages. These files are community subtitle drafts, not official transcripts. Indonesian tracks received an AI editorial pass; native-speaker review and direct audio confirmation remain pending. See `id/README.md`.

The SRT cues preserve the source timeline. Long-text wrapping and screen-aspect behavior belong to the consuming player; these files do not change cue duration. Keep the experimental folders separate from the primary set:

- `audio-sync-candidates-20261011/` contains ASR-derived localized-stream text and candidate timings.
- `audio-sync-retimed-20261011/` contains ASR-aligned timing experiments and a cue-by-cue CSV report.

Neither experimental set is certified as lip-synced. No video or audio is distributed here. Any original pre-edit rollback copies mentioned in old project notes remain outside this public data snapshot.
