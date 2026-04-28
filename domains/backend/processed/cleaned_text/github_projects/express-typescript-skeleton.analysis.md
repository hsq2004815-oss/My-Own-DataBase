# express-typescript-skeleton

## 1. 项目定位

- Express TypeScript production template
- DDD/hexagonal architecture
- Prisma persistence
- Docker Compose
- CI/CD
- Jest unit/integration/e2e
- Logger/cache/DI

## 2. 技术栈

- 后端框架：Express via Ts.ED platform 线索、TypeScript
- 数据库：PostgreSQL、Redis/cache 线索
- ORM：Prisma
- migration 工具：Prisma Migrate
- 认证方式：JWT/session modules
- 权限方式：用户/session 领域，RBAC 未完整确认
- 缓存：Redis/ioredis
- 队列：未发现
- 文件存储：未发现
- 部署方式：docker/Dockerfile、docker/docker-compose.yml、Makefile
- 测试工具：Jest、Supertest、unit/integration/e2e
- 文档工具：README、.github docs
- CI/CD：GitHub Actions CI/CD、Renovate

## 3. 目录结构观察

- src 分为 application、domain、infrastructure、presentation、types。
- presentation/rest/controllers、middlewares、filters、exceptions 与 domain/application 分离。
- infrastructure/shared 包含 authentication、cache、config、di、logger、persistence。
- test 下有 unit、integration、e2e。
- 这是重型架构模板。

## 4. API 设计观察

- REST presentation 层明确。
- controller/middleware/filter/exception 分离。
- healthcheck 存在。
- OpenAPI/Swagger 有 Ts.ED/swagger 依赖线索。
- 参数校验可能由 Ts.ED/AJV/schema 完成，需专项确认。

## 5. 数据库设计观察

- Prisma + PostgreSQL。
- Docker compose 提供 Postgres 和 pgweb。
- persistence 放在 infrastructure 层。
- 事务/索引/seed 需进一步专项阅读。

## 6. 鉴权和权限观察

- sessions/users/authentication 领域存在。
- JWT 依赖线索。
- RBAC 未明确发现。
- 结构适合复杂认证，但个人项目默认过重。

## 7. 错误处理和日志观察

- domain/shared/exceptions、presentation/rest/filters、infrastructure/shared/logger 完整。
- 日志 volume 在 docker-compose 中配置。
- request_id/trace_id 未明确发现。

## 8. 部署和环境变量观察

- docker/Dockerfile 多阶段生产镜像，pm2/wait。
- docker-compose 包含 app、postgres、pgweb 和日志 volume。
- Makefile 检查 docker/docker-compose/npm。
- CI/CD、CODEOWNERS、SECURITY、renovate 等治理文件完整。

## 9. 测试和质量观察

- unit/integration/e2e 三层测试目录。
- package scripts 覆盖 type、format、lint、markdown、packagejson 等。
- 架构质量强，但学习和维护成本高。

## 10. 可提炼规则

- 规则 1：大型 Express 项目可以采用 presentation/application/domain/infrastructure，但个人默认不应上来就生成重型 DDD。
  - 来源观察：express-typescript-skeleton 结构完整但明显重于 express-ts-pg-prisma-boilerplate。
  - 适合场景：中型以上、领域复杂、团队维护项目。
  - Agent 生成代码时应该怎么做：除非用户明确要求 DDD/hexagonal，否则优先生成四层 feature-based 结构。
- 规则 2：生产 Node 模板应提供 unit/integration/e2e 分层测试和 CI/CD。
  - 来源观察：express-typescript-skeleton 和 express-ts-pg-prisma-boilerplate 都有多层测试，前者 CI/CD 更完整。
  - 适合场景：中型 Node API。
  - Agent 生成代码时应该怎么做：测试目录按层次和场景拆分，app factory/DI 使 controller 与集成测试可启动。

## 11. 不建议照搬的地方

- 复杂 DDD/hexagonal 对个人项目默认不划算。
- 工具链和 GitHub 治理文件非常多，初学者维护成本高。
- Ts.ED 平台依赖可能偏离普通 Express 项目预期。

## 12. 适合进入哪些知识库文件

- rules/backend-layered-architecture-rules.md：可作为重型架构上限参考。
- rules/backend-project-template-rules.md：用于定义个人项目不要默认上过重 DDD。
- rules/error-handling-and-logging-rules.md：filters/exceptions/logger 分层可作候选。
- wiki/templates/express-project-template.md：适合作为中型/大型 Express 模板参考。

## 13. 项目质量评分

- README 清晰度：5/5
- 目录结构清晰度：5/5
- 测试完整度：5/5
- Docker / 部署完整度：5/5
- 数据库迁移完整度：4/5
- 权限系统完整度：4/5
- 日志异常完整度：5/5
- 对个人项目的参考价值：2/5
- 对中型项目的参考价值：5/5
- 是否适合进入核心规则库：4/5

trust_level：`good_reference`
