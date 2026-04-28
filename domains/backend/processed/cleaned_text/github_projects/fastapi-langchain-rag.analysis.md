# fastapi-langchain-rag

## 1. 项目定位

- RAG / AI backend 项目结构
- PostgreSQL + pgvector 向量检索
- FastAPI routes/services/models/schemas 分层
- 文档 ingestion 与文件处理
- Redis 辅助能力
- Cloud Run / Terraform 部署思路

## 2. 技术栈

- 后端框架：FastAPI、LangChain
- 数据库：PostgreSQL/pgvector
- ORM：SQLModel、SQLAlchemy
- migration 工具：Alembic 文档/迁移说明
- 认证方式：NextAuth JWT 集成线索、python-jose
- 权限方式：订阅/用户限制线索，RBAC 未完整确认
- 缓存：Redis
- 队列：未发现
- 文件存储：本地/文档解析管线，云存储未完整确认
- 部署方式：Dockerfile、GCP Cloud Run/Terraform 文档、Vercel 前端说明
- 测试工具：未发现完整 tests 目录
- 文档工具：README、docs 分章节教程
- CI/CD：GitHub Actions 线索

## 3. 目录结构观察

- 后端代码集中在 backend/app，下分 api、config、core、crud、ingestion、models、schemas、utils。
- docs 按 getting-started、project-structure、database、data-migration、IaC 分章，适合学习项目说明文档组织。
- ingestion 单独成模块，说明 RAG 项目应把文档解析/切分/入库和普通 API 路由隔离。
- 结构对个人项目可复用，但 Terraform、订阅、Redis、pgvector、非结构化文档解析依赖较重。

## 4. API 设计观察

- 存在 FastAPI API 路由组织线索。
- OpenAPI/Swagger 可由 FastAPI 默认提供，未发现独立文档增强。
- API versioning 未明确发现。
- 统一响应格式、统一错误格式未从静态摘要中确认。
- 分页线索存在，但未确认完整规范。
- 健康检查接口未明确发现。

## 5. 数据库设计观察

- 使用 PostgreSQL + pgvector 作为 RAG 向量存储核心。
- 使用 SQLModel/SQLAlchemy，适合学习模型与向量库结合。
- Alembic 主要通过 docs 中 migration 章节体现，源码内完整迁移目录未确认。
- 有 asyncpg/psycopg2 依赖，连接池细节需进一步专项阅读。
- 适合 PostgreSQL/pgvector，不适合作为 SQLite 默认方案。

## 6. 鉴权和权限观察

- 存在 python-jose、fastapi-nextauth-jwt、passlib 等依赖。
- 用户/订阅限制是项目目标之一，但 RBAC/管理员权限实现未完整确认。
- 对个人项目可参考 JWT 接入位置，但不要直接照搬订阅和第三方 auth 复杂度。
- 越权风险无法仅靠摘要确认，需要后续审计依赖注入和路由保护。

## 7. 错误处理和日志观察

- 使用 loguru 作为日志系统。
- 统一异常类、错误码、request_id/trace_id 未明确发现。
- 生产环境错误隐藏策略未确认。

## 8. 部署和环境变量观察

- 有 backend/Dockerfile。
- README 描述 Cloud Run、CloudSQL、Redis 和 Terraform。
- 未发现本项目根部 docker-compose 作为默认本地部署入口。
- 环境变量依赖较多，适合在报告中提醒不要复制真实密钥。

## 9. 测试和质量观察

- 未发现成体系 tests 目录。
- README/docs 清晰，但缺少测试证据降低模板可信度。
- 对 AI/RAG 架构参考价值高，对通用质量基线参考价值中等。

## 10. 可提炼规则

- 规则 1：RAG 后端应把 ingestion、vector store、API routes、schemas/models 分开。
  - 来源观察：fastapi-langchain-rag 和 rag_api 都把文档解析/向量存储从普通路由中拆出。
  - 适合场景：文件上传、文档问答、向量检索项目。
  - Agent 生成代码时应该怎么做：新建 ingestion/vector_store/service 层，不把 PDF 解析、embedding、数据库写入直接塞进 controller。
- 规则 2：pgvector 项目默认以 PostgreSQL 为核心，不把 SQLite 当向量检索默认方案。
  - 来源观察：fastapi-langchain-rag 与 rag_api 都围绕 Postgres/pgvector。
  - 适合场景：需要 metadata filter、并发检索、文件级 ID 检索的 RAG API。
  - Agent 生成代码时应该怎么做：生成配置、模型、迁移和连接时优先显式 PostgreSQL/pgvector，并在个人轻量版中降低依赖。

## 11. 不建议照搬的地方

- Terraform/Cloud Run/订阅系统对个人项目默认偏重。
- OCR/unstructured/pdf 依赖很重，不应无需求默认加入。
- 缺少完整测试目录时不要把实现细节提升为核心规则。

## 12. 适合进入哪些知识库文件

- rules/ai-backend-design-rules.md：RAG ingestion、pgvector、LangChain 服务分层可沉淀为候选规则。
- wiki/patterns/rag-backend-pipeline-pattern.md：适合描述文档解析、chunk、embedding、vector store、问答链路。
- wiki/templates/rag-backend-template.md：可作为偏完整的 FastAPI RAG 模板样本，但需去除云部署和订阅复杂度。
- rules/deployment-and-env-rules.md：Cloud Run/Terraform/Docker/env 线索可用于部署规则候选。

## 13. 项目质量评分

- README 清晰度：4/5
- 目录结构清晰度：4/5
- 测试完整度：1/5
- Docker / 部署完整度：3/5
- 数据库迁移完整度：3/5
- 权限系统完整度：3/5
- 日志异常完整度：3/5
- 对个人项目的参考价值：3/5
- 对中型项目的参考价值：4/5
- 是否适合进入核心规则库：4/5

trust_level：`good_reference`
