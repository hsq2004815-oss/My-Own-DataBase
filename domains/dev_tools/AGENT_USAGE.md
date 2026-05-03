# Dev Tools AGENT_USAGE

## Purpose

Use this domain for GitHub repository import, download acceleration, proxy fallback decisions, and agent-safe project intake.

## When to Use

- Importing a GitHub repository into the database
- Choosing download acceleration or fallback methods
- Recording project intake provenance
- Evaluating whether raw material should be distilled later

## Read First

1. [GitHub Import Rules](rules/github_import_rules.md)
2. [Dev Tools wiki index](wiki/index.md)
3. [Agent Download Workflow](wiki/topics/agent_download_workflow.md)
4. [GitHub Download Acceleration](wiki/topics/github_download_acceleration.md)
5. [GitHub Repo Import Template](wiki/topics/github_repo_import_template.md)

## Task Routing

- Public repo import: use shallow clone first, then documented fallback order
- Release/raw file download: use proxy fallbacks only after official source fails
- Private repo: use official GitHub/VPN/self-hosted route, not public proxies

## Do Not Use by Default

- public proxies for private or signed URLs
- full history clone unless needed
- raw source as reusable rules without distillation

## Output Requirements

- Record URL, method used, fallback sequence, local path, and files read.
- State `raw source modified: false`.
- Record security or license concerns.
