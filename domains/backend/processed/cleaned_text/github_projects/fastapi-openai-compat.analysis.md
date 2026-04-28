# fastapi-openai-compat

## 1. 项目定位

- OpenAI-compatible API 设计
- Chat Completions / Responses API
- SSE streaming 响应
- 文件上传端点
- FastAPI router factory
- 工具调用/自定义 chunk 映射

## 2. 技术栈

- 后端框架：FastAPI
- 数据库：未发现
- ORM：未发现
- migration 工具：未发现
- 认证方式：未发现
- 权限方式：未发现
- 缓存：未发现
- 队列：未发现
- 文件存储：Files endpoint 回调处理，具体存储由调用方实现
- 部署方式：未发现 Docker；库项目以包发布为主
- 测试工具：pytest、pytest-asyncio、pytest-cov、httpx、OpenAI client integration tests
- 文档工具：README、examples README、FastAPI/OpenAPI 默认能力
- CI/CD：GitHub Actions tests、PyPI publish workflow

## 3. 目录结构观察

- src/fastapi_openai_compat 下按 chat_completions、responses、files、models、router、streaming 拆分。
- tests 覆盖导出、集成、OpenAI client、Responses streaming 等场景。
- examples 提供 basic echo、Haystack chat、responses with files 等示例。
- 这是库型项目，不是完整业务后端模板。

## 4. API 设计观察

- REST/OpenAI-compatible endpoints 是核心能力。
- 覆盖 /v1/models、/v1/chat/completions、Responses、Files 等 OpenAI 风格接口。
- 支持 streaming/SSE 与非 streaming 响应。
- API versioning 采用 OpenAI 风格 /v1 路径。
- 统一错误/响应格式围绕 OpenAI 兼容模型，适合 AI Agent 调用。
- 参数校验依赖 Pydantic 模型。

## 5. 数据库设计观察

- 未发现数据库、ORM 或 migration。
- 文件上传由回调处理，持久化交给接入方。
- 不适合作为数据库建模参考。

## 6. 鉴权和权限观察

- 未发现内置 JWT/Session/OAuth/RBAC。
- 作为 router factory 更适合由宿主应用在外层处理中间件、API key 或用户权限。
- Agent 生成代码时不应默认认为 OpenAI-compatible endpoint 已有鉴权。

## 7. 错误处理和日志观察

- 未发现完整业务日志系统。
- 错误与响应更偏协议兼容层，request_id/trace_id 未明确发现。
- 测试覆盖是主要质量证据。

## 8. 部署和环境变量观察

- 没有 Docker 默认路径。
- pyproject、Makefile、GitHub Actions 支撑库发布和测试。
- 适合被后端项目依赖或复制协议层设计，不适合直接部署。

## 9. 测试和质量观察

- 测试目录完整，覆盖 streaming、OpenAI client、Files、Responses、exports。
- Makefile 提供 lint、format-check、typecheck、pytest。
- 对 AI backend API 协议兼容非常有参考价值。

## 10. 可提炼规则

- 规则 1：OpenAI-compatible API 应保持 /v1、models、chat/completions、responses、files 等协议边界清晰。
  - 来源观察：fastapi-openai-compat 将不同协议族拆成独立模块并用 tests 验证 OpenAI client 兼容。
  - 适合场景：自建模型网关、RAG API 暴露 OpenAI 风格接口。
  - Agent 生成代码时应该怎么做：先生成 Pydantic request/response 模型和 router factory，再接入实际 LLM/RAG 执行函数。
- 规则 2：Streaming endpoint 必须同时覆盖非流式、SSE chunk、错误中断和客户端兼容测试。
  - 来源观察：fastapi-openai-compat 与 fastapi-openai-sse-stream 都围绕 streaming 端点测试。
  - 适合场景：LLM token streaming、工具调用、长响应生成。
  - Agent 生成代码时应该怎么做：使用生成器/异步迭代器封装 chunk，不在业务路由里拼接裸字符串。

## 11. 不建议照搬的地方

- 不要把库项目当完整业务模板。
- 未内置鉴权/数据库，不应提升为通用后端模板规则。
- 文件上传持久化策略需由宿主实现。

## 12. 适合进入哪些知识库文件

- rules/ai-backend-design-rules.md：OpenAI-compatible router、streaming、files endpoint 可作为 AI backend 核心候选。
- rules/api-design-rules.md：/v1 协议兼容、Pydantic 模型和 response shape 有 API 规则价值。
- wiki/patterns/sse-streaming-response-pattern.md：流式响应和 chunk 映射是典型 pattern。
- wiki/templates/rag-backend-template.md：适合作为 RAG API 对外兼容层的模板片段。

## 13. 项目质量评分

- README 清晰度：5/5
- 目录结构清晰度：4/5
- 测试完整度：5/5
- Docker / 部署完整度：1/5
- 数据库迁移完整度：0/5
- 权限系统完整度：0/5
- 日志异常完整度：3/5
- 对个人项目的参考价值：4/5
- 对中型项目的参考价值：4/5
- 是否适合进入核心规则库：5/5

trust_level：`core_reference`
