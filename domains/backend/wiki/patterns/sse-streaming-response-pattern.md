# SSE Streaming Response Pattern

## 解决什么问题
稳定返回 LLM/AI 流式输出。

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
client -> SSE endpoint -> async generator -> event chunks -> done/error
```

## 关键实现点
- 心跳或超时。
- 取消处理。
- 错误事件。
- 客户端兼容测试。

## 失败案例
- 裸字符串拼接。
- 断连后任务继续消耗资源。

## Agent 生成代码注意事项
- 生成必要文件，不复制开源项目源码。
- 同步生成输入校验、错误处理、日志和最小测试。
- 涉及 secret 时只使用明显占位符。
- 涉及数据库时生成 migration，不只生成 model。

## 关联规则
- rules/ai-backend-design-rules.md
