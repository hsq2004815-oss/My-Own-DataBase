# Backend Layered Architecture Rules

## 文件用途

为 Agent 生成可维护的后端目录结构和分层边界，避免 controller 肥大和过度架构。

## 适用场景

- 生成新后端项目。
- 新增业务模块。
- 重构 routes/controller/service/repository/model/schema。
- 选择 FastAPI、Express 或 NestJS 项目结构。

## 优先读取条件

- 项目结构、分层、controller、service、repository、model、schema、DTO、module、feature、DDD。

## 适合的项目类型

- 个人项目
- 管理系统后端
- FastAPI API
- Express TypeScript API
- NestJS API
- RAG 后端

## 不适合的项目类型

- 纯前端
- 一次性脚本
- 需要服务网格/微服务治理的大型平台

## 推荐做法

- 默认模块化单体。
- FastAPI 优先 core + feature 分层。
- Express TypeScript 优先 feature 下 routes/controllers/services/repositories/schemas/tests。
- NestJS 优先 module/controller/service/dto/entity/guard/spec。
- 复杂 domain/application/infrastructure/presentation 只在中型以上项目或用户明确要求时使用。

## 禁止做法

- 不要默认微服务。
- 不要把所有路由放到一个巨大文件。
- 不要让 controller 直接访问数据库。
- 不要为个人项目默认生成复杂 DDD/CQRS。

## Agent 生成代码时必须遵守的规则

1. 每个业务模块必须有清晰入口和边界。
2. controller 只处理 HTTP 和调用 service。
3. service 处理业务规则。
4. repository/ORM 层处理持久化。
5. schema/DTO 处理输入输出校验。
6. 跨模块共享逻辑放 core/common/shared，不复制粘贴。

## 常见失败案例

- controller 包含 SQL 查询、密码校验和文件解析。
- utils 目录变成业务逻辑垃圾桶。
- DDD 分层很多但每层只有转发。
- 新增业务只加路由不加测试。

## 检查清单

- [ ] 目录按 feature 或 module 清晰组织
- [ ] controller/service/repository/schema 边界明确
- [ ] 没有默认微服务
- [ ] 没有过度 DDD
- [ ] 共享逻辑位置明确

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
- rules/api-design-rules.md
- rules/database-modeling-rules.md
- wiki/patterns/controller-service-repository-pattern.md
