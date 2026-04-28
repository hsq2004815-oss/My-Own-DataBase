# Performance And Stability Rules

## 文件用途

为 Agent 生成后端性能、稳定性、超时、重试、连接池、后台任务和可观测规则。

## 适用场景

- 接口性能优化。
- 后台任务。
- 队列和重试。
- 数据库连接池。
- SSE/长连接。
- 上线稳定性检查。

## 优先读取条件

- 性能、稳定性、超时、重试、连接池、缓存、队列、后台任务、healthcheck、metrics、SSE。

## 适合的项目类型

- API 服务
- RAG/AI backend
- 文件处理服务
- 管理系统后端
- 自动化工具后端

## 不适合的项目类型

- 一次性脚本
- 纯前端页面
- 无需并发的离线文档

## 推荐做法

- 所有外部调用设置超时。
- 后台任务必须有状态、失败记录、重试次数、幂等键。
- 数据库使用连接池且配置上限。
- 缓存只用于明确热点或外部 API 限流，不默认引入。
- 健康检查区分 liveness 和 readiness。
- SSE/LLM 流式输出支持取消和超时。

## 禁止做法

- 不要无限重试。
- 不要把长时间 CPU/OCR/embedding 任务放在请求线程里。
- 不要无上限读取上传文件。
- 不要缓存权限判断结果但没有失效策略。

## Agent 生成代码时必须遵守的规则

1. 每个外部 HTTP/LLM/DB 调用必须有超时。
2. 后台任务必须可重试且幂等。
3. 队列任务必须记录失败原因。
4. 上传和解析必须有大小与耗时限制。
5. 关键指标至少包含请求耗时、错误数、队列失败、DB 连接状态。
6. RAG ingestion 不阻塞普通 API。

## 常见失败案例

- 用户上传大文件导致请求进程卡死。
- LLM 请求无超时导致连接占满。
- 任务失败只写日志没有状态表。
- Redis 被当成必选依赖但没有使用场景。

## 检查清单

- [ ] 超时存在
- [ ] 重试有限且幂等
- [ ] 连接池配置明确
- [ ] 健康检查存在
- [ ] metrics 关键项存在
- [ ] 长任务不阻塞请求

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

- rules/error-handling-and-logging-rules.md
- rules/deployment-and-env-rules.md
- rules/ai-backend-design-rules.md
- wiki/patterns/background-task-queue-pattern.md
