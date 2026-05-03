# High-Value Isolated and Weak Nodes

Baseline scan date: 2026-05-03

This report lists high-value isolated or weak Markdown nodes that should be connected to the knowledge network. Counts are from the baseline scan before this upgrade.

## Immediate Connection Set

| File | In | Out | Domain | Why it is valuable | Suggested hubs | Modify now |
| --- | ---: | ---: | --- | --- | --- | --- |
| `README.md` | 0 | 0 | root | Repository purpose and runtime contract | `CLAUDE.md`, `wiki/index.md` | Yes |
| `AGENT.md` | 0 | 0 | root | Canonical agent behavior rules | `CLAUDE.md`, `wiki/index.md` | Yes |
| `AGENT_USAGE.md` | 0 | 0 | root | Short local API usage guide | `CLAUDE.md`, `wiki/index.md` | Yes |
| `domains/backend/README.md` | 0 | 0 | backend | Backend domain entry | `domains/backend/AGENT_USAGE.md` | Yes |
| `domains/backend/rules/backend-engineering-map.md` | 0 | 0 | backend | Main backend routing map | backend rules index, backend AGENT_USAGE | Yes |
| `domains/backend/rules/backend-agent-usage-rules.md` | 0 | 0 | backend | Agent consumption rules for backend docs | backend rules index | Yes via index |
| `domains/backend/rules/api-design-rules.md` | 0 | 0 | backend | API contract and response rules | backend rules/topics/patterns indexes | Yes via index |
| `domains/backend/rules/database-modeling-rules.md` | 0 | 0 | backend | Schema, constraint, index rules | backend rules/topics/checklists indexes | Yes via index |
| `domains/backend/rules/auth-and-permission-rules.md` | 0 | 0 | backend | Auth, JWT, RBAC boundary rules | backend rules/topics/patterns indexes | Yes via index |
| `domains/backend/rules/backend-layered-architecture-rules.md` | 0 | 0 | backend | Controller/service/repository boundaries | backend rules/patterns indexes | Yes via index |
| `domains/backend/rules/error-handling-and-logging-rules.md` | 0 | 0 | backend | Error envelope and observability rules | backend rules/topics/patterns indexes | Yes via index |
| `domains/backend/rules/deployment-and-env-rules.md` | 0 | 0 | backend | Env and deployment constraints | backend rules/topics/checklists indexes | Yes via index |
| `domains/backend/rules/performance-and-stability-rules.md` | 0 | 0 | backend | Cache, queue, idempotency, stability | backend rules/topics/patterns indexes | Yes via index |
| `domains/backend/rules/ai-backend-design-rules.md` | 0 | 0 | backend | RAG, SSE, LLM backend rules | backend rules/topics/patterns indexes | Yes via index |
| `domains/backend/rules/backend-project-template-rules.md` | 0 | 0 | backend | Scaffolding/template selection | backend rules/templates indexes | Yes via index |
| `domains/backend/rules/backend-security-checklist.md` | 0 | 0 | backend | Security gate | backend rules/checklists indexes | Yes via index |
| `domains/backend/rules/github-backend-project-selection-rules.md` | 0 | 0 | backend | Raw project evaluation without copying | backend rules/topics indexes | Yes via index |
| `domains/ui_design/wiki/topics/premium-ui-execution-quality-rules.md` | 0 | 0 | ui_design | Premium UI execution self-check | UI AGENT_USAGE, topics index | Yes |
| `domains/ui_design/wiki/topics/premium-web-ui-initial-aesthetic-rules.md` | 0 | 0 | ui_design | Default premium web aesthetic layer | UI AGENT_USAGE, topics index | Yes via index |
| `domains/ui_design/wiki/topics/premium-typography-and-layout-rules.md` | 0 | 0 | ui_design | Typography/layout quality rules | UI AGENT_USAGE, topics index | Yes via index |
| `domains/ui_design/wiki/topics/motion-interaction-premium-rules.md` | 0 | 0 | ui_design | Motion/interaction rules | UI AGENT_USAGE, UI assets entry | Yes via index |
| `domains/ui_design/wiki/topics/liquid-glass-design-system.md` | 0 | 0 | ui_design | Material system rule | UI AGENT_USAGE, topics index | Yes via index |
| `domains/ui_design/wiki/topics/liquid-glass-web-app-ui-kit.md` | 0 | 0 | ui_design | Web app/dashboard component system | UI AGENT_USAGE, topics index | Yes via index |
| `domains/ui_design/wiki/topics/cinematic-video-hero-rules.md` | 0 | 0 | ui_design | Hero/media layout rule | UI AGENT_USAGE, topics index | Yes via index |
| `domains/ui_design/wiki/topics/video-hero-layout-patterns.md` | 0 | 0 | ui_design | Hero variants and CTA/nav patterns | UI AGENT_USAGE, topics index | Yes via index |
| `domains/ui_design/wiki/topics/landing-page-section-patterns.md` | 0 | 0 | ui_design | Landing page section patterns | UI AGENT_USAGE, topics index | Yes via index |
| `domains/ui_design/wiki/topics/ui-agent-starter-prompt.md` | 0 | 0 | ui_design | Agent-facing UI starter prompt | UI AGENT_USAGE, topics index | Yes via index |
| `domains/agent_workflow/README.md` | 0 | 0 | agent_workflow | Domain entry | agent workflow AGENT_USAGE | Yes |
| `domains/agent_workflow/rules/code-asset-reuse-rules.md` | 0 | 0 | agent_workflow | Code reuse safety and lookup order | agent workflow AGENT_USAGE, code asset index | Yes |
| `domains/agent_workflow/wiki/topics/gstack-agentic-development-workflow.md` | 1 | 0 | agent_workflow | Agent software delivery topic | agent workflow AGENT_USAGE | Yes via entry |
| `domains/agent_workflow/wiki/patterns/think-plan-build-review-test-ship-reflect.md` | 1 | 0 | agent_workflow | Reusable delivery loop pattern | agent workflow AGENT_USAGE | Yes via entry |
| `domains/agent_workflow/wiki/patterns/role-based-agent-review-gates.md` | 1 | 0 | agent_workflow | Review-gate pattern | agent workflow AGENT_USAGE | Yes via entry |
| `domains/agent_workflow/wiki/patterns/agent-retro-learning-loop.md` | 1 | 0 | agent_workflow | Retrospective learning loop | agent workflow AGENT_USAGE | Yes via entry |
| `domains/automation/README.md` | 0 | 0 | automation | Automation domain entry | automation AGENT_USAGE | Yes |
| `domains/automation/wiki/topics/persistent-browser-daemon-for-agent-qa.md` | 1 | 0 | automation | Persistent browser QA topic | automation AGENT_USAGE | Yes via entry |
| `domains/automation/wiki/patterns/browser-qa-with-persistent-session.md` | 1 | 0 | automation | Browser QA pattern | automation AGENT_USAGE | Yes via entry |
| `domains/dev_tools/README.md` | 0 | 0 | dev_tools | Dev tools domain entry | dev tools AGENT_USAGE | Yes |
| `domains/dev_tools/rules/github_import_rules.md` | 0 | 0 | dev_tools | GitHub import safety and fallback rules | dev tools AGENT_USAGE, dev tools wiki | Yes |
| `domains/dev_tools/wiki/topics/agent_download_workflow.md` | 1 | 0 | dev_tools | Agent download workflow | dev tools AGENT_USAGE | Yes via entry |
| `domains/dev_tools/wiki/topics/github_download_acceleration.md` | 1 | 0 | dev_tools | Download acceleration knowledge | dev tools AGENT_USAGE | Yes via entry |
| `domains/dev_tools/wiki/topics/github_repo_import_template.md` | 1 | 0 | dev_tools | Import record template | dev tools AGENT_USAGE | Yes via entry |
| `domains/voice_assistant/README.md` | 0 | 8 | voice_assistant | Voice assistant domain entry | voice assistant AGENT_USAGE | Yes |
| `domains/voice_assistant/wiki/topics/xiaohuang_project_context.md` | 1 | 0 | voice_assistant | Project context | voice assistant AGENT_USAGE | Yes via entry |
| `domains/voice_assistant/wiki/topics/xiaohuang_voice_pipeline_notes.md` | 1 | 0 | voice_assistant | Voice pipeline notes | voice assistant AGENT_USAGE | Yes via entry |
| `domains/voice_assistant/wiki/topics/stt_engine_comparison.md` | 1 | 0 | voice_assistant | STT engine decision support | voice assistant AGENT_USAGE | Yes via entry |
| `domains/voice_assistant/wiki/topics/tts_engine_notes.md` | 1 | 0 | voice_assistant | TTS decision support | voice assistant AGENT_USAGE | Yes via entry |
| `domains/voice_assistant/wiki/topics/wake_word_trigger_command.md` | 1 | 0 | voice_assistant | Wake command design | voice assistant AGENT_USAGE | Yes via entry |

## Backend Curated Wiki Sets

The following backend sets were high-value but disconnected enough that they needed MOCs rather than per-file rewrites:

- Topics: `domains/backend/wiki/topics/*.md`
- Patterns: `domains/backend/wiki/patterns/*.md`
- Checklists: `domains/backend/wiki/checklists/*.md`
- Templates: `domains/backend/wiki/templates/*.md`

Action taken: create indexes under each folder and link them from [Backend AGENT_USAGE](../../domains/backend/AGENT_USAGE.md) and [Backend wiki index](../../domains/backend/wiki/index.md).

## UI Brand Topics and Summaries

Brand analysis files under `domains/ui_design/wiki/topics/design-*.md` and `domains/ui_design/wiki/summaries/design-*.md` are useful as flavor references, but they should not override the premium UI rule layer.

Action taken: create [UI topics index](../../domains/ui_design/wiki/topics/index.md) and [UI summaries index](../../domains/ui_design/wiki/summaries/index.md).

## Raw Source Material

No raw source file was recommended for immediate link editing. Raw files remain provenance and future curation inputs.
