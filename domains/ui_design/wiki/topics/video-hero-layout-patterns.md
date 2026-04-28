# Video Hero Layout Patterns

## Purpose

This rule set is for premium full-screen Hero sections, landing page openings,
SaaS / app launch pages, portfolio first screens, coding education platforms,
and cinematic product websites.

The goal is to avoid generic centered hero templates and provide multiple
high-end hero compositions using video, typography, glass, navigation, CTA
systems, and information clusters.

## Core Principle

A premium hero should choose a clear composition model before coding.

Do not default to the same centered layout every time.

Recommended hero composition models:

1. Top-aligned cinematic hero.
2. Bottom-left cinematic hero.
3. Full-screen MP4 dark video hero.
4. Centered SaaS / App video hero.
5. Strict grayscale liquid glass hero.
6. Two-panel liquid glass split hero.
7. Technical education HLS hero.

A premium hero should use video, typography, glass material, navigation, CTA,
and information clusters to create a clear visual direction instead of a generic
template.

## Top-Aligned Cinematic Hero

Use when the page needs a campaign-like, bold, brand-launch feeling.

Suitable for:

- design agency
- creative product launch
- campaign landing page
- brand announcement page
- high-impact homepage

Rules:

- Container uses `min-h-screen`.
- Content is aligned near the top, not vertically centered.
- Use large top padding: mobile around `pt-32`, desktop around `pt-48`.
- Use dark video or strong visual background.
- Use a large uppercase headline.
- Line height should be very tight, around `0.98`.
- Letter spacing should be negative, around `-2px` to `-4px`.
- This layout creates pressure and impact through top alignment, giant type,
  and strong CTA.

Typography:

- Font: Rubik or strong geometric sans.
- Weight: bold.
- Transform: uppercase.
- Color: white.
- Mobile size: `text-6xl`.
- Tablet size: `text-8xl`.
- Desktop size: around `100px`.
- Line-height: `0.98`.
- Letter-spacing: `-2px` to `-4px`.

CTA:

- CTA can use a custom SVG background shape instead of a normal rounded
  rectangle.
- Fixed-size CTA can be used for a brand-campaign effect.
- Example size: `184px` by `65px`.
- SVG fills the entire button container.
- Text sits above the SVG and is centered.
- Text should be bold and uppercase.
- Hover: `scale-105`.
- Active: `scale-95`.

Avoid:

- Do not center this type of hero vertically by default.
- Do not use small body-like headlines.
- Do not use generic rounded buttons if the brand direction calls for a custom
  CTA shape.

## Bottom-Left Cinematic Hero

Use when the hero should feel like a film poster, luxury campaign, editorial
website, or visual-first portfolio.

Suitable for:

- portfolio
- film-like landing page
- luxury / fashion / art direction
- cinematic product homepage
- visual-first startup landing page

Rules:

- Use a full-screen video background.
- Content is positioned bottom-left instead of centered.
- Navbar floats above the video.
- Content max-width must be controlled.
- Use a local dark gradient or vignette behind the text.
- White text must not sit directly over bright video areas.

Recommended z-index:

- video: `z-0`
- overlay: `z-5`
- content: `z-10` or `z-20`
- navbar: `z-50`

Readability:

- Add bottom gradient when content sits near the bottom.
- Add left-side gradient when text sits on the left.
- Use directional overlays instead of only a generic black overlay.

Key idea: bottom-left cinematic hero should feel like a film poster, not a
generic SaaS template.

## Full-Screen MP4 Dark Video Hero

Use when a simple MP4 background is enough and HLS is not required.

Suitable for:

- dark premium hero
- simple cinematic background
- MVP landing page
- static marketing page with one video
- atmospheric brand hero

Implementation:

```tsx
<video
  autoPlay
  loop
  muted
  playsInline
  className="absolute inset-0 w-full h-full object-cover z-0"
>
  <source src="<mp4-url>" type="video/mp4" />
</video>
```

Rules:

