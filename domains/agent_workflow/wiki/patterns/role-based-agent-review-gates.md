# Pattern: Role-Based Agent Review Gates

> 来源：`garrytan/gstack` (MIT) — 多重审查闸门机制
> 生成时间：2026-04-30
> 适用平台：Claude Code / Codex / opencode / Cursor

## 模式概述

在 AI agent 开发流程的 Plan、Review、Test、Ship 阶段插入基于角色的审查闸门，防止 agent 跳过设计直接写代码、跳过测试直接发布。

## 核心原则

**Agent 的本能是"直接写代码"，审查闸门的作用是强制它先想清楚。**

没有闸门，Agent 会：
- 不确认需求就开始实现
- 跳过边界情况处理
- 忽略安全考虑
- 生成 AI 视觉垃圾 (过度渐变、无意义动画)
- 只写代码不写测试

## 闸门类型与触发条件

### Plan 阶段闸门 (阻止 Building 开始)

| 闸门 | 触发条件 | 检查内容 | 强制？ |
|------|---------|---------|:-----:|
| **CEO Gate** | 新功能、新项目 | 范围是否最小？是否在解决正确的问题？能不能不做？ | 新项目必须 |
| **Eng Gate** | 涉及架构变更 | 数据流清晰？边界条件完整？测试策略？ | 架构变更必须 |
| **Design Gate** | 有 UI 的项目 | 设计评分 0-10，一致性检查 | Web/UI 项目必须 |
| **DX Gate** | 有 API 的项目 | API 命名合理？错误消息可理解？文档是否完整？ | API 项目必须 |

### Review 阶段闸门 (阻止 Ship 开始)

| 闸门 | 触发条件 | 检查内容 | 强制？ |
|------|---------|---------|:-----:|
| **Code Review Gate** | 任何代码提交 | bug 检查、代码风格、类型安全、完整度 | 必须 |
| **Design Review Gate** | 有 UI 变更 | 视觉对比、交互可用性、响应式 | UI 变更必须 |
| **DX Review Gate** | API/CLI 变更 | 实时 DX 审计，name-and-shame | API 变更建议 |
| **Security Gate** | 认证/支付/用户数据 | OWASP Top 10 + STRIDE | 高风险必须 |

### Test 阶段闸门 (阻止 Ship 开始)

| 闸门 | 触发条件 | 检查内容 | 强制？ |
|------|---------|---------|:-----:|
| **QA Gate** | Web 项目 | 浏览器操作流程测试、截图验证 | Web 项目建议 |
| **Security Gate** | 高风险项目 | 安全扫描、prompt injection 测试 | 高风险必须 |
| **Benchmark Gate** | 性能敏感 | 性能基准对比 | 按需 |

### Ship 阶段闸门

| 闸门 | 触发条件 | 检查内容 | 强制？ |
|------|---------|---------|:-----:|
| **Ship Gate** | 所有项目 | 测试通过？审查完成？覆盖率达标？ | 必须 |
| **Canary Gate** | 生产部署 | 部署后 console 错误、性能退化 | 生产必须 |

## 实现方式 (按平台)

### Claude Code

使用 slash commands：
```
/plan-ceo-review    → CEO Gate
/plan-eng-review    → Eng Gate
/plan-design-review → Design Gate
/review             → Code Review Gate
/cso                → Security Gate
/qa                 → QA Gate
/ship               → Ship Gate
```

### opencode / Codex / 通用 Agent

通过数据库 rules 实现：
```
1. Agent 启动项目时，系统 prompt 注入闸门规则
2. Plan 完成后，检查是否所有 required gates 都已执行
3. 未通过的闸门阻止进入 Build 阶段
4. 闸门结果记录在 database 中供后续 Agent 使用
```

### Cursor

通过 `.cursorrules` 实现：
```
- 新功能开发：必须先输出 Plan，得到用户确认后才开始写代码
- UI 变更：分析变更，识别是否需要设计审查
- API 变更：检查参数校验和错误处理是否完整
```

## 闸门跳过规则

以下情况可以跳过某些闸门：
- 单行修复 → 跳过所有 Plan gates，保留 Code Review
- 纯文档 → 跳过所有 gates
- Hotfix → 跳过 Plan/Design，保留 Code Review + Test + Ship
- 实验性代码 → 跳过所有 gates，但标记为 experimental

## 闸门失败的后果

```
Plan Gate 失败 → 回到 Think，重新定义范围
Review Gate 失败 → 回到 Build，修复问题
Test Gate 失败 → 回到 Build，修复 bug
Ship Gate 失败 → 回到 Test/Review
```

失败的闸门结果应记录到数据库，供 Reflect 阶段使用。

## 与数据库现有规则的关系

- `backend-security-checklist.md` → Security Gate 的检查标准
- `api-design-rules.md` → DX Gate 的 API 审查标准
- `error-handling-and-logging-rules.md` → Code Review Gate 的代码质量检查
- `deployment-and-env-rules.md` → Ship Gate 的部署检查
