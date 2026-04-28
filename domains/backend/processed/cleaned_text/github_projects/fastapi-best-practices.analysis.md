# fastapi-best-practices

## 1. 项目定位

- FastAPI 最佳实践文档
- 项目结构规则候选
- Pydantic/Settings 使用规范
- SQLAlchemy 2 / Alembic 规则候选
- JWT 与依赖注入建议
- AI Agent 代码生成约束

## 2. 技术栈

- 后端框架：FastAPI 文档规则
- 数据库：文档覆盖 SQLAlchemy/PostgreSQL 等实践
- ORM：SQLAlchemy 2 文档实践
- migration 工具：Alembic 文档实践
- 认证方式：JWT 文档实践
- 权限方式：依赖/权限建议，具体实现未运行
- 缓存：未发现
- 队列：未发现
- 文件存储：未发现
- 部署方式：未发现
- 测试工具：文档提及测试实践，项目本身非测试套件
- 文档工具：README、README_ZH、AGENTS.md
- CI/CD：未发现

## 3. 目录结构观察

- 该项目基本是文档仓库，不是可运行应用。
- README 目录覆盖 Project Structure、Async Routes、Pydantic、Dependencies 等主题。
- 有 AGENTS.md 机器可读规则，对 AI Agent 生成 FastAPI 代码很有价值。
- 结构评分按文档清晰度高，但代码结构不适用。

## 4. API 设计观察

- 非应用项目，未提供实际 API。
- 文档可作为 REST API 组织、依赖注入、响应模型候选来源。
- OpenAPI/版本/统一响应等只能作为规则讨论，不是源码证据。

## 5. 数据库设计观察

- 文档覆盖 SQLAlchemy 2 和 Alembic，但不是本地可运行数据库实现。
- 可作为规则候选来源，必须与 minimal-fastapi-postgres-template 等代码项目共同验证。

## 6. 鉴权和权限观察

- 文档提到 JWT 等实践。
- 非完整权限系统源码，不应单独作为 RBAC 规则来源。

## 7. 错误处理和日志观察

- 文档覆盖错误处理/反模式线索。
- 无可验证运行日志或中间件实现。

## 8. 部署和环境变量观察

- 未发现 Docker/Compose/CI 作为本项目核心。
- 更适合 rules，不适合 deployment template。

## 9. 测试和质量观察

- 文档质量高但无项目测试。
- 对核心规则库价值高，对模板代码价值低。

## 10. 可提炼规则

- 规则 1：FastAPI 规则必须区分 I/O async、CPU-bound sync/offload，避免盲目 async。
  - 来源观察：fastapi-best-practices 明确讨论 async routes 与 I/O/CPU 区分。
  - 适合场景：Agent 生成 FastAPI endpoint、服务调用、后台任务。
  - Agent 生成代码时应该怎么做：网络/DB I/O 使用 async 驱动；CPU 重任务放线程/进程或任务队列，不阻塞事件循环。
- 规则 2：Pydantic schema、Settings、依赖注入应与 ORM model 解耦。
  - 来源观察：fastapi-best-practices 与多个 FastAPI 模板都区分 schemas/models/config。
  - 适合场景：FastAPI CRUD、认证、配置。
  - Agent 生成代码时应该怎么做：生成 schemas、models、settings、dependencies 文件，不在路由里直接读 env 或返回 ORM 裸对象。

## 11. 不建议照搬的地方

- 不要把文档仓库当可运行模板。
- 单条建议进入核心 rules 前应与代码项目或官方文档交叉验证。
- 没有 Docker/test/db 实现证据。

## 12. 适合进入哪些知识库文件

- rules/backend-layered-architecture-rules.md：项目结构、依赖和分层建议是核心候选。
- rules/api-design-rules.md：FastAPI endpoint、response model、validation 建议可沉淀。
- rules/database-modeling-rules.md：SQLAlchemy/Alembic 文档实践需与模板项目共同支持。
- rules/backend-project-template-rules.md：可作为 Agent 生成 FastAPI 项目的约束来源。

## 13. 项目质量评分

- README 清晰度：5/5
- 目录结构清晰度：4/5
- 测试完整度：0/5
- Docker / 部署完整度：0/5
- 数据库迁移完整度：3/5
- 权限系统完整度：2/5
- 日志异常完整度：3/5
- 对个人项目的参考价值：4/5
- 对中型项目的参考价值：4/5
- 是否适合进入核心规则库：5/5

trust_level：`core_reference`
