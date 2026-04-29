# Database Modeling And Indexing

## 主题说明
表结构、迁移、约束、索引和数据生命周期。

## 为什么重要
数据库模型决定长期可维护性，Agent 不能只生成 ORM model。

## 核心概念
- 先确定业务边界，再生成目录、接口、数据模型和部署文件。
- 让 Agent 生成代码时优先满足校验、错误、日志、安全和迁移，而不是只生成可运行 demo。
- raw GitHub 项目是证据来源；可执行规则来自 rules、patterns、checklists、templates 和 references。

## 适用场景
- API 后端
- 小程序后端
- 管理系统后端
- 自动化工具后端
- AI 后端 / RAG / Agent API

## 小项目推荐方案
SQLite 或 PostgreSQL + migration + 基础索引。

## 中型项目推荐方案
PostgreSQL、连接池、复合索引、审计字段、读写分离前的监控。

## 大型项目才需要的方案
分库分表、多主复制、复杂 CQRS 只在容量和团队能力明确时使用。

## Agent 使用建议
- 先读取相关 rules，再生成代码。
- 生成目录结构时明确 controller/service/repository/schema 或 module/dto/entity 边界。
- 生成 env/template 时只使用明显占位符，不复制任何 secret-looking 示例。
- 生成后给出最小验证命令，但不要在知识库建设阶段运行项目。

## 常见误区
- 只生成接口实现，不生成校验、错误、日志和测试。
- 把 sample_only 项目写法提升为核心规则。
- 个人项目默认上微服务、K8s、复杂 DDD 或服务网格。
- 把 .env.example 里的示例密钥当模板内容。

## 推荐来源
- `rules/backend-engineering-map.md`
- `rules/api-design-rules.md`
- `rules/database-modeling-rules.md`
- `rules/auth-and-permission-rules.md`
- `rules/backend-security-checklist.md`
- `domains/backend/output/reports/github-projects-analysis-report.md`
- 对应官方文档类型：OpenAPI、FastAPI、PostgreSQL、Redis、Docker、OWASP、OAuth2/OIDC、OpenTelemetry。

## 关联文件
- `rules/backend-engineering-map.md`
- `rules/api-design-rules.md`
- `rules/backend-project-template-rules.md`
- `wiki/checklists/backend-project-start-checklist.md`
- `domains/backend/references`
