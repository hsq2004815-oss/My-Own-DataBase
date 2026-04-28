# Backend Project Template Rules

## 文件用途

为 Agent 选择和生成后端项目模板提供默认技术栈、目录、质量门槛和避免过重规则。

## 适用场景

- 从零生成后端项目。
- 选择 FastAPI/Express/NestJS 模板。
- 生成个人项目、小程序后端、管理系统后端或 RAG 后端基础结构。

## 优先读取条件

- 项目模板、FastAPI template、Express template、NestJS template、个人项目、管理系统、小程序后端、RAG template。

## 适合的项目类型

- 个人项目
- 小程序后端
- 管理系统后端
- FastAPI API
- Express TypeScript API
- NestJS API
- RAG 后端

## 不适合的项目类型

- 大型平台微服务治理
- K8s 服务网格
- 纯前端页面
- 无需持久化的一次性脚本

## 推荐做法

- 个人项目默认模块化单体。
- FastAPI 默认 core + feature + tests + Alembic。
- Express 默认 feature-based routes/controllers/services/repositories/schemas/tests + Prisma migration。
- NestJS 默认 module/controller/service/dto/entity/spec + Swagger。
- 默认提供 lint、typecheck、test、Docker Compose、healthcheck 和 .env.example 占位符。
- Redis、队列、对象存储、搜索服务按需求加入。

## 禁止做法

- 不要默认微服务、K8s、服务网格、复杂 DDD、CQRS、Event Sourcing。
- 不要生成只有 README 没有测试命令的模板。
- 不要生成 hardcoded-looking secret。
- 不要把重型 boilerplate 的所有依赖复制给个人项目。

## Agent 生成代码时必须遵守的规则

1. 模板必须有 README 运行说明但不执行安装。
2. 模板必须包含最小测试样例或测试命令。
3. 模板必须包含统一错误处理和日志入口。
4. 模板必须包含 migration 策略。
5. 模板必须包含健康检查。
6. 模板必须明确哪些依赖是可选。

## 常见失败案例

- 个人 CRUD 模板引入 S3、Meilisearch、BullMQ、CQRS。
- 没有 migration 但有 ORM model。
- Dockerfile 用 dev server 作为生产入口。
- .env.example 使用看似真实密码。

## 检查清单

- [ ] 模块化单体默认
- [ ] 技术栈与任务匹配
- [ ] 测试/质量命令存在
- [ ] migration 存在
- [ ] env 安全
- [ ] 可选依赖未默认启用

## 推荐参考来源

- FastAPI official docs
- PostgreSQL official docs
- Redis official docs
- Docker / Docker Compose official docs
- OpenAPI Specification
- OWASP API Security Top 10
- OAuth2 / OpenID Connect official resources
- Stripe API idempotency docs
- GitHub REST API docs
- Microsoft REST API Guidelines
- Martin Fowler Monolith First
- 本地 backend GitHub 项目分析报告

## 关联文件

- rules/backend-engineering-map.md
- rules/backend-layered-architecture-rules.md
- rules/database-modeling-rules.md
- rules/deployment-and-env-rules.md
- wiki/templates/fastapi-project-template.md
- wiki/templates/express-project-template.md
- wiki/templates/nestjs-project-template.md
