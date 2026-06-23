# Aerial Photography — website

Static marketing + portfolio site for **Aerial Photography** (drone photo/video,
Central Virginia).

## Pages
- `index.html` — main page (the "Golden Atlas" design)
- `portfolio.html` — full portfolio, grouped by category and sub-category

## How to view / test
Open `index.html` in any web browser. It needs an internet connection — it loads
the fonts and a small page runtime from a CDN; the photos themselves are local in
`images/`.

To update this folder on another device from GitHub, double-click `pull.bat`.

## Photos
Web-ready images live in `images/` (main-page top 8 = `images/aerial-0*.jpg`;
portfolio = `images/portfolio/<category>/`). These are optimized copies of the
master library, which is kept off GitHub (too large). On a machine that has the
master `Photos/` folder, rebuild them with:

```
python -m pip install Pillow
python optimize_photos.py
```

## Going live
This repo is private. To publish for free via **GitHub Pages**, the repo needs to
be public (or on a paid plan); then enable Pages on the `main` branch in the
repo's Settings. Until then, testing is local (open `index.html`).
