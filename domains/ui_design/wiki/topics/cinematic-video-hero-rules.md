# Cinematic Video Hero Rules

Video heroes create atmosphere and make premium pages feel like product
launches or film title frames. They are suitable for high-end landing pages,
AI product sites, portfolios, editorial product pages, and design agency
websites.

## Hero Layout

- Avoid generic left-text-right-image by default.
- Use full-bleed or large poster composition.
- Put video at `z-0`, overlay at `z-0` or `z-5`, content at `z-10` or `z-20`, navbar at `z-50`.
- Use large centered headline, short subheadline, CTA row, and a floating navbar.
- Add gradient fades for readability.

## Video Attributes

Base attributes:

- `autoPlay`
- `muted`
- `loop` or manual custom loop
- `playsInline`
- `preload="auto"`

Layout:

- Atmospheric background video: `object-cover`.
- Product/light/transparent video: `w-full h-auto`; avoid cropping.
- Text overlay requires gradient fade.
- z-index must be explicit.

Common overlays:

- `bg-black/20`
- `bg-gradient-to-t from-black to-transparent`
- `bg-gradient-to-b from-black via-transparent to-black`
- Bottom fade height `160px` to `300px` depending on contrast.

## Premium Loop Behavior

If a video hard-cuts, use a manual `requestAnimationFrame` driven fade loop:

- Fade in over `0.5s` at start.
- Fade out over `0.5s` before the end.
- On ended: opacity `0`.
- Wait `100ms`.
- Reset `currentTime = 0`.
- Play again.
- Fade back to `1`.

## HLS

- Use hls.js for `.m3u8` when the browser needs it.
- Fallback to native HLS when possible.
- Fallback to MP4 when HLS fails if provided.

## Avoid

- Cropping important product/video content by accident.
- Placing white text over bright video without overlay.
- Letting video steal attention from CTA.
- Heavy CSS blur on full-screen video.
- Motion that makes reading difficult.
