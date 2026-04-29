# Modular Monolith Pattern

## 解决什么问题
在个人和中型项目中保持单体部署，同时通过模块边界避免代码混乱。

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
src/features/<feature> -> route/controller -> service -> repository -> model/schema
```

## 关键实现点
- 按 feature/module 分目录。
- 共享能力放 core/common。
- 模块间通过 service 接口调用。

## 失败案例
- 把所有代码塞进 main/app。
- 默认拆微服务。

## Agent 生成代码注意事项
- 生成必要文件，不复制开源项目源码。
- 同步生成输入校验、错误处理、日志和最小测试。
- 涉及 secret 时只使用明显占位符。
- 涉及数据库时生成 migration，不只生成 model。

## 关联规则
- rules/backend-layered-architecture-rules.md
