# Premium UI Execution Quality Rules

## Purpose

This rule set prevents agents from producing safe but generic UI after retrieving premium design rules.

A generated page should not only be clean. It should have a clear visual concept, a strong hero composition, a memorable visual anchor, refined component states, precise spacing, and professional material quality.

This file is an execution layer. It should be used together with:
- premium-web-ui-initial-aesthetic-rules.md
- liquid-glass-design-system.md
- liquid-glass-web-app-ui-kit.md
- video-hero-layout-patterns.md
- cinematic-video-hero-rules.md
- motion-interaction-premium-rules.md
- premium-typography-and-layout-rules.md

## Core Principle

Premium UI is not achieved by adding glass cards to a normal layout.

A premium page must combine:
- precise composition
- strong visual anchor
- refined typography
- material depth
- interaction states
- custom visual components
- scenario-specific layout
- strict avoidance of generic templates

The agent must not only say "liquid glass" or "cinematic". It must implement the visual details that make those styles premium.

## Required Design Decision Before Coding

Before implementation, the agent must choose and state:

1. visual direction
2. hero pattern
3. material system
4. component system
5. visual anchor
6. motion strategy
7. database rules / record_id used

Example:

```text
visual direction: light liquid glass workspace
hero pattern: two-panel liquid glass split hero
material system: liquid-glass-web-app-ui-kit
component system: command bar + glass tabs + status chips + project bento
visual anchor: edge device topology + residual curve panel
motion strategy: reveal + shimmer + hover lift
database records: implementation-liquid-glass-web-app-ui-kit, pattern-two-panel-liquid-glass-hero
```

If the agent cannot state these decisions, it should not start coding yet.

## Visual Anchor Requirement

Every premium hero must include at least one strong visual anchor.

Acceptable visual anchors:
- full-screen video background
- SVG glow
- system topology diagram
- waveform / signal curve
- task queue visualization
- knowledge graph
- floating product panel
- technical dashboard cluster
- 3D-like glass cards
- metric visualization
- animated canvas / SVG micro-motion
- device / service node map
- timeline rail with meaningful states

Avoid:
- empty white cards
- plain statistic cards only
- generic particles only
- plain text-only right panel
- random decorative circles
- ordinary skill chip lists as the main visual

## Technical Portfolio Visual Anchors

For technical portfolio pages, use project-specific visuals instead of generic cards.

Recommended mappings:

### STM32 / sensor project

Use:
- waveform
- vibration signal
- sensor stream
- serial data panel
- threshold alarm indicator
- device-to-PC data flow

### RK3588 / edge gateway

Use:
- topology graph
- node map
- service monitor
- edge device card
- process pipeline
- local database / dashboard preview

### Sensor compensation / ML

Use:
- residual curve
- MAE / RMSE / R2 metric panel
- before-after calibration chart
- feature processing pipeline
- model split diagram

### Windows desktop tool

Use:
- window panels
- shortcut launcher
- file/resource grid
- command palette
- tray / hotkey status chip

### Browser automation / upload tool

Use:
- task queue
- retry status
- upload pipeline
- log stream
- screenshot checkpoint strip
- timeout / skip state

### AI database / agent workflow

Use:
- retrieval graph
- chunk network
- brief API flow
- knowledge map
- domain routing panel

## Component Density Rule

A premium web page should include a meaningful component system.

For landing pages:
- hero
- navbar
- CTA
- tagline pill
- information cluster
- section cards
- motion reveal

For web app / workspace style pages:
- command bar or search input
- glass tabs / filter chips
- status chip
- KPI card
- project bento
- toast or modal
- loading shimmer
- hover / focus / active states
- optional empty / loading / error / success states

Do not produce only:
- hero + cards + footer
- plain skill chips
- generic stat cards
- empty decorative panels
- black background + gray cards
- flat white SaaS layout

## Glass Quality Rule

Do not call a UI "liquid glass" unless it includes most of:

- translucent fill
- backdrop blur
- saturate
- rim or pseudo-rim
- inset highlight
- subtle dark inset
- outer shadow
- hover state
- active/focus state when interactive
- distinct light / strong glass hierarchy

Avoid:
- only bg-white/10 backdrop-blur
- flat white cards
- ordinary border-only cards
- no hover/focus states
- all glass elements having the same strength

## Recommended Glass Execution Tokens

Agents should copy these starting values instead of guessing.

Light glass workspace:

```css
--glass-blur-sm: blur(18px) saturate(160%);
--glass-blur-md: blur(24px) saturate(180%);
--glass-blur-lg: blur(28px) saturate(185%);

--glass-fill-light: rgba(255,255,255,0.48);
--glass-fill-thick: rgba(255,255,255,0.62);
--glass-fill-strong: rgba(255,255,255,0.85);

--glass-rim: rgba(255,255,255,0.55);
--glass-rim-bright: rgba(255,255,255,0.68);

--glass-shadow-outer: 0 14px 36px rgba(31,38,135,0.16);
--glass-shadow-thick: 0 22px 54px rgba(20,30,60,0.28);

--glass-highlight: inset 0 1px 1px rgba(255,255,255,0.80);
--glass-inset-dark: inset 0 -1px 3px rgba(20,30,60,0.18);

--radius-field: 22px;
--radius-card: 28px;
--radius-modal: 40px;
--radius-pill: 999px;
```

