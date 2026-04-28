# Backend Knowledge Domain

`domains/backend` 是本地 AI 数据库里的后端工程知识域。它用于把后端 API、数据库、鉴权权限、安全、部署、可观测性、AI backend 和 GitHub 开源项目分析沉淀成 Agent 可读取、可执行、可检索的规则。

GitHub 项目源码只是 `raw/github_projects` 原始资料；真正给 Agent 使用的是 `rules/`、`wiki/`、`references/` 和 `processed/` chunks。不要让 Agent 为普通任务直接读取或照搬 raw 源码。

## 这个领域给 Agent 解决什么问题

- 生成 API / 后台接口 / 小程序后端 / 管理系统后端时，先确定架构边界、接口约定、错误处理、日志、安全和部署基线。
- 设计数据库、表结构、迁移、索引、约束、审计字段和数据生命周期。
- 生成登录、注册、用户系统、管理员权限、RBAC、JWT、refresh token、session 等鉴权和授权代码。
- 为 Docker Compose、环境变量、CI、健康检查、日志与监控生成保守默认方案。
- 为 AI 应用后端、RAG、Agent API、OpenAI-compatible API、SSE 流式输出和文件 ingestion 生成工程化规则。
- 分析 GitHub 后端开源项目时，区分核心参考、较好参考、样本和低价值样本。

## 什么时候优先读取 backend 规则

当任务包含 API、后端、后台、服务端、数据库、登录、注册、权限、JWT、Session、RBAC、Docker、部署、环境变量、RAG、Agent、大模型 API、流式输出、文件上传、Webhook、任务队列、日志、监控、错误码、分页、幂等、GitHub 后端项目分析等关键词时，优先读取本领域规则。

不要把后端规则用于纯前端页面、纯 UI 视觉、landing page、素材整理或浏览器自动化任务。普通个人项目默认不要强行引入微服务、Kubernetes、服务网格、复杂 DDD、CQRS、Event Sourcing 或多租户 SaaS 高级隔离。

## 任务路由优先级

### 开发 API / 后台接口 / 小程序后端 / 管理系统后端

优先读取：

- `rules/backend-engineering-map.md`
- `rules/api-design-rules.md`
- `rules/backend-layered-architecture-rules.md`
- `rules/error-handling-and-logging-rules.md`

### 数据库 / 表结构 / 数据存储

优先读取：

- `rules/database-modeling-rules.md`
- `wiki/checklists/database-design-checklist.md`
- `wiki/patterns/controller-service-repository-pattern.md`

### 登录 / 注册 / 权限 / 管理员 / 用户系统

优先读取：

- `rules/auth-and-permission-rules.md`
- `rules/backend-security-checklist.md`
- `wiki/checklists/auth-security-checklist.md`
- `wiki/patterns/jwt-refresh-token-pattern.md`
- `wiki/patterns/rbac-permission-pattern.md`

### 上线 / 部署 / Docker / 环境变量 / 服务器

优先读取：

- `rules/deployment-and-env-rules.md`
- `wiki/checklists/deployment-readiness-checklist.md`
- `wiki/templates/docker-compose-backend-template.md`

### AI 应用 / RAG / Agent / 大模型 API / 流式输出

优先读取：

- `rules/ai-backend-design-rules.md`
- `wiki/topics/ai-application-backend-rag-agent.md`
- `wiki/checklists/ai-backend-checklist.md`
- `wiki/patterns/rag-backend-pipeline-pattern.md`
- `wiki/patterns/sse-streaming-response-pattern.md`

### 分析 GitHub 后端开源项目

优先读取：

- `rules/github-backend-project-selection-rules.md`
- `wiki/topics/github-backend-project-analysis.md`
- `wiki/checklists/github-project-quality-checklist.md`

## API 项目优先读取哪些文件

1. `rules/backend-engineering-map.md`
2. `rules/api-design-rules.md`
3. `rules/backend-layered-architecture-rules.md`
4. `rules/error-handling-and-logging-rules.md`
5. `rules/backend-security-checklist.md`

## 数据库设计任务优先读取哪些文件

1. `rules/database-modeling-rules.md`
2. `rules/backend-project-template-rules.md`
3. `wiki/checklists/database-design-checklist.md`
4. `wiki/patterns/controller-service-repository-pattern.md`

## 登录权限任务优先读取哪些文件

1. `rules/auth-and-permission-rules.md`
2. `rules/backend-security-checklist.md`
3. `wiki/checklists/auth-security-checklist.md`
4. `wiki/patterns/jwt-refresh-token-pattern.md`
5. `wiki/patterns/rbac-permission-pattern.md`

## 后端安全任务优先读取哪些文件

1. `rules/backend-security-checklist.md`
2. `rules/auth-and-permission-rules.md`
3. `rules/deployment-and-env-rules.md`
4. `rules/api-design-rules.md`

## 部署任务优先读取哪些文件

1. `rules/deployment-and-env-rules.md`
2. `rules/performance-and-stability-rules.md`
3. `rules/error-handling-and-logging-rules.md`
4. `wiki/checklists/deployment-readiness-checklist.md`

## AI 应用后端任务优先读取哪些文件

1. `rules/ai-backend-design-rules.md`
2. `rules/api-design-rules.md`
3. `rules/backend-security-checklist.md`
4. `wiki/patterns/rag-backend-pipeline-pattern.md`
5. `wiki/patterns/sse-streaming-response-pattern.md`

## GitHub 项目分析任务优先读取哪些文件

1. `rules/github-backend-project-selection-rules.md`
2. `domains/backend/output/reports/github-projects-analysis-report.md`
3. `domains/backend/processed/metadata/github_projects/*.metadata.json`
4. `domains/backend/processed/chunks/github_projects/*.chunks.json`

## 扩展 backend 领域数据库的顺序

1. 先放 raw 原始资料，不运行、不安装、不改源码。
2. 再生成 processed analysis、metadata、chunks。
3. 经人工确认后生成 `backend_reference.schema.json`。
4. 再写 rules。
5. 再写 wiki topics / patterns / checklists / templates。
6. 再生成 references JSON。
7. 最后才构建 SQLite 检索索引和 API 检索接口。

## 当前 backend 数据状态

- `raw/github_projects` 已有 FastAPI、AI backend、NestJS、Node/Express 项目样本。
- `processed/github_projects` analysis、metadata、chunks 已有。
- `common/schemas/backend_reference.schema.json` 正在建设。
- `rules/` 正在建设。
- `wiki/` 和 `references/` 目录已预留，内容仍待后续阶段生成。
- `runtime/db/sqlite` 不是本阶段目标，不要在规则建设阶段修改。
