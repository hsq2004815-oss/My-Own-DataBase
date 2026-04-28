# Backend Security Checklist

## 文件用途

为 Agent 生成后端安全基线，覆盖 secret、输入校验、上传、鉴权、Webhook、日志和部署。

## 适用场景

- 安全评审。
- 生成登录权限代码。
- 生成文件上传/Webhook。
- 生成 Docker/env 配置。
- 上线前检查。

## 优先读取条件

- 安全、OWASP、secret、env、文件上传、Webhook、权限、CORS、rate limit、审计。

## 适合的项目类型

- 所有后端 API
- 管理系统后端
- 小程序后端
- AI backend
- 文件上传服务

## 不适合的项目类型

- 纯前端静态页面
- 不处理用户输入的本地脚本

## 推荐做法

- 所有输入都在服务端校验。
- secret 只通过环境变量或秘密管理系统注入。
- .env.example 只写变量名和明显占位符。
- 文件上传限制类型、大小、扩展名、真实内容检测和存储隔离。
- Webhook 验签、幂等、事件日志、重试。
- CORS 白名单明确，管理后台接口限制来源和权限。

## 禁止做法

- 不允许把示例 RSA private key、JWT secret、DB password 当成模板内容。
- 不允许在 README、template、rules、references 中沉淀真实或疑似真实 secret。
- 不允许信任前端 MIME、文件名、role、user_id。
- 不允许把 debug stack trace 暴露给生产用户。

## Agent 生成代码时必须遵守的规则

1. 模板 secret 必须使用 CHANGE_ME、REPLACE_WITH_RANDOM_SECRET、your_postgres_password 等明显占位符。
2. 发现 secret-looking 内容只能写存在风险，需要替换，不复制原文。
3. 所有上传文件必须生成安全文件名并隔离存储。
4. 所有 Webhook 必须验签和幂等。
5. 所有敏感接口必须有认证和授权。
6. 所有日志必须脱敏。

## 常见失败案例

- .env.example 中出现看似真实的长 secret。
- 上传文件使用原始文件名保存。
- Webhook 不验签且重复处理。
- 日志打印 Authorization header。
- 管理员接口只靠前端隐藏按钮。

## 检查清单

- [ ] 无 secret 被复制
- [ ] env 示例使用明显占位符
- [ ] 上传限制完整
- [ ] Webhook 验签/幂等
- [ ] 权限后端校验
- [ ] 日志脱敏
- [ ] CORS/rate limit 明确

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

- rules/auth-and-permission-rules.md
- rules/deployment-and-env-rules.md
- rules/api-design-rules.md
- wiki/checklists/auth-security-checklist.md
