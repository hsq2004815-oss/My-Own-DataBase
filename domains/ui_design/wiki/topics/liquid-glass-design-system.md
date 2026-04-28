# Liquid Glass Design System

Use Liquid Glass as a premium material system, not as `bg-white/10
backdrop-blur` sprinkled everywhere. It is preferred for high-end landing
pages, AI product pages, design agency pages, cinematic heroes, portfolio
surfaces, and selected controls. It remains optional for ordinary admin tables,
dense forms, and CRUD dashboards.

For advanced Web App, SaaS Workspace, Dashboard, and AI Project Workspace
tasks, use `liquid-glass-web-app-ui-kit.md` as the component-system layer.
That topic is not a landing page rule: it defines workspace tokens, project
cards, toolbar search, tabs, modals, validation, toasts, and disabled/loading
states.

## Web App UI Kit Tokens

For light glass workspace surfaces, prefer:

- `blur-sm`: `blur(18px) saturate(160%)`
- `blur-md`: `blur(24px) saturate(180%)`
- `blur-lg`: `blur(28px) saturate(185%)`
- `fill-light`: `rgba(255,255,255,0.48)`
- `fill-thick`: `rgba(255,255,255,0.62)`
- `rim`: `rgba(255,255,255,0.55)`
- `rim-bright`: `rgba(255,255,255,0.68)`
- `shadow-outer`: `0 14px 36px rgba(31,38,135,0.16)`
- `shadow-thick`: `0 22px 54px rgba(20,30,60,0.28)`
- `highlight`: `inset 0 1px 1px rgba(255,255,255,0.80)`
- `inset-dark`: `inset 0 -1px 3px rgba(20,30,60,0.18)`

For dark neon workspace cards, prefer:

- `fill`: `rgba(8,10,16,0.78)`
- `secondary fill`: `rgba(15,23,42,0.64)`
- `rim`: `rgba(255,255,255,0.18)`
- `rim-hover`: `rgba(255,255,255,0.42)`
- `cyan glint`: `rgba(34,211,238,0.36)`
- `magenta glint`: `rgba(217,70,239,0.30)`
- `orange glint`: `rgba(251,146,60,0.20)`
- `deep shadow`: `0 24px 60px rgba(2,6,23,0.34), 0 8px 24px rgba(15,23,42,0.22)`
- `neon ring`: `0 0 0 1px rgba(34,211,238,0.38), 0 0 24px rgba(217,70,239,0.24)`

Radius tokens:

- field: `22px`
- card: `28px`
- modal: `40px`
- pill: `999px`

## Two Levels Of Glass

Subtle liquid glass:

- Use for navbars, badges, chips, cards, stat blocks, secondary panels.
- Background: `rgba(255,255,255,0.01)` to `rgba(255,255,255,0.12)`.
- `backdrop-filter: blur(4px)` to `blur(16px)`.
- Include `-webkit-backdrop-filter`.
- Add inset highlight shadow.
- Add subtle gradient border.
- Use `position: relative` and `overflow: hidden`.

Strong liquid glass:

- Use for primary CTAs and emphasized controls.
- `backdrop-filter: blur(40px)` to `blur(50px)`.
- Subtle outer shadow.
- Stronger inset highlight.
- Gradient rim border.
- `rounded-full` for nav, badges, and CTA; `rounded-2xl` or `rounded-3xl` for cards.

## Hero Glass System

For video hero and landing page openings, use the two-tier glass system from
`video-hero-layout-patterns.md`:

- Light glass for pills, chips, social buttons, small cards, secondary controls,
  and feature cards.
- Strong glass for CTA, large panels, main overlays, primary cards, and major
  information blocks.

Do not use the same glass intensity everywhere. Hero glass needs hierarchy:
`.liquid-glass` for supporting elements and `.liquid-glass-strong` for CTA or
major panels.

Strict grayscale Liquid Glass heroes must avoid colored accents entirely. Use
HSL grayscale tokens, white opacity hierarchy, glass material, typography,
video atmosphere, spacing, blur, and pseudo-element rim effects to create the
premium feel.

## High-End Glass Border

Prefer a pseudo-element gradient border:

- `::before` with `inset: 0`.
- `border-radius: inherit`.
- Padding around `1px` to `1.5px`.
- Linear gradient with stronger top/bottom opacity and transparent middle.
- Mask-composite exclude/xor trick where supported.

Normal `border-white/20` is acceptable for quick drafts, but premium hero
glass should use `::before`, `1px` to `1.5px` padding, gradient rim, and
`mask-composite: exclude` / `xor` where possible.

## Layout Rules

- Use glass where background media or ambient scenery gives the blur meaningful visual input.
- Keep text on stable surfaces; do not place small text directly on busy media.
- Reserve strong glass for hero controls, selected states, modals, and premium CTA surfaces.
- In Web App / Workspace / Dashboard tasks, reserve strong glass for hero
  summary panels, toolbar actions, selected cards, modals, and feedback. Do not
  convert the workspace into a landing-page hero.
- Do not apply backdrop-filter to hundreds of repeated rows.
- Avoid edge-to-edge stacked glass layers because seams and optical noise become visible.

## Accessibility

- Provide fallback solid/translucent colors when backdrop-filter is unsupported.
- Check contrast on final composited surfaces.
- Respect reduced transparency where practical.
- Use icons or labels in addition to glow for selected, error, and success states.

## Implementation Notes

Use CSS custom properties for glass opacity, blur, rim opacity, highlight
strength, and background dim. Keep animated filters limited; animate transform
and opacity instead of full-screen blur radius.

For workspace components, define primitives such as `glass-card`,
`glass-thick`, `glass-dark`, `glass-pill`, `glass-pill-primary`,
`glass-input`, `glass-toggle`, `tab-bar`, `tab`, `glass-icon-button`,
`glass-modal`, and `glass-toast`. Each primitive must include hover, focus,
loading, disabled, validation, and fallback states where applicable.
