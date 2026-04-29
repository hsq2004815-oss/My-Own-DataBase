# Docker Compose Backend Pattern

## 解决什么问题
为个人/中小项目提供可复现本地部署。

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
app + db + optional redis/worker + volumes + healthcheck + env placeholders
```

## 关键实现点
- volume 持久化。
- healthcheck。
- env 占位符。

## 失败案例
- Compose 里写真实 secret。
- 默认上 K8s。

## Agent 生成代码注意事项
- 生成必要文件，不复制开源项目源码。
- 同步生成输入校验、错误处理、日志和最小测试。
- 涉及 secret 时只使用明显占位符。
- 涉及数据库时生成 migration，不只生成 model。

## 关联规则
- rules/deployment-and-env-rules.md
