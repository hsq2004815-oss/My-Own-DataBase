# Backend GitHub Projects Analysis Report

## 1. 本次扫描范围

本次只围绕 `E:\DataBase\domains\backend\raw\github_projects` 做静态分析，未运行项目、未安装依赖、未启动 API、未改 runtime SQLite、未写 rules/wiki。

扫描目录和项目：

- `ai_backend`：fastapi-langchain-rag、fastapi-openai-compat、fastapi-openai-sse-stream、rag_api
- `fastapi`：fastapi-best-practices、fastapi-sqlalchemy2-alembic-postgresql、fastapi-template、minimal-fastapi-postgres-template
- `nestjs`：awesome-nest-boilerplate、prime-nestjs
- `node`：express-ts-pg-prisma-boilerplate、express-typescript-skeleton、nodebestpractices

忽略策略：`.git`、`node_modules`、`venv`、`.venv`、`__pycache__`、`dist`、`build`、`target`、`.next`、`.cache`、`.vscode`、`.idea`、`coverage`、数据库/日志/压缩包/图片/视频等非分析文件。

## 2. 项目分级结果

### core_reference

- `fastapi-openai-compat`：协议边界清晰；测试/CI 完整；限制：不是完整应用；无数据库/鉴权。
- `rag_api`：RAG 领域完整度高；测试较完整；限制：无明确 migration；依赖重。
- `fastapi-best-practices`：规则清晰；有中文 README；限制：文档仓库非应用；无运行测试。
- `minimal-fastapi-postgres-template`：现代质量链完整；测试强；限制：Python 版本较新；refresh/RBAC 不完整。
- `express-ts-pg-prisma-boilerplate`：分层清楚；auth 安全细节强；限制：生产 Docker 还可改进；无 Swagger。
- `nodebestpractices`：社区最佳实践丰富；多语言文档；限制：非应用源码；无 DB/auth 实现。

### good_reference

- `fastapi-langchain-rag`：RAG 架构完整；docs 分章清晰；限制：测试证据弱；部署和解析依赖偏重。
- `fastapi-sqlalchemy2-alembic-postgresql`：结构清晰；DB/migration 线索明确；限制：无测试；部署不完整。
- `awesome-nest-boilerplate`：模块化完整；权限/Swagger/migration 清楚；限制：过重；env 私钥风险。
- `prime-nestjs`：生产能力均衡；auth/RBAC 清楚；限制：个人项目偏重；migration 需规范化。
- `express-typescript-skeleton`：架构边界强；测试/CI/CD 完整；限制：过重；个人项目性价比低。

### sample_only

- `fastapi-openai-sse-stream`：简单直接；有基础测试；限制：缺少工程化层次；无安全/部署/数据库。
- `fastapi-template`：简单；Docker Compose 包含 Redis/Postgres；限制：偏旧；扁平结构扩展性弱。

### low_reference

- 暂无

## 3. FastAPI 方向共同规则

- FastAPI 项目应区分 `core/config/database_session/lifespan` 与业务 feature，避免把配置、DB session、路由和业务逻辑堆在 `main.py`。
- 使用 PostgreSQL 的项目共同支持 SQLAlchemy/SQLModel + Alembic 的组合；进入核心 rules 前应优先采用 `minimal-fastapi-postgres-template` 和 `fastapi-sqlalchemy2-alembic-postgresql` 的交集。
- Pydantic schemas/settings 与 ORM models 应解耦；路由层只做请求/响应和依赖注入，业务逻辑放 service。
- 健康检查、metrics、pytest/coverage、Ruff/mypy/CI 是现代模板应优先提供的质量基线。
- 文档型 `fastapi-best-practices` 可支持 rules，但不能替代源码模板证据。

## 4. Node / Express 方向共同规则

- Express TypeScript 项目更适合按 feature 拆分 `routes/controllers/services/repositories/schemas/tests`，比单一全局 routes 文件更利于 Agent 生成可维护代码。
- Prisma + PostgreSQL 项目应把 schema、migrations、seed、DB client 和测试数据库准备纳入模板，不只生成 model。
- 认证项目应优先采用 access token + refresh token rotation、refresh token hash 存储、HttpOnly cookie 和 RBAC middleware。
- 统一 `AppError` / error middleware / validation middleware 是 Express 项目核心规则候选。
- DDD/hexagonal 结构只适合中型以上项目；个人项目默认使用较轻的 feature-based 四层结构。

## 5. NestJS 方向共同规则

- NestJS 样本数量只有 2 个，但共同支持 `module/controller/service/dto/entity/guard/strategy/spec` 的资源组织方式。
- Swagger/OpenAPI、class-validator DTO、JWT strategy、roles guard、TypeORM migrations 和 healthcheck 是可复用候选。
- `awesome-nest-boilerplate` 功能很全但明显偏重，且 `.env.example` 出现完整 RSA private key 文本风险；`prime-nestjs` 更适合作为较平衡样本。
- 因样本不足，NestJS 核心规则后续应再补官方文档或更多项目验证。

## 6. AI backend / RAG 方向共同规则

- RAG 后端应分离 ingestion、document loader、vector store、routes/services/schemas/models，不能把上传、解析、embedding、检索全部写进 controller。
- PostgreSQL/pgvector 是当前样本共同支持的向量存储默认参考；SQLite 不应作为 RAG 生产默认。
- 文件级 `file_id/document_id`、metadata filter、路径校验、上传隔离和文档解析测试应进入 AI backend 安全与稳定性规则候选。
- OpenAI-compatible API 应优先保持 `/v1/models`、`/v1/chat/completions`、Responses、Files、SSE streaming 的协议边界，并用 OpenAI client 兼容测试验证。
- 文档解析依赖、OCR、多向量存储和云部署应按需求加入，不作为个人项目默认依赖。

