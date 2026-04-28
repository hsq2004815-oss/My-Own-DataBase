# Auth And Permission Rules

## 文件用途

为 Agent 生成登录、注册、JWT、session、refresh token、RBAC、管理员权限和用户系统提供规则。

## 适用场景

- 登录注册。
- 用户系统。
- 管理员后台。
- JWT/refresh token/session。
- RBAC/角色权限。

## 优先读取条件

- 登录、注册、权限、管理员、用户系统、JWT、refresh token、session、RBAC、OAuth2、OIDC。

## 适合的项目类型

- 小程序后端
- 管理系统后端
- FastAPI/Express/NestJS API
- 需要用户隔离的 RAG 后端

## 不适合的项目类型

- 无用户身份的公开静态 API
- 纯内部一次性脚本
- 不涉及权限的纯前端任务

## 推荐做法

- 明确区分 authentication 和 authorization。
- 短期 access token 与长期 refresh token 分离。
- refresh token 必须 hash 存储、可撤销、可轮换。
- session 适合传统 Web 和需要服务端撤销的场景。
- RBAC 适合管理员后台、组织角色和资源访问控制。
- 所有权限校验放在 middleware/guard/dependency 层，不散落在 controller。
- 模板 secret 只能使用 CHANGE_ME、REPLACE_WITH_RANDOM_SECRET、your_postgres_password 这类明显占位符。

## 禁止做法

- 不要明文存储密码或 refresh token。
- 不要把 role、is_admin 只交给前端传参。
- 不要复制示例 RSA private key、JWT secret、DB password。
- 不要在 README、template、rules、references 中沉淀真实或疑似真实 secret。
- 不要把 authentication 当 authorization。

## Agent 生成代码时必须遵守的规则

1. 密码必须使用成熟哈希算法。
2. refresh token 入库前必须 hash。
3. 管理员/角色权限必须由后端从可信数据源读取。
4. 每个受保护路由必须有认证依赖或 guard。
5. 每个敏感操作必须有授权检查。
6. .env.example 只说明变量名，值必须是明显占位符。
7. 发现 secret-looking 内容时只能写存在风险，需要替换，不复制原文。

## 常见失败案例

- 只校验 JWT 是否存在，不校验权限。
- refresh token 明文入库。
- 管理员接口只看前端传来的 role。
- 把示例私钥复制进新模板。
- RBAC 没有测试越权路径。

## 检查清单

- [ ] 认证和授权已分离
- [ ] token 生命周期明确
- [ ] refresh token hash/rotation 明确
- [ ] RBAC guard/middleware 存在
- [ ] secret 使用占位符
- [ ] 越权测试路径明确

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
- rules/deployment-and-env-rules.md
- wiki/patterns/jwt-refresh-token-pattern.md
- wiki/patterns/rbac-permission-pattern.md
- wiki/checklists/auth-security-checklist.md
