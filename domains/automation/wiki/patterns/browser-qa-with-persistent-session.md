# Pattern: Browser QA with Persistent Session

> 来源：`garrytan/gstack` (MIT) — GStack Browser QA 流程
> 生成时间：2026-04-30
> 适用工具：Playwright / Puppeteer / CDP

## 模式概述

使用持久化浏览器会话进行 QA 测试，避免每次测试冷启动浏览器、重新登录、重建状态。QA agent 在真实 Chromium 中操作应用流程，自动截图、记录错误、生成报告。

## 适用场景

- Web 前端的功能回归测试
- 后台管理系统的操作流程验证
- 登录态依赖的应用测试
- 文件上传/下载功能测试
- 多页面流程的端到端测试

## 不适用场景

- 纯 API 测试（不需要浏览器）
- 单元测试（不需要浏览器）
- 无状态页面的一次性截图

## QA 流程

### 1. 启动阶段

```
1. 启动持久化浏览器 daemon
2. 导入 cookie（如需登录态）
3. 打开目标页面
4. 等待页面加载完成
```

### 2. 测试阶段

```
for each 测试场景:
  1. 执行操作流程 (点击、输入、导航)
  2. 截图记录关键状态
  3. 检查预期结果（文本、元素、状态）
  4. 发现问题 → 原子提交修复
  5. 回归测试 → 确认修复不引入新问题
```

### 3. 报告阶段

```
1. 收集所有截图和日志
2. 生成 QA 报告（通过/失败/跳过）
3. 列出 P0/P1/P2 问题
4. 输出到 report 文件
```

## 核心命令参考（gstack 风格）

```
$B snapshot -i      → 交互式页面快照（自然语言识别）
$B type "selector" "text" → 输入文本
$B click "selector" → 点击元素
$B screenshot       → 截图
$B console          → 获取 console 日志
$B network          → 获取网络请求
$B handoff          → 切换到可见浏览器（CAPTCHA 等场景）
$B resume           → 恢复 headless 会话
```

## 关键设计决策

### 为什么不每次启动新浏览器？

- 冷启动 3-5 秒 × 20+ QA 命令 = 60-100 秒纯启动开销
- Cookie/Session 全部丢失
- 登录态需要每次重建

### 为什么用 daemon 而不是 CDP attach？

- Daemon 管理生命周期（自动启动/关闭/版本更新）
- 统一的 HTTP API，不依赖 CDP 细节
- 跨平台一致性（Chromium 在不同 OS 上的 CDP 行为差异被抽象掉）

## 安全注意事项

- 浏览器 daemon 仅绑定 localhost
- Cookie 导入只从本地浏览器读取
- 不在 QA 报告中输出敏感信息（token/password/cookie）
- QA 浏览器环境与日常浏览器隔离
- 不在共享/远程环境使用真实 cookie

## 集成到数据库

当 Agent 需要做浏览器 QA 时：
1. 调用 `/brief` 获取 automation chunks
2. 读取 `persistent-browser-daemon-for-agent-qa.md` 了解架构
3. 参考本 pattern 设计 QA 流程
4. QA 报告写入 `domains/automation/output/reports/`
