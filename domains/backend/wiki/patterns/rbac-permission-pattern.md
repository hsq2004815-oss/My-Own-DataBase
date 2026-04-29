# RBAC Permission Pattern

## 解决什么问题
管理用户角色、管理员权限、菜单和接口权限。

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
user -> roles -> permissions -> guard/middleware -> route
```

## 关键实现点
- 后端读取角色。
- 路由层声明权限。
- 越权路径测试。

## 失败案例
- 只靠前端隐藏按钮。
- role 从请求体传入。

## Agent 生成代码注意事项
- 生成必要文件，不复制开源项目源码。
- 同步生成输入校验、错误处理、日志和最小测试。
- 涉及 secret 时只使用明显占位符。
- 涉及数据库时生成 migration，不只生成 model。

## 关联规则
- rules/auth-and-permission-rules.md
