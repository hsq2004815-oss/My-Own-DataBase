# Agent Workflow

这个知识域用于沉淀“其他智能体如何使用本地知识库完成任务”的流程规范。

目标不是存普通聊天记录，而是存可复用的工作流：

- 什么时候调用本地 API
- 如何从用户任务中提取检索关键词
- 如何组合 UI/design chunks
- 如何处理 Windows 路径和 Bash/PowerShell 差异
- 如何要求智能体报告证据
- 如何处理检索为空、API 未启动、路径错误、结果不相关

## 数据流

raw -> processed/references -> processed/chunks -> SQLite/FTS5 -> backend_api

## 当前重点

第一阶段先服务前端生成：让 Claude Code、Codex、Cursor 等智能体在设计页面前调用 `http://127.0.0.1:8765/ui/search`。
后续再扩展到 automation、文档处理、报告生成等其他知识域。
