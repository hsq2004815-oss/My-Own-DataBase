# UI Design Curation Guide

这个知识域的目标不是收藏“漂亮网页”，而是沉淀能让大模型稳定生成更好 UI 的可检索设计证据。

## 收录优先级

1. 官方设计系统：优先收 Apple HIG、Material Design、Fluent、Carbon、Atlassian、Polaris、Primer、Ant Design。
2. 真实产品流程：收登录、定价、设置、数据表、onboarding、checkout、AI chat、dashboard 等完整页面/流程。
3. 组件级模式：收按钮、表单、表格、导航、弹窗、空状态、错误状态、toast、command menu 等状态完整的组件。
4. 灵感站案例：只收你确实想复用的布局/视觉语言，并补“适合什么/不适合什么”。

## 不建议收录

- 只有链接、没有总结的资料。
- 只有一句品牌风格描述、没有组件/布局/状态规则的资料。
- 无法溯源的截图。
- 付费或限制访问内容的原文大段复制。
- 只适合炫技但不适合业务落地的动效页面，除非明确标注使用边界。

## 单条资料应该回答的问题

- 它适合什么页面类型？
- 它解决什么 UI 问题？
- 视觉特征是什么？
- 布局规则是什么？
- 组件由哪些部分组成？
- 有哪些交互状态？
- 对代码实现有什么提示？
- 什么时候不该用？
- 证据强度如何：直接规范、截图观察、人工总结、仅链接？

## 推荐目录落点

- `raw/source_catalog`: 外部资料源清单和人工采集记录。
- `raw/screenshots`: 你自己保存的截图或截图索引。
- `processed/references`: 按 `common/schemas/ui_reference.schema.json` 清洗后的记录。
- `processed/chunks`: 面向检索的短 chunk。
- `wiki/topics`: 人类可读的专题总结。
- `registry/priority_sources.json`: 优先采集来源。

## 采集步骤

1. 选一个页面类型，例如 `data_table`。
2. 从 `registry/priority_sources.json` 选 2-3 个高质量来源。
3. 按 `common/templates/ui_reference.template.json` 填一条记录。
4. 把大段文档改写成短规则，不复制完整原文。
5. 标注 `quality.evidence_level`，避免以后模型把弱资料当强证据。
6. 生成 3-8 条检索 chunk，每条只讲一个模式或规则。
7. 更新 registry 的 `status` 或新增文件索引。

## 质量标准

高质量记录：
- 有明确页面类型和使用场景。
- 至少包含布局、组件、状态、实现提示中的三类。
- 能告诉模型“该用”和“不该用”的边界。
- 有来源 URL 和采集时间。

低质量记录：
- 只有品牌名、颜色词、形容词。
- 无法区分 landing page、dashboard、form、table 等场景。
- 没有状态规则。
- 没有证据等级。

