# gstack Integration Report

**集成日期：** 2026-04-30
**集成人：** 知识集成员 (Claude Code)
**项目来源：** https://github.com/garrytan/gstack (MIT, v1.21.1.0)
**集成目标域：** agent_workflow (主), automation (副), backend (副)

---

## 集成目标

将 gstack 的 agentic software delivery 方法论沉淀为 My-Own-DataBase 的通用 AI 工程知识。不照搬 gstack 的 SKILL.md 或代码，而是提炼可跨项目、跨平台复用的 workflow 模式、质量闸门设计、浏览器 QA 架构和复盘学习循环。

## 输入材料

| 文件 | 用途 |
|------|------|
| `gstack-handoff.md` | 收录员交接文档，了解项目定位和集成建议 |
| `gstack-raw-analysis-report.md` | 详细分析报告，了解 7 阶段流程和 23 角色设计 |
| `gstack.metadata.json` | 结构化元数据 |
| `gstack.chunks.json` | 预处理 chunks |
| `gstack/ARCHITECTURE.md` | 浏览器 daemon 架构和双监听器安全设计 |
| `gstack/ETHOS.md` | Builder 哲学：Boil the Lake / Search Before Building / User Sovereignty |
| `AGENT.md` / `AGENTS.md` / `README.md` (数据库) | 数据库规范和 agent 调用规则 |
| `agent_workflow_reference.schema.json` | Reference 格式约束 |
| `automation_reference.schema.json` | Automation reference 格式约束 |
| 现有 taxonomy JSON | 对齐 workflow_type 和 automation_type |

## 新增文件

### agent_workflow 域

| 文件 | 类型 |
|------|------|
| `wiki/topics/gstack-agentic-development-workflow.md` | 通用 topic |
| `wiki/topics/virtual-engineering-team-skills.md` | 通用 topic |
| `wiki/patterns/think-plan-build-review-test-ship-reflect.md` | 通用 pattern |
| `wiki/patterns/role-based-agent-review-gates.md` | 通用 pattern |
| `wiki/patterns/agent-retro-learning-loop.md` | 通用 pattern |
| `wiki/checklists/agentic-development-preflight-checklist.md` | checklist |
| `wiki/templates/agentic-development-handoff-template.md` | template |
| `processed/references/workflow-gstack-agentic-development-workflow.json` | reference |
| `processed/references/workflow-virtual-engineering-team-skills.json` | reference |
| `processed/references/pattern-think-plan-build-review-test-ship-reflect.json` | reference |
| `processed/references/pattern-role-based-agent-review-gates.json` | reference |
| `processed/references/pattern-agent-retro-learning-loop.json` | reference |
| `processed/chunks/*.json` (5 new) | retrieval chunks |
| `output/reports/gstack-integration-report.md` | 本报告 |

### automation 域

| 文件 | 类型 |
|------|------|
| `wiki/topics/persistent-browser-daemon-for-agent-qa.md` | topic |
| `wiki/patterns/browser-qa-with-persistent-session.md` | pattern |
| `processed/references/automation-persistent-browser-daemon-agent-qa.json` | reference |
| `processed/references/automation-browser-qa-persistent-session.json` | reference |

### backend 域

| 文件 | 类型 |
|------|------|
| `wiki/topics/agentic-software-delivery-pipeline.md` | topic |
| `processed/references/backend-agentic-software-delivery-pipeline.json` | reference |

## 修改文件

| 文件 | 修改内容 |
|------|---------|
| `common/taxonomy/agent_workflow_types.json` | 新增 4 个 workflow_type：agentic_software_delivery, virtual_engineering_team, review_gate, retro_learning_loop |
| `common/taxonomy/automation_types.json` | 新增 2 个 automation_type：persistent_browser_daemon, browser_qa_session |
| `domains/agent_workflow/processed/chunks/all_agent_workflow_chunks.json` | 重建，66 chunks (原 10+ 新 5 records) |
| `runtime/db/sqlite/agent_workflow/agent_workflow_references.db` | 重建 SQLite/FTS5 索引 |

## 新增 references

| record_id | domain | type |
|-----------|--------|------|
| `workflow-gstack-agentic-development-workflow` | agent_workflow | agentic_software_delivery |
| `workflow-virtual-engineering-team-skills` | agent_workflow | virtual_engineering_team |
| `pattern-think-plan-build-review-test-ship-reflect` | agent_workflow | agentic_software_delivery |
| `pattern-role-based-agent-review-gates` | agent_workflow | review_gate |
| `pattern-agent-retro-learning-loop` | agent_workflow | retro_learning_loop |
| `automation-persistent-browser-daemon-agent-qa` | automation | persistent_browser_daemon |
| `automation-browser-qa-persistent-session` | automation | browser_qa_session |
| `backend-agentic-software-delivery-pipeline` | backend | agentic_software_delivery |

## 新增 / 更新知识点

### 通用 Topic

