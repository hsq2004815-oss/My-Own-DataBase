# Error Code System Pattern

## 解决什么问题
建立稳定错误码，避免前端依赖异常文本。

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
exception -> error code registry -> error middleware/filter -> response
```

## 关键实现点
- 错误码按领域命名。
- 错误消息可本地化。
- 生产隐藏内部错误。

## 失败案例
- 直接返回数据库异常。
- 错误码重复或随意变化。

## Agent 生成代码注意事项
- 生成必要文件，不复制开源项目源码。
- 同步生成输入校验、错误处理、日志和最小测试。
- 涉及 secret 时只使用明显占位符。
- 涉及数据库时生成 migration，不只生成 model。

## 关联规则
- rules/error-handling-and-logging-rules.md
