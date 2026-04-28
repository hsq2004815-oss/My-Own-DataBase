# Error Handling And Logging Rules

## 文件用途

为 Agent 生成统一异常处理、错误码、日志、request_id/trace_id 和生产错误隐藏规则。

## 适用场景

- 设计 API 错误格式。
- 生成中间件/异常过滤器。
- 接入日志系统。
- 定位生产问题。

## 优先读取条件

- 错误处理、错误码、日志、request_id、trace_id、异常、中间件、filter、observability。

## 适合的项目类型

- FastAPI API
- Express API
- NestJS API
- 管理系统后端
- AI backend

## 不适合的项目类型

- 纯静态页面
- 无 HTTP 边界的一次性脚本

## 推荐做法

- 所有请求生成或透传 request_id。
- 统一错误响应包含 code、message、request_id，生产环境隐藏内部细节。
- 业务异常和系统异常分开。
- 日志记录上下文但不泄漏 secret、token、password、private key。
- 关键写操作记录审计日志。
- RAG/LLM 请求记录模型、耗时、token/成本摘要，但不记录完整敏感 prompt。

## 禁止做法

- 不要把异常堆栈返回给用户。
- 不要在日志里打印 Authorization、Cookie、API key、数据库密码、私钥或完整用户敏感输入。
- 不要每个 controller 自己拼错误格式。
- 不要吞掉异常后返回成功。

## Agent 生成代码时必须遵守的规则

1. 每个服务必须有统一异常入口。
2. 每个请求日志必须带 request_id。
3. 业务错误必须有稳定 error code。
4. 生产错误必须隐藏内部实现。
5. 敏感字段必须脱敏。
6. 后台任务失败必须记录可重试状态。

## 常见失败案例

- 返回 200 但 body 里写 error。
- 日志泄漏 JWT 或 API key。
- 没有 request_id 导致无法追踪。
- 数据库错误直接暴露表名和 SQL。

## 检查清单

- [ ] 统一异常处理存在
- [ ] 错误码稳定
- [ ] request_id/trace_id 存在
- [ ] 日志脱敏
- [ ] 生产错误隐藏
- [ ] 后台任务失败可追踪

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

- rules/api-design-rules.md
- rules/backend-security-checklist.md
- rules/performance-and-stability-rules.md
- wiki/checklists/deployment-readiness-checklist.md