- MP4 does not need hls.js.
- Use native video tag.
- Required attributes: `autoPlay`, `loop`, `muted`, `playsInline`.
- Layout: `absolute`, `inset-0`, `w-full`, `h-full`, `object-cover`, `z-0`.
- Content must sit above video at `z-10` or `z-20`.
- Add dark overlay or gradient fade if text readability is weak.
- If the video is already dark and stable, overlay may be omitted, but
  readability must be checked.

Avoid:

- Do not crop important product visuals by accident.
- Do not place text directly over bright video areas.
- Do not let the video dominate CTA readability.

## Centered SaaS / App Video Hero

Use for polished SaaS, app, booking, AI product, and product launch pages.

Suitable for:

- SaaS homepage
- AI app landing page
- booking / travel platform
- software product launch
- startup landing page

Rules:

- Hero content is centered vertically and horizontally.
- Use full-screen video background.
- Navbar can be transparent full-width overlay instead of pill navbar.
- Use a tagline pill above the headline.
- Use one or two CTAs below the subtext.
- Desktop shows nav links and action buttons.
- Mobile hides desktop navigation and uses hamburger plus full-screen overlay
  menu.

Tagline pill:

- Use glass container.
- Height around `38px`.
- Radius around `10px`.
- Include an inner solid badge such as `New`.
- Follow with a short version/update message.
- Useful format: `New` plus `Say Hello to Product v3.2`.

CTA:

- Primary CTA uses brand color.
- Secondary CTA uses dark neutral or dark brand shade.
- Buttons should share the same height and radius.
- Hover should slightly lighten backgrounds.
- Avoid large motion or bouncy interactions.

Mobile navigation:

- Hide desktop links/buttons.
- Show hamburger.
- Hamburger opens a full-screen dark overlay menu.
- Do not cram desktop navigation into mobile.

## Multi-Font Role Split

High-end hero pages can use multiple fonts if each font has a clear role.

Do not use many fonts randomly.

Recommended role splits:

- App / SaaS video hero: Manrope for UI/navigation, Cabin for buttons/tags,
  Instrument Serif for headline, Inter for body.
- Strict liquid glass brand hero: Poppins for display/body, Source Serif 4 for
  serif accent.
- Technical education hero: Inter Extra Bold for headline, Plus Jakarta Sans
  for eyebrow, Instrument Serif italic for emphasis.

Rules:

- Display, UI, button, and body can differ.
- Font role must be explicit.
- Serif italic is best used for short emphasis inside headings, not as full
  body text.
- Dashboard and workspace UI often work better with Inter plus Outfit.
- Brand, art, and editorial hero pages can use sans plus serif accent.

## Strict Grayscale Liquid Glass Hero

Use when the design should feel premium, artistic, and restrained.

Suitable for:

- luxury AI product
- art / creative platform
- plant / floral / lifestyle AI product
- high-end editorial landing page
- minimal cinematic brand page

Rules:

- Use strict grayscale only.
- No colored accents.
- Use HSL grayscale tokens only, such as `0 0% X%`.
- Text hierarchy should rely on white opacity: primary `text-white`,
  secondary `text-white/80`, body `text-white/60`, muted `text-white/50`.
- Use glass material, typography, layout, video atmosphere, spacing, blur, and
  pseudo-element rim effects to create premium feel.
- Do not suddenly introduce purple, cyan, green, orange, or other colored
  accents.

Core idea: premium does not always require colored gradients. It can come from
strict grayscale, material quality, layout, and typography.

## Two-Tier Liquid Glass System

Serious glass UI should use at least two glass tiers.

Light glass is used for:

- pills
- chips
- social buttons
- small cards
- secondary controls
- feature cards

Light glass traits:

- lower blur
- lighter visual weight
- supporting role

Strong glass is used for:

- CTA
- large panels
- main overlays
- primary cards
- major information blocks

Strong glass traits:

- stronger blur
- stronger inset highlight
- stronger pseudo-border
- more physical and closer to the viewer

Rules:

