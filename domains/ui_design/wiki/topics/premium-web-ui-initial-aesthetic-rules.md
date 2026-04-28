# Premium Web UI Initial Aesthetic Rules

## Goal

When an agent designs Web UI, landing pages, SaaS pages, dashboards,
portfolios, or product websites, it should not default to generic templates.
The default target is premium, cinematic, responsive, visually disciplined,
and implementation-ready.

High-end UI comes from restraint, spacing, hierarchy, typography, material
quality, controlled color, cinematic media, subtle motion, and responsive
composition. Avoid generic blue-white SaaS templates unless explicitly
requested.

## Default Visual Directions

Choose one dominant direction based on task context. Do not mix all styles at once.

1. Dark cinematic glass.
2. Black-white neutral SaaS.
3. White editorial luxury.
4. Portfolio editorial dark.
5. Video-first immersive landing page.
6. Premium AI product or design agency landing page.
7. Liquid Glass Web App / SaaS Workspace / Dashboard UI Kit.

Use direction 7 when the task is an app surface rather than a marketing page:
AI project workspace, SaaS dashboard, internal tool, project management
workspace, app UI kit, control-heavy dashboard, or a screen with search, tabs,
cards, modal forms, validation, and toast feedback. In this mode, do not default
to landing-page hero composition.

## Color Rules

Dark premium UI:

- Background: `#000000`, `#010101`, `#0A0A0A`, or `hsl(0 0% 4%)`.
- Main text: white or `white/95`.
- Body text: `white/60` to `white/80`.
- Muted text: `white/40` to `white/60`.
- Border: `white/5` to `white/15`.
- Surface: `rgba(255,255,255,0.03)` to `rgba(255,255,255,0.12)`.

Accent systems:

- Use only one accent system per page.
- Recommended purple/pink gradient: `#FA93FA -> #C967E8 -> #983AD6`.
- Recommended blue steel gradient: `#89AACC -> #4E85BF`.
- Recommended monochrome precision: black, white, neutral-900, and opacity variants only.

White editorial UI:

- Background: `#FFFFFF`.
- Headline, logo, and CTA: `#000000`.
- Description and nav muted text: `#6F6F6F`.
- Rely on typography, spacing, video, and composition rather than colorful gradients.

Avoid mixing purple, blue, green, orange, and pink in one page; default bright
blue SaaS primary colors; heavy shadows on dark surfaces; thick borders; and
low-contrast gray text on glass.

## Typography Rules

Use separate display and body fonts when possible.

Recommended pairings:

- Instrument Serif italic + Inter.
- Instrument Serif italic + Barlow.
- Readex Pro + Readex Pro.
- Inter + Inter.
- Geist + Inter for black-white developer SaaS.

Hero titles should be very large, short, memorable, and tightly set:
line-height `0.8` to `0.95`, letter-spacing `-0.02em` to `-0.05em`,
font-weight `400` to `500`. Avoid default `font-bold` unless the brand
requires it.

Section headings should use `text-4xl` to `text-6xl`, tight line-height, and
clear contrast with body text. Body copy should be small but readable,
`white/60` to `white/80` on dark backgrounds, with max-width around `32ch` to
`64ch`.

## Hero Section Rules

Avoid generic left-text-right-image by default. Prefer one of these:

1. Center cinematic poster hero: floating navbar, large centered headline,
   short subheadline, CTA row, cinematic video or image background, gradient
   readability fades.
2. Giant staggered typography hero: absolute-positioned huge words,
   magazine-cover composition, minimal palette, useful for data, security, AI,
   finance, and creative portfolios.
3. Video-first immersive hero: video `z-0`, overlay `z-0` or `z-5`, content
   `z-10` or `z-20`, navbar `z-50`, explicit readability overlay.
4. Product or design agency hero: announcement pill, gradient headline or
   editorial serif title, glass CTA, logo cloud or partner row, video or
   animated visual below hero text.

Hero should feel like a launch page or film title frame, not a generic template.

## Web App / Dashboard Rules

When the task is a Web App, SaaS Workspace, Dashboard, or AI Project Workspace,
prioritize component-system polish over marketing sections:

- Use a contained app shell, ambient background, and a functional hero or
  summary glass panel.
- Put search, filters, and primary actions in a glass toolbar.
- Use a glass tab bar for project/status filters.
- Use a responsive card grid for workspace entities.
- Include create/edit glass modal, validation states, disabled states, loading
  shimmer, and toast feedback.
- Use Liquid Glass UI Kit tokens and components from
  `liquid-glass-web-app-ui-kit.md`.
- Do not treat this pattern as a normal landing page or SaaS homepage.

## Navbar Rules

Default premium navbar:

- Fixed or absolute top, `z-50`.
- `px-6` to `px-8`, `lg:px-16`.
- Floating pill structure.
- Left logo, center nav links in a glass pill, right CTA or invisible spacer for balance.
- Use `bg-neutral-900/90` or `bg-black/20`, `backdrop-blur-md`, `border-white/10`, `rounded-full`.
- On mobile, hide center links, keep logo and primary CTA, and do not cram desktop navigation into mobile.

## Button Rules

Primary CTA styles:

- Dark page: white button with black text, or strong liquid glass.
- White page: black button with white text.
- Video/glass page: strong liquid glass.

CTA composition should use text plus an ArrowUpRight icon, text plus circular
icon container, or a secondary action with Play icon. Hover should be
restrained: `hover:scale-[1.03]`, `hover:scale-105`,
`hover:bg-neutral-200`, or gradient-border change. Avoid bouncing, rainbow
glow, too many button variants, and unclear primary action.

## Responsive Rules

Mobile:

- Hide desktop nav links.
- Stack vertically.
- Keep CTA visible.
- Use `clamp()` or viewport-based sizes for huge typography.
- Avoid horizontal overflow.
- Reduce parallax and heavy effects.

Desktop:

- Use asymmetry, large whitespace, and clear z-index layering.
- Let hero sections breathe.
- Do not fill every empty area.

Recommended type scale:

- Hero heading: `text-5xl -> md:text-7xl -> lg:text-[5.5rem]`.
- Giant type: `text-[14vw] md:text-[13vw]`.
- Section heading: `text-4xl -> md:text-5xl -> lg:text-6xl`.

## Negative Rules

Do not generate generic blue-white SaaS templates, big random gradient
backgrounds, many colors at once, thick borders, heavy dark-mode shadows,
same-size card grids everywhere, over-centered layouts for every section,
excessive animations, accidentally cropped video content, unclear z-index
layering, desktop nav forced into mobile, or adjective-only style notes without
implementable CSS/layout rules.
