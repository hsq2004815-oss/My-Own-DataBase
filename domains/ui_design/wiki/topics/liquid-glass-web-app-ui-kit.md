# Liquid Glass Web App UI Kit

This topic is for premium Web App, SaaS Workspace, Dashboard, and AI Project
Workspace component systems. It is not a landing page rule. Use it when the
requested surface has persistent controls, project cards, tab filters, forms,
modals, validation, and feedback states.

## Source Pattern

The seed interface is an AI Project Workspace with:

- hero glass panel
- toolbar with glass search input and glass pill actions
- glass tab filter bar
- responsive project card grid
- create/edit glass modal
- form validation states
- toast feedback

## Light Glass Tokens

Use these token values for bright dashboard and workspace surfaces:

```css
--glass-blur-sm: blur(18px) saturate(160%);
--glass-blur-md: blur(24px) saturate(180%);
--glass-blur-lg: blur(28px) saturate(185%);
--glass-fill-light: rgba(255,255,255,0.48);
--glass-fill-thick: rgba(255,255,255,0.62);
--glass-rim: rgba(255,255,255,0.55);
--glass-rim-bright: rgba(255,255,255,0.68);
--glass-shadow-outer: 0 14px 36px rgba(31,38,135,0.16);
--glass-shadow-thick: 0 22px 54px rgba(20,30,60,0.28);
--glass-highlight: inset 0 1px 1px rgba(255,255,255,0.80);
--glass-inset-dark: inset 0 -1px 3px rgba(20,30,60,0.18);
```

Use `blur-sm` for inputs and pills, `blur-md` for normal cards and toolbars,
and `blur-lg` for hero panels, thick cards, and modal surfaces.

## Dark Neon Glass Tokens

Use these token values for premium dark project cards, selected cards, or
high-emphasis AI feature panels inside the workspace:

```css
--dark-fill: rgba(8,10,16,0.78);
--dark-fill-secondary: rgba(15,23,42,0.64);
--dark-rim: rgba(255,255,255,0.18);
--dark-rim-hover: rgba(255,255,255,0.42);
--dark-cyan: rgba(34,211,238,0.36);
--dark-magenta: rgba(217,70,239,0.30);
--dark-orange: rgba(251,146,60,0.20);
--dark-shadow-deep: 0 24px 60px rgba(2,6,23,0.34), 0 8px 24px rgba(15,23,42,0.22);
--dark-neon-ring: 0 0 0 1px rgba(34,211,238,0.38), 0 0 24px rgba(217,70,239,0.24);
```

Dark neon glass should be rare. Use it for premium cards, active AI modules,
error-prone high-risk project states, or selected hero-level cards.

## Radius Tokens

```css
--radius-field: 22px;
--radius-card: 28px;
--radius-modal: 40px;
--radius-pill: 999px;
```

Fields and search bars use `22px`. Cards use `28px`. Modals use `40px`.
Pills, segmented tabs, toggle tracks, and compact action buttons use `999px`.

## Component Rules

`glass-card`:

- Base surface for project cards, hero panels, and workspace panels.
- Use `fill-light`, `blur-md`, 1px to 1.5px rim, outer shadow, inset highlight,
  and inset-dark shadow.
- Add pseudo-element gloss and subtle chromatic caustics only when the
  background has enough visual depth.

`glass-thick`:

- Use for hero panel, modal content, and primary workspace cards.
- Use `fill-thick`, brighter rim, `shadow-thick`, and stronger inset highlight.

`glass-dark`:

- Use for selected or premium project cards.
- Use dark fill, dark rim, deep shadow, inset gloss, and cyan/magenta/orange
  glints.
- On hover, raise rim opacity toward `rim-hover`; do not add noisy flashing.

`glass-pill`:

- Use for secondary toolbar actions, modal cancel, invite, filters, and compact
  commands.
- Use `blur-sm`, thick fill, pill radius, inset highlight, and modest
  translateY hover.

`glass-pill-primary`:

