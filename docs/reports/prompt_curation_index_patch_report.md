# Prompt Curation Index Patch Report

## Date

2026-05-03

## Goal

Connect the remaining high-value prompt, curation, ingestion, handoff, and optimization nodes to the curated agent workflow and reports network without connecting raw or temporary files.

## Files Scanned

Searched with `rtk find` / `rtk grep` for:

- `CURATION_GUIDE`
- `codex_dev_prompt`
- `download_prompt`
- `ingest_prompt`
- `optimization_report`
- `gstack-handoff`
- `TASK_MEMORY`
- `AGENTS`
- `download_log`
- `*.canvas`
- `*.base`

## Files Added

- `domains/agent_workflow/wiki/prompt-and-curation-index.md`
- `docs/reports/prompt_curation_index_patch_report.md`

## Files Modified

- `domains/agent_workflow/AGENT_USAGE.md`
- `docs/reports/index.md`

## Agent Workflow Links Added

Added to `domains/agent_workflow/wiki/prompt-and-curation-index.md`:

- `domains/agent_workflow/CURATION_GUIDE.md`
- `domains/automation/CURATION_GUIDE.md`
- `domains/ui_design/CURATION_GUIDE.md`
- `domains/voice_assistant/prompts/codex_dev_prompt.md`
- `domains/voice_assistant/prompts/download_prompt.md`
- `domains/voice_assistant/prompts/ingest_prompt.md`
- `domains/dev_tools/AGENT_USAGE.md`
- `domains/dev_tools/rules/github_import_rules.md`

Added to `domains/agent_workflow/AGENT_USAGE.md`:

- `domains/agent_workflow/wiki/prompt-and-curation-index.md`

## Reports Links Added

Added to `docs/reports/index.md`:

- `domains/ui_design/optimization_report.md`
- `domains/agent_workflow/output/handoffs/gstack-handoff.md`

## Intentionally Not Connected

- `TASK_MEMORY.md`: left as maintenance history, not a default task entry.
- `AGENTS.md`: already functions as a compatibility entry pointing to canonical agent rules.
- `domains/backend/raw/github_projects/fastapi/fastapi-best-practices/AGENTS.md`: raw third-party project file, not linked.
- `download_log.md` files: operational download records, not reusable knowledge.
- `未命名.canvas`, `未命名 1.canvas`, `未命名.base`: temporary Obsidian/local files, not linked.
- `hot` / `log` style files: no durable knowledge asset identified in this pass.

## Validation

- `git diff --check`: pass
- raw modified: no
- processed modified: no
- runtime modified: no
- `.obsidian` modified: no
- canvas/base added: no
- unresolved links introduced: no

## Next Recommended Work

Do not continue large-scale graph linking. Build a small evals task set for database maintenance workflows instead:

1. raw-to-rules distillation task
2. prompt design task
3. source ingestion task
4. report/index update task
5. no-raw-modification regression check
