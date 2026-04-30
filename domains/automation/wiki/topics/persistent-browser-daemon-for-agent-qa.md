# Persistent Browser Daemon for Agent QA

> 来源：`garrytan/gstack` (MIT) — GStack Browser 持久化浏览器 daemon 架构
> 生成时间：2026-04-30
> 适用范围：需要真实浏览器进行 UI/功能测试的 AI agent 项目

## 一、为什么 Agent 需要持久化浏览器

### 问题

每次工具调用都冷启动浏览器 → 3-5 秒延迟 × N 次调用 = 严重影响 agent 效率。更糟的是：每次冷启动丢失所有状态（cookie、localStorage、登录会话、打开的标签页）。

### 解决方案

运行一个**长期存活的 Chromium daemon**，agent CLI 通过 localhost HTTP 与之通信。

```
Agent CLI → POST /command (localhost:PORT) → Bun/Node Server → Chromium (headless)
                                     ← plain text / JSON  ←
```

**首次调用**：启动 daemon + Chromium (~3s)
**后续调用**：纯 HTTP round-trip (~100-200ms)

## 二、架构核心要素

### 2.1 Daemon 生命周期

- **自动启动**：首次调用时自动 spawn
- **自动关闭**：30 分钟空闲后自动 shutdown
- **版本感知**：二进制版本变更时自动重启
- **健康检查**：GET /health 作为活性检测（Windows 上 PID 检测不可靠）

### 2.2 状态持久化

- 浏览器在窗口打开期间保持存活
- Cookie 跨命令保持（登录一次，一直保持）
- localStorage 跨命令保持
- 标签页状态保持

### 2.3 Cookie 导入

从 Chrome/Arc/Brave/Edge 导入真实浏览器 cookie 到 headless 会话，让 QA agent 能以已登录状态测试。

### 2.4 CAPTCHA Handoff

遇到 CAPTCHA 时：
1. `$B handoff` → 打开可见浏览器在同一页面
2. 用户手动解决 CAPTCHA
3. `$B resume` → 恢复 headless 会话，保持登录态

## 三、安全架构

### 3.1 本地绑定

HTTP server 绑定 `127.0.0.1`，不绑定 `0.0.0.0`。不可从网络访问。

### 3.2 双监听器隧道架构

当需要远程配对 agent 访问时：

| | 本地监听器 (127.0.0.1) | 隧道监听器 (127.0.0.1) |
|---|---|---|
| 服务范围 | 全部命令 + 管理接口 | 仅浏览器驱动 allowlist |
| 暴露方式 | 永不转发 | ngrok 转发 |
| `/health` | 公开 | **404** |
| `/cookie-picker` | 公开 UI | **404** |
| `/command` | auth (Bearer) | auth (scoped token only) |
| 安全属性 | 本地独占 | 物理端口隔离 |

**核心原则：** 安全靠物理端口隔离，不靠 header 推断。

### 3.3 Token 体系

- **Root token**：仅本地监听器 + 管理操作
- **Scoped token**：隧道监听器，限浏览器驱动命令 allowlist
- **SSE cookie**：HttpOnly, SameSite=Strict, 30min, 仅 view-only

### 3.4 Prompt Injection 防御

3 层防御：
1. ML 分类器（@huggingface/transformers）— 检测已知注入模式
2. LLM 投票 — 两个模型独立判断是否为注入
3. Canary token — 蜜罐 token，一旦出现在输出中则确定注入

## 四、Domain Skills 机制

Agent 可以为每个常访问的站点保存知识笔记：
- 站点的特殊性（哪些选择器有效，哪些会反爬）
- 登录流程
- 常见陷阱
- 下次访问时自动激活

## 五、适用项目类型

| 项目类型 | 使用方式 | 优先级 |
|---------|---------|:-----:|
| Web 前端 QA | agent 在真实浏览器中测试 UI 流程 | 高 |
| 后台管理系统测试 | 登录态保持 → 操作测试 → 截图验证 | 高 |
| 浏览器自动化工具 | 持久化会话降低延迟 | 高 |
| 桌面 AI 助手 | 浏览器集成能力 | 中 |
| 后端 API 项目 | 不需要（无 UI） | 低 |

## 六、风险与边界

| 风险 | 缓解 |
|------|------|
| ngrok 暴露本地端口 | 仅转发隧道端口，限 allowlist |
| 浏览器沙箱逃逸 | 依赖操作系统安全，建议 Docker 隔离 |
| Cookie 泄露 | token HttpOnly + scoped，不存磁盘 |
| 空闲 Daemon 被人利用 | 30min 自动关闭，端口随机 |
| Windows 兼容性 | Bun Playwright pipe transport bug，需额外 Node.js |

## 七、安全红线

- **不对外暴露 `/health` 和 `/cookie-picker`**（本地独占）
- **不把 root token 放到隧道端口**
- **不在日志中打印 token**
- **不把真实浏览器 cookie 导入共享/远程环境**
- **不使用公共 ngrok 隧道处理敏感数据**