## 7. 候选 rules 写入清单

- `rules/api-design-rules.md`：REST route 组织、OpenAI-compatible `/v1` 协议、参数校验、healthcheck、统一响应/错误候选。
- `rules/database-modeling-rules.md`：SQLAlchemy/Alembic、Prisma migrations、PostgreSQL/pgvector、seed、连接/session 边界。
- `rules/auth-and-permission-rules.md`：JWT、refresh token rotation、HttpOnly cookie、RBAC guard/middleware、RSA key placeholder。
- `rules/backend-layered-architecture-rules.md`：FastAPI feature/core、Express 四层 feature、NestJS module/controller/service/dto/entity。
- `rules/error-handling-and-logging-rules.md`：Express error middleware、NestJS filters、FastAPI exception handler、request_id/trace_id 待补。
- `rules/backend-security-checklist.md`：secret/env 占位、上传路径校验、token hash、RBAC 越权、Docker 非 root。
- `rules/deployment-and-env-rules.md`：Docker/Compose healthcheck、env.example 占位、CI lint/type/test、不要复制真实密钥。
- `rules/performance-and-stability-rules.md`：healthcheck、metrics、connection pool、async I/O、streaming/backpressure。
- `rules/ai-backend-design-rules.md`：RAG pipeline、OpenAI-compatible API、SSE、file ingestion、pgvector。
- `rules/github-backend-project-selection-rules.md`：如何区分 core/good/sample/low reference。
- `rules/backend-project-template-rules.md`：个人默认模板的最小质量基线和避免过重架构。

## 8. 候选 wiki/patterns 写入清单

- `wiki/patterns/controller-service-repository-pattern.md`：Express 四层和 FastAPI feature 分层。
- `wiki/patterns/jwt-refresh-token-pattern.md`：refresh token hash、rotation、HttpOnly cookie、jti。
- `wiki/patterns/rbac-permission-pattern.md`：NestJS decorator+guard+strategy、Express authorize middleware。
- `wiki/patterns/file-upload-processing-pattern.md`：上传隔离、路径净化、文档解析和测试。
- `wiki/patterns/background-task-queue-pattern.md`：本批次只有 BullMQ/Celery 线索不足，暂不建议直接写核心内容。
- `wiki/patterns/sse-streaming-response-pattern.md`：OpenAI streaming、SSE chunk、客户端兼容测试。
- `wiki/patterns/rag-backend-pipeline-pattern.md`：ingestion、chunk、embedding、vector store、metadata filter、retrieval。
- `wiki/patterns/docker-compose-backend-pattern.md`：web/app + postgres + redis/search 的 compose 组合和 healthcheck。

## 9. 候选 wiki/templates 写入清单

- `wiki/templates/fastapi-project-template.md`：以 minimal-fastapi-postgres-template 为主，补充 fastapi-sqlalchemy2 的轻量 feature 结构。
- `wiki/templates/nestjs-project-template.md`：以 prime-nestjs 为主，awesome-nest 作为重型扩展参考。
- `wiki/templates/django-project-template.md`：本批次未扫描 Django 项目，暂不建议生成。
- `wiki/templates/express-project-template.md`：以 express-ts-pg-prisma-boilerplate 为核心，express-typescript-skeleton 作为中型/DDD 上限。
- `wiki/templates/rag-backend-template.md`：结合 rag_api、fastapi-langchain-rag、fastapi-openai-compat。
- `wiki/templates/docker-compose-backend-template.md`：抽取 Postgres/Redis/Search/healthcheck，但保持个人项目最小化。

## 10. 不适合个人项目默认使用的设计

- 微服务：本批次没有足够必要性证据，个人项目默认单体模块化更合适。
- Kubernetes：未见必须采用，个人项目默认不推荐。
- 服务网格：无需求证据，不推荐。
- 复杂 DDD：`express-typescript-skeleton` 可作为中型上限，不应默认生成。
- CQRS：`awesome-nest-boilerplate` 有 CQRS 依赖线索，但默认过重。
- Event Sourcing：未发现足够项目证据，不推荐。
- 过重 Clean Architecture：对个人 CRUD/RAG 起步不划算。
- 复杂云部署：Cloud Run/Terraform 只在明确部署需求时加入。
- 多租户 SaaS 高级隔离：本批次未形成足够源码证据，不作为默认规则。

## 11. 文件生成检查

- `analysis.md`：已生成 13 个，对应 13 个项目。
- `metadata.json`：已生成 13 个，对应 13 个项目。
- `chunks.json`：已生成 13 个，对应 13 个项目，每个文件 3 条 chunk。
- JSON 是否可解析：全部 metadata/chunks JSON 通过 `json.loads` 校验。
- trust_level 校验：全部为 `core_reference`、`good_reference`、`sample_only`、`low_reference` 之一。
- chunk 长度校验：全部 chunk content 在 300 到 800 字符范围内。
- 是否存在空文件：未发现空文件。
- 是否误扫 `node_modules` / `.git` / `venv`：未发现生成产物中包含这些路径；静态扫描过程已忽略这些目录。
- 是否发生路径异常：未发现路径异常。
- schema 缺失：`E:\DataBase\common\schemas` 当前未发现 backend 专用 schema，例如 `backend_reference.schema.json`，建议下一阶段由用户确认后再生成。

## 12. 下一步建议

下一步不要直接运行项目。建议顺序：

1. 由你确认项目分析结果。
2. 再生成 `backend_reference.schema.json`。
3. 再生成 backend README。
4. 再生成 rules。
5. 再生成 wiki topics / patterns / checklists / templates。
6. 再生成 references JSON。
7. 最后才考虑构建 backend SQLite 检索索引和 API 检索接口。
