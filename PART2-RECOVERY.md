# Recovered clean presenter part 2

Recovered 1 October 2026 through the authenticated Higgsfield history connector. No generation, re-encoding, audio replacement, or editing was performed.

## Download and restore

On branch `recovery/w46b-p2`:

```sh
git fetch origin recovery/w46b-p2
git checkout recovery/w46b-p2
python3 restore_part2.py
```

This restores `src/w46b_p2.mp4` from two binary chunks, 89,000,000 bytes and 27,926,233 bytes. Both are strictly under 90 MB. The script verifies each chunk and the reconstructed MP4 using SHA-256.

## Provenance

- Higgsfield job: `ea657df7-3966-4cbc-a45b-0dd9865408ee`.
- Generated: 1 October 2026, 10:41:37 UTC, according to the history record.
- Model: `seedance_2_5`; mode: `video_extension`, forward.
- [Original MP4](https://d8j0ntlcm91z4.cloudfront.net/user_3B2TkzjFQaqg6v69LxXPlh5VT9f/hf_20261001_104137_ea657df7-3966-4cbc-a45b-0dd9865408ee.mp4).
- Reference input ID: `0fa24878-54a0-4d85-9311-a7eb71bc0f7a`.
- The recorded prompt specifies the same woman, oatmeal sweater, sunlit kitchen, General American voice and continuation beginning “Everyone's talking about longevity right now” and ending “Forty-nine dollars. Honestly? I'm in.”
- Retrieved media: HEVC video, 1080 × 1920, 24 fps, AAC audio, 30.000 seconds, 116,926,233 bytes.
- SHA-256: `7dc8f9d1cafbb39e6dc93625626b147eb76c27322a3381eedd29c56beef855e9`.

The old handover described the working part 2 as 29.92 seconds. This recovery deliberately preserves the full 30.000-second provider original. Byte identity with that unavailable historical working copy is not claimed. The generation record, script, date, and sampled visual frames identify this as the matching clean continuation source.

This is source recovery, not a new final-ad quality audit. Existing ads, campaigns and published pages have not been changed.

## Rollback

This recovery is isolated on its own branch. Main remains at `6ca4c05be212c63bb84c4b1cb90a4934b468617d`; switch back to `main` to use the prior handover.
