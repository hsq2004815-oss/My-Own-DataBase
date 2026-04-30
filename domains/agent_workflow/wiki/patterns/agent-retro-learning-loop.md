# Pattern: Agent Retro Learning Loop

> 来源：`garrytan/gstack` (MIT) — retro + learn 机制
> 生成时间：2026-04-30
> 适用平台：所有 AI agent 平台

## 模式概述

每次开发完成后的复盘机制，将失败经验、踩坑记录、项目约束沉淀为数据库中的可复用知识，让后续 Agent 不再从零开始。

## 核心问题

**Agent 的默认行为：每次新会话都从零开始，相同的错误反复犯。**

没有 Retro Loop，Agent 会：
- 在同一个 Windows 路径问题上反复失败
- 在同一个 API 设计缺陷上反复踩坑
- 不知道上次开发留下了哪些约束
- 无法从历史错误中学习

## Retro Loop 流程

```
Ship 完成后
    ↓
1. 收集——这次开发过程中发生了什么？
    ↓
2. 分析——哪些是成功的？哪些是失败的？
    ↓
3. 提炼——哪些经验值得保存？
    ↓
4. 写入——按规则/checklist/template/pattern 分别写入数据库
    ↓
5. 验证——下次 Agent 启动时能否读取到？
```

## 复盘问题清单

### 个人复盘 (单个项目)

1. 这次做对了什么？下次应该继续做什么？
2. 这次做错了什么？下次应该避免什么？
3. 有什么意外的发现？(工具、方法、边界情况)
4. 有什么约束需要记录下来？(平台限制、权限、依赖)
5. 有什么规则应该更新？(安全规则、编码规则)
6. 下次类似项目应该怎么开始？

### 全局复盘 (跨项目)

1. 最近 N 个项目有没有反复出现的错误模式？
2. 哪些规则没有被 agent 遵守？为什么？
3. 数据库中的知识是否能有效指导 agent？
4. 哪些检查清单需要更新？

## 写入数据库的格式

### 作为 Rule 写入

```
适合：通用编码规则、安全规则、平台限制
位置：domains/<domain>/rules/<rule-name>.md
示例：Windows 上不能用 /tmp，必须用 %TEMP% 或 $TMP
```

### 作为 Checklist 写入

```
适合：开发前/发布前检查清单
位置：domains/<domain>/wiki/checklists/<checklist-name>.md
示例：Windows 项目开发前检查清单
```

### 作为 Pattern 写入

```
适合：可复用的设计模式、架构模式
位置：domains/<domain>/wiki/patterns/<pattern-name>.md
示例：异步任务幂等设计模式
```

### 作为 Template 写入

```
适合：项目启动模板、PR 模板、handoff 模板
位置：domains/<domain>/wiki/templates/<template-name>.md
示例：Agent 开发项目 handoff 模板
```

## Agent 调用时机

| 时机 | 触发条件 | 操作 |
|------|---------|------|
| 每次 Ship 后 | 自动 | 执行个人 Retro |
| 每周 | 定时 | 执行全局 Retro |
| 遇到失败后 | 手动或自动 | 记录失败原因和上下文 |
| 新 Agent 启动时 | 自动 | 读取最近 N 条 Retro 记录 |

## 阻止 Agent 从零开始的机制

1. **AGENT.md / CLAUDE.md** 中写入最新约束和规则
2. **rules/** 文件被 agent 自动包含在上下文中
3. **/brief** API 返回相关 chunks 时自动包含 recent retro 条目
4. **checklists** 在开发前被强制读取
5. **patterns** 在遇到相似场景时被检索命中

## 示例 Retro 条目

```markdown
## Retro: gstack Integration — 2026-04-30

### 做对了
- 先读了 schema 和模板再生成 references，格式一次对齐
- 把 gstack 的 23 角色抽象成通用质量闸门，而非照搬角色名

### 做错了
- taxonomy 更新应该在生成 references 之前做

### 意外发现
- agent_workflow scripts 的 make_chunks.py 支持 --references 参数直接输入

### 约束记录
- agent_workflow_reference.schema 的 workflow_type 必须匹配 taxonomy
- 批量重建 SQLite 时需要先删除旧索引
```

## 与数据库的关系

- **写入目标**：`domains/<domain>/rules/`, `wiki/`, `processed/`
- **读取入口**：`/brief` API, `search_workflow.py`, `AGENT.md`
- **索引更新**：retro 写入后应重建对应 domain 的 chunks 和 SQLite 索引
