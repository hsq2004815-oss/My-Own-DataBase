# express-ts-pg-prisma-boilerplate

## 1. 项目定位

- Express TypeScript 分层架构
- Prisma + PostgreSQL
- JWT access/refresh token rotation
- RBAC middleware
- Zod validation
- unit/integration tests
- Docker-first workflow

## 2. 技术栈

- 后端框架：Express 5、TypeScript
- 数据库：PostgreSQL
- ORM：Prisma
- migration 工具：Prisma Migrate
- 认证方式：JWT access token、Refresh token rotation、HttpOnly cookie
- 权限方式：RBAC USER/ADMIN middleware
- 缓存：未发现
- 队列：未发现
- 文件存储：未发现
- 部署方式：Dockerfile、Makefile、docker compose workflow 线索
- 测试工具：Vitest、Supertest、integration tests
- 文档工具：README
- CI/CD：GitHub Actions CI

## 3. 目录结构观察

- src/features/auth 与 src/features/user 按 feature 自包含。
- 每个 feature 下有 controllers、repositories、routes、schemas、services、tests。
- src/middleware 包含 authenticate、authorize、error、request-guard、security、validation。
- src/config 管 env schema、Prisma client；prisma/migrations 完整。

## 4. API 设计观察

- README 明确 routes/controllers/services/repositories 四层。
- REST API 组织清晰。
- 统一错误 middleware 和 AppError 存在。
- Zod schema + validation middleware 负责参数校验。
- health 线索存在。
- API versioning 未明确发现。

## 5. 数据库设计观察

- Prisma schema、seed.ts、migrations 多个版本。
- PostgreSQL 通过 pg/Prisma adapter。
- RefreshToken model migration 存在。
- 事务边界需进一步专项阅读，但 repository 层隔离较好。
- 适合个人项目默认 Express 数据库模板。

## 6. 鉴权和权限观察

- JWT access token + refresh token rotation。
- refresh token 以 SHA-256 hash 入库，HttpOnly cookie，jti 防碰撞。
- RBAC USER/ADMIN middleware。
- 安全中间件和 rate limit 线索。
- OAuth/OIDC 未发现。

## 7. 错误处理和日志观察

- src/errors/app-error.ts 和 error.middleware.ts 体现统一异常。
- LOG_LEVEL env 存在。
- request_id/trace_id 未明确发现。

## 8. 部署和环境变量观察

- Dockerfile 偏开发，Makefile 提供 docker compose、migration、seed、test、lint 操作。
- GitHub Actions CI 存在。
- .env.example 使用 placeholder，同时故意包含 UNUSED_VARIABLE 用于 env 校验警告。

## 9. 测试和质量观察

- unit tests 和 integration tests 分开。
- Vitest + Supertest 覆盖 auth/user。
- 对个人项目和中型项目都具有高参考价值。

## 10. 可提炼规则

- 规则 1：Express TypeScript 项目应按 feature 拆分 routes/controllers/services/repositories/schemas。
  - 来源观察：express-ts-pg-prisma-boilerplate 结构完整，Express skeleton 也强调分层/边界。
  - 适合场景：Node/Express CRUD、认证 API。
  - Agent 生成代码时应该怎么做：新增 feature 时一次生成 route、controller、service、repository、schema、test，并在 app factory 注册。
- 规则 2：Refresh token 应 hash 存储并轮换，cookie 使用 HttpOnly。
  - 来源观察：该项目 README 和 migrations 展示 refresh token model、hash、rotation、jti。
  - 适合场景：自建账户系统。
  - Agent 生成代码时应该怎么做：不要明文存 refresh token；生成 rotation、revoke、reuse detection 测试。

## 11. 不建议照搬的地方

- Dockerfile 使用 npm install/dev 命令，生产镜像还需优化。
- 没有 OpenAPI/Swagger 默认能力。
- 不要把 UNUSED_VARIABLE 当真实配置复制。

## 12. 适合进入哪些知识库文件

- rules/backend-layered-architecture-rules.md：四层 feature-based Express 结构非常清楚。
- rules/auth-and-permission-rules.md：access/refresh rotation、RBAC、HttpOnly cookie 有核心价值。
- rules/database-modeling-rules.md：Prisma migrations/seed/schema 可作 Node DB 规则来源。
- wiki/templates/express-project-template.md：适合作为核心 Express 模板参考。
- wiki/patterns/jwt-refresh-token-pattern.md：refresh token hash + rotation 是明确 pattern。

## 13. 项目质量评分

- README 清晰度：5/5
- 目录结构清晰度：5/5
- 测试完整度：5/5
- Docker / 部署完整度：4/5
- 数据库迁移完整度：5/5
- 权限系统完整度：5/5
- 日志异常完整度：3/5
- 对个人项目的参考价值：5/5
- 对中型项目的参考价值：5/5
- 是否适合进入核心规则库：5/5

trust_level：`core_reference`
