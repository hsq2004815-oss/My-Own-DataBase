# backend_api

本地知识库 API，用于让 Claude Code、Codex、Cursor、其他本地智能体通过 HTTP 检索 `E:\DataBase` 中的知识。

## Local Database API First Protocol

My-Own-DataBase is primarily accessed through this local FastAPI service.

Default local API:

```text
http://127.0.0.1:8765
```

GitHub is not the default runtime source. GitHub is only for backup, inspection, ChatGPT structure review, and version synchronization.

When the user says "根据我的数据库", "用我的数据库", "按我的数据库规则", "调用我的数据库", "based on my database", or "use my database", the agent must call:

```http
GET http://127.0.0.1:8765/health
POST http://127.0.0.1:8765/brief
```

If the API is not reachable, tell the user the local database API is not running and suggest the startup command below. Do not silently fall back to GitHub unless the user explicitly asks.

## 启动

```powershell
cd E:\DataBase\backend_api
python -m uvicorn app.main:app --host 127.0.0.1 --port 8765 --reload
```

## 通用

- `GET /health`: 查看 UI、agent_workflow、automation 数据库和 ui_assets metadata 是否存在、reference/chunk/asset 数量。
- `GET /docs`: FastAPI 自动生成的接口测试页面。
- `GET /brief?task=...`: 输入短任务描述，自动返回相关 UI chunks、workflow chunks、asset suggestions；automation 默认关闭。
- `POST /brief`: 推荐给智能体使用，支持较长任务描述和 JSON 参数。默认返回素材建议但不返回 automation chunks；只有明确需要浏览器自动化、上传、CDP、截图或验证时才设置 `automation_limit` 大于 0。
- API 请求日志写入 `runtime/logs/api_requests.jsonl`，记录 endpoint、query/task、limit、派生 queries 和返回的 chunk/reference ids，不记录完整 chunk 正文。

## Brief 接口

POST 示例：

```powershell
$body = @{
  task = "做一个玻璃生态 AI dashboard，带入场动画、通知toast、表单弹窗、暗色霓虹卡片"
  ui_limit = 8
  workflow_limit = 2
  automation_limit = 0
  asset_limit = 10
} | ConvertTo-Json

Invoke-RestMethod "http://127.0.0.1:8765/brief" -Method Post -ContentType "application/json" -Body $body
```

推荐 payload：

UI / frontend / portfolio / landing page / dashboard / app UI:

```json
{
  "task": "<user task>",
  "ui_limit": 8,
  "workflow_limit": 2,
  "automation_limit": 0,
  "asset_limit": 10
}
```

Browser automation / RPA / upload tool:

```json
{
  "task": "<user task>",
  "ui_limit": 2,
  "workflow_limit": 4,
  "automation_limit": 8,
  "asset_limit": 0
}
```

General coding / agent workflow:

```json
{
  "task": "<user task>",
  "ui_limit": 2,
  "workflow_limit": 6,
  "automation_limit": 2,
  "asset_limit": 0
}
```

GET 示例：

```powershell
Invoke-RestMethod "http://127.0.0.1:8765/brief?task=做一个玻璃生态AI dashboard，带website reveal动效、通知toast和表单弹窗&ui_limit=8&workflow_limit=2&asset_limit=10"
```

需要自动化知识时的 GET 示例：

```powershell
Invoke-RestMethod "http://127.0.0.1:8765/brief?task=Playwright上传文件并处理iframe弹窗&ui_limit=2&workflow_limit=4&automation_limit=8&asset_limit=0"
```

返回内容：`brief`、`ui_queries`、`workflow_queries`、`automation_queries`、`asset_queries`、`ui_chunks`、`workflow_chunks`、`automation_chunks`、`asset_suggestions`、`guidance`。

Ranking 规则：优先保留每个 query 的高分 chunk，再按分数补满；implementation/parameters、layout、interaction、accessibility、高证据等级、prompt_tags 命中会被加权。

`asset_suggestions` 会返回素材 id、类型、授权/使用策略、路径和简短摘要。当前素材多数是 `inspiration_only` 或 `review_required`：前者只能做视觉参考，后者直接用于项目之前需要先看 license。

## UI 设计接口

- `GET /ui/search?q=liquid%20glass&limit=5`: 检索 UI 知识 chunks。
- `GET /ui/search?q=玻璃生态&limit=5`: 中文同义词会归一化到英文检索词。
- `GET /ui/search?q=暗色玻璃&limit=5`: 命中 dark neon glass 参数。
- `GET /ui/search?q=入场动画&limit=5`: 命中 website reveal motion 参数。
- `GET /ui/references`: 列出 UI reference 摘要。
- `GET /ui/reference/{record_id}`: 获取某条完整 UI reference JSON。

## Agent Workflow 接口

- `GET /workflow/search?q=api%20first&limit=5`: 检索智能体工作流 chunks。
- `GET /workflow/references`: 列出工作流 reference 摘要。
- `GET /workflow/reference/{record_id}`: 获取某条完整工作流 reference JSON。

## UI Assets 接口

- `GET /assets/search?q=dynamic%20background&limit=8`: 检索素材 metadata，适合找动态背景、界面截图、字体、图标库、UI kit。
- `GET /assets/search?q=icon%20library&asset_type=asset_collection&limit=5`: 只找集合级素材。
- `GET /assets/reference/{asset_id}`: 获取某条完整素材 metadata。

## Automation 接口

- `GET /automation/search?q=file%20upload&limit=5`: 检索自动化知识 chunks，API 会对候选结果二次 ranking，减少泛相关结果排在前面。
- `GET /automation/search?q=chrome%20cdp&limit=5`: 命中连接现有 Chrome/Edge 登录态、CDP 远程调试相关规范。
- `GET /automation/search?q=overlay%20modal%20iframe&limit=5`: 命中弹窗、遮罩、下拉、iframe 处理规范。
- `GET /automation/references`: 列出自动化 reference 摘要。
- `GET /automation/reference/{record_id}`: 获取某条完整自动化 reference JSON。

## 给其他智能体的调用约定

优先调用本机 `POST /brief` 获取任务相关 UI + workflow chunks 和 asset suggestions。普通前端设计任务保持 `automation_limit=0`；只有浏览器自动化、上传、CDP、截图或验证任务才提高 `automation_limit`。如果需要更精确，再补充调用 `/ui/search`、`/workflow/search`、`/assets/search` 或 `/automation/search`。不要一次性读取全部知识，也不要默认去 GitHub 读取仓库，否则上下文会被低相关内容污染。
