#!/usr/bin/env python3
"""news-image-20261122 — entry point.

The picture for Sunday 22 November 2026, "THE WORLD IN ONE PAGE",
sits next to this file as entry.png. It was drawn fresh in this
session by build_image.py from the day's real news: the Gulf war
widening (Iran striking US bases in Bahrain again, tankers hit off
Oman, a crashed Patriot interceptor), COP31 deadlocked over fossil
fuels, the Sparta II ablaze in the Baltic, Estonia shutting its
border, and thirty more stories first reported on 22 November 2026.

This program has a single job: copy that PNG to the output folder
byte for byte. Standard library only — no network, no randomness,
no arguments — so two runs write identical files. Before copying it
checks the file is a whole PNG within the competition's limits
(at most 1 MiB, at most 1024 by 1024), reading the dimensions
straight out of the IHDR chunk with struct.

Usage:
    MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PNG = HERE / "entry.png"

MAX_BYTES = 1_048_576
MAX_SIDE = 1024
MAGIC = b"\x89PNG\r\n\x1a\n"


def check_png(data):
    """Return (width, height) or raise ValueError for a bad file."""
    if len(data) > MAX_BYTES:
        raise ValueError(f"entry.png is {len(data)} bytes, over the 1 MiB cap")
    if not data.startswith(MAGIC):
        raise ValueError("entry.png does not start with the PNG magic bytes")
    if len(data) < 33 or data[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk where one belongs")
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_SIDE or height > MAX_SIDE:
        raise ValueError(f"entry.png is {width}x{height}, over the 1024 cap")
    return width, height


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    data = PNG.read_bytes()
    width, height = check_png(data)
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(data)
    # Read it back: a short or partial write must fail loudly here,
    # not surface later as two runs writing different bytes.
    if target.read_bytes() != data:
        raise ValueError(f"{target} did not round-trip byte for byte")
    print(f"wrote {target} ({width}x{height}, {len(data)} bytes)")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as exc:
        print(f"main.py: {exc}", file=sys.stderr)
        raise SystemExit(1)
