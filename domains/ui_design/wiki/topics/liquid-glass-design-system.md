# Liquid Glass Design System

Use Liquid Glass as a premium material system, not as `bg-white/10 backdrop-blur` sprinkled everywhere. It is preferred for high-end landing pages, AI product pages, design agency pages, cinematic heroes, portfolio surfaces, and selected controls. It remains optional for ordinary admin tables, dense forms, and CRUD dashboards.

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

## High-End Glass Border

Prefer a pseudo-element gradient border:

- `::before` with `inset: 0`.
- `border-radius: inherit`.
- Padding around `1px` to `1.5px`.
- Linear gradient with stronger top/bottom opacity and transparent middle.
- Mask-composite exclude/xor trick where supported.

## Layout Rules

- Use glass where background media or ambient scenery gives the blur meaningful visual input.
- Keep text on stable surfaces; do not place small text directly on busy media.
- Reserve strong glass for hero controls, selected states, modals, and premium CTA surfaces.
- Do not apply backdrop-filter to hundreds of repeated rows.
- Avoid edge-to-edge stacked glass layers because seams and optical noise become visible.

## Accessibility

- Provide fallback solid/translucent colors when backdrop-filter is unsupported.
- Check contrast on final composited surfaces.
- Respect reduced transparency where practical.
- Use icons or labels in addition to glow for selected, error, and success states.

## Implementation Notes

Use CSS custom properties for glass opacity, blur, rim opacity, highlight strength, and background dim. Keep animated filters limited; animate transform and opacity instead of full-screen blur radius.
