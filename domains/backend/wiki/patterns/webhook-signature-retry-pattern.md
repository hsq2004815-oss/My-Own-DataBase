# Webhook Signature Retry Pattern

## 解决什么问题
安全处理外部事件回调、签名、重试和幂等。

## 适用场景
- API 后端
- 小程序后端
- 管理系统后端
- 自动化工具后端
- AI/RAG 后端

## 不适合场景
- 纯前端页面
- 一次性脚本
- 用户明确要求不同架构且有充分理由
- 会让个人项目过度复杂的场景

## 推荐目录结构或数据流
```text
receive -> verify signature -> idempotency check -> process -> event log
```

## 关键实现点
- 验签。
- 事件 id 去重。
- 记录处理状态。

## 失败案例
- 不验签。
- 重复事件重复执行业务。

## Agent 生成代码注意事项
- 生成必要文件，不复制开源项目源码。
- 同步生成输入校验、错误处理、日志和最小测试。
- 涉及 secret 时只使用明显占位符。
- 涉及数据库时生成 migration，不只生成 model。

## 关联规则
- rules/api-design-rules.md
- rules/backend-security-checklist.md
