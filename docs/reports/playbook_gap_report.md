# Playbook Gap Report

Date: 2026-05-03

This report lists task playbooks that would make the database more directly usable by Claude Code, Codex, and similar agents. This stage only recommends playbooks; it does not create them.

| Playbook | Suggested path | Suitable tasks | Read domains | Read rules/patterns/templates | Output should include |
| --- | --- | --- | --- | --- | --- |
| Premium Frontend Page Playbook | `domains/ui_design/playbooks/premium-frontend-page-playbook.md` | 高级前端页面, landing page, portfolio, SaaS homepage | `ui_design`, `ui_assets`, `agent_workflow` | Premium UI execution, typography/layout, motion interaction, video hero/landing patterns, asset policy | Visual direction, pattern, material system, visual anchor, component system, asset usage policy, verification |
| Backend API Design Playbook | `domains/backend/playbooks/backend-api-design-playbook.md` | REST API, admin API, public API, OpenAPI | `backend`, `agent_workflow` | API design rules, response wrapper pattern, error code pattern, OpenAPI doc template, API checklist | Endpoint map, request/response schemas, error envelope, pagination/idempotency, auth assumptions, tests |
| Database Schema Playbook | `domains/backend/playbooks/database-schema-design-playbook.md` | 数据库表结构, PostgreSQL schema, indexes, migrations | `backend` | Database modeling rules, database topic, database checklist | ER model, table definitions, constraints, indexes, migration plan, data integrity risks |
| Windows Desktop Tool Playbook | `domains/agent_workflow/playbooks/windows-desktop-tool-playbook.md` | Windows desktop app/tool, tray app, local GUI utility | `agent_workflow`, `backend`, `voice_assistant` when voice is involved | Code asset reuse rules, desktop assistant adapters/snippets, backend env/logging rules | Architecture, UI/runtime boundary, config/logging, startup/health checks, packaging/test plan |
| Browser Automation / RPA Playbook | `domains/automation/playbooks/browser-automation-rpa-playbook.md` | Upload tool, CDP automation, Playwright scripts, logged-in browser flows | `automation`, `agent_workflow`, `dev_tools` when downloads/imports are involved | Persistent browser daemon topic, browser QA pattern, agent preflight, GitHub import rules when needed | Browser/session assumptions, selectors, retries, upload/iframe/modal handling, screenshots/logs, verification |
| GitHub Project Analysis Intake Playbook | `domains/dev_tools/playbooks/github-project-analysis-intake-playbook.md` | Analyze GitHub repo and distill into database | `dev_tools`, `agent_workflow`, target domain | GitHub import rules, agent download workflow, code asset intake checklist, target domain rules | Download method, files read, license/security notes, raw modified=false, distillation target |
| Use This Database Playbook | `domains/agent_workflow/playbooks/use-local-database-for-task-playbook.md` | Let Claude Code/Codex use this database for a real task | `agent_workflow`, task-specific domains | Root AGENT_USAGE, CLAUDE, domain AGENT_USAGE, local API protocol | Retrieved queries/chunks/assets, domains used, files read, uncertainty, output constraints |
| Raw-to-Rules Distillation Playbook | `domains/agent_workflow/playbooks/raw-to-rules-distillation-playbook.md` | Upgrade raw资料 to rules/patterns/templates | `agent_workflow`, source domain, `dev_tools` for imports | Code asset reuse rules, curation guides, GitHub project selection rules, target domain templates | Source list, distilled rules/patterns/templates, provenance, rejected raw details, verification |

## Highest Priority

1. `premium-frontend-page-playbook.md` because UI tasks are frequent and require disciplined asset/rule routing.
2. `backend-api-design-playbook.md` because backend rules/templates already exist but need a task-shaped entry.
3. `raw-to-rules-distillation-playbook.md` because the graph contains a large amount of raw material that should not become default context.

## Risk Notes

- Playbooks should not duplicate whole rule files.
- Playbooks should point to existing rules, patterns, templates, and checklists.
- Raw playbooks must preserve `raw source modified: false` unless the user explicitly asks for maintenance work.
