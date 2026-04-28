# Deployment And Env Rules

## 文件用途

为 Agent 生成 Docker、Docker Compose、环境变量、健康检查、CI 和部署就绪规则。

## 适用场景

- 生成 Dockerfile。
- 生成 docker-compose.yml。
- 设计 .env.example。
- 上线部署前检查。
- CI lint/type/test 配置。

## 优先读取条件

- 部署、Docker、docker-compose、环境变量、.env.example、CI、服务器、healthcheck、上线。

## 适合的项目类型

- 个人项目
- 管理系统后端
- FastAPI/Express/NestJS API
- RAG 后端
- 自动化工具后端

## 不适合的项目类型

- 纯前端静态页面
- 不需要部署的本地脚本
- K8s/服务网格专项平台任务

## 推荐做法

- 个人项目优先 Docker Compose，而不是 K8s。
- Dockerfile 使用多阶段或最小运行镜像，并避免把 dev 依赖带进生产。
- 容器默认非 root 用户。
- Compose 至少包含 app/db/redis 可选和 healthcheck。
- .env.example 只说明变量名，值用明显占位符。
- CI 至少运行 lint、typecheck、tests。

## 禁止做法

- 不要运行 docker compose up 作为规则建设步骤。
- 不要在 .env.example 放真实或 hardcoded-looking secret。
- 不要复制示例 RSA private key、JWT secret、DB password。
- 不要把生产密码写入 README。
- 不要默认 Kubernetes。

## Agent 生成代码时必须遵守的规则

1. 所有 secret 示例必须是 CHANGE_ME、REPLACE_WITH_RANDOM_SECRET、your_postgres_password 这类占位符。
2. .env.example 用于说明变量名，不用于提供真实值。
3. 发现 secret-looking 内容只能记录风险，不能复制原文。
4. Docker Compose 中数据库必须使用 volume。
5. 服务必须有 healthcheck 或健康检查 endpoint。
6. 部署文档必须列出迁移命令但不自动执行。

## 常见失败案例

- Dockerfile 用 `npm install` 和 dev server 作为生产 CMD。
- Compose 暴露数据库到 0.0.0.0 且无说明。
- .env.example 带长随机密钥或私钥。
- 没有 healthcheck，失败时只能看日志。

## 检查清单

- [ ] Dockerfile 生产可用
- [ ] Compose 有 volume/healthcheck
- [ ] env 示例全是占位符
- [ ] CI 命令明确
- [ ] 没有默认 K8s
- [ ] 迁移步骤未被自动执行

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

- rules/backend-security-checklist.md
- rules/performance-and-stability-rules.md
- rules/error-handling-and-logging-rules.md
- wiki/templates/docker-compose-backend-template.md
