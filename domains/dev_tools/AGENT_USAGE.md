# Dev Tools AGENT_USAGE

Use this domain for GitHub repository import, download acceleration, proxy fallback decisions, and agent-safe project intake.

## Agent Read Order

1. [GitHub Import Rules](rules/github_import_rules.md)
2. [Dev Tools wiki index](wiki/index.md)
3. [Agent Download Workflow](wiki/topics/agent_download_workflow.md)
4. [GitHub Download Acceleration](wiki/topics/github_download_acceleration.md)
5. [GitHub Repo Import Template](wiki/topics/github_repo_import_template.md)

## Task Routing

- Public repo import: use shallow clone first, then documented fallback order
- Release/raw file download: use proxy fallbacks only after official source fails
- Private repo: use official GitHub/VPN/self-hosted route, not public proxies

## Output Requirement

Record URL, method used, fallback sequence, local path, files read, and `raw source modified: false`.