- Do not use the same glass intensity everywhere.
- Glass UI needs hierarchy.
- `.liquid-glass` should be used for light elements.
- `.liquid-glass-strong` should be used for CTA and major panels.
- Strong glass should dominate only where hierarchy requires it.

## Advanced Glass Border Rule

Normal quick draft:

- `border-white/20`

Premium glass:

- `::before` pseudo-element
- padding: `1px` to `1.5px`
- linear-gradient border
- `mask-composite: exclude` / `xor`

Rules:

- Premium glass boundaries should come from pseudo-element gradient rim when
  possible.
- Normal borders are acceptable for quick drafts but not enough for premium
  output.
- Gradient rims can be brighter at top/bottom and transparent in the middle to
  mimic glass edges.
- Do not make the rim too thick.
- Use pseudo-rim especially for glass panels, glass CTA, glass cards, floating
  controls, and social pills.

## Two-Panel Liquid Glass Split Hero

Use for premium creative platforms, AI products, design platforms,
art/lifestyle products, and visual-generation platforms.

Layout:

- full-screen video background
- flex row
- `min-h-screen`
- left panel around `52%`
- right panel around `48%`
- right panel hidden on mobile

Left panel:

- brand navigation
- logo
- large headline
- CTA
- tags / pills
- quote / brand statement

Right panel:

- social icon pill
- account / sparkle button
- community card
- feature preview cards
- bottom feature card
- thumbnail / plus button

Rules:

- Left side carries main narrative.
- Right side carries secondary information clusters.
- Both sides should float above video using glass containers.
- Mobile should prioritize the left main narrative.
- Do not force the right panel onto small screens.

## Hero Information Cluster

A premium hero can include a small content system next to the main headline.

Information clusters can include:

- social proof
- community entry
- social icons
- feature preview
- mini cards
- product teaser
- account CTA
- quote
- tags
- stats
- version badge

Rules:

- Information clusters must support the main hero narrative.
- They should not feel like random floating decoration.
- Main headline is always first-level hierarchy.
- Information cluster is second-level hierarchy.
- Use glass cards or small panels to group cluster content.
- Good locations: right side, bottom area, above headline, or near CTA.

## Technical Education HLS Hero

Use for coding education, technical career platforms, engineering learning
products, or career-ready curriculum landing pages.

Suitable for:

- coding education
- technical bootcamp
- career-ready curriculum
- engineering course platform
- developer portfolio landing page

Core pattern:

- HLS video background
- hls.js implementation
- video opacity around `60%`
- dark left gradient
- bottom-up gradient
- desktop vertical grid lines
- central SVG ellipse glow
- floating `200px` by `200px` glass info card
- large uppercase headline
- single accent punctuation

HLS:

- Use hls.js for `.m3u8`.
- Use native HLS if browser supports it.
- Use MP4 fallback if provided.
- In sandboxed environments, use `enableWorker: false` for stability.

Video readability:

- Video opacity can be around `60%`.
- Left-side text uses left gradient.
- Bottom content uses bottom gradient.
- Do not rely only on one black transparent overlay.

Technical grid:

- Place vertical lines at `25%`, `50%`, and `75%`.
- Opacity around `white/10`.
- Show on desktop.
- Hide or reduce on mobile.
- Use grid lines to create engineering structure, not noise.

SVG glow:

- Use SVG ellipse.
- Apply Gaussian blur.
- Blur around `20px` to `40px`.
- Color should match accent.
- Place behind content, not over text.

Floating glass info card:

- Size around `200px` by `200px`.
- Position above headline.
- Can be shifted upward with `translate-y-[-50px]`.
- Use for year, credibility, instructor proof, feature highlight, or product
  claim.
- Serif italic can be used for one emphasized word.

## Single Accent Punctuation Rule

A premium title does not always need a full gradient.

A more restrained approach:

- color only one word
- or one punctuation mark
- or one symbol

Examples:

- final period
- slash
- bracket
- cursor
- keyword

Rules:

