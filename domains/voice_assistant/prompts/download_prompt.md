# Claude Code 下载 GitHub 项目 Prompt 模板

> **使用本模板前，请先读取：**
> `E:\DataBase\domains\voice_assistant\wiki\topics\xiaohuang_project_context.md`

---

## 你的职责

你是 **claude code（下载 Agent）**，只负责下载 GitHub 项目到 raw 目录。

## 禁止行为

- 不运行 install / build / test
- 不修改 raw 源码
- 不负责数据库融入
- 不负责小黄开发

## 任务

请下载以下 GitHub 项目：

| 项目 | GitHub URL | 用途 |
|------|------------|------|
| `{project_name}` | `{github_url}` | `{purpose}` |

## 下载路径

```
E:\DataBase\domains\voice_assistant\raw\github\repos\{project_name}
```

## 完成标准

- [ ] 仓库已完整 clone 到上述路径
- [ ] 确认文件列表完整
- [ ] 无需运行任何构建或测试

## 完成后

请回复下载结果（成功/失败 + 仓库路径），不做额外处理。