1. **Agentic Software Development Workflow** — 7 阶段软件交付闭环，适用于任何 AI agent 开发流程
2. **Virtual Engineering Team Skills** — 多角色 agent 团队设计方法论，角色=质量闸门，不是人格模拟
3. **Persistent Browser Daemon for Agent QA** — 持久化浏览器 daemon 架构，含安全模型
4. **Agentic Software Delivery Pipeline (Backend)** — 后端项目适配版

### 通用 Pattern

1. **Think→Plan→Build→Review→Test→Ship→Reflect** — 7 阶段开发模式
2. **Role-Based Agent Review Gates** — 多阶段审查闸门
3. **Agent Retro Learning Loop** — 跨会话学习循环
4. **Browser QA with Persistent Session** — 持久化浏览器 QA 模式

### Checklist

1. **Agentic Development Preflight Checklist** — Agent 开发前必检清单

### Template

1. **Agentic Development Handoff Template** — Agent 交接模板

## 检索测试

| 查询 | 命中 record_id | 状态 |
|------|---------------|:--:|
| `gstack agentic software delivery` | workflow-gstack-agentic-development-workflow, pattern-think-plan-build-review-test-ship-reflect | ✅ |
| `Think Plan Build Review Test Ship Reflect` | pattern-think-plan-build-review-test-ship-reflect | ✅ |
| `virtual engineering team` | workflow-virtual-engineering-team-skills | ✅ |
| `retro learning loop` | pattern-agent-retro-learning-loop | ✅ |
| `review gate quality checkpoint` | workflow-virtual-engineering-team-skills (steps) | ✅ |
| 中文查询 | FTS5 tokenizer 依赖英文分词，中文查询需通过 `/brief` API 的 BM25 混合检索或后续优化 | ⚠️ |

## 对未来 agent 的影响

以后 Codex / Claude Code / opencode 做项目时，可通过以下方式调用 gstack 知识：

### 通过 `/brief` API

```json
{
  "task": "开发一个 Web 后台项目",
  "workflow_limit": 8
}
```

将返回 gstack 相关的 7 阶段 workflow、review gate 和 retro loop 知识。

### 通过 search_workflow.py

```bash
python scripts/agent_workflow/search_workflow.py "agentic software delivery"
python scripts/agent_workflow/search_workflow.py "review gate"
python scripts/agent_workflow/search_workflow.py "retro learning"
```

### Agent 默认行为改变

- Agent 接收到开发任务时，应先执行 **Think → Plan**（不是直接写代码）
- 新项目启动前读取 `agentic-development-preflight-checklist.md`
- 开发完成后自动执行 Retro，写入数据库
- 项目交接时使用 `agentic-development-handoff-template.md`

## 可选应用案例

### 小黄桌面 AI 助手
- 流程思想可启发：7 阶段可适配为语音驱动的开发流程
- retro/learn 可用于语音交互的持续优化
- 角色分工体系不完全适用于语音助手（小黄是用户交互 agent，不是工程开发 agent）

### Web 后台项目
- 完整 7 阶段：Plan 阶段设计审查 + Test 阶段浏览器 QA
- QA gate 使用持久化浏览器，测试后台操作流程

### 浏览器自动化项目
- 持久化浏览器 daemon 架构直接参考
- 安全模型（双监听器）可迁移

### 后端 API 项目
- 使用 backend 适配版 pipeline
- API Design Gate + Security Gate + DX Gate

### AI Agent 项目
- 最直接的迁移价值
- 虚拟工程团队 + 跨模型审查 + retro 学习

## 未完成或风险

| 事项 | 状态 | 说明 |
|------|------|------|
| 中文 FTS5 检索 | ⚠️ 受限 | 当前 FTS5 tokenizer 对中文分词支持有限，需后续优化 |
| automation/backend 的 chunks 和索引 | ⚠️ 未建 | 本次仅重建了 agent_workflow 索引。automation 和 backend 的 chunks 管线需后续运行 |
| ngrok 安全 | ⚠️ 风险 | 远程浏览器访问涉及公网暴露，未在本地测试 |
| Windows 兼容性 | ⚠️ 已知 | gstack 的 Bun Playwright pipe transport 在 Windows 上有已知 bug |
| 跨模型验证成本 | ⚠️ 成本 | Claude + Codex 双重审查需要两个 API key，成本加倍 |

## 下一步建议

1. **重建 automation/backend 索引**：运行对应 scripts 生成 chunks 和 SQLite 索引
2. **优化中文检索**：考虑 jieba 分词 + FTS5 自定义 tokenizer，或使用 BM25 混合检索
3. **把 workflow 做成 Codex/opencode skills**：参考 gstack 的模板驱动 skill 生成方式
4. **增加 workflow selector**：`/brief` API 增加 workflow_type 过滤参数
5. **浏览器 QA 与 automation domain 打通**：把 browser daemon 模式与现有 Playwright rules 整合
6. **定期 retro**：在 AGENT.md 中增加定期 retro 触发机制

---

*本报告由知识集成员生成，记录了 gstack 项目从 raw 收录到通用知识融入的全过程。*
