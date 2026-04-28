# AI Backend Design Rules

## 文件用途

为 Agent 生成 RAG、Agent、大模型 API、OpenAI-compatible API、SSE streaming、文件 ingestion 和 vector store 后端规则。

## 适用场景

- RAG 后端。
- Agent API。
- 大模型 API 网关。
- OpenAI-compatible API。
- SSE 流式输出。
- 文件上传和向量检索。

## 优先读取条件

- AI backend、RAG、Agent、大模型 API、OpenAI-compatible、SSE、streaming、vector store、pgvector、embedding、ingestion。

## 适合的项目类型

- FastAPI RAG
- OpenAI-compatible gateway
- 文档问答后端
- Agent 服务端
- 管理后台里的 AI 功能

## 不适合的项目类型

- 普通 CRUD API
- 纯前端聊天 UI
- 无需模型调用的静态页面

## 推荐做法

- prompt、API key、用户输入、文件内容必须隔离。
- RAG pipeline 分为 upload、parse、chunk、embed、store、retrieve、answer。
- vector store 默认优先 PostgreSQL/pgvector 或明确外部向量库。
- 检索必须带 user_id/document_id/file_id metadata filter。
- SSE 必须有超时、取消、错误事件和客户端兼容测试。
- OpenAI-compatible API 保持 `/v1/models`、`/v1/chat/completions`、Responses、Files 协议边界。

## 禁止做法

- 不要把用户 prompt、API key 或 system prompt 写入日志。
- 不要全库检索忽略权限范围。
- 不要在 controller 里直接做 PDF 解析、embedding 和数据库写入。
- 不要把 SQLite 作为 pgvector 生产替代。
- 不要无上限流式输出。

## Agent 生成代码时必须遵守的规则

1. ingestion 必须独立于普通 API route。
2. 每个文档 chunk 必须带来源和权限 metadata。
3. 向量检索必须按用户/文件范围过滤。
4. LLM 调用必须有超时、取消、错误处理和成本边界。
5. SSE 响应必须符合客户端协议。
6. 文件上传必须遵守安全上传规则。

## 常见失败案例

- RAG 查询跨用户返回文件片段。
- 上传解析失败后没有状态记录。
- OpenAI-compatible 响应 shape 随意改变导致 SDK 不兼容。
- 日志记录完整 prompt 和 API key。

## 检查清单

- [ ] prompt/API key 隔离
- [ ] RAG pipeline 分层
- [ ] metadata filter 存在
- [ ] SSE 超时/取消/错误存在
- [ ] OpenAI-compatible 协议稳定
- [ ] 文件上传安全

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
- wiki/patterns/rag-backend-pipeline-pattern.md
- wiki/patterns/sse-streaming-response-pattern.md
