# File Upload Processing Pattern

## 解决什么问题
安全处理上传、解析、存储和异步处理。

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
upload -> validate -> safe name -> isolated storage -> scan/parse -> record status
```

## 关键实现点
- 限制大小和类型。
- 不信任 MIME。
- 安全文件名。
- 失败状态记录。

## 失败案例
- 使用原文件名保存。
- 解析阻塞请求线程。

## Agent 生成代码注意事项
- 生成必要文件，不复制开源项目源码。
- 同步生成输入校验、错误处理、日志和最小测试。
- 涉及 secret 时只使用明显占位符。
- 涉及数据库时生成 migration，不只生成 model。

## 关联规则
- rules/backend-security-checklist.md
- rules/ai-backend-design-rules.md
