# API Response Wrapper Pattern

## 解决什么问题
让前端和 Agent 稳定处理成功与错误响应。

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
handler -> response wrapper -> {code,message,data,request_id}
```

## 关键实现点
- 定义统一成功和错误结构。
- 分页信息单独字段。
- request_id 全链路返回。

## 失败案例
- 所有接口返回不同结构。
- HTTP 200 包裹业务错误。

## Agent 生成代码注意事项
- 生成必要文件，不复制开源项目源码。
- 同步生成输入校验、错误处理、日志和最小测试。
- 涉及 secret 时只使用明显占位符。
- 涉及数据库时生成 migration，不只生成 model。

## 关联规则
- rules/api-design-rules.md
