# API Design Rules

## 文件用途

为 Agent 生成 REST、OpenAPI、OpenAI-compatible、后台接口和小程序后端接口提供可检查规则。

## 适用场景

- 开发 REST API。
- 开发管理系统/小程序后端接口。
- 生成 OpenAPI/Swagger 文档。
- 设计分页、错误码、幂等、Webhook 或流式接口。

## 优先读取条件

- API、接口、REST、OpenAPI、Swagger、分页、错误码、幂等、Webhook、SSE、streaming。

## 适合的项目类型

- FastAPI API
- Express API
- NestJS API
- RAG/OpenAI-compatible API
- 管理系统后端

## 不适合的项目类型

- 纯数据库脚本
- 纯前端页面
- 没有外部接口的本地脚本

## 推荐做法

- 所有请求参数必须经过 schema/DTO 校验。
- 错误返回使用统一 shape，至少包含 code、message、request_id。
- 列表接口必须定义分页参数和排序规则。
- 写操作需要明确幂等策略，支付/Webhook/外部回调必须有 idempotency key 或事件去重。
- OpenAPI/Swagger 文档随路由和 DTO 生成。
- SSE/streaming 必须定义连接超时、取消、错误事件和客户端兼容测试。

## 禁止做法

- 不要在 controller 里直接写数据库逻辑。
- 不要返回裸异常堆栈。
- 不要让分页默认无限制返回。
- 不要信任前端传来的用户 id、role 或 MIME。
- 不要把 OpenAI-compatible API 当普通 JSON API 随意改变响应协议。

## Agent 生成代码时必须遵守的规则

1. 每个 endpoint 必须有 request schema 和 response schema。
2. 每个错误路径必须进入统一异常处理。
3. 分页接口必须有默认 limit 和最大 limit。
4. Webhook 必须验证签名、记录事件、支持重试和幂等。
5. OpenAPI 文档必须与实际 DTO 一致。
6. 流式接口必须支持超时、取消和错误收尾。

## 常见失败案例

- 路由函数里直接 `try/except` 后返回字符串错误。
- 列表接口无分页导致一次返回全表。
- Webhook 不验签，重复事件造成重复扣款或重复发货。
- SSE 只拼接字符串，没有异常和断连处理。

## 检查清单

- [ ] 参数校验完整
- [ ] 统一错误格式存在
- [ ] 分页和排序规则存在
- [ ] 幂等策略存在
- [ ] OpenAPI/Swagger 可生成
- [ ] Webhook/SSE 特殊接口有专项规则

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

- rules/backend-layered-architecture-rules.md
- rules/error-handling-and-logging-rules.md
- rules/backend-security-checklist.md
- rules/ai-backend-design-rules.md
- wiki/patterns/sse-streaming-response-pattern.md
