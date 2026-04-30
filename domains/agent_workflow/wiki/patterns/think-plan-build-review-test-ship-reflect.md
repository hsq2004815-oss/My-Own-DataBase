# Pattern: Think → Plan → Build → Review → Test → Ship → Reflect

> 来源：`garrytan/gstack` (MIT) — 7 阶段软件交付工作流
> 生成时间：2026-04-30
> 适用平台：Claude Code / Codex / opencode / Cursor / OpenClaw

## 模式概述

7 阶段软件开发闭环。每个阶段有明确的输入、输出、停止条件和验证标准。上一步产出自动喂养下一步。

## 适用场景

- 新功能开发（完整流程）
- 大重构（需要 Plan + Review）
- Web 项目（需要浏览器 QA）
- 多人协作项目（需要审查闸门）

## 不适用场景

- 单行代码修改
- 纯咨询问题
- 紧急 hotfix（压缩为 Build → Test → Ship）

## 各阶段详解

### Stage 1: Think — 需求重定义

```
输入：用户提出的任务或问题
输出：明确的问题陈述 + 约束 + 成功标准
停止条件：6 个强制问题全部回答完成
验证：用户确认理解正确
```

**强制问题：**
1. 我们到底在解决什么问题？
2. 谁是这个问题的用户？
3. 成功的标准是什么？
4. 有什么已知的约束？
5. 现有的方案是什么？为什么不够？
6. 最简单能验证的 MVP 是什么？

### Stage 2: Plan — 方案设计

```
输入：Think 输出的问题陈述
输出：架构设计 + 数据流图 + 测试矩阵 + 技术选型
停止条件：所需审查全部通过
验证：审查者签字
```

**审查选项（按需选择）：**
- CEO 审查：范围是否最小？是否 over-engineering？
- 工程审查：架构是否合理？数据流是否清晰？
- 设计审查：设计维度评分 (0-10)
- DX 审查：API 命名、错误消息、文档完整性

### Stage 3: Build — 实现

```
输入：Plan 输出的架构设计
输出：代码 + 测试 + 文档
停止条件：全部测试通过
验证：CI 或本地测试全部绿
```

**行为准则：**
- Boil the Lake：做完整的事，不跳过测试和边界情况
- Search Before Building：实现前确认没有现成方案
- WIP checkpoint：定期提交，方便回退

### Stage 4: Review — 审查

```
输入：Build 输出的代码
输出：审查报告 + 修复建议
停止条件：审查通过或修复完成
验证：所有标注的问题已解决
```

**审查层：**
- 代码审查：找 bug、标记不完整
- 设计审查：视觉还原度
- DX 审查：API 可用性
- 安全审查：(高风险项目) OWASP + STRIDE
- 跨模型审查：(可选) 另一个模型独立审查

### Stage 5: Test — 测试

```
输入：Review 通过的代码
输出：测试报告 + 截图/日志
停止条件：0 个 P0 问题
验证：测试报告可追溯
```

**测试方式：**
- 浏览器 QA：真实 Chromium，操作流程验证
- 回归测试：自动生成
- 安全扫描：(如适用) prompt injection、XSS、CSRF
- 性能基准：(如适用)

### Stage 6: Ship — 发布

```
输入：Test 通过的代码
输出：合并的 PR + 部署 + 更新的文档
停止条件：CI 绿 + 部署验证通过
验证：金丝雀监控正常
```

**步骤：**
1. 同步 main 分支
2. 运行完整测试套件
3. Push + 打开 PR
4. Merge (CI 通过后)
5. 部署
6. 金丝雀监控 (console 错误、性能退化)
7. 文档自动更新

### Stage 7: Reflect — 复盘

```
输入：Ship 后的项目状态
输出：retro 条目 + 更新的规则/checklist/template
停止条件：learn 记录已写入
验证：下次 Agent 启动时能读取到
```

**记录内容：**
- 这次做对了什么？
- 这次做错了什么？
- 有什么意外的发现？
- 下次应该怎么改进？
- 有什么新的约束需要记住？

## Agent 调用指南

### Claude Code 调用方式

```
/project-think  → "让我们先重定义问题..."
/plan           → "设计架构方案，至少包含工程审查"
/build          → "按计划实现"
/review         → "审查代码"
/test           → "浏览器 QA"
/ship           → "发布"
/retro          → "记录复盘"
```

### opencode 调用方式

```
1. 读取 agent_workflow/wiki/patterns 下的本文件
2. 按阶段执行，每阶段询问用户是否进入下一阶段
3. Reflect 阶段写入 domains/agent_workflow/processed/retro/
```

### 通用 CLI Agent 调用方式

```
Task: "实现 XXX"
→ Agent 应先问 Think 阶段的问题
→ 再输出 Plan 阶段的方案
→ 得到确认后才 Build
→ 完成后主动 Review
→ 主动提议 Test
→ Ship 前确认
→ 完成后记录 Reflect
```
