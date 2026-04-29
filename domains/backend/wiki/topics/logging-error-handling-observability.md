# Logging Error Handling Observability

## 主题说明
统一异常、日志、request_id、trace_id 和指标。

## 为什么重要
没有可观测性，Agent 生成的后端难以调试和上线。

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
统一异常处理 + request_id + 基础结构化日志。

## 中型项目推荐方案
OpenTelemetry、Prometheus/Grafana、告警、慢查询和队列监控。

## 大型项目才需要的方案
全链路追踪平台只在多服务或高并发场景需要。

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
