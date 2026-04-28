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

For more specific composition choices, use `video-hero-layout-patterns.md`.
Choose a model before coding: top-aligned campaign, bottom-left cinematic
poster, full-screen MP4 dark video, centered SaaS/app video, strict grayscale
Liquid Glass, two-panel Liquid Glass split hero, or technical education HLS
hero.

## Composition Models

Top-aligned cinematic hero:

- Use for campaign, brand launch, creative product, and high-impact homepage.
- Align content near the top with large padding, around `pt-32` mobile and
  `pt-48` desktop.
- Use uppercase giant type, line-height around `0.98`, and letter-spacing
  around `-2px` to `-4px`.
- CTA may use a fixed-size custom SVG background shape, for example `184px` by
  `65px`.

Bottom-left cinematic hero:

- Use for film-poster, luxury, fashion, portfolio, and visual-first startup
  pages.
- Position content bottom-left, not centered.
- Add bottom and left directional gradients behind text.
- Keep content max-width controlled and put navbar above video at `z-50`.

Centered SaaS / app video hero:

- Use for polished SaaS, booking, AI app, and software launch pages.
- Center content vertically and horizontally.
- Use a tagline pill above the headline, one or two CTAs, and transparent
  overlay navigation.
- Mobile navigation should use hamburger plus full-screen dark overlay menu.

Technical education HLS hero:

- Use for coding education, technical career platforms, bootcamps, and developer
  learning products.
- Combine HLS video, dark directional gradients, desktop vertical grid lines,
  SVG ellipse glow, floating `200px` glass info card, uppercase headline, and
  single accent punctuation.

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
- In sandboxed preview environments, use `enableWorker: false` when worker
  setup causes instability.

## CTA And Navigation

- Use transparent overlay navbar for clean SaaS/app video heroes.
- Use glass navigation for busy video backgrounds or changing brightness.
- Do not squeeze desktop links into mobile; use hamburger plus full-screen dark
  overlay menu.
- Match CTA to hero style: custom SVG CTA for campaign heroes, dual CTA for
  SaaS/app heroes, strong glass CTA for Liquid Glass video heroes.
- Avoid mixing too many button systems in one hero.

## Avoid

- Cropping important product/video content by accident.
- Placing white text over bright video without overlay.
- Letting video steal attention from CTA.
- Heavy CSS blur on full-screen video.
- Motion that makes reading difficult.
- Defaulting every video hero to centered text.
- Applying Web App / Dashboard UI Kit rules to marketing hero composition.
