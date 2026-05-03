# Raw-to-Rules Distillation Playbook

## When to Use

Use this playbook when the task is to:

- upgrade raw material into rules, patterns, templates, checklists, or topics
- analyze a GitHub project and add durable knowledge to the database
- clean source notes into reusable agent context
- extract reusable engineering ideas from one-off project experience
- connect curated knowledge to existing indexes without touching raw source

Do not use it for ordinary code generation tasks.

## Read First

- [Agent Workflow AGENT_USAGE](../AGENT_USAGE.md)
- [Code Asset Reuse Rules](../rules/code-asset-reuse-rules.md)
- [Dev Tools AGENT_USAGE](../../dev_tools/AGENT_USAGE.md)
- [GitHub Import Rules](../../dev_tools/rules/github_import_rules.md)

Choose the target domain entry:

- [Backend AGENT_USAGE](../../backend/AGENT_USAGE.md)
- [UI Design AGENT_USAGE](../../ui_design/AGENT_USAGE.md)
- [UI Assets AGENT_USAGE](../../ui_assets/AGENT_USAGE.md)
- [Automation AGENT_USAGE](../../automation/AGENT_USAGE.md)
- [Voice Assistant AGENT_USAGE](../../voice_assistant/AGENT_USAGE.md)

## Intake Checklist

- Original source path
- Target domain
- Source type
- License and security risk
- Existing processed, chunks, wiki, rules, patterns, templates, or checklists
- Intended output type
- Whether raw content is reference-only or can become reusable guidance

## Distillation Steps

1. Identify source material and scope.
2. Read only necessary raw or processed files.
3. Extract reusable engineering ideas.
4. Separate facts, rules, patterns, templates, and project-specific details.
5. Create or update curated files in the target domain.
6. Add provenance links where they help future agents.
7. Update the relevant index or MOC.
8. Report rejected or low-value material.

## Must Include in Output

- Source files read
- Curated files created or updated
- Rules, patterns, templates, checklists, or topics extracted
- What was intentionally not promoted
- `raw source modified: false`
- Remaining uncertainty

## Avoid

- Copying large raw README passages into wiki
- Turning project-specific details into universal rules
- Marking code as reusable before license review
- Modifying raw source material
- Adding links only to make the graph look denser
- Rebuilding runtime SQLite unless the task explicitly asks for retrieval maintenance

## Completion Check

- Raw source files were not modified.
- New links point to existing Markdown files.
- Curated output has a clear domain entry path.
- The final report separates promoted knowledge from rejected material.
- Any license, security, or provenance uncertainty is stated.
