#!/usr/bin/env python3
"""Rejoin the recovered original Higgsfield part 2, without transcoding."""
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXPECTED = "7dc8f9d1cafbb39e6dc93625626b147eb76c27322a3381eedd29c56beef855e9"
PARTS = [
    ("w46b_p2.mp4.part00", "b02ef1f7dd7805c8ab3f2233a9f35f48e5794f8e76a0616a6c952b2488070b86"),
    ("w46b_p2.mp4.part01", "d3496fd2990f7165a1d57429643bd57a037e35b184caf77b62a9663d75d6337b"),
]

def main():
    target = ROOT / "src" / "w46b_p2.mp4"
    temporary = target.with_suffix(".mp4.restoring")
    full = hashlib.sha256()
    with temporary.open("wb") as output:
        for name, expected in PARTS:
            part = ROOT / "src" / "original-parts" / name
            digest = hashlib.sha256()
            with part.open("rb") as source:
                while chunk := source.read(1024 * 1024):
                    digest.update(chunk)
                    full.update(chunk)
                    output.write(chunk)
            if digest.hexdigest() != expected:
                raise SystemExit(f"Checksum mismatch: {name}")
    if full.hexdigest() != EXPECTED:
        raise SystemExit("Reconstructed file checksum mismatch")
    temporary.replace(target)
    print(f"VERIFIED {target}: {target.stat().st_size:,} bytes; SHA256 {EXPECTED}")

if __name__ == "__main__":
    main()
