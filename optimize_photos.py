#!/usr/bin/env python
"""
Optimize the master photo library (Photos/) into web-ready files (images/).

Why: the originals in Photos/ are full-resolution (4-27 MB each) — far too heavy
for a website. This downscales them to a long edge of MAX_EDGE px at JPEG quality
QUALITY, auto-orients by EXIF, and strips metadata. The Top-8 are already
web-sized, so they are copied verbatim.

Re-run any time you add photos to Photos/. It only writes outputs; it never
touches the master library. Requires Pillow:  python -m pip install Pillow
"""
from pathlib import Path
import shutil
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent
MAX_EDGE = 2000      # longest side, in px
QUALITY = 82         # JPEG quality

# (source path under Photos/, dest path under images/)
PORTFOLIO = [
    # Cityscape / Richmond Area
    ("portfolio/Cityscape/Richmond Area/RIC.JPG",            "portfolio/cityscape/richmond-01.jpg"),
    ("portfolio/Cityscape/Richmond Area/RIC1.JPG",           "portfolio/cityscape/richmond-02.jpg"),
    ("portfolio/Cityscape/Richmond Area/RIC3.JPG",           "portfolio/cityscape/richmond-03.jpg"),
    ("portfolio/Cityscape/Richmond Area/RIC4.JPG",           "portfolio/cityscape/richmond-04.jpg"),
    ("portfolio/Cityscape/Richmond Area/RIC5.JPG",           "portfolio/cityscape/richmond-05.jpg"),
    ("portfolio/Cityscape/Richmond Area/RIC7.JPG",           "portfolio/cityscape/richmond-06.jpg"),
    ("portfolio/Cityscape/Richmond Area/RIC8.JPG",           "portfolio/cityscape/richmond-07.jpg"),
    # Family
    ("portfolio/Family/FAMILY.JPG",                          "portfolio/family/family-01.jpg"),
    # Landscape & Nature / Animals
    ("portfolio/Landscape & Nature/Animals/ANIMAL.JPG",      "portfolio/landscape/animals-01.jpg"),
    ("portfolio/Landscape & Nature/Animals/ANIMAL (2).JPG",  "portfolio/landscape/animals-02.jpg"),
    ("portfolio/Landscape & Nature/Animals/ANIMAL (3).JPG",  "portfolio/landscape/animals-03.jpg"),
    ("portfolio/Landscape & Nature/Animals/ANIMAL (4).JPG",  "portfolio/landscape/animals-04.jpg"),
    # Landscape & Nature / Landscape
    ("portfolio/Landscape & Nature/Landscape/NATURE.JPG",    "portfolio/landscape/nature-01.jpg"),
    ("portfolio/Landscape & Nature/Landscape/NATURE1.JPG",   "portfolio/landscape/nature-02.jpg"),
    ("portfolio/Landscape & Nature/Landscape/RIver.JPG",     "portfolio/landscape/river-01.jpg"),
    ("portfolio/Landscape & Nature/Landscape/River (2).JPG", "portfolio/landscape/river-02.jpg"),
    ("portfolio/Landscape & Nature/Landscape/River (3).JPG", "portfolio/landscape/river-03.jpg"),
]

TOP8 = [(f"Website (Top 8)/aerial-0{i}.jpg", f"aerial-0{i}.jpg") for i in range(1, 9)]


def optimize(src: Path, dst: Path):
    dst.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im)        # honor camera orientation
        if im.mode != "RGB":
            im = im.convert("RGB")
        w, h = im.size
        scale = min(1.0, MAX_EDGE / max(w, h))
        if scale < 1.0:
            im = im.resize((round(w * scale), round(h * scale)), Image.LANCZOS)
        im.save(dst, "JPEG", quality=QUALITY, optimize=True, progressive=True)
    nw, nh = Image.open(dst).size
    kb = dst.stat().st_size / 1024
    print(f"  {dst.relative_to(ROOT).as_posix():46s} {nw}x{nh}  ar {nw/nh:4.2f}  {kb:6.0f} KB")


def main():
    photos = ROOT / "Photos"
    images = ROOT / "images"

    print("Top 8 (copied verbatim — already web-sized):")
    for s, d in TOP8:
        src, dst = photos / s, images / d
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.exists():
            shutil.copy2(src, dst)
            w, h = Image.open(dst).size
            print(f"  {dst.relative_to(ROOT).as_posix():46s} {w}x{h}  ar {w/h:4.2f}  {dst.stat().st_size/1024:6.0f} KB")
        else:
            print(f"  MISSING: {src}")

    print("\nPortfolio (downscaled):")
    for s, d in PORTFOLIO:
        src, dst = photos / s, images / d
        if src.exists():
            optimize(src, dst)
        else:
            print(f"  MISSING: {src}")


if __name__ == "__main__":
    main()
