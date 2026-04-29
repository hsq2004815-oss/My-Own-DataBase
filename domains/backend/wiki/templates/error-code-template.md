# Error Code Template

## 适用场景
错误码注册和异常映射。

## 推荐目录结构
```text
src/errors/error-codes
src/errors/app-error
src/middleware/error-handler
```

## 必备模块
- 配置读取和环境变量校验
- API 路由/controller
- service 业务层
- repository/ORM 层
- schema/DTO 校验
- 统一异常处理和日志
- 测试入口

## 关键文件说明
- config/settings：只读取环境变量和默认配置。
- routes/controller：只处理 HTTP 边界。
- service：执行业务规则。
- repository/model：处理数据访问和迁移。
- middleware/guard：处理认证、授权、request_id、错误。

## Agent 生成步骤
1. 确认任务类型和技术栈。
2. 生成目录结构和关键文件。
3. 生成 schema/DTO、错误处理和日志。
4. 生成数据库 migration 或 schema。
5. 生成安全 env 示例和 README。
6. 生成最小测试或检查清单。

## 安全要求
- secret 必须使用明显占位符。
- 不要使用真实-looking JWT secret、DB password、RSA key。
- 输入必须服务端校验。
- 权限必须由后端校验。
- 日志必须脱敏。
- 文件上传/RAG/AI API 必须限制大小、权限、超时和成本。

## 不要生成的内容
- 默认微服务、K8s、服务网格。
- 默认复杂 DDD、CQRS、Event Sourcing。
- 没有需求的 Redis、队列、对象存储、搜索服务。
- 任何可直接使用的密钥或私钥。

## 检查清单
- [ ] 目录结构已生成
- [ ] 输入校验已生成
- [ ] 统一错误处理已生成
- [ ] 数据库迁移策略已生成
- [ ] env 示例只有明显占位符
- [ ] README/测试入口已生成
