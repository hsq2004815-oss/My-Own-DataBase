# Backend Search Test Queries

## English Queries

- backend architecture API design JWT RBAC PostgreSQL Redis Docker
  - Expected: `rules/backend-engineering-map.md`, `wiki/topics/modern-backend-architecture.md`, `wiki/templates/fastapi-project-template.md`, `references/architecture/martin-fowler-monolith-first.json`
- REST API error code pagination idempotency OpenAPI
  - Expected: `rules/api-design-rules.md`, `wiki/patterns/error-code-system-pattern.md`, `wiki/templates/openapi-doc-template.md`, `references/api/openapi-specification.json`
- FastAPI project structure SQLAlchemy Alembic PostgreSQL
  - Expected: `wiki/templates/fastapi-project-template.md`, `rules/database-modeling-rules.md`, `references/api/fastapi-official-docs.json`, `references/github_projects/minimal-fastapi-postgres-template-analysis.json`
- NestJS clean architecture Prisma PostgreSQL auth
  - Expected: `wiki/templates/nestjs-project-template.md`, `rules/auth-and-permission-rules.md`, `wiki/patterns/rbac-permission-pattern.md`
- AI backend RAG SSE WebSocket vector database
  - Expected: `rules/ai-backend-design-rules.md`, `wiki/topics/ai-application-backend-rag-agent.md`, `wiki/patterns/rag-backend-pipeline-pattern.md`, `references/ai_backend/rag-backend-patterns.json`
- file upload backend security signed url
  - Expected: `wiki/patterns/file-upload-processing-pattern.md`, `wiki/templates/file-upload-backend-template.md`, `rules/backend-security-checklist.md`
- webhook signature retry idempotency
  - Expected: `wiki/patterns/webhook-signature-retry-pattern.md`, `references/api/stripe-idempotency.json`, `rules/api-design-rules.md`
- Docker env Nginx deployment backend
  - Expected: `rules/deployment-and-env-rules.md`, `wiki/templates/docker-compose-backend-template.md`, `references/deployment/nginx-reverse-proxy.json`

## Chinese Queries

- 后端架构 接口设计 数据库设计 权限 日志 部署
  - Expected: `rules/backend-engineering-map.md`, `wiki/topics/modern-backend-architecture.md`, `wiki/checklists/backend-project-start-checklist.md`
- 小程序后端 登录 权限 文件上传 安全
  - Expected: `wiki/topics/backend-for-mini-program-and-admin-system.md`, `rules/auth-and-permission-rules.md`, `wiki/patterns/file-upload-processing-pattern.md`
- 管理系统后端 RBAC 菜单权限 接口权限
  - Expected: `wiki/patterns/rbac-permission-pattern.md`, `wiki/checklists/auth-security-checklist.md`, `rules/auth-and-permission-rules.md`
- AI 应用后端 RAG 流式输出 向量数据库
  - Expected: `wiki/topics/ai-application-backend-rag-agent.md`, `wiki/patterns/sse-streaming-response-pattern.md`, `references/ai_backend/sse-streaming-ai-response.json`
- Docker 环境变量 Nginx FastAPI PostgreSQL
  - Expected: `wiki/topics/docker-env-deployment.md`, `wiki/templates/docker-compose-backend-template.md`, `references/deployment/docker-compose-env-secrets.json`
- 接口错误码 分页 幂等 OpenAPI
  - Expected: `wiki/topics/rest-api-response-and-error-code.md`, `wiki/patterns/api-response-wrapper-pattern.md`, `references/api/openapi-specification.json`
- 后端安全 越权 SQL注入 文件上传
  - Expected: `rules/backend-security-checklist.md`, `wiki/topics/backend-security-owasp-api.md`, `references/security/owasp-api-security-top10-2023.json`
- 后台任务 队列 重试 超时 日志
  - Expected: `wiki/patterns/background-task-queue-pattern.md`, `rules/performance-and-stability-rules.md`, `references/performance/celery-task-queue.json`

## Expected Retrieval Targets

每条查询应至少召回一个 rules 文件和一个 wiki/reference 文件。中文查询应通过 `retrieval.prompt_tags` 和 `keywords` 命中中英文混合标签。
