# Markdown Format and Playbook Fix Report

## Date

2026-05-03

## Problem Found

The previous second-brain graph upgrade created useful routing files, but several entry and report files still had readability issues:

- `AGENT_USAGE.md` had long paragraphs that mixed multiple rules in one line.
- `domains/backend/AGENT_USAGE.md` had long task-routing list items.
- `domains/agent_workflow/AGENT_USAGE.md` had long routing and code asset lines.
- `docs/reports/playbook_gap_report.md` used a very wide Markdown table that was hard to read in Obsidian and GitHub.
- `docs/reports/high_value_isolated_nodes.md` had several long table rows and paragraphs.

`CLAUDE.md` was already readable, but it needed a separate `Start Here` section and playbook links.

## Files Reformatted

- `CLAUDE.md`
- `AGENT_USAGE.md`
- `domains/backend/AGENT_USAGE.md`
- `domains/ui_design/AGENT_USAGE.md`
- `domains/ui_assets/AGENT_USAGE.md`
- `domains/agent_workflow/AGENT_USAGE.md`
- `domains/automation/AGENT_USAGE.md`
- `domains/dev_tools/AGENT_USAGE.md`
- `domains/voice_assistant/AGENT_USAGE.md`
- `docs/reports/high_value_isolated_nodes.md`
- `docs/reports/playbook_gap_report.md`

## Playbooks Added

- `domains/ui_design/playbooks/premium-frontend-page-playbook.md`
- `domains/backend/playbooks/backend-api-design-playbook.md`
- `domains/agent_workflow/playbooks/raw-to-rules-distillation-playbook.md`

## Links Added

- `CLAUDE.md` now links to the first three task playbooks.
- `AGENT_USAGE.md` now has a `Task Playbooks` section.
- `domains/ui_design/AGENT_USAGE.md` links to the Premium Frontend Page Playbook.
- `domains/backend/AGENT_USAGE.md` links to the Backend API Design Playbook.
- `domains/agent_workflow/AGENT_USAGE.md` links to the Raw-to-Rules Distillation Playbook.
- `domains/ui_design/wiki/index.md` links to the frontend playbook.
- `domains/backend/wiki/index.md` links to the backend API playbook.
- `domains/agent_workflow/wiki/index.md` links to the raw-to-rules playbook.

## Validation

- Markdown readability check: passed for the edited entry files and new playbooks.
- Long-line check: no checked entry file or playbook has lines over 180 characters.
- Relative Markdown link check: passed for this round's changed files.
- New unresolved links from this round: none found.
- Raw files modified by this round: no.
- Runtime DB modified by this round: no.

Existing local raw changes and untracked raw directories were present before this task and were intentionally left untouched.

## Remaining Issues

- The repository still has pre-existing raw upstream Markdown links that may be unresolved.
- Several future playbooks from `docs/reports/playbook_gap_report.md` are still only recommendations.
- Some UI brand design topics may still need later quality review before promotion.

## Next Recommended Work

1. Add the database schema design playbook.
2. Add the browser automation / RPA playbook.
3. Add a small reusable Markdown graph check script for curated files only.
