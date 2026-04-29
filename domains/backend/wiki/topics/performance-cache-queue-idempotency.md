# Performance Cache Queue Idempotency

## 主题说明
性能、缓存、队列、幂等、超时和重试。

## 为什么重要
稳定性来自边界：超时、重试、幂等、失败记录和可观测。

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
DB 索引、超时、有限重试、简单后台任务。

## 中型项目推荐方案
Redis 缓存、队列、幂等键、死信/失败记录、指标。

## 大型项目才需要的方案
分布式事务、事件溯源、全局调度平台只在复杂系统需要。

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
