# Isolated Node Connection Report

## Date

2026-05-03

## Scan Scope

Scanned Markdown files under `E:\DataBase`.

Excluded non-knowledge/runtime folders:

- `.git`
- `.venv`
- `venv`
- `env`
- `node_modules`
- `__pycache__`
- `.omx`
- `.obsidian`
- `.claude`

## Scan Result

- Markdown files scanned: 1332
- Isolated nodes found: 358
- Weak connection nodes found: 1024
- Existing unresolved links found during scan: 32

The unresolved links are from existing raw or upstream documents. This pass did not modify those files.

## Classification Result

### A Class: UI Design References

Detected 198 weak or isolated UI design reference nodes.

Connected through:
- [Design Reference Index](../../domains/ui_design/wiki/references/design-reference-index.md)

Connected node types:
- `domains/ui_design/wiki/topics/design-*.md`
- `domains/ui_design/wiki/summaries/design-*.md`
- `domains/ui_design/processed/cleaned_text/design-*.md`

Reason:
these are curated or processed UI design references that help Claude Code choose visual flavor after reading the premium UI rule layer.

### B Class: Backend Project Analyses

Detected 13 weak or isolated backend project analysis nodes.

Connected through:
- [Backend Project Analysis Index](../../domains/backend/wiki/references/backend-project-analysis-index.md)

Connected node type:
- `domains/backend/processed/cleaned_text/github_projects/*.analysis.md`

Reason:
these are processed analysis artifacts, not raw source. They are useful evidence for backend API, RAG, SSE, PostgreSQL, Node, Express, Prisma, and NestJS tasks.

### C Class: Database Maintenance Reports

Detected 14 report nodes in the report layer.

Connected through:
- [Reports Index](index.md)

Connected report areas:
- graph audit
- playbook gap report
- index build report
- GitHub project analysis report
- markdown format fix report
- backend phase reports
- agent workflow reports

Reason:
reports are historical maintenance context and should be discoverable from a report index instead of being linked into task rules directly.

## Actually Connected High-Value Nodes

Existing high-value weak or isolated nodes connected in this pass:

- UI design reference nodes: 198
- Backend project analysis nodes: 13
- Existing report nodes: 14

Total connected existing high-value nodes: 225

The new `isolated_node_connection_report.md` is also linked from [Reports Index](index.md), but it is not counted as a pre-existing isolated node.

## Post-Connection Check

After adding the indexes and this report:

- Markdown files scanned: 1336
- Isolated nodes remaining: 266
- Weak connection nodes remaining: 879
- Unresolved links from files changed in this pass: 0

## Nodes Not Connected

### D Class: Raw README / Multilingual README / Third-Party Docs

Not connected by design.

Detected examples:
- `README.md`
- `README_zh.md`
- `readme.md`
- translated `nodebestpractices` files
- third-party project docs under `raw/`

Reason:
raw docs are provenance and curation inputs. Connecting them all would make agents read upstream source material instead of curated rules and indexes.

### E Class: Temporary or Low-Value Files

Not connected by design.

Detected examples:
- `download_log.md`
- `screenshot-placeholder.md`
- `未命名.canvas`
- `未命名.base`

Reason:
these are operational or temporary artifacts. They should be manually reviewed or ignored, not connected into the knowledge network.

### Other Isolated Nodes

Some non-raw isolated nodes remain unconnected because they are not part of this pass:

- old output reports not relevant to current entry routing
- script or maintenance notes that need separate review
- files already reachable through runtime API or existing domain entry points

## Files Added

- `domains/ui_design/wiki/references/design-reference-index.md`
- `domains/backend/wiki/references/backend-project-analysis-index.md`
- `docs/reports/index.md`
- `docs/reports/isolated_node_connection_report.md`

## Files Modified

- `domains/ui_design/wiki/index.md`
- `domains/backend/wiki/index.md`

## Raw Modification Status

Raw modified by this pass: no.

No `raw/` file was edited, moved, renamed, or staged.

## Link Validation

Missing links produced by this pass: none.

Raw Markdown links added by this pass: none.

All new index links point to existing Markdown files.

## Next Recommended Work

1. Add an ignore/review policy for `download_log`, canvas, base, and placeholder files.
2. Add a curated-only graph checker script that excludes `raw/` by default.
3. Review remaining non-raw isolated nodes in `scripts/`, `backend_api/`, and older output reports.
4. Consider adding `docs/reports/index.md` to a higher-level agent entry only if reports become common task context.
