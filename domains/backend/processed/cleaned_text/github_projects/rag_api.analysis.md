# rag_api

## 1. 项目定位

- RAG / AI backend
- 文件级 ID 检索
- PostgreSQL/pgvector
- LangChain vector store
- 文件上传与文档解析
- FastAPI async API
- Docker/GitHub Actions

## 2. 技术栈

- 后端框架：FastAPI、LangChain
- 数据库：PostgreSQL/pgvector、MongoDB 线索
- ORM：SQLAlchemy
- migration 工具：未发现 Alembic/Prisma migration
- 认证方式：PyJWT 依赖，具体认证边界需专项确认
- 权限方式：未发现完整 RBAC
- 缓存：未发现 Redis
- 队列：未发现
- 文件存储：uploads volume、S3/boto3 依赖线索、本地文档处理
- 部署方式：Dockerfile、api-compose.yaml、devcontainer
- 测试工具：pytest、unittest、integration tests
- 文档工具：README
- CI/CD：GitHub Actions CI/docker/release workflows

## 3. 目录结构观察

- app 下有 routes、services、utils、config、middleware、models。
- services/vector_store 单独处理向量存储，routes/document_routes 和 pgvector_routes 区分 API 面。
- tests 下包含 unit、services、utils、integration，覆盖上传隔离、配置、middleware、vector store。
- utils/document_loader 聚焦文档解析，说明 ingestion 能力没有直接混进路由。

## 4. API 设计观察

- 提供文档管理、添加/查询/删除和 pgvector 相关 REST API。
- OpenAPI/Swagger 可由 FastAPI 默认提供。
- API versioning 未明确发现。
- 有健康检查 utils 线索。
- 分页/统一响应/统一错误格式未完整确认。
- 文件上传和路径校验有测试线索。

## 5. 数据库设计观察

- 核心是 PostgreSQL/pgvector 与 LangChain vector store。
- 使用 SQLAlchemy/asyncpg/psycopg2。
- 未发现 migration 目录，数据库初始化和 schema 演进规则不足。
- 有 MongoDB/LangChain MongoDB 线索，说明项目支持多存储但复杂度增加。
- 适合 PostgreSQL/pgvector 与 RAG metadata filter，不适合作为 SQLite 默认方案。

## 6. 鉴权和权限观察

- 有 PyJWT 依赖，但未从摘要确认完整登录/用户/RBAC。
- 面向集成场景时应在网关或 API 层补充 API key/JWT 权限。
- 文件级 ID 检索要特别防止跨 file_id 越权。

## 7. 错误处理和日志观察

- app/middleware.py 和 tests/test_middleware.py 说明有中间件层。
- 统一异常处理、错误码、trace_id 未完整确认。
- 文档上传/路径校验测试是安全与稳定性亮点。

## 8. 部署和环境变量观察

- Dockerfile 安装 pandoc、libmagic、OCR/文档处理依赖。
- api-compose.yaml 提供 API service 和 uploads volume。
- GitHub Actions 覆盖 CI、Docker build、images、release。
- 依赖重，个人项目默认不应一次性照搬全部文档解析栈。

## 9. 测试和质量观察

- 测试覆盖比多数样本强，包含 services、utils、integration。
- 对 RAG API、文件上传隔离、向量服务工厂有较高参考价值。
- 缺少迁移目录导致数据库治理分偏低。

## 10. 可提炼规则

- 规则 1：RAG API 应围绕 file_id / metadata 做隔离和检索过滤。
  - 来源观察：rag_api README 强调 ID-based retrieval，并有上传隔离、pgvector filter 测试。
  - 适合场景：LibreChat 集成、用户文件问答、多文档检索。
  - Agent 生成代码时应该怎么做：设计 document_id/file_id 字段、metadata filter 和权限校验，不生成全库无隔离检索。
- 规则 2：文档上传处理必须有路径校验、格式解析隔离和服务层测试。
  - 来源观察：rag_api 有 document_loader、upload isolation、path validation 测试。
  - 适合场景：文件 ingestion、企业知识库、RAG 上传。
  - Agent 生成代码时应该怎么做：把上传目录、文件名净化、文档解析、向量入库拆成可测函数，并补单元/集成测试。

## 11. 不建议照搬的地方

- 不要默认引入所有文档格式和 OCR 依赖。
- 无明确 migration 时不应作为数据库演进规则来源。
- 多向量/多模型支持会增加个人项目维护成本。

## 12. 适合进入哪些知识库文件

- rules/ai-backend-design-rules.md：ID-based RAG、vector store、file ingestion 有核心候选价值。
- wiki/patterns/rag-backend-pipeline-pattern.md：适合沉淀上传、解析、embedding、pgvector 检索模式。
- wiki/patterns/file-upload-processing-pattern.md：上传隔离和路径校验测试是可复用观察。
- rules/backend-security-checklist.md：文件路径、上传隔离、metadata 越权风险可进入 checklist。

## 13. 项目质量评分

- README 清晰度：4/5
- 目录结构清晰度：4/5
- 测试完整度：4/5
- Docker / 部署完整度：4/5
- 数据库迁移完整度：1/5
- 权限系统完整度：2/5
- 日志异常完整度：3/5
- 对个人项目的参考价值：4/5
- 对中型项目的参考价值：4/5
- 是否适合进入核心规则库：4/5

trust_level：`core_reference`
