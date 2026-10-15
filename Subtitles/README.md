# BLACK cutscene captions

The primary subtitle set contains nine tracks for each locale: English (`en`), Brazilian Portuguese (`pt-BR`), Spanish (`es`), French (`fr`), German (`de`), Italian (`it`), Indonesian (`id`), and Russian (`ru`), for 72 SRT files total. English tracks are in `Subtitles/en/<stem>.srt`; other locales use `Subtitles/<locale>/<stem>.srt`.

The launcher uses the selected game-menu language to choose a subtitle locale. Videos without spoken dialogue, including `AK_N` and `MP5_N`, intentionally have no SRT track.

Spanish, French, German, and Italian received an AI/editorial pass, but native-speaker review and full cue-by-cue audio verification may remain pending. Consult each locale README. Russian and Indonesian review limitations are also documented in their locale READMEs. Inclusion does not claim an official transcript or final synchronization.

All nine spoken cutscenes prefix cues with localized speaker labels. The opening exchange identifies the first voice as the Interrogator and Kellar's replies as Sgt. Kellar. The PT-BR `07_N` track has two speakers within one cue; both are labeled while its existing timing is retained. Some speaker assignments are contextual estimates; see `SPEAKER_ATTRIBUTION_REVIEW.csv`.

Subtitle rendering in the related runtime wraps long cues to the selected presentation aspect ratio; this repository contains the SRT source data and does not itself implement that renderer.

Experimental ASR and retimed SRTs are kept separately in `../Test/Audio-Sync/`. They are not primary captions and should not replace this directory without review.