Dark neon glass:

```css
--dark-fill: rgba(8,10,16,0.78);
--dark-fill-secondary: rgba(15,23,42,0.64);

--dark-rim: rgba(255,255,255,0.18);
--dark-rim-hover: rgba(255,255,255,0.42);

--dark-cyan: rgba(34,211,238,0.36);
--dark-magenta: rgba(217,70,239,0.30);
--dark-orange: rgba(251,146,60,0.20);

--dark-shadow-deep:
  0 24px 60px rgba(2,6,23,0.34),
  0 8px 24px rgba(15,23,42,0.22);

--dark-inset-gloss:
  inset 0 1px 1px rgba(255,255,255,0.22),
  inset 0 -1px 2px rgba(0,0,0,0.35);

--dark-neon-ring:
  0 0 0 1px rgba(34,211,238,0.38),
  0 0 24px rgba(217,70,239,0.24);
```

## Motion Execution Tokens

Use precise motion values instead of random transition-all.

Recommended reveal sequence:

```css
--ease-reveal: cubic-bezier(0.16, 1, 0.3, 1);
--ease-spring: cubic-bezier(0.2, 1.2, 0.2, 1);
--ease-overshoot: cubic-bezier(0.2, 1.25, 0.25, 1);
```

Component motion:
- background reveal: opacity 0 to 1, blur 18px to 0, 600ms
- hero reveal: translateY 34px, blur 12px, 800ms, delay around 100ms
- toolbar reveal: translateY 22px, blur 8px, 620ms, delay around 190ms
- card reveal: translateY 28px, scale 0.975, blur 10px, 660ms, stagger 80ms to 140ms
- toast spring-in: translateX 24px to 0, 440ms
- loading shimmer: 1.2s to 1.6s ease-in-out infinite

Rules:
- Do not reveal all elements at once.
- Do not leave persistent will-change.
- Respect prefers-reduced-motion.

## Layout Differentiation Rule

The agent must avoid repeating the same safe layout.

If the user says "高级个人网站" or "高级作品集", do not always default to dark portfolio.

Consider:
- light liquid glass workspace
- strict grayscale glass
- two-panel split hero
- bottom-left cinematic hero
- technical education hero
- editorial portfolio
- dashboard-like productized portfolio

If the previous generated version was dark, the next version should explore a non-dark layout unless the user explicitly requests dark.

## Style Routing Rule

Use task intent to route visual styles:

Landing page / SaaS homepage:
- video-hero-layout-patterns
- cinematic-video-hero-rules
- premium-typography-and-layout-rules

Dashboard / workspace / app UI:
- liquid-glass-web-app-ui-kit
- glass-form-controls
- motion-interaction-premium-rules

Technical portfolio:
- technical visual anchors
- project-specific visuals
- premium-ui-execution-quality-rules
- liquid-glass-design-system

Dark cinematic:
- use only when user requests dark / cinematic / film / black / dramatic

Light workspace:
- use when user requests productized portfolio, web app feel, clean, high-end workspace, dashboard-like, or non-dark

## Visual Anchor to Asset Search Rule

When a design pattern needs a strong visual anchor, the agent should search ui_assets.

Do not directly copy inspiration_only or review_required assets.

Recommended asset search mapping:
- cinematic hero -> search "motion reference hero background", "cinematic loop", "video background"
- liquid glass workspace -> search "liquid glass UI kit", "glass dashboard", "workspace UI"
- micro-interaction -> search "Lottie small animation", "loading animation", "hover motion"
- technical portfolio -> search "dashboard preview", "technical diagram", "motion reference", "small animation"
- strict grayscale -> search "grayscale interface", "monochrome glass", "minimal editorial"

If retrieved asset usage_policy is:
- direct_use: may use directly
- inspiration_only: style reference only
- review_required: do not directly use unless license is confirmed
- internal_reference: internal analysis only

For inspiration_only or review_required, recreate similar effects using CSS / SVG / Canvas / self-authored animation.

## Truthfulness Rule for Portfolio Content

Premium UI must not create fake credibility.

For personal portfolio / resume / CV / project pages:
- do not invent metrics
- do not invent years
- do not invent companies
- do not invent technical stacks
- do not replace the user's real stack with fashionable tools
- use "TBD" or omit if exact data is unknown
- only use verified project metrics from the database

A visually premium portfolio with fake claims is lower quality than a simple but truthful portfolio.

## Negative Rules

Avoid:
- generic dark developer portfolio
- blue-white SaaS template
- plain black background with gray cards
- fake metrics
- emoji icons in premium technical UI
- empty right-side panels
- low-density hero sections
- using only particles as the main visual
- all cards having the same size and weight
- all glass elements having the same intensity
- plain skill chips as the main design feature
- ordinary stat cards without technical visuals
- overusing gradients as a replacement for composition

## Output Self-Check

Before finalizing code, the agent should check:

1. Does the page have a strong visual anchor?
2. Does it use the correct pattern for the task?
3. Does it avoid generic template layout?
4. Are glass components actually refined?
5. Are hover/focus/active/loading states present?
6. Are visuals connected to the user's project domain?
7. Are metrics real or safely marked as placeholders?
8. Is the result visually different from a common template?
9. Are database record_id / rules reflected in the implementation?
10. Did the agent use ui_assets when motion or visual references were relevant?

If the answer is no, revise before final output.