- Works especially well in minimal technical hero pages.
- More premium than applying gradient to the whole headline.
- Use when the overall color system is restrained.
- Do not overuse accents.

## CTA Button Patterns

Custom SVG-shaped CTA:

- Use when the brand needs a more distinctive or playful CTA.
- SVG fills the button container.
- Text is centered above the SVG.
- Fixed dimensions can be used for campaign pages.
- Example size: `184px` by `65px`.
- Hover: `scale-105`.
- Active: `scale-95`.

Dual CTA:

- Use for SaaS, app landing, AI product, or booking platform.
- Primary CTA uses brand color.
- Secondary CTA uses dark neutral or deep brand shade.
- Both buttons should share height and radius.
- Hover should be subtle.

Glass CTA:

- Use for video backgrounds and liquid glass hero pages.
- Use strong glass.
- Add icon in circular container if appropriate.
- Hover: `scale-105`.
- Active: `scale-95`.
- Do not mix too many button systems in one hero.

General:

- CTA should visually match hero style.
- Avoid large bouncing animations.
- Avoid too many button variants in one hero.

## Video Hero Navigation Patterns

Transparent overlay navbar:

- Suitable for full-screen video hero, SaaS app first screen, and product launch
  pages.
- Use full width.
- Use transparent background.
- Use `z-20` or higher.
- Desktop padding can be wide, such as `px-[120px]`.
- Put logo on left, links center or center-left, actions on right.

Glass navigation:

- Suitable for busy backgrounds, video with changing brightness, and floating
  control feel.
- Can be full-width glass header or pill-style nav.
- Must not compete with hero headline.
- Check contrast on video backgrounds.

Mobile navigation:

- Hide desktop links/buttons.
- Show hamburger.
- Open full-screen dark overlay menu.
- Menu must be functional.
- Do not squeeze desktop navigation into mobile.

## Video Background Implementation Rules

MP4:

- Use native video tag.
- Use `autoPlay`, `loop`, `muted`, `playsInline`.
- Use `object-cover`, `absolute inset-0`, `w-full h-full`, `z-0`.

HLS:

- Use hls.js for `.m3u8`.
- Use native HLS if supported.
- Use MP4 fallback if provided.
- Use `enableWorker: false` in sandboxed preview environments if needed.

Overlay:

- Generic black overlay is acceptable but less refined.
- Directional overlays are better:
  - left text uses left-to-right dark gradient
  - bottom text uses bottom-up gradient
  - centered text uses radial or central contrast layer

Readability:

- Always check text contrast.
- White text on bright video needs gradient support.
- Video opacity can be reduced, for example `60%`.
- Do not let the video steal attention from CTA.

## Landing Page Hero Categories

Campaign Hero:

- top-aligned
- uppercase giant title
- SVG CTA
- strong visual background

Cinematic Poster Hero:

- bottom-left content
- full-screen video
- cinematic overlay
- editorial typography

SaaS App Hero:

- centered content
- tagline pill
- dual CTA
- transparent navigation
- mobile full-screen menu

Creative AI Split Hero:

- two-panel layout
- liquid glass panels
- left narrative
- right information cluster
- video background

Technical Education Hero:

- HLS video
- technical grid
- SVG glow
- floating glass info card
- career-ready eyebrow
- uppercase headline
- single accent punctuation

Strict Grayscale Hero:

- no colored accent
- white opacity hierarchy
- glass plus typography plus video plus spacing

## Avoid

- Do not default every hero to centered text.
- Do not use video background without readability checks.
- Do not overuse colored gradients when grayscale glass would be more premium.
- Do not use normal border classes for advanced liquid glass if pseudo-rim is
  available.
- Do not use HLS without fallback or native support check.
- Do not force desktop navigation into mobile.
- Do not use the same glass strength for every component.
- Do not introduce colored accents inside strict grayscale systems.
- Do not let information clusters feel like random decoration.
- Do not mix too many CTA styles in one hero.
- Do not overuse full-line gradient headlines.
- Do not let the video overpower the content.
