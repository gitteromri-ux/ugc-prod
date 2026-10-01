# Julie UGC v12: public source handover for Claude

Updated 1 October 2026. This repository is PUBLIC at Omri's explicit request. No sign-in is needed to download it. This is a recovery handover, not a claim that the original editing project has been recovered in full.

## Start here

```sh
git clone https://github.com/gitteromri-ux/ugc-prod.git
cd ugc-prod
python3 restore_originals.py
sha256sum -c SHA256SUMS.txt
```

`restore_originals.py` rejoins the two binary chunks into the byte-identical, untrimmed `src/w46b_p1.mp4`. It does not transcode. The original is split because it exceeds GitHub's per-file limit. Its SHA-256 is checked before the script succeeds.

Read this README first, then `refs/CLAUDE-UGC-V12-AUDIT.md`, `refs/ORIGINAL-BRIEF.md`, and `HANDOVER-TO-CLAUDE.md`. The latter is the earlier historical handover; its claims about complete local project availability and QA are NOT a current verification.

## Supplied files

| Path | Provenance and use |
|---|---|
| `src/original-parts/w46b_p1.mp4.part00` and `.part01` | Complete untrimmed presenter part 1, split without modifying bytes. Run the restoration script. 170,623,737 bytes; approximately 30.05 s. |
| `src/w46b_p1_trim.mp4` | Previously shared trimmed presenter part 1. Approximately 29.92 s, 1080×1920. |
| `src/julie-film-full.mp4` | 139.05 s Julie film, downloaded from `lla-masterclass-assets/video/julie-masterclass-film-full-1080p.mp4`. Same duration as the historical film map; byte identity with the old sandbox copy was not established. |
| `src/press-as-seen-on.mp4` | Original supplied 4K press sequence, 13.4 s. The historical handover specifies approximately 3.75–9.5 s for the logo run. Check frame boundaries yourself. |
| `src/lla-outro-card-official.mp4` | Original supplied official outro, 8.3 s. |
| `src/lla-logo-transparent.png` | Logo retrieved from the assets repository. |
| `src/zoom/zoom-40-ppl-logos.jpg` | Original clean Zoom gallery artwork, including Julie as host. This is the source artwork, NOT the complete v12 animated composition. |
| `src/zoom/zoom-meeting-ui-chat.jpg` | Original Zoom interface artwork. |
| `src/zoom/zoomui-julie-tile.jpg` | Isolated host tile from the existing assets repository. |
| `src/zoom/zoomui-logo-tile.jpg` | Isolated logo tile from the existing assets repository. |
| `src/zoom/zoomui-video-grid.jpg` | Existing gallery-grid extraction. |
| `recovered-from-exports/zoom-v12-1x1-57.00-59.25-noaudio.mp4` | The delivered square Zoom animation, extracted at 57.00–59.25 s. Audio removed, re-encoded for standalone use. Burned-in text remains. NOT a clean original render. |
| `recovered-from-exports/zoom-v12-9x16-57.00-59.25-noaudio.mp4` | Equivalent vertical extraction. Burned-in text remains. NOT a clean original render. |
| `recovered-from-exports/zoom-v12-square-frame58.jpg` | Frame reference showing the exact delivered composition. |
| `reference-exports/ad5-woman46__1x1__75.mp4` | Delivered v12 square file, copied without modification. Reference only; contains the defects in Claude's audit. |
| `reference-exports/ad5-woman46__9x16__75.mp4` | Delivered v12 vertical file, copied without modification. Reference only. |
| `music/Exhilarate.mp3` | Standalone Kevin MacLeod track downloaded from Incompetech. Historical handover names this track; byte identity with the old source was not established. Attribution/licensing remains a release decision. |
| `fonts/brand/PlayfairDisplay-*.ttf` | Google Fonts variable font files. These are NOT the original renamed `LLASerif-*` instances used by libass. |
| `refs/canva/` | Four supplied visual references. |
| `refs/CLAUDE-UGC-V12-AUDIT.md` | Actual audit from the `claude/audits-2026-10-01` branch of `final-versions`. |
| `refs/ORIGINAL-BRIEF.md`, `refs/META-UPLOAD-SPEC.md` | Existing project brief and upload specification, preserved for context. |
| `refs/Julie-Masterclass-Video-Audit-UGC-Ads-Film.docx` | Earlier supplied audit. |

## Exact remaining gaps

The following files have NOT been recovered or uploaded:

- `src/w46b_p2.mp4`: the clean second presenter take.
- `assemble75.py`, `render_cards.py`, `render_zoom.py`, `qc.py`, `fix_end.sh`, `tx.py`, `tx_json.py`, `run_ad5.sh`: original editing code.
- Original word-alignment caches, ASS caption sources, standalone animated Zoom renders, and renamed font instances.

The previous README called these files “lost” and claimed a Higgsfield history entry was available. Neither assertion was verified. The accurate status is **not recovered in this session**. The local browser connection failed with “No local browser is reachable in this session”; the device list returned no devices. That is not evidence that Omri closed his browser or that these assets were deleted.

The checked local attachments, generated assets, downloaded session assets, current GitHub trees and selected historical trees did not contain the missing originals. No substitute has been mislabeled as `w46b_p2.mp4` or `assemble75.py`.

## Editing handoff

- No new Higgsfield generation was performed for this recovery.
- Use the clean part 1 take to fix captions and framing in its segment.
- Use the clean Zoom artwork and isolated host/grid assets for a new composition, or the explicitly labeled export extracts if suitable.
- The historical handover describes the original assembly order and environment options, but it is not runnable code.
- Do not claim a full clean-source re-render until part 2 is actually available. Export extraction does not recover its clean dialogue, unobscured picture, or original framing.
- Preserve the user's required scope: 75-second vertical and square ads, exact brand references, clear on-brand captions, correct offer/CTA, no unsupported “audited” claims.
- Campaign, tracking and publication permissions are outside this repository handover. No live campaign or existing video was modified.

## Provenance links

- Existing final deliverables: https://github.com/gitteromri-ux/final-versions
- Claude audit: https://github.com/gitteromri-ux/final-versions/blob/claude/audits-2026-10-01/audits/2026-10-01/UGC-V12-AUDIT.md
- Original Zoom assets: https://github.com/gitteromri-ux/lla-masterclass-assets
- Music retrieval: https://incompetech.com/music/royalty-free/mp3-royaltyfree/Exhilarate.mp3
- Font retrieval: https://github.com/google/fonts/tree/main/ofl/playfairdisplay
