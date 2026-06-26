# Aerial Photography VA — Brand Assets

All marks are vector SVGs — infinitely scalable, embed-friendly.

## Files

| File | Use |
| --- | --- |
| `logo-lockup-light.svg` | Full primary lockup on light backgrounds (site header, invoices, letterhead) |
| `logo-lockup-dark.svg` | Full primary lockup on dark backgrounds (portfolio covers, hero overlays) |
| `wordmark-only.svg` | Just the typeset name — for tight horizontal spaces |
| `drone-mark.svg` | The drone icon, full color (black + orange) — primary icon use |
| `drone-mark-black.svg` | One-color black icon — embroidery, stamps, single-color print |
| `drone-mark-white.svg` | One-color white icon — for use on dark photos / backgrounds |
| `avatar-orange.svg` | 512×512 rounded-square avatar, orange background — Instagram, profile photos |
| `avatar-dark.svg` | 512×512 rounded-square avatar, dark background — alternative profile photo |
| `favicon.svg` | 64×64 favicon — browser tab, mobile bookmark icon |

## Colors

| Name | Hex | Use |
| --- | --- | --- |
| Ink | `#1A1A1A` | Wordmark, drone body, rules |
| Signal Orange | `#E85D3A` | Camera hub, accent, cert chip |
| Paper | `#FAFAF7` | Light background, inverse fill |

## Type

- **Archivo Black** (900) — wordmark, headlines
- **JetBrains Mono** (700) — Part 107 chip, metadata labels, rules

Both are available free on Google Fonts. To use the lockup SVGs as-is on the web, make sure these fonts are loaded on the page where the SVG appears (your site already loads them). For maximum portability when sending the lockup to clients or printers, outline the text in a vector editor first.

## Web usage

```html
<!-- favicon -->
<link rel="icon" type="image/svg+xml" href="/logo/favicon.svg">

<!-- inline lockup -->
<img src="/logo/logo-lockup-light.svg" alt="Aerial Photography VA" width="440">

<!-- icon only -->
<img src="/logo/drone-mark.svg" alt="" width="48" height="48">
```

## Clear space

Minimum clear space around any mark = the height of the drone icon on all sides. Don't crowd it.

## Don't

- Don't recolor the orange (it's the trust signal — Part 107 chip + camera hub stay #E85D3A)
- Don't stretch or skew the drone mark
- Don't drop the Part 107 chip from the primary lockup unless space genuinely forces it
- Don't put the color drone on a busy photo — use `drone-mark-white.svg` for watermarks
