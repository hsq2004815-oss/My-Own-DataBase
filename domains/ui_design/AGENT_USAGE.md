# UI Design AGENT_USAGE

## Purpose

Use this domain for UI, frontend, landing page, SaaS homepage, dashboard, portfolio, visual direction, typography, layout, motion, and component quality tasks.

## When to Use

- High-end page or product site generation
- Portfolio, resume site, or SaaS homepage
- Web app, dashboard, or workspace UI
- Visual direction, typography, layout, motion, or component quality review

## Default Retrieval

Prefer the local API before file reading:

- `POST http://127.0.0.1:8765/brief`
- use `ui_limit=8`, `workflow_limit=2`, `automation_limit=0`, `backend_limit=0`, `asset_limit=10`

If the task mentions motion, animation, Lottie, dynamic background, or advanced visual effects, also use [UI Assets AGENT_USAGE](../ui_assets/AGENT_USAGE.md).

## Read First

1. [UI Design wiki index](wiki/index.md)
2. [UI Design topic index](wiki/topics/index.md)
3. Premium topic files relevant to the task
4. Brand design topics only as secondary flavor references
5. `processed/cleaned_text` only for maintenance or provenance checks
6. `raw/` only for curation maintenance, not default generation

## Task Playbooks

- [Premium Frontend Page Playbook](playbooks/premium-frontend-page-playbook.md)

## Core Premium Rules

- [Premium UI Execution Quality Rules](wiki/topics/premium-ui-execution-quality-rules.md)
- [Premium Web UI Initial Aesthetic Rules](wiki/topics/premium-web-ui-initial-aesthetic-rules.md)
- [Premium Typography and Layout Rules](wiki/topics/premium-typography-and-layout-rules.md)
- [Motion Interaction Premium Rules](wiki/topics/motion-interaction-premium-rules.md)
- [Liquid Glass Design System](wiki/topics/liquid-glass-design-system.md)
- [Liquid Glass Web App UI Kit](wiki/topics/liquid-glass-web-app-ui-kit.md)
- [Cinematic Video Hero Rules](wiki/topics/cinematic-video-hero-rules.md)
- [Video Hero Layout Patterns](wiki/topics/video-hero-layout-patterns.md)
- [Landing Page Section Patterns](wiki/topics/landing-page-section-patterns.md)
- [UI Agent Starter Prompt](wiki/topics/ui-agent-starter-prompt.md)

## Do Not Use by Default

- `raw/`
- unknown-license assets
- brand flavor files as primary rules
- automation context unless browser control or QA is explicitly needed

## Output Requirements

- Report selected visual direction, pattern, material system, visual anchor, and component system.
- Report record/topic files that shaped the result.
- Report asset usage policy when assets or motion references were used.
