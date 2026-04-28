# Motion Interaction Premium Rules

Premium motion is slow, subtle, and staggered. It should reveal hierarchy and state, not show off.

## Default Entrance

Initial:

- `opacity: 0`
- `y: 20`
- `filter: blur(10px)`

Animate:

- `opacity: 1`
- `y: 0`
- `filter: blur(0px)`

Parameters:

- Duration `0.6s` to `1.2s`.
- Easing `easeOut` or `power3.out`.

## Hero Sequence

- Badge: `0.3s` to `0.4s`.
- Heading: `0.4s` to `0.6s`.
- Subheading: `0.8s`.
- CTA: `1.0s` to `1.1s`.
- Stats/partners: `1.2s` to `1.4s`.

## BlurText

Use for major hero headings:

- Split by words.
- Each word enters from `blur(10px)`, opacity `0`, `y: 50`.
- Middle state `blur(5px)`, opacity `0.5`, `y: -5`.
- Final state `blur(0)`, opacity `1`, `y: 0`.
- Stagger `0.08s` to `0.12s` per word.

## Scroll Reveal

- Use `whileInView`.
- Viewport once.
- Opacity `0` to `1`.
- `y: 30` to `0`.
- Duration `0.8s` to `1s`.

## Interaction States

- Buttons: slight scale, border/rim change, or icon nudge.
- Glass cards: edge highlight and modest background opacity change.
- Media cards: slow hover zoom or overlay reveal.
- Nav links: muted to white or underline/rim state.

## Web App Workspace Reveal

For advanced Web App, SaaS Workspace, Dashboard, and AI Project Workspace
interfaces, use a stateful workspace reveal rather than a marketing landing
hero sequence:

- Background reveal: opacity `0` to `1`, blur `18px` to `0`, `600ms`.
- Hero or summary glass panel: `translateY(34px)`, blur `12px`, `800ms`,
  delay around `100ms`.
- Toolbar with search and pill actions: `translateY(22px)`, blur `8px`,
  `620ms`, delay around `190ms`.
- Project or dashboard cards: `translateY(28px)`, scale `.975`, blur `10px`,
  `660ms`, stagger `80ms` to `140ms`.
- Toast feedback: `translateX(24px)` to `0`, `440ms`,
  `cubic-bezier(0.2,1.2,0.2,1)`.
- Loading shimmer: `1.2s ease-in-out infinite`.
- Remove persistent `will-change` after animation completes.
- Support `prefers-reduced-motion`; skip translate and blur when requested.

Use this pattern for persistent tools and dashboards with search, tabs, cards,
modals, validation, and toast feedback. Do not apply the landing-page section
sequence to workspace surfaces unless the user explicitly asks for a marketing
page.

## Avoid

Avoid fast bouncing, excessive spinning, neon flashing, every element moving at
once, looping chart motion after values settle, and animation that hurts
readability.
