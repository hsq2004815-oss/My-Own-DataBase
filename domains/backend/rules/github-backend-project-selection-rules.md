# GitHub Backend Project Selection Rules

## 文件用途

为 Agent 分析 GitHub 后端开源项目时提供评分、分级和规则提取标准。

## 适用场景

- 分析 GitHub 后端项目。
- 从开源项目提取 backend rules 候选。
- 判断项目是否适合进入核心知识库。

## 优先读取条件

- GitHub 项目分析、开源项目、质量评分、规则候选、core_reference、sample_only。

## 适合的项目类型

- FastAPI 项目分析
- Express/NestJS 项目分析
- AI backend/RAG 项目分析
- 本地 backend 数据库建设

## 不适合的项目类型

- 直接生成业务代码
- 纯前端项目筛选
- 不需要规则提取的随手浏览

## 推荐做法

- 先区分项目类型：完整模板、库项目、文档型规则、demo/sample。
- 评分维度包括 README、结构、测试、部署、migration、auth、日志错误、个人价值、中型价值、核心规则价值。
- star 少不是绝对不可靠，但低星项目不能直接作为核心规则来源。
- 只有多个项目或官方文档共同支持的做法才进入核心 rules。
- 单个低星或 sample 项目只进入 sample/wiki 候选。

## 禁止做法

- 不要只看 star 数决定质量。
- 不要把 sample_only 项目写法提升为核心规则。
- 不要运行项目或安装依赖。
- 不要删除、移动、覆盖 raw 源码。
- 不要复制 .env.example 中的 secret-looking 内容。

## Agent 生成代码时必须遵守的规则

1. 每个项目必须给 trust_level。
2. 每个规则候选必须有来源观察和适用场景。
3. 每个项目必须说明不建议照搬的地方。
4. 安全风险只描述风险，不复制原文 secret。
5. 总报告必须汇总共同规则和下一步建议。

## 常见失败案例

- 把一个 demo 的单文件结构写成核心模板。
- 因 star 少直接丢弃有清晰测试的小项目。
- 把文档型最佳实践当可运行模板。
- 忽略 env 示例风险。

## 检查清单

- [ ] 项目类型已识别
- [ ] trust_level 合法
- [ ] 规则有多来源支撑
- [ ] sample 没有升格
- [ ] 安全风险已标注
- [ ] raw 源码未修改

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

- domains/backend/output/reports/github-projects-analysis-report.md
- domains/backend/processed/metadata/github_projects
- rules/backend-project-template-rules.md
- rules/backend-security-checklist.md
