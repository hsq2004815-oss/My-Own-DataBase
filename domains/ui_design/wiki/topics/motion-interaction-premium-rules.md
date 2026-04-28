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

## Avoid

Avoid fast bouncing, excessive spinning, neon flashing, every element moving at once, looping chart motion after values settle, and animation that hurts readability.