- Use for the single primary action in a toolbar or modal.
- Use translucent accent fill, accent rim, glow, and restrained hover lift.

`glass-input`:

- Use for search, select, text input, and textarea controls.
- Use `blur-sm`, `fill-light` to `fill-thick`, `radius-field`, inset shadow,
  placeholder contrast, and focus ring.

`glass-toggle`:

- Use pill track plus circular knob.
- Checked state uses accent translucent fill, accent border, and subtle glow.

`tab-bar` / `tab`:

- Use an inline glass filter bar for project state filters.
- Active tab uses stronger fill and rim, not only color text.
- Keep tabs keyboard focusable and avoid wrapping into cramped lines on mobile.

`glass-icon-button`:

- Use for close, quick action, or card-level icon commands.
- Keep square/circular dimensions stable and include `aria-label`.

`glass-modal`:

- Use thick glass with modal radius and backdrop overlay.
- Dialog must be centered, readable, keyboard dismissible, and protected from
  background scroll.

`glass-toast`:

- Use compact glass feedback with `role="status"` or `aria-live`.
- Success/error must include text and icon, not glow alone.

`loading shimmer`:

- Use a gradient shimmer overlay for submit buttons or skeleton states.
- Duration is `1.2s ease-in-out infinite`.

`error/success validation glow`:

- Error field: red rim plus soft red outer/inset glow and text message.
- Success field: green rim plus soft green glow and text message.

`disabled states`:

- Reduce opacity, remove hover transform, reduce shadow, and prevent pointer
  events.
- Do not rely on disabled color alone; cursor and state should communicate
  non-interactivity.

## Motion Rules

Use these exact motion families for workspace entrance and feedback:

- Background reveal: opacity `0` to `1`, blur `18px` to `0`, `600ms`.
- Hero reveal: `translateY(34px)`, blur `12px`, `800ms`, delay around `100ms`.
- Toolbar reveal: `translateY(22px)`, blur `8px`, `620ms`, delay around
  `190ms`.
- Card reveal: `translateY(28px)`, scale `.975`, blur `10px`, `660ms`,
  stagger `80ms` to `140ms`.
- Toast spring-in: `translateX(24px)` to `0`, `440ms`,
  `cubic-bezier(0.2,1.2,0.2,1)`.
- Loading shimmer: `1.2s ease-in-out infinite`.
- Remove persistent `will-change` after animation completes.
- Support `prefers-reduced-motion`; skip translate and blur and use quick
  opacity where possible.

## Layout Pattern

For AI Project Workspace / SaaS Dashboard:

1. Use a contained app shell with a soft ambient background and subtle grid.
2. Place a hero glass panel at top only if it functions as product context or
   workspace summary, not as a marketing landing hero.
3. Place toolbar controls directly under the hero: search input first, then
   primary/secondary pill actions.
4. Add a glass tab filter bar before the grid.
5. Render project cards in a responsive grid with stable gaps and card radii.
6. Use a create/edit modal for structured creation flows.
7. Include validation feedback, loading state, and toast feedback as first-class
   UI states.

## Accessibility And Fallback

- Provide solid/translucent fallback colors when `backdrop-filter` is
  unsupported.
- Support `prefers-reduced-transparency` with stronger opaque fills.
- Support `prefers-reduced-motion`.
- Use `:focus-visible` rings on buttons, inputs, tabs, and icon buttons.
- Toasts need `aria-live` or `role="status"`.
- Dialogs need `role="dialog"` and `aria-modal="true"`.
- `Escape` closes the modal.
- Close buttons need `aria-label`.
- Validation messages need `aria-describedby`.

## Avoid

- Do not treat this as a marketing landing page pattern.
- Do not apply full-screen cinematic hero rules when the task is a workspace.
- Do not make every dashboard cell glass; use glass for grouped panels,
  controls, cards, modals, and feedback.
- Do not copy `inspiration_only` screenshots or review-required assets directly.
- Do not animate persistent filters or blur on every frame after initial reveal.
