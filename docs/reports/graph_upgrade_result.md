# Graph Upgrade Result

Date: 2026-05-03

## Baseline Scan

- Scanned Markdown files before modification: **1309**
- Isolated nodes before modification: **568**
- Weak nodes before modification: **1078**
- Unresolved links before modification: **41**

Scan exclusions: `.git`, `.venv`, `venv`, `env`, `node_modules`, `__pycache__`, `.omx`, `.obsidian`, `.claude`.

## Current Post-Skeleton State

After adding the knowledge skeleton but before counting generated reports as core knowledge:
- Markdown files: **1324**
- Isolated nodes: **354**
- Weak nodes: **1024**
- Unresolved links: **32**

The remaining unresolved links are in raw upstream material, mostly imported GitHub docs with broken or nonstandard relative links. They were not changed.

Final verification after generating reports and updating task memory:
- Markdown files: **1328**
- Isolated nodes: **357**
- Weak nodes: **1027**
- Unresolved links: **32**
- Unresolved links from changed files: **0**

## Files Added

1. `CLAUDE.md`
2. `domains/backend/AGENT_USAGE.md`
3. `domains/ui_design/AGENT_USAGE.md`
4. `domains/ui_assets/AGENT_USAGE.md`
5. `domains/agent_workflow/AGENT_USAGE.md`
6. `domains/automation/AGENT_USAGE.md`
7. `domains/dev_tools/AGENT_USAGE.md`
8. `domains/voice_assistant/AGENT_USAGE.md`
9. `domains/backend/rules/index.md`
10. `domains/backend/wiki/topics/index.md`
11. `domains/backend/wiki/patterns/index.md`
12. `domains/backend/wiki/checklists/index.md`
13. `domains/backend/wiki/templates/index.md`
14. `domains/ui_design/wiki/topics/index.md`
15. `domains/ui_design/wiki/summaries/index.md`
16. `docs/reports/obsidian_graph_audit.md`
17. `docs/reports/high_value_isolated_nodes.md`
18. `docs/reports/playbook_gap_report.md`
19. `docs/reports/graph_upgrade_result.md`

## Files Modified

1. `wiki/index.md`
2. `domains/backend/wiki/index.md`
3. `domains/ui_design/wiki/index.md`
4. `domains/backend/rules/backend-engineering-map.md`
5. `domains/ui_design/wiki/topics/premium-ui-execution-quality-rules.md`
6. `domains/agent_workflow/rules/code-asset-reuse-rules.md`
7. `domains/dev_tools/rules/github_import_rules.md`

## What Was Not Modified

- No `raw/` file was modified.
- No raw GitHub project was deleted, moved, renamed, or normalized.
- No SQLite index or runtime DB was rebuilt.
- No processed JSON/chunk files were changed.
- Prior output reports were left unchanged because they are historical artifacts.

## Main Improvements

1. Root `CLAUDE.md` now gives Claude Code and similar agents a short, task-routed entry.
2. Each major domain now has an `AGENT_USAGE.md` that tells agents what to read first and what to avoid.
3. Backend curated rules/topics/patterns/checklists/templates now have index files instead of being many isolated high-value docs.
4. UI premium topics and brand topics/summaries now have real topic/summary indexes.
5. Selected high-value rule files now have explicit `Related Knowledge` sections.
6. Raw sources remain separate from reusable rules, patterns, templates, and playbooks.

## Files Left for Later Human Judgment

- `domains/backend/processed/cleaned_text/github_projects/*.analysis.md`: useful provenance, but not all should be promoted.
- `domains/backend/output/reports/*.md`: historical reports; link only from maintenance playbooks if needed.
- `domains/ui_design/processed/cleaned_text/design-*.md`: processed source, useful for curation but not default task context.
- `domains/ui_design/wiki/topics/design-*.md`: useful brand flavor references; some may still be information-light.
- `domains/backend/raw/**`, `domains/ui_design/raw/**`, `domains/voice_assistant/raw/**`, `domains/dev_tools/raw/**`: raw source material; do not force-connect.

## Claude Code Usability Gains

Claude Code can now answer these questions quickly:

1. Which domain should I read for the task?
2. Which rules, patterns, checklists, or templates apply?
3. Which files are source material only?
4. Which asset policies constrain UI work?
5. Which raw-to-curated path should future maintenance follow?

## Next Best Work

1. Create the high-priority playbooks from `docs/reports/playbook_gap_report.md`.
2. Add backend `playbooks/` after selecting the exact tasks that recur most.
3. Review UI brand topics and mark low-information ones as secondary references.
4. Add a small automated graph check script that reports isolated curated nodes without touching raw.
5. Consider API retrieval updates only after file-level graph routing stabilizes.
