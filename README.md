# My Own DataBase

这是一个面向本地 AI 工作流的个人知识工程与检索底座。它把 UI 设计参考、素材资产、智能体工作流规范和浏览器自动化经验整理成可检索的本地知识库，并提供 FastAPI 与 CLI 给 Codex、Claude Code、Cursor 或其他本地智能体调用。

## 当前快照

- UI Design: 38 references / 228 chunks
- Agent Workflow: 5 references / 33 chunks
- Automation: 11 references / 77 chunks
- UI Assets: 255 metadata records
  - 13 motion references
  - 46 screenshot references
  - 184 fonts
  - 12 asset collections
- 可用 SQLite 索引位于 `runtime/db/sqlite/*`

Git 仓库保留可复用的知识、脚本、配置、素材 metadata、原始参考素材和 SQLite 索引；会忽略 Python 缓存、运行日志、临时 brief artifacts 等可再生成文件。

## 目录结构

```text
.
├─ AGENT.md                  # 给智能体的工作规则
├─ AGENTS.md                 # Codex/agent 入口，指向 AGENT.md
├─ AGENT_USAGE.md            # 简短调用说明
├─ backend_api/              # 本地 FastAPI 检索服务
├─ common/                   # schemas、templates、taxonomy、config
├─ domains/
│  ├─ ui_design/             # UI 设计规则、组件模式、视觉风格、实现提示
│  ├─ ui_assets/             # 素材 metadata 与本地参考素材
│  ├─ agent_workflow/        # 智能体检索、交接、失败恢复流程
│  └─ automation/            # Playwright、CDP、上传、iframe、弹窗等自动化经验
├─ runtime/
│  └─ db/sqlite/             # 可直接使用的 SQLite 检索索引
├─ scripts/
│  ├─ brief.py               # 调用 /brief 的智能体友好 CLI
│  ├─ ui_design/             # UI reference 标准化、分块、建库、搜索
│  ├─ ui_assets/             # 素材导入与 metadata 生成
│  ├─ agent_workflow/        # 工作流 reference 管线
│  └─ automation/            # 自动化 reference 管线
└─ TASK_MEMORY.md            # 维护记录和下一步注意事项
```

## 数据流

```text
raw -> processed -> wiki -> output -> runtime/db/sqlite
```

- `raw`: 原始资料和素材入口。
- `processed`: 清洗后的 reference、chunks、metadata。
- `wiki`: 人类可读专题总结。
- `output`: 任务产物或导出结果。
- `runtime/db/sqlite`: 智能体和 API 实际检索用的索引。

## 快速开始

安装 API 依赖：

```powershell
cd E:\DataBase\backend_api
python -m pip install -r requirements.txt
```

启动本地检索 API：

```powershell
cd E:\DataBase\backend_api
python -m uvicorn app.main:app --host 127.0.0.1 --port 8765 --reload
```

检查服务：

```powershell
Invoke-RestMethod "http://127.0.0.1:8765/health"
```

## 推荐给智能体的入口

普通 UI/前端/设计任务优先调用本机 API 或 brief CLI，不要整库读取，也不要默认去 GitHub 读取仓库：

```powershell
python E:\DataBase\scripts\brief.py "做一个玻璃生态 AI dashboard，带动态背景和字体" --ui 8 --workflow 2 --automation 0 --assets 10
```

当用户说“根据我的数据库”“用我的数据库”“按我的数据库规则”“调用我的数据库”“based on my database” 或 “use my database” 时，本机 agent 应先调用 `GET http://127.0.0.1:8765/health`，再调用 `POST http://127.0.0.1:8765/brief`。GitHub 只用于远程备份、人工查看、ChatGPT 检查结构和版本同步。

普通 Web UI、landing page、SaaS 官网、portfolio 和产品页任务会优先检索 `ui_design` 的高级审美总规则层，包括 premium Web UI、Liquid Glass、cinematic video hero、typography/layout、motion reveal 和 landing page section patterns。品牌 `design-*.md` 文件只作为补充参考，不覆盖这些默认规则。

如果 UI / frontend / portfolio / landing page 任务同时要求“高级、动效、动画、小动画、motion、Lottie、视觉效果、交互高级”，agent 不能只调用 `/brief`，还必须追加 `/assets/search` 检索小动画、微交互、loading animation、hover motion、button animation、animated icon、lottie animation、motion reference、hero background motion，并在最终输出里说明素材 id、usage_policy、是否直接使用和 CSS/SVG/Canvas/Lottie/video 实现方式。

需要浏览器自动化、上传、CDP、截图或验证时再打开 automation：

```powershell
python E:\DataBase\scripts\brief.py "Playwright 上传文件并处理 iframe 弹窗" --ui 2 --workflow 4 --automation 8 --assets 0
```

也可以直接调 HTTP：

```http
POST http://127.0.0.1:8765/brief
```

```json
{
  "task": "任务描述",
  "ui_limit": 8,
  "workflow_limit": 2,
  "automation_limit": 0,
  "asset_limit": 10
}
```

## API 概览

- `GET /health`: 数据库和素材 metadata 状态。
- `GET /docs`: FastAPI 自动文档。
- `GET /brief` / `POST /brief`: 面向智能体的综合检索。
- `GET /ui/search`: 检索 UI 设计 chunks。
- `GET /workflow/search`: 检索智能体工作流 chunks。
- `GET /assets/search`: 检索素材 metadata。
- `GET /automation/search`: 检索自动化 chunks。
- `GET /ui/reference/{record_id}`: 获取完整 UI reference。
- `GET /workflow/reference/{record_id}`: 获取完整 workflow reference。
- `GET /assets/reference/{asset_id}`: 获取完整 asset metadata。
- `GET /automation/reference/{record_id}`: 获取完整 automation reference。

## 素材使用策略

`ui_assets` 中的素材 metadata 包含 `usage_policy`：

- `inspiration_only`: 只能做视觉参考，不要直接复制到项目中。
- `review_required`: 直接使用前必须先检查 license、来源和授权状态。
- 只有未来明确标记为 `direct_use` 的素材，才适合直接进入产品代码或交付物。

## 维护约定

1. 原始资料进入对应 domain 的 `raw`。
2. 标准化后的 JSON/reference/chunks 进入 `processed`。
3. 人类可读总结进入 `wiki`。
4. 检索索引统一重建到 `runtime/db/sqlite/*`。
5. 普通前端任务保持 `automation_limit=0`。
6. 不提交 `__pycache__`、`.pyc`、运行日志和临时 brief artifacts。
7. 更新检索逻辑后至少运行：

```powershell
python -m py_compile E:\DataBase\backend_api\app\main.py E:\DataBase\scripts\brief.py
```

## 给后续维护者

更多面向智能体的细则见 `AGENT.md` 和 `AGENT_USAGE.md`。历史维护上下文和已知陷阱见 `TASK_MEMORY.md`。
