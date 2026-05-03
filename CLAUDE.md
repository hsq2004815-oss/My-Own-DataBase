# CLAUDE.md

## Role of This Repository

This repository is a local AI second-brain knowledge base for engineering tasks.

## Default Rule

Do not read the whole repository for ordinary tasks. Use the local API and documented domain entry files first.

Start here:
- [Repository README](README.md)
- [Root AGENT_USAGE](AGENT_USAGE.md)
- [Root AGENT rules](AGENT.md)
- [Global wiki index](wiki/index.md)

Raw third-party repositories are source material only. Do not use `raw/` as default task context.

## Task Routing

### Frontend / UI / Product Page

Read:
- [UI Design AGENT_USAGE](domains/ui_design/AGENT_USAGE.md)
- [UI Design wiki index](domains/ui_design/wiki/index.md)
- [UI Design topic index](domains/ui_design/wiki/topics/index.md)
- [UI Assets AGENT_USAGE](domains/ui_assets/AGENT_USAGE.md)

Use assets only according to metadata `usage_policy`.

### Backend / API / Database / Auth / Deployment

Read:
- [Backend AGENT_USAGE](domains/backend/AGENT_USAGE.md)
- [Backend rules index](domains/backend/rules/index.md)
- [Backend topics index](domains/backend/wiki/topics/index.md)
- [Backend patterns index](domains/backend/wiki/patterns/index.md)
- [Backend checklists index](domains/backend/wiki/checklists/index.md)
- [Backend templates index](domains/backend/wiki/templates/index.md)

Prefer `/brief` or `/backend/search` before opening individual files.

### Browser Automation / RPA / Upload / QA

Read:
- [Automation AGENT_USAGE](domains/automation/AGENT_USAGE.md)
- [Automation wiki index](domains/automation/wiki/index.md)

Only request automation context when the task involves browser control, CDP, selectors, upload, screenshots, or verification.

### Agent Workflow / Code Asset Reuse

Read:
- [Agent Workflow AGENT_USAGE](domains/agent_workflow/AGENT_USAGE.md)
- [Agent Workflow wiki index](domains/agent_workflow/wiki/index.md)
- [Code Assets Global Index](domains/agent_workflow/wiki/indexes/code-assets-global-index.md)
- [Code Asset Reuse Rules](domains/agent_workflow/rules/code-asset-reuse-rules.md)

### Dev Tools / GitHub Import

Read:
- [Dev Tools AGENT_USAGE](domains/dev_tools/AGENT_USAGE.md)
- [GitHub Import Rules](domains/dev_tools/rules/github_import_rules.md)
- [Dev Tools wiki index](domains/dev_tools/wiki/index.md)

### Voice Assistant / Windows Desktop Voice

Read:
- [Voice Assistant AGENT_USAGE](domains/voice_assistant/AGENT_USAGE.md)
- [Voice Assistant README](domains/voice_assistant/README.md)
- [Voice Assistant wiki index](domains/voice_assistant/wiki/index.md)

## Output Requirement

When using this database, mention:
1. Which domain was used
2. Which rule, pattern, template, or asset policy affected the result
3. Which files were read
4. What uncertainty remains
