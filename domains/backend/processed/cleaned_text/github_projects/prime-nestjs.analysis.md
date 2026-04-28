# prime-nestjs

## 1. 项目定位

- NestJS production starter
- JWT + RBAC
- PostgreSQL + TypeORM
- Swagger docs
- Docker Compose
- Jest unit/e2e
- Health checks

## 2. 技术栈

- 后端框架：NestJS
- 数据库：PostgreSQL
- ORM：TypeORM
- migration 工具：TypeORM migrations scripts
- 认证方式：JWT RSA256、Passport
- 权限方式：RBAC/CASL/roles guard
- 缓存：未发现
- 队列：schedule 依赖线索
- 文件存储：未发现
- 部署方式：Dockerfile、docker-compose
- 测试工具：Jest、Supertest、e2e
- 文档工具：Swagger、documentation/*.md
- CI/CD：GitHub Actions CI、CodeQL

## 3. 目录结构观察

- src/auth、src/users、src/tasks、src/config、src/logger 按模块组织。
- auth 中有 controller/service/module/dto/strategy/guard/spec。
- tasks/users 有 dto/entities/services/controllers/spec。
- documentation/auth.md 与 config.md 提供专题文档。

## 4. API 设计观察

- REST API 由 NestJS controllers 暴露。
- Swagger 自动文档位于 /api。
- 健康检查在 docker-compose healthcheck 中调用 /health-check。
- 参数校验通过 DTO/class-validator。
- API versioning 未明确发现。

## 5. 数据库设计观察

- PostgreSQL + TypeORM。
- package scripts 提供 migration:generate/run/revert/schema sync/drop。
- config/database.ts 集中数据库配置，docker-compose 有 Postgres healthcheck。
- 种子数据未明确发现。

## 6. 鉴权和权限观察

- JWT RSA256 with private/public key placeholders。
- roles.guard、jwt.strategy、jwt-auth.guard、role enum 明确。
- 有 auth service/controller/guard specs。
- OAuth/OIDC 未发现。

## 7. 错误处理和日志观察

- src/logger/logger.module/service 存在。
- Helmet/CORS 和 health checks 有生产治理线索。
- 统一错误格式/错误码未完整确认。

## 8. 部署和环境变量观察

- 多阶段 Dockerfile，生产阶段非 root 用户。
- docker-compose 绑定 127.0.0.1 暴露端口，有 healthcheck 和 network。
- CI/CodeQL 存在。
- .env.example 使用 placeholder key，风险低于直接放真实 key，但仍需提醒生成时使用占位。

## 9. 测试和质量观察

- Jest unit + e2e，多个 spec 文件。
- README 清楚列出质量工具。
- 适合作为 NestJS good reference。

## 10. 可提炼规则

- 规则 1：NestJS production starter 应同时提供 Swagger、healthcheck、Docker healthcheck、unit/e2e tests。
  - 来源观察：prime-nestjs 明确包含这些能力，awesome-nest 也有 health-checker/Swagger/tests。
  - 适合场景：中型 NestJS API。
  - Agent 生成代码时应该怎么做：创建 main.ts 时启用 validation/security/docs，并在 compose 中添加 healthcheck。
- 规则 2：RSA JWT 示例必须用 placeholder，不写真实私钥。
  - 来源观察：prime-nestjs 用 <your-rsa-private-key-here> 占位，awesome-nest 则出现完整私钥文本风险。
  - 适合场景：所有 JWT RSA256 模板。
  - Agent 生成代码时应该怎么做：生成 .env.example 只写占位符，并在 README 提示本地生成密钥。

## 11. 不建议照搬的地方

- 仍然比个人 CRUD 项目重。
- TypeORM schema:sync 脚本在生产应谨慎，不应作为默认迁移方式。
- CASL/RBAC 需要需求明确后再默认启用。

## 12. 适合进入哪些知识库文件

- wiki/templates/nestjs-project-template.md：适合作为较平衡 NestJS 模板参考。
- rules/auth-and-permission-rules.md：JWT RSA + RBAC/roles guard 候选。
- rules/deployment-and-env-rules.md：Docker healthcheck、非 root runtime、env placeholders 可入规则。
- wiki/patterns/rbac-permission-pattern.md：Roles guard + strategy 是明确 pattern。

## 13. 项目质量评分

- README 清晰度：5/5
- 目录结构清晰度：4/5
- 测试完整度：4/5
- Docker / 部署完整度：5/5
- 数据库迁移完整度：4/5
- 权限系统完整度：5/5
- 日志异常完整度：4/5
- 对个人项目的参考价值：4/5
- 对中型项目的参考价值：5/5
- 是否适合进入核心规则库：4/5

trust_level：`good_reference`
