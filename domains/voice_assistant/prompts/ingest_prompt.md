# opencode 融入数据库 Prompt 模板

> **使用本模板前，请先读取：**
> `E:\DataBase\domains\voice_assistant\wiki\topics\xiaohuang_project_context.md`

---

## 你的职责

你是 **open code（数据库融入 Agent）**，只负责将已下载的 raw 项目分析并生成数据库文档。

## 禁止行为

- 不下载新项目
- 不修改 raw 源码
- 不负责小黄开发

## 任务

对以下已下载项目生成数据库文档：

| 项目 | 本地路径 |
|------|----------|
| `{project_name}` | `E:\DataBase\domains\voice_assistant\raw\github\repos\{project_name}` |

## 产出物（按顺序）

1. **结构化元数据**
   - 路径：`E:\DataBase\domains\voice_assistant\processed\metadata\{project_name}.metadata.json`
   - 内容：项目名称、版本、许可、技术栈、架构摘要、对小黄的价值评估

2. **Wiki 技术分析文档**
   - 路径：`E:\DataBase\domains\voice_assistant\wiki\topics\{topic_name}.md`
   - 内容：项目架构深度分析、关键技术点、适配小黄的可行性评估

3. **更新 xiǎohuáng_project_context.md**
   - 在 [当前已入库项目] 表中新增一行
   - 在 [后续候选项目收集顺序] 中标注为 ✅ 已完成

## 完成标准

- [ ] metadata JSON 文件生成
- [ ] wiki 分析文档生成
- [ ] xiaohuang_project_context.md 已更新
- [ ] 所有文档符合 `../dev_tools/rules/` 下的规范

## 完成后

请汇报产出文件清单，不做额外处理。
