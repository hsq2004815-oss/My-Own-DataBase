# Playbook Gap Report

Date: 2026-05-03

This report lists task playbooks that would make the database more directly usable by Claude Code, Codex, and similar agents.

This stage recommends playbooks. It does not replace the underlying rules, patterns, templates, or checklists.

## Recommended Playbooks

### Premium Frontend Page Playbook

Suggested path:
`domains/ui_design/playbooks/premium-frontend-page-playbook.md`

Suitable tasks:
- 高级前端页面
- landing page
- portfolio
- SaaS homepage

Read domains:
- `ui_design`
- `ui_assets`
- `agent_workflow`

Read rules, patterns, and templates:
- Premium UI execution
- typography and layout rules
- motion interaction rules
- video hero and landing section patterns
- asset usage policy

Output should include:
- visual direction
- pattern
- material system
- visual anchor
- component system
- asset usage policy
- verification

### Backend API Design Playbook

Suggested path:
`domains/backend/playbooks/backend-api-design-playbook.md`

Suitable tasks:
- REST API
- admin API
- public API
- OpenAPI

Read domains:
- `backend`
- `agent_workflow`

Read rules, patterns, and templates:
- API design rules
- response wrapper pattern
- error code pattern
- OpenAPI doc template
- API checklist

Output should include:
- endpoint map
- request and response schemas
- error envelope
- pagination and idempotency notes
- auth assumptions
- tests

### Database Schema Playbook

Suggested path:
`domains/backend/playbooks/database-schema-design-playbook.md`

Suitable tasks:
- 数据库表结构
- PostgreSQL schema
- indexes
- migrations

Read domains:
- `backend`

Read rules, patterns, and templates:
- database modeling rules
- database topic
- database checklist

Output should include:
- ER model
- table definitions
- constraints
- indexes
- migration plan
- data integrity risks

### Windows Desktop Tool Playbook

Suggested path:
`domains/agent_workflow/playbooks/windows-desktop-tool-playbook.md`

Suitable tasks:
- Windows desktop app/tool
- tray app
- local GUI utility

Read domains:
- `agent_workflow`
- `backend`
- `voice_assistant` when voice is involved

Read rules, patterns, and templates:
- code asset reuse rules
- desktop assistant adapters/snippets
- backend env and logging rules

Output should include:
- architecture
- UI/runtime boundary
- config and logging
- startup and health checks
- packaging and test plan

### Browser Automation / RPA Playbook

Suggested path:
`domains/automation/playbooks/browser-automation-rpa-playbook.md`

Suitable tasks:
- upload tool
- CDP automation
- Playwright scripts
- logged-in browser flows

Read domains:
- `automation`
- `agent_workflow`
- `dev_tools` when downloads or imports are involved

Read rules, patterns, and templates:
- persistent browser daemon topic
- browser QA pattern
- agent preflight checklist
- GitHub import rules when needed

Output should include:
- browser/session assumptions
- selectors
- retries
- upload, iframe, and modal handling
- screenshots/logs
- verification

### GitHub Project Analysis Intake Playbook

Suggested path:
`domains/dev_tools/playbooks/github-project-analysis-intake-playbook.md`

Suitable tasks:
- analyze GitHub repo and distill into database

Read domains:
- `dev_tools`
- `agent_workflow`
- target domain

Read rules, patterns, and templates:
- GitHub import rules
- agent download workflow
- code asset intake checklist
- target domain rules

Output should include:
- download method
- files read
- license/security notes
- `raw modified=false`
- distillation target

### Use This Database Playbook

Suggested path:
`domains/agent_workflow/playbooks/use-local-database-for-task-playbook.md`

Suitable tasks:
- let Claude Code or Codex use this database for a real task

Read domains:
- `agent_workflow`
- task-specific domains

Read rules, patterns, and templates:
- root `AGENT_USAGE.md`
- `CLAUDE.md`
- domain `AGENT_USAGE.md`
- local API protocol

Output should include:
- retrieved queries, chunks, and assets
- domains used
- files read
- uncertainty
- output constraints

### Raw-to-Rules Distillation Playbook

Suggested path:
`domains/agent_workflow/playbooks/raw-to-rules-distillation-playbook.md`

Suitable tasks:
- upgrade raw material to rules, patterns, or templates

Read domains:
- `agent_workflow`
- source domain
- `dev_tools` for imports

Read rules, patterns, and templates:
- code asset reuse rules
- curation guides
- GitHub project selection rules
- target domain templates

Output should include:
- source list
- distilled rules, patterns, and templates
- provenance
- rejected raw details
- verification

## Highest Priority

1. `premium-frontend-page-playbook.md` because UI tasks are frequent and require disciplined asset/rule routing.
2. `backend-api-design-playbook.md` because backend rules/templates already exist but need a task-shaped entry.
3. `raw-to-rules-distillation-playbook.md` because the graph contains a large amount of raw material that should not become default context.

## Risk Notes

- Playbooks should not duplicate whole rule files.
- Playbooks should point to existing rules, patterns, templates, and checklists.
- Raw playbooks must preserve `raw source modified: false` unless the user explicitly asks for maintenance work.
