# fastapi-template

## 1. 项目定位

- FastAPI 模板
- Redis + PostgreSQL
- Docker Compose 部署
- Alembic migration
- 基础 auth
- 简单 routes/services/schema

## 2. 技术栈

- 后端框架：FastAPI
- 数据库：PostgreSQL
- ORM：SQLAlchemy/Databases 线索
- migration 工具：Alembic
- 认证方式：python-jose、passlib
- 权限方式：未发现 RBAC
- 缓存：Redis/aioredis
- 队列：未发现
- 文件存储：未发现
- 部署方式：Dockerfile、docker-compose
- 测试工具：pytest、auth tests
- 文档工具：README
- CI/CD：未发现

## 3. 目录结构观察

- app 下是 base/db/models/routes/schema/services/settings 的扁平结构。
- auth 模块单独包含 api、exceptions、models、schema、services、tests。
- alembic 在根目录。
- 结构简单易懂，但随着业务增长可能变成扁平拥挤。

## 4. API 设计观察

- 有 app/routes.py 和 auth/api.py。
- API versioning 未发现。
- 统一响应格式未明确发现。
- auth/exceptions.py 提供业务异常线索。
- 分页/健康检查未发现。

## 5. 数据库设计观察

- PostgreSQL、Databases、asyncpg、SQLAlchemy utils、Alembic。
- Redis 由 docker-compose 提供。
- 索引、连接池、事务细节未明确发现。
- 适合小型模板参考，现代 SQLAlchemy 2/Pydantic 2 价值不如 minimal 模板。

## 6. 鉴权和权限观察

- 使用 python-jose/passlib/python-multipart。
- 有 auth tests。
- 未发现 refresh token、OAuth2/OIDC、RBAC。

## 7. 错误处理和日志观察

- auth/exceptions.py 有局部异常。
- 未发现统一错误码、日志系统、request_id。

## 8. 部署和环境变量观察

- Dockerfile 使用 Python 3.9 slim、pipenv。
- docker-compose 启动 web、postgres、redis。
- 未发现 CI/GitHub Actions。

## 9. 测试和质量观察

- auth/tests/test_auth_api.py 提供少量测试。
- 测试覆盖不完整。
- 依赖和模板风格偏旧。

## 10. 可提炼规则

- 规则 1：个人 FastAPI 模板可以从简单结构开始，但应在业务增多时迁移到 feature-based。
  - 来源观察：fastapi-template 结构简单，fastapi-sqlalchemy2 与 minimal 模板展示更清晰 feature/core 分层。
  - 适合场景：demo、小型 API。
  - Agent 生成代码时应该怎么做：少量模块时可用 routes/services/schema；新增多个业务域时改成每个 feature 独立目录。

## 11. 不建议照搬的地方

- Pipfile/Python 3.9 模板偏旧。
- Dockerfile 使用 pipenv 安装对现代 uv/poetry/pip-tools 项目未必合适。
- 测试和错误处理不足。

## 12. 适合进入哪些知识库文件

- wiki/templates/fastapi-project-template.md：可作为简单模板对照样本。
- wiki/patterns/docker-compose-backend-pattern.md：web/postgres/redis compose 结构可作为 sample。
- rules/backend-project-template-rules.md：用于提醒个人项目避免过早复杂化。

## 13. 项目质量评分

- README 清晰度：4/5
- 目录结构清晰度：3/5
- 测试完整度：2/5
- Docker / 部署完整度：4/5
- 数据库迁移完整度：3/5
- 权限系统完整度：3/5
- 日志异常完整度：2/5
- 对个人项目的参考价值：3/5
- 对中型项目的参考价值：3/5
- 是否适合进入核心规则库：2/5

trust_level：`sample_only`
