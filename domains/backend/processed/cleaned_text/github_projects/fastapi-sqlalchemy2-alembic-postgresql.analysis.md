# fastapi-sqlalchemy2-alembic-postgresql

## 1. 项目定位

- FastAPI 项目结构
- SQLAlchemy 2 ORM
- Alembic 数据库迁移
- PostgreSQL
- JWT auth starter
- Feature-based 分层

## 2. 技术栈

- 后端框架：FastAPI
- 数据库：PostgreSQL
- ORM：SQLAlchemy 2
- migration 工具：Alembic
- 认证方式：JWT/PyJWT、bcrypt
- 权限方式：用户/认证基础，RBAC 未发现
- 缓存：未发现
- 队列：未发现
- 文件存储：未发现
- 部署方式：docker-compose PostgreSQL 服务
- 测试工具：未发现 tests
- 文档工具：README
- CI/CD：未发现

## 3. 目录结构观察

- 按 auth、user、core、alembic 拆分，auth/user 内再分 models/routes/services/schemas。
- core 包含 config、config_loader、database。
- alembic/versions 有 create_users_table migration。
- 适合学习小型 feature-based FastAPI 结构。

## 4. API 设计观察

- 存在 auth_router、user_router。
- 未发现 API versioning。
- 统一响应/统一错误格式未明确发现。
- 参数校验通过 Pydantic schemas。
- 健康检查、分页未发现。

## 5. 数据库设计观察

- PostgreSQL + SQLAlchemy 2 + Alembic 是核心价值。
- 有 users table migration。
- 连接配置集中在 core/database 与 config。
- 种子数据、索引设计、事务边界未明确发现。
- 适合个人项目学习，但缺测试会降低可信度。

## 6. 鉴权和权限观察

- auth/models/token、auth_service、auth_utils 和 PyJWT/bcrypt 体现 JWT 登录基础。
- 未发现 refresh token 或 RBAC。
- 管理员权限和越权风险需要后续审计。

## 7. 错误处理和日志观察

- 未发现统一异常处理、错误码、日志系统、request_id。
- 错误处理价值较低。

## 8. 部署和环境变量观察

- docker-compose 只提供 PostgreSQL 服务。
- 未发现 Dockerfile 和 CI。
- README 有 .env 配置说明。

## 9. 测试和质量观察

- 未发现 tests。
- 适合作为结构/数据库 starter 样本，不适合作为质量核心模板。

## 10. 可提炼规则

- 规则 1：小型 FastAPI CRUD 可以按 feature 分组，每个 feature 包含 routes/services/models/schemas。
  - 来源观察：该项目和 minimal-fastapi-postgres-template 都把 auth/user 等业务域拆开。
  - 适合场景：个人项目、中小 CRUD API。
  - Agent 生成代码时应该怎么做：新增模块时同时生成 router/service/schema/model，不把所有路由塞进 main.py。
- 规则 2：SQLAlchemy 2 + Alembic + PostgreSQL 模板必须把配置和 DB session 放在 core 层。
  - 来源观察：该项目有 core/config、core/database；minimal 模板也有 app/core/database_session。
  - 适合场景：FastAPI 使用关系数据库。
  - Agent 生成代码时应该怎么做：生成 settings、engine/session、migration 配置，不在业务服务里硬编码连接串。

## 11. 不建议照搬的地方

- 无 tests/CI，不应作为唯一核心规则来源。
- docker-compose 只有数据库，完整部署参考不足。
- 缺少统一错误和权限策略。

## 12. 适合进入哪些知识库文件

- rules/database-modeling-rules.md：SQLAlchemy 2、Alembic、PostgreSQL starter 可作候选。
- rules/backend-layered-architecture-rules.md：feature-based routes/services/models/schemas 有结构价值。
- rules/auth-and-permission-rules.md：JWT 基础可作为 sample，不足以做 refresh/RBAC 核心。
- wiki/templates/fastapi-project-template.md：可作为轻量 FastAPI DB 模板样本。

## 13. 项目质量评分

- README 清晰度：4/5
- 目录结构清晰度：4/5
- 测试完整度：0/5
- Docker / 部署完整度：2/5
- 数据库迁移完整度：4/5
- 权限系统完整度：3/5
- 日志异常完整度：2/5
- 对个人项目的参考价值：4/5
- 对中型项目的参考价值：3/5
- 是否适合进入核心规则库：3/5

trust_level：`good_reference`
