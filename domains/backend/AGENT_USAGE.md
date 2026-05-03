# Backend AGENT_USAGE

Use this domain for API, database, auth, security, deployment, observability, RAG, queue, webhook, and backend project template tasks.

## Default Retrieval

Prefer runtime retrieval before file reading:
- `POST http://127.0.0.1:8765/brief` with `backend_limit` set to 6-10
- `GET http://127.0.0.1:8765/backend/search?q=<query>&limit=<n>`

If the API is unavailable, read [README](README.md), then route through the indexes below.

## Agent Read Order

1. [Rules Index](rules/index.md)
2. [Topics Index](wiki/topics/index.md)
3. [Patterns Index](wiki/patterns/index.md)
4. [Checklists Index](wiki/checklists/index.md)
5. [Templates Index](wiki/templates/index.md)
6. `references/**/*.json` only when source metadata is needed
7. `processed/retrieval/backend-retrieval-chunks.jsonl` only when retrieval chunk inspection is needed

Do not read or copy from `raw/` for normal backend generation. Raw projects are source material for maintenance and later distillation only.

## Task Routing

- API contract / response shape: [API Design Rules](rules/api-design-rules.md), [API First Design](wiki/topics/api-first-design.md), [API Response Wrapper Pattern](wiki/patterns/api-response-wrapper-pattern.md), [API Response Template](wiki/templates/api-response-template.md)
- Database schema / indexing: [Database Modeling Rules](rules/database-modeling-rules.md), [Database Modeling and Indexing](wiki/topics/database-modeling-and-indexing.md), [Database Design Checklist](wiki/checklists/database-design-checklist.md)
- Auth / permission / session: [Auth and Permission Rules](rules/auth-and-permission-rules.md), [Auth Session JWT OAuth RBAC](wiki/topics/auth-session-jwt-oauth-rbac.md), [JWT Refresh Token Pattern](wiki/patterns/jwt-refresh-token-pattern.md), [RBAC Permission Pattern](wiki/patterns/rbac-permission-pattern.md)
- Security review: [Backend Security Checklist](rules/backend-security-checklist.md), [Backend Security OWASP API](wiki/topics/backend-security-owasp-api.md), [Security Before Release Checklist](wiki/checklists/security-before-release-checklist.md)
- Deployment / env / Docker: [Deployment and Env Rules](rules/deployment-and-env-rules.md), [Docker Env Deployment](wiki/topics/docker-env-deployment.md), [Docker Compose Backend Pattern](wiki/patterns/docker-compose-backend-pattern.md)
- RAG / LLM backend / SSE: [AI Backend Design Rules](rules/ai-backend-design-rules.md), [AI Application Backend RAG Agent](wiki/topics/ai-application-backend-rag-agent.md), [RAG Backend Pipeline Pattern](wiki/patterns/rag-backend-pipeline-pattern.md), [SSE Streaming Response Pattern](wiki/patterns/sse-streaming-response-pattern.md)
- Project scaffolding: [Backend Project Template Rules](rules/backend-project-template-rules.md), then choose a template from [Templates Index](wiki/templates/index.md)

## Output Requirement

Report which backend rules, patterns, checklists, and templates affected the answer. State when raw source was not read.
