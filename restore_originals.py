#!/usr/bin/env python3
"""Restore byte-identical presenter part 1 from GitHub-sized binary chunks."""
import hashlib
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
EXPECTED = "5d0527b4a6e6"

def main():
    source = ROOT / "src" / "original-parts"
    parts = [source / f"w46b_p1.mp4.part{i:02d}" for i in range(2)]
    for part in parts:
        if not part.is_file():
            raise SystemExit(f"Missing chunk: {part}")
    expected = (ROOT / "ORIGINAL-SHA256.txt").read_text().split()[0]
    target = ROOT / "src" / "w46b_p1.mp4"
    temporary = target.with_suffix(".mp4.restoring")
    with temporary.open("wb") as out:
        for part in parts:
            with part.open("rb") as incoming:
                shutil.copyfileobj(incoming, out)
    with temporary.open("rb") as incoming:
        digest = hashlib.file_digest(incoming, "sha256").hexdigest()
    if digest != expected:
        temporary.unlink()
        raise SystemExit(f"Checksum mismatch: {digest} != {expected}")
    temporary.replace(target)
    print(f"Restored {target.relative_to(ROOT)} ({target.stat().st_size:,} bytes)")
    print(f"SHA256 {digest} VERIFIED")

if __name__ == "__main__":
    main()
