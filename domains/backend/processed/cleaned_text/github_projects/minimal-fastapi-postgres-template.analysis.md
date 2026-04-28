# minimal-fastapi-postgres-template

## 1. 项目定位

- FastAPI 现代项目模板
- PostgreSQL + SQLAlchemy async
- Alembic migration
- JWT auth
- 健康检查/metrics
- pytest 100% coverage 目标
- Docker/CI/typecheck

## 2. 技术栈

- 后端框架：FastAPI
- 数据库：PostgreSQL
- ORM：SQLAlchemy async
- migration 工具：Alembic
- 认证方式：JWT/PyJWT、bcrypt
- 权限方式：基础 auth，RBAC 未完整发现
- 缓存：未发现
- 队列：未发现
- 文件存储：未发现
- 部署方式：Dockerfile、docker-compose、Makefile
- 测试工具：pytest、pytest-asyncio、pytest-cov、pytest-xdist、httpx、freezegun、polyfactory
- 文档工具：README、FastAPI docs
- CI/CD：GitHub Actions tests、type_check、dev_build、Dependabot

## 3. 目录结构观察

- app 下有 auth、core、probe、tests，业务域和基础设施边界清楚。
- core 包含 config、database_session、lifespan、metrics、models。
- auth 包含 dependencies、jwt、models、password、responses、schemas、views 和 tests。
- probe 提供健康检查视图。
- alembic/versions 有 initial auth migration。

## 4. API 设计观察

- FastAPI REST API 结构清楚。
- probe/views.py 提供健康检查/探针线索。
- auth/views.py、responses.py 体现响应组织。
- 参数校验由 schemas/Pydantic 完成。
- API versioning 未明确发现，分页不是重点。

## 5. 数据库设计观察

- PostgreSQL + asyncpg + SQLAlchemy[asyncio]。
- Alembic migration 完整存在。
- database_session 集中管理连接/session。
- 没有 Redis/队列等多余依赖，适合个人项目默认基线。
- 种子数据未明确发现。

## 6. 鉴权和权限观察

- JWT、bcrypt、auth dependencies、password 模块齐全。
- 有 auth tests 和 factories。
- 未发现完整 refresh token/RBAC，但基础 auth 质量较高。

## 7. 错误处理和日志观察

- core/lifespan、metrics、probe 有生产可观测性线索。
- 统一业务异常/错误码未完整确认。
- Prometheus 指标是亮点。

## 8. 部署和环境变量观察

- Dockerfile 使用 uv export/requirements 分阶段思路。
- docker-compose 提供 postgres 服务。
- Makefile、pre-commit、Ruff、mypy、GitHub Actions 形成完整质量链。
- .env.example 含示例 JWT_SECRET 和 DB 密码，应标注为示例不要照搬。

## 9. 测试和质量观察

- pyproject 设置 pytest、coverage、100% coverage gate、xdist。
- CI 覆盖 tests/type_check。
- 这是 FastAPI 个人/中型项目模板中最强样本之一。

## 10. 可提炼规则

- 规则 1：FastAPI + PostgreSQL 默认模板应包含 core/config、core/database_session、alembic、auth/tests、probe。
  - 来源观察：minimal-fastapi-postgres-template 结构完整，fastapi-sqlalchemy2 也支持 core + feature 分层。
  - 适合场景：个人项目默认后端模板、中小型 REST API。
  - Agent 生成代码时应该怎么做：生成最小可测骨架：settings、DB session、migration、health probe、auth schema/view/test。
- 规则 2：后端模板必须把 lint/type/test/coverage/CI 写成可重复命令。
  - 来源观察：minimal 模板有 Ruff、mypy、pytest、coverage、GitHub Actions；Express/NestJS 优质模板也类似。
  - 适合场景：所有可维护后端项目。
  - Agent 生成代码时应该怎么做：在 pyproject/package scripts/Makefile 中提供 lint、type-check、test，并在 CI 调用。

## 11. 不建议照搬的地方

- Python 3.14 要求较新，复制时需按项目环境调整。
- 示例 .env 中的 secret/password 只能作为本地占位，生成规则时应改成 <change-me>。
- 未覆盖 refresh token/RBAC，不应作为完整权限系统来源。

## 12. 适合进入哪些知识库文件

- rules/backend-project-template-rules.md：现代 FastAPI 模板基线强。
- rules/database-modeling-rules.md：async SQLAlchemy + Alembic + PostgreSQL 可作为核心候选。
- rules/deployment-and-env-rules.md：Docker、Compose、Makefile、env 示例有部署规则价值。
- wiki/templates/fastapi-project-template.md：适合作为核心 FastAPI 模板参考。
- rules/performance-and-stability-rules.md：probe、metrics、lifespan 可沉淀稳定性规则。

## 13. 项目质量评分

- README 清晰度：5/5
- 目录结构清晰度：5/5
- 测试完整度：5/5
- Docker / 部署完整度：5/5
- 数据库迁移完整度：5/5
- 权限系统完整度：4/5
- 日志异常完整度：4/5
- 对个人项目的参考价值：5/5
- 对中型项目的参考价值：5/5
- 是否适合进入核心规则库：5/5

trust_level：`core_reference`
