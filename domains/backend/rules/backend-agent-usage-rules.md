# Backend Agent Usage Rules

## 文件用途

约束 Agent 如何使用 backend 知识库：优先读取 rules/processed，避免整库扫描和照搬 raw 源码。

## 适用场景

- Agent 准备生成后端代码。
- Agent 准备分析 GitHub 后端项目。
- Agent 准备从 backend 数据库提取规则、pattern 或模板。

## 优先读取条件

- 任务要求使用 backend 数据库。
- 任务涉及 API、DB、auth、deployment、AI backend。
- 任务要求继续建设 backend 知识库。

## 适合的项目类型

- 本地知识库维护
- 规则检索
- 代码生成前上下文选择
- GitHub 项目分析

## 不适合的项目类型

- 纯前端视觉任务
- 素材检索任务
- 浏览器自动化任务

## 推荐做法

- 优先读取 README 和 rules，再按任务读取 processed chunks。
- 读取 GitHub 项目时只读取 processed analysis/metadata/chunks，除非任务明确要求重新审查 raw。
- 把 core_reference 与 good_reference 作为主要依据，把 sample_only 作为反例或示例。
- 最终回答说明使用了哪些 backend 文件和验证方式。

## 禁止做法

- 不要整库乱扫。
- 不要运行 raw GitHub 项目。
- 不要安装依赖或启动服务。
- 不要把 .env.example 中疑似 secret 的内容复制进规则、README、模板或 references。

## Agent 生成代码时必须遵守的规则

1. 先读 `domains/backend/README.md`。
2. 按任务读取具体 rules 文件。
3. 需要项目证据时读取 `processed/metadata` 和 `output/reports`。
4. 只在后续阶段被授权时生成 wiki、references、SQLite 或 API。
5. 发现 secret-looking 内容时只记录风险，不复制原文。

## 常见失败案例

- Agent 直接打开 raw 项目所有源码。
- Agent 使用低星 sample 生成核心规则。
- Agent 把示例私钥或密码写进模板。

## 检查清单

- [ ] 已读取 backend README
- [ ] 已选择具体 rule 文件
- [ ] 未运行项目或安装依赖
- [ ] 未复制 secret-looking 内容
- [ ] 输出包含验证结果

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

- domains/backend/README.md
- rules/github-backend-project-selection-rules.md
- domains/backend/processed/metadata/github_projects
- domains/backend/output/reports/github-projects-analysis-report.md
