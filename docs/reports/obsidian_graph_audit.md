# Obsidian Graph Audit

Audit date: 2026-05-03

## Scope

Baseline scan covered Markdown files under the repository root and excluded `.git`, `.venv`, `venv`, `env`, `node_modules`, `__pycache__`, `.omx`, `.obsidian`, and `.claude`.

The scan counted:
- Obsidian double-bracket wiki links
- Markdown links whose target ends in `.md`

Raw third-party repositories were scanned for graph shape, but they were not modified.

## Current Database Structure

The repository is a local AI second-brain and retrieval database. The main domains found in the baseline scan were:

| Domain | Baseline Markdown files | Role |
| --- | ---: | --- |
| `backend` | 803 | Backend rules, wiki, templates, processed project analyses, and raw GitHub backend sources |
| `ui_design` | 273 | Premium UI rules, brand design topics/summaries, processed design references, and raw design source |
| `voice_assistant` | 168 | XiaoHuang voice assistant context plus raw STT/TTS/wake-word projects |
| `agent_workflow` | 21 | Agent delivery workflow, review gates, code asset reuse, handoff templates |
| `dev_tools` | 20 | GitHub import/download acceleration rules and raw proxy tool sources |
| `scripts` | 8 | Script README files |
| `automation` | 5 | Playwright/CDP/browser QA patterns |
| `wiki` | 3 | Root wiki and shared indexes |
| `ui_assets` | 2 | Asset usage policy and metadata workflow |
| root entry files | 5 | `README.md`, `AGENT.md`, `AGENTS.md`, `AGENT_USAGE.md`, `TASK_MEMORY.md` |
| `backend_api` | 1 | Local API README |

## File Type Statistics

Baseline Markdown count: **1309**

| Layer | Count | Notes |
| --- | ---: | --- |
| `raw` | 946 | Mostly third-party GitHub sources; do not force-connect |
| `wiki` | 200 | Human-readable topics, summaries, patterns, checklists, templates |
| `processed` | 80 | Cleaned text and processed analysis artifacts |
| `entry` | 21 | README/AGENT/AGENT_USAGE/TASK_MEMORY style entry files |
| `patterns` | 16 | Pattern files, mainly backend and agent workflow |
| `rules` | 15 | Curated rule files |
| `templates` | 14 | Template files |
| `output` | 10 | Reports/handoffs from prior maintenance phases |
| `other` | 7 | Curation guides and miscellaneous docs |

## Link Statistics

Baseline graph:
- Isolated nodes: **568**
- Weak nodes (`in + out <= 1`): **1078**
- Unresolved Markdown/wiki links: **41**

Important interpretation:
- Most isolated nodes are raw upstream docs or processed artifacts. This is expected and should not be "fixed" by random links.
- The problem worth fixing is that curated rules/wiki/templates had few explicit entry paths.
- Several high-degree nodes are raw upstream READMEs. They are core only inside their imported project, not core to the user's second-brain graph.

## Core Nodes Found

High-degree nodes in the baseline scan were dominated by raw imported repositories:

| Node | In | Out | Judgment |
| --- | ---: | ---: | --- |
| `domains/backend/raw/github_projects/node/nodebestpractices/README.md` | 4 | 97 | Raw source hub, do not use as default agent entry |
| `domains/backend/raw/github_projects/node/nodebestpractices/README.*.md` | 0-11 | 59-95 | Raw translated upstream hubs |
| `domains/voice_assistant/raw/github/repos/FunASR/runtime/readme_cn.md` | 18 | 6 | Raw source hub |
| `domains/agent_workflow/wiki/index.md` | 1 | 14 | Real curated domain hub |
| `wiki/index.md` | 0 | 10 | Real root knowledge hub |
| `domains/voice_assistant/README.md` | 0 | 8 | Real domain entry |

## Initial Node Classes

### A Class: High-Value Isolated or Weak Nodes

These should be connected through domain entry files and MOCs:
- Backend curated `rules/`, `wiki/topics/`, `wiki/patterns/`, `wiki/checklists/`, `wiki/templates/`
- UI premium rule topics under `domains/ui_design/wiki/topics/`
- Agent workflow code asset rules, patterns, checklists, and templates
- Automation topic/pattern files
- Dev tools GitHub import/download rules
- Voice assistant distilled wiki topics
- Root agent entry files and domain README files

### B Class: Ordinary Isolated Nodes

These can remain weak until a concrete retrieval need appears:
- `processed/cleaned_text` design files
- Brand summary files not yet promoted to task routing
- Prior `output/reports` files
- Script README files not used by agent routing

### C Class: Raw Source Material

Raw files should not be force-connected:
- `domains/backend/raw/**`
- `domains/ui_design/raw/**`
- `domains/voice_assistant/raw/**`
- `domains/dev_tools/raw/**`

Raw files are provenance and curation inputs, not ordinary agent context.

### D Class: Needs Later Human Judgment

Do not delete. Review later:
- Translated duplicates in `nodebestpractices/README.*.md`
- Prior backend phase reports under `domains/backend/output/reports/`
- Processed GitHub project analyses under `domains/backend/processed/cleaned_text/github_projects/`
- Information-light brand design topics marked by `domains/ui_design/optimization_report.md`

## Recommended Upgrade Direction

The graph should be improved by adding agent-useful middle layers:
- Root `CLAUDE.md`
- Domain `AGENT_USAGE.md`
- Rules/topic/pattern/checklist/template indexes
- Playbook gap report for future task playbooks

Do not optimize for graph density. Optimize for reliable task routing.
