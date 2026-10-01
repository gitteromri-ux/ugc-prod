# ugc-prod — source files for the Julie Masterclass UGC ad (v12)

Rebuilt for Claude on 2026-10-01 from what survives of Perplexity's original `ugc-prod/` working folder. Read `HANDOVER-TO-CLAUDE.md` first (brief, film timecode map, pipeline order, music curve, brand values).

Finished v12 files being fixed: `gitteromri-ux/final-versions` → `videos/ad5-woman46__9x16__75.mp4`, `videos/ad5-woman46__1x1__75.mp4`.

## What is here (VERIFIED: ffprobe + sha256 in `SHA256SUMS.txt`)

| File | What it is | Spec |
|---|---|---|
| `src/w46b_p1_trim.mp4` | Clean presenter take, part 1 (no captions, no music). The exact file used in v12 for 0–29.9 s | 1080×1920, 29.92 s |
| `src/julie-film-full.mp4` | Julie's film. Matches the 139 s film the handover timecode map refers to | 1920×1080, 139.05 s |
| `src/press-as-seen-on.mp4` | Omri's "As seen on" press logo sequence (USA Today, Yahoo Finance, MarketWatch, AP, The Sun) | 3840×2160, 13.4 s |
| `src/lla-outro-card-official.mp4` | Official LLA ENROLL NOW outro card | 1920×1080, 8.3 s |
| `src/lla-logo-transparent.png` | LLA lockup (from `lla-masterclass-assets/parts/`) | 1314×596 |
| `music/Exhilarate.mp3` | The v12 music bed: "Exhilarate", Kevin MacLeod (incompetech.com), CC BY 4.0. Needs credit line or replacement | 320 kbps |
| `fonts/brand/PlayfairDisplay-*.ttf` | Playfair Display (Google Fonts, OFL). v12 used these renamed as `LLASerif-*` for libass | variable weight |
| `refs/canva/*.png` | Omri's Canva card references (the required card look) | |
| `refs/Julie-Masterclass-Video-Audit-UGC-Ads-Film.docx` | Earlier audit Omri supplied | |

## What is NOT recoverable from this side

- `src/w46b_p2.mp4` — presenter part 2 (29.92 s, Seedance 2.5 Extend of part 1). Only copy was in the original sandbox. Get it from Omri's Higgsfield account history (it is the Extend generation made from `w46b_p1_trim.mp4`, 2026-10-01). No new generation needed.
- `assemble75.py` — the assembler script. Lost with the sandbox. Its full order, timings, music curve and caption setup are written out in `HANDOVER-TO-CLAUDE.md` (pipeline table, assembly order, music curve).
- The 50-tile Zoom mockup render. Closest source: `gitteromri-ux/lla-masterclass-assets/zoom-40-ppl-logos.jpg`.

## Other usable sources

- `gitteromri-ux/lla-masterclass-assets/julie-film-v4/video/cuts/` — Julie film cuts 45/60/75 s in all formats.
- `gitteromri-ux/lla-julie-ugc-ads/gen/` — earlier presenter takes (rejected; do not use as the presenter).
