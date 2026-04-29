# Backend Knowledge Domain

`domains/backend` 是本地 AI 数据库里的后端工程知识域。它用于把后端 API、数据库、鉴权权限、安全、部署、可观测性、AI backend 和 GitHub 开源项目分析沉淀成 Agent 可读取、可执行、可检索的规则。

GitHub 项目源码只是 `raw/github_projects` 原始资料；真正给 Agent 使用的是 `rules/`、`wiki/`、`references/` 和 `processed/` chunks。不要让 Agent 为普通任务直接读取或照搬 raw 源码。

当前阶段：backend 已完成 Phase 2A/2B 文档化知识层，包括 schema、README、13 个 rules、12 个 topics、12 个 patterns、10 个 checklists、12 个 templates 和 28 个 references JSON。它尚未进入 runtime SQLite、API 检索或 `/brief` 接入阶段。

## Agent 入口规则

当任务涉及后端、API、数据库、登录权限、安全、部署、Docker、RAG、AI backend、SSE、Webhook、任务队列或后端 GitHub 项目分析时，先读取本文件，再按任务类型读取下方优先文件。

当前不要为了 backend 任务启动 `backend_api`、调用 `/brief` 期待 backend 结果、构建 SQLite 索引或修改 `runtime/db/sqlite`。在 Phase 2C 完成 processed manifest / chunks / 检索准备之前，backend 的权威入口是 curated docs：

- `rules/*.md`
- `wiki/topics/*.md`
- `wiki/patterns/*.md`
- `wiki/checklists/*.md`
- `wiki/templates/*.md`
- `references/**/*.json`
- `processed/metadata/github_projects/*.metadata.json`
- `processed/chunks/github_projects/*.chunks.json`

不要把 `raw/github_projects` 当作日常 Agent 上下文。只有维护、审计或补充分析任务明确要求时，才静态读取 raw；仍然不要运行项目、安装依赖或复制开源源码/secret 原文。

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
- `common/schemas/backend_reference.schema.json` 已创建并用于 28 个 references JSON。
- `rules/` 已有 13 个核心规则文件。
- `wiki/topics` 已有 12 个专题。
- `wiki/patterns` 已有 12 个可落地模式。
- `wiki/checklists` 已有 10 个项目审查清单。
- `wiki/templates` 已有 12 个后端模板。
- `references/` 已有 28 个 JSON reference，覆盖 API、数据库、鉴权、安全、部署、可观测性、性能队列、架构、AI backend 和 GitHub 项目分析。
- `output/reports/backend-phase-2b-wiki-references-report.md` 和 `output/reports/backend-phase-2b-audit-and-repair-report.md` 记录了 Phase 2B 生成与审计结果。
- `runtime/db/sqlite` 不是当前 backend 阶段目标；不要在文档入口更新或 Phase 2B 审计阶段修改。

## 下一阶段

下一阶段建议进入 Phase 2C：

1. 生成 backend processed knowledge manifest。
2. 汇总 rules/wiki/references 为可检索 chunks。
3. 验证 chunk 结构、标签、来源和 secret 安全。
4. 再评估是否构建 SQLite 索引。
5. 最后才考虑 backend API / brief 接入。
