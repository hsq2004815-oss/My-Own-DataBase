# awesome-nest-boilerplate

## 1. 项目定位

- NestJS 分层架构
- TypeORM + migrations
- JWT + roles guard
- Swagger/OpenAPI
- 文件/S3 服务
- i18n
- Docker Compose
- 大型 boilerplate

## 2. 技术栈

- 后端框架：NestJS、Express platform
- 数据库：PostgreSQL、Meilisearch、多 ORM 依赖线索
- ORM：TypeORM
- migration 工具：TypeORM migrations
- 认证方式：JWT、Passport strategies
- 权限方式：Roles guard/RBAC
- 缓存：Meilisearch 非缓存但作为搜索服务；Redis 未明确
- 队列：BullMQ 依赖线索
- 文件存储：AWS S3 service
- 部署方式：Dockerfile、docker-compose
- 测试工具：Jest、Supertest/e2e、controller spec
- 文档工具：Swagger setup、docs、VitePress docs
- CI/CD：GitHub Actions docs/lint

## 3. 目录结构观察

- 源码在 awesome-nest-boilerplate-main/src。
- common/dto、constants、database/migrations、decorators、filters、guards、interceptors、modules、providers、shared/services 分层很细。
- modules/auth、modules/user、modules/post 按 NestJS module 组织。
- 有 .cursor/rules 和 docs/testing.md，适合提取 Agent 生成 NestJS 的约束。

## 4. API 设计观察

- NestJS controller/service/module 结构完整。
- setup-swagger.ts 和 decorators/swagger.schema.ts 提供 OpenAPI/Swagger。
- API_VERSION 在 env 中，版本化线索存在。
- 分页 DTO page/page-meta/page-options 完整。
- health-checker module 存在。
- 统一异常 filters 存在 bad-request/query-failed 等。

## 5. 数据库设计观察

- TypeORM + PostgreSQL 是主要路径。
- src/database/migrations 有 users、settings、posts 等迁移。
- 实体 ownership、DTO、validators 有规则文件。
- Meilisearch、S3、BullMQ 等扩展增加复杂度。

## 6. 鉴权和权限观察

- auth module 包含 controller/service/jwt.strategy/public.strategy。
- guards/auth.guard、guards/roles.guard、roles.decorator、role-type constant 说明 RBAC 边界清晰。
- JWT_PRIVATE_KEY 在 .env.example 中放入完整 RSA private key 文本，是明显安全风险，不能照搬。

## 7. 错误处理和日志观察

- filters、exceptions、interceptors 较完整。
- request_id/trace_id 未明确发现。
- 生产错误隐藏策略需专项审计。

## 8. 部署和环境变量观察

- Dockerfile 多阶段构建。
- docker-compose 包含 app、postgres、pgadmin、meilisearch。
- 依赖 Node 25/pnpm，个人项目默认偏重。

## 9. 测试和质量观察

- auth.controller.spec 和 e2e 测试存在，docs/testing.md 说明测试规则。
- lint workflow 存在。
- 工程化强，但模板复杂度高。

## 10. 可提炼规则

- 规则 1：NestJS 项目应按 module/controller/service/entity/dto/guard/filter/interceptor 分层。
  - 来源观察：awesome-nest-boilerplate 和 prime-nestjs 都采用模块化 NestJS 结构。
  - 适合场景：中型 NestJS REST API。
  - Agent 生成代码时应该怎么做：新增资源时生成 module、controller、service、dto、entity、spec，并注册 Swagger decorator。
- 规则 2：RBAC 需要 decorator + guard + auth strategy 联合实现，不能只在 service 里判断 role。
  - 来源观察：awesome-nest-boilerplate 有 roles.decorator/roles.guard/jwt.strategy，prime-nestjs 也有 roles guard。
  - 适合场景：NestJS JWT/RBAC API。
  - Agent 生成代码时应该怎么做：在 controller route 层声明角色，在 guard 层统一校验，并给测试覆盖未授权/越权路径。

## 11. 不建议照搬的地方

- .env.example 含完整 RSA private key，存在 secret 示例风险。
- S3/Meilisearch/BullMQ/i18n/CQRS 等对个人项目默认过重。
- Node 25 和复杂构建链不适合作为保守默认。

## 12. 适合进入哪些知识库文件

- rules/backend-layered-architecture-rules.md：NestJS module 分层和 DTO/entity/guard/filter 结构完整。
- rules/auth-and-permission-rules.md：JWT + roles guard 是 RBAC 候选来源。
- wiki/templates/nestjs-project-template.md：可作为重型 NestJS 模板参考。
- rules/backend-security-checklist.md：env private key 风险和 guard 权限边界值得进入 checklist。
- wiki/patterns/rbac-permission-pattern.md：decorator + guard + strategy 模式适合作为 RBAC pattern。

## 13. 项目质量评分

- README 清晰度：4/5
- 目录结构清晰度：5/5
- 测试完整度：4/5
- Docker / 部署完整度：5/5
- 数据库迁移完整度：4/5
- 权限系统完整度：5/5
- 日志异常完整度：4/5
- 对个人项目的参考价值：2/5
- 对中型项目的参考价值：5/5
- 是否适合进入核心规则库：4/5

trust_level：`good_reference`
