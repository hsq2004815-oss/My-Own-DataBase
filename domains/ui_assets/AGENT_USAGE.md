# UI Assets AGENT_USAGE

## Purpose

Use this domain when a UI/frontend task needs screenshots, motion references, fonts, icons, backgrounds, UI kits, Lottie collections, or visual asset policy.

## When to Use

- UI task needs motion references, fonts, screenshots, icons, backgrounds, or Lottie
- The user asks for high-end animation or visual effects
- A generated UI needs asset license or usage policy decisions

## Read First

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

## Do Not Use by Default

- raw asset files without checking `usage_policy`
- `review_required` assets as direct production assets
- `inspiration_only` assets as copied deliverables

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

## Output Requirements

- Report asset ids.
- Report usage policy.
- Report direct-use versus inspiration-only status.
- Report implementation method.
