# Agentic Software Development Workflow — gstack 通用模式

> 来源：`garrytan/gstack` (MIT) — 分析与提炼
> 生成时间：2026-04-30
> 适用范围：任何使用 AI agent (Claude Code / Codex / opencode / Cursor) 进行软件开发的通用流程

## 一、定位：不是普通 prompt，是软件交付流水线

gstack 的本质是**用 Markdown 技能文件把 AI agent 组建成一支遵循软件开发纪律的虚拟工程团队**。它与普通 "帮我写个登录页面" prompt 的本质区别：

| 维度 | 普通 Prompt | Agentic Delivery Workflow |
|------|-----------|--------------------------|
| 流程 | 单次问答，一次性吐代码 | Think→Plan→Build→Review→Test→Ship→Reflect 七阶段闭环 |
| 质量 | 靠 prompt 措辞和模型运气 | 多层 review gate，每个阶段有停止条件 |
| 角色 | 通用助手 | 多个专业角色，各有方法论和审查清单 |
| 状态 | 无状态，每次从零开始 | 上一步产出自动喂养下一步 |
| 浏览器 | 无或纯代码推演 | 真实 Chromium QA，dom 截图验证 |
| 安全 | 无 | OWASP+STRIDE 审计，prompt injection 防御 |
| 复盘 | 无 | 周回顾 + 跨会话学习 |

当用户说"帮我做个 XXX 项目"时，Agent 应默认进入 **Think → Plan** 阶段，而不是直接开始 Build。

## 二、七阶段软件交付闭环

```
Think → Plan → Build → Review → Test → Ship → Reflect
  │       │       │        │       │      │        │
  │       │       │        │       │      │        └─ 复盘学习，沉淀规则
  │       │       │        │       │      └─ 测试→push→PR→merge→部署
  │       │       │        │       └─ 真实浏览器 QA + 安全审计
  │       │       │        └─ PR 审查 + 设计审查 + DX 审查
  │       │       └─ 正常实现
  │       └─ CEO/Eng/Design/DX 多方计划审查
  └─ 需求重定义，明确真实问题
```

### 各阶段说明

| 阶段 | 核心问题 | 输出 | 停止条件 |
|------|---------|------|---------|
| **Think** | 我们到底在解决什么问题？ | 需求重定义 | 回答完 6 个强制问题 |
| **Plan** | 怎么解决？架构合理吗？范围能不能砍？ | 架构设计 + 数据流 + 测试矩阵 | CEO/Eng/Design/DX 审查全部通过 |
| **Build** | 按计划实现 | 代码 + 测试 | 全部测试通过 |
| **Review** | 代码有没有 bug？设计符不符合？ | 审查报告 | PR review + 设计审计完成 |
| **Test** | 浏览器 QA / 安全审计 | QA 报告 + 安全报告 | 0 个 P0 问题 |
| **Ship** | 能不能安全上线？ | PR merged + 部署 + 文档更新 | CI 绿 + 金丝雀监控正常 |
| **Reflect** | 这次学到了什么？ | retro 条目 + 规则更新 | learn 命令执行完毕 |

## 三、适用项目类型

| 项目类型 | 适用阶段 | 说明 |
|---------|---------|------|
| **Web 前端项目** | Think→Plan→Build→Review→Test→Ship→Reflect | 全流程，特别是设计审查 + 浏览器 QA |
| **后端/API 项目** | Think→Plan→Build→Review→Test→Ship→Reflect | 全流程，特别是工程审查 + 安全审计 |
| **浏览器自动化项目** | Plan→Build→Test→Ship | 浏览器 QA 和 domain skills 尤其重要 |
| **AI Agent 项目** | Think→Plan→Build→Reflect | 重点在角色定义和跨模型验证 |
| **桌面助手项目** | Think→Plan→Reflect | 流程思想可启发，具体实现不同 |
| **文档/报告项目** | Think→Build→Review→Ship | 简化流程，重点在审查和发布 |

## 四、不适用场景

- 单行代码修改（用完整的 7 阶段是浪费时间）
- 纯咨询/问答（不需要交付物）
- 一次性脚本（不需要审查和复盘）
- 紧急 hotfix（缩短流程，但至少保留 Test + Ship）

## 五、Agent 调用建议

当 Agent 收到开发任务时，参考以下路由：

```
我需要理解问题 → Think 阶段 → office-hours 式需求重定义
需要设计方案 → Plan 阶段 → 架构设计 + 审查
开始写代码 → Build 阶段 → 按计划实现
代码写完了 → Review → Test → Ship → Reflect
```

**关键原则：**
1. 不要在 Think 完成前进入 Build
2. Plan 阶段必须有至少一种审查（架构/设计/范围）
3. 每次 Ship 后必须 Reflect（哪怕只记录一行）
4. Reflect 的产出必须写回数据库（让下次 Agent 能看到）

## 六、与数据库现有知识的关系

- `backend_system_design_patterns.md` — 分层架构、异步任务等与 Plan 阶段互补
- `backend_project_application_reference.md` — 项目类型匹配参考
- `persistent-browser-daemon-for-agent-qa.md` — Test 阶段的浏览器 QA 实现方案
- `backend rules (api-design, auth, security)` — Review/Test 阶段的审查标准
