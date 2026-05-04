# Agent Workflow AGENT_USAGE

## Purpose

Use this domain for agentic coding workflows, review gates, handoffs, task decomposition, code asset reuse, and knowledge-base maintenance.

## When to Use

- Planning or executing agentic software work
- Designing review gates or handoff artifacts
- Reusing code assets from this database
- Distilling raw source material into reusable rules, patterns, templates, or checklists

## Read First

1. [Agent Workflow wiki index](wiki/index.md)
2. [Code Asset Reuse Rules](rules/code-asset-reuse-rules.md) when reusing code capabilities
3. [Code Assets Global Index](wiki/indexes/code-assets-global-index.md)
4. Relevant patterns, checklists, templates, snippets, or adapters
5. `output/` only for provenance or handoff history

## Task Playbooks

- [Use Local Database for Task Playbook](playbooks/use-local-database-for-task-playbook.md)
- [Windows Desktop Tool Playbook](playbooks/windows-desktop-tool-playbook.md)
- [Raw-to-Rules Distillation Playbook](playbooks/raw-to-rules-distillation-playbook.md)

## Prompt and Curation Index

For reusable prompts, curation guides, ingestion prompts, and database maintenance workflows, read:

- [Prompt and Curation Index](wiki/prompt-and-curation-index.md)

## Task Routing

- Agent delivery flow:
  [GStack Agentic Development Workflow](wiki/topics/gstack-agentic-development-workflow.md),
  [Think Plan Build Review Test Ship Reflect](wiki/patterns/think-plan-build-review-test-ship-reflect.md)
- Review gates: [Role-Based Agent Review Gates](wiki/patterns/role-based-agent-review-gates.md)
- Learning loop: [Agent Retro Learning Loop](wiki/patterns/agent-retro-learning-loop.md)
- Preflight: [Agentic Development Preflight Checklist](wiki/checklists/agentic-development-preflight-checklist.md)
- Handoff: [Agentic Development Handoff Template](wiki/templates/agentic-development-handoff-template.md)
- Code assets:
  [Code Assets Global Index](wiki/indexes/code-assets-global-index.md),
  [Code Asset Record Template](wiki/templates/code-asset-record-template.md),
  [Code Asset Intake Checklist](wiki/checklists/code-asset-intake-checklist.md)

## Do Not Use by Default

- raw source projects
- output reports as current rules
- code assets without license, dependency, adapter, and test review

## Output Requirements

- State which workflow pattern or code asset rule shaped the execution.
- List source files read when distilling or reusing knowledge.
- Do not scan all raw source projects to find reusable code.
