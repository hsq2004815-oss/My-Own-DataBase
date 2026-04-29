# API Design Checklist

用于直接审查后端项目或 Agent 生成的后端代码。

## 通用检查
- [ ] 是否有统一响应格式。
- [ ] 是否有错误码。
- [ ] 是否有请求参数校验。
- [ ] 是否有鉴权中间件。
- [ ] 是否有权限边界。
- [ ] 是否有越权防护。
- [ ] 是否有日志。
- [ ] 是否有统一异常处理。
- [ ] 是否有 request_id / trace_id。
- [ ] 是否有环境变量。
- [ ] .env.example 是否只使用明显占位符。
- [ ] 是否有数据库迁移。
- [ ] 是否有数据库约束和索引。
- [ ] 是否有 Docker 配置。
- [ ] 是否有 README。
- [ ] 是否有 OpenAPI / Swagger。
- [ ] 是否有测试。
- [ ] 是否有安全风险。
- [ ] 是否避免把 secret 写入代码、README、模板、reference。
- [ ] 是否避免个人项目过度引入微服务、K8s、复杂 DDD。

## 专项检查
- [ ] 列表接口是否有分页上限。
- [ ] 写操作是否有幂等策略。
- [ ] Webhook 是否验签和去重。

## 关联规则
- `rules/backend-engineering-map.md`
- `rules/api-design-rules.md`
- `rules/backend-security-checklist.md`
- `rules/deployment-and-env-rules.md`
