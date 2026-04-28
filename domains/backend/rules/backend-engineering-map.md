# Backend Engineering Map

## 文件用途

给 Agent 一个后端任务总入口，用来判断应该读取哪些 backend rules、wiki、patterns 和 checklists，并选择保守的工程默认值。

## 适用场景

- 开发 API、后台接口、小程序后端、管理系统后端。
- 需要从零生成后端项目结构。
- 需要判断是否应该采用 FastAPI、Express、NestJS、数据库、缓存、Docker 或 AI backend 能力。

## 优先读取条件

- 任务出现 backend、API、服务端、后台、小程序后端、管理系统、数据库、登录、部署、RAG、Agent API。
- 用户说按我的 backend 数据库规则生成代码。

## 适合的项目类型

- 个人项目
- 小程序后端
- 管理系统后端
- FastAPI API
- Express / NestJS API
- RAG 后端
- 自动化工具后端

## 不适合的项目类型

- 纯前端页面
- 只做 UI/landing page
- 大型微服务治理
- Kubernetes 服务网格
- 未明确需要的复杂 DDD/CQRS/Event Sourcing

## 推荐做法

- 默认采用模块化单体，按功能域分层。
- 先确定 API、数据、鉴权、安全、日志、部署的最小闭环。
- 个人项目优先 FastAPI + SQLite/PostgreSQL；Redis、队列、对象存储和搜索引擎只有需求明确时加入。
- 规则只写 Agent 可执行约束，不写长篇教程。

## 禁止做法

- 不要默认微服务。
- 不要为普通个人项目强行引入 K8s、服务网格或复杂 DDD。
- 不要从 raw GitHub 项目源码直接复制模板。
- 不要把 sample_only 项目观察提升为核心规则。

## Agent 生成代码时必须遵守的规则

1. 先识别任务类型，再读取对应 rule 文件。
2. 生成后端代码前必须明确数据存储、错误处理、鉴权边界和部署假设。
3. 默认输出模块化单体结构，除非用户明确要求分布式。
4. 所有环境变量示例必须使用明显占位符。
5. 每个后端变更都要给出最小验证方式。

## 常见失败案例

- Agent 只生成 controller，不生成 service/repository/schema。
- 把 Redis、队列、微服务和对象存储作为默认依赖。
- 只看 GitHub raw 源码，忽略 processed 分析结果。

## 检查清单

- [ ] 任务已路由到具体 rule 文件
- [ ] 默认架构没有过度设计
- [ ] 关键安全和 env 规则已纳入
- [ ] 没有引用 raw 项目源码作为可直接复制模板

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
- rules/database-modeling-rules.md
- rules/auth-and-permission-rules.md
- rules/backend-project-template-rules.md
- domains/backend/output/reports/github-projects-analysis-report.md
