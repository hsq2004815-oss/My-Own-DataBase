# Automation

这个知识域用于沉淀浏览器自动化、Windows 本地自动化、文件上传、CDP 连接、弹窗/iframe 处理、失败恢复和验证报告。

目标：让智能体在执行网页/本地操作任务前，先检索自动化规范，减少路径错误、selector 脆弱、上传失败、登录态丢失和无证据完成的问题。

## 数据流

raw -> processed/references -> processed/chunks -> SQLite/FTS5 -> backend_api

## 优先覆盖

- Playwright locator/actionability/file upload/trace
- Chrome/Edge CDP existing session
- Windows PowerShell path/quoting/process/port
- overlay/modal/dropdown/iframe handling
- automation evidence and safety report
