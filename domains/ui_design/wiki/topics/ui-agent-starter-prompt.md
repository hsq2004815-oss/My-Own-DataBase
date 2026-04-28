# UI Agent Starter Prompt

Use this as the default design stance before generating premium Web UI.

## Starter Prompt

Design the UI as a premium, cinematic, responsive Web experience rather than a
generic template. Choose one dominant visual direction: dark cinematic glass,
black-white neutral SaaS, white editorial luxury, portfolio editorial dark,
video-first immersive landing page, or premium AI product/design agency landing
page.

Use disciplined typography, large whitespace, clear hierarchy, restrained
color, high-quality material treatment, subtle motion, and explicit responsive
composition. Avoid generic blue-white SaaS defaults unless the user asks for
them.

For landing pages and premium product sites, prioritize:

1. `premium-web-ui-initial-aesthetic-rules.md`
2. `liquid-glass-design-system.md`
3. `cinematic-video-hero-rules.md`
4. `premium-typography-and-layout-rules.md`
5. `motion-interaction-premium-rules.md`
6. `landing-page-section-patterns.md`

Use brand `design-*.md` files only as secondary references. If a brand topic is
marked information-insufficient, do not let it override the premium rules.

## Implementation Checklist

- Pick one visual direction.
- Define background, text, muted text, border, surface, and one accent system.
- Use a real hero composition: poster hero, giant staggered type, video-first hero, or product/agency hero.
- Use display/body font pairing.
- Add premium motion: blur/y/opacity entrance, staggered sequence, scroll reveal.
- For video, use explicit z-index and overlay fades.
- For glass, use two material levels and gradient pseudo-element borders.
- Keep mobile simple: stacked layout, hidden desktop nav, visible CTA, no horizontal overflow.
- End with a clean CTA/footer and avoid unnecessary visual noise.
