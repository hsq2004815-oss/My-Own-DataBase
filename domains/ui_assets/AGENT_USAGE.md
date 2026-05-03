# UI Assets AGENT_USAGE

Use this domain when a UI/frontend task needs screenshots, motion references, fonts, icons, backgrounds, UI kits, Lottie collections, or visual asset policy.

## Agent Read Order

1. [UI Assets README](README.md)
2. [UI Assets wiki index](wiki/index.md)
3. `processed/metadata/*.json` records returned by `/assets/search`
4. `processed/chunks` only when search result details are insufficient
5. `raw/` only after checking `usage_policy`

## Usage Policy

- `direct_use`: may be used directly if the task needs the file and the path exists.
- `inspiration_only`: use as visual reference only; do not copy into deliverables.
- `review_required`: inspect license/source before direct use.
- `internal_reference`: internal analysis only.
- `unknown`: do not use directly.

## Motion Tasks

For high-end UI tasks with animation or motion, search for:
- `小动画`
- `微交互`
- `loading animation`
- `hover motion`
- `button animation`
- `animated icon`
- `lottie animation`
- `motion reference`
- `hero background motion`

Report asset ids, usage policy, direct-use status, and implementation method.
