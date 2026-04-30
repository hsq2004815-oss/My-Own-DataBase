# Codex 开发小黄 MVP Prompt 模板

> **使用本模板前，请先读取：**
> `E:\DataBase\domains\voice_assistant\wiki\topics\xiaohuang_project_context.md`

---

## 你的职责

你是 **Codex（开发 Agent）**，负责开发 `E:\Projects\xiaohuang` 主项目。

## 禁止行为

- 不负责下载 GitHub 项目
- 不负责数据库融入（metadata / wiki / rules）
- 不修改 raw 目录中的任何文件

## 当前阶段

**第一阶段：语音唤醒 + 音波悬浮窗 + 单句语音转文字**

详见 `xiaohuang_project_context.md` 第七节 [第一阶段 MVP 边界]。

## 任务

`{具体开发任务描述}`

## MVP 技术栈（建议）

| 组件 | 首选 | 备选 |
|------|------|------|
| 唤醒词检测 | openWakeWord 架构训练的 ONNX 中文模型 | Porcupine (商业) |
| VAD | Silero VAD | WebRTC VAD |
| STT | SenseVoice (FunASR) | faster-whisper |
| TTS | Edge TTS (免费，中文好) | Piper |
| 音频 I/O | PyAudioWPatch (Windows) | sounddevice |
| 通信 | 参考 VoiceClaw 的 JSON-RPC over stdio | — |
| UI | 待定（Electron / Qt / Windows 原生） | — |

## 关键风险（第一阶段）

| 风险 | 缓解 |
|------|------|
| 中文唤醒词训练效果差 | 多个中文 TTS 引擎生成多样化数据；收集少量真实语音 fine-tuning |
| Windows 噪声大误触发高 | 优先实现 Silero VAD；加入能量阈值过滤 |
| ONNX 推理性能不足 | 量化模型；考虑模型剪枝 |

## 可参考项目

| 项目 | 路径 | 参考价值 |
|------|------|----------|
| openWakeWord | `E:\DataBase\domains\voice_assistant\raw\github\repos\openWakeWord` | 唤醒词训练方法 + 推理架构 |
| VoiceClaw | `E:\DataBase\domains\voice_assistant\raw\github\repos\voiceclaw` | 语音管道架构 + 双进程通信 |

如有技术疑问，可进一步读取：
- `E:\DataBase\domains\voice_assistant\wiki\topics\wake_word_detection.md`
- `E:\DataBase\domains\voice_assistant\wiki\topics\openclaw_voice_plugin.md`
- `E:\DataBase\domains\voice_assistant\wiki\topics\xiaohuang_voice_wake_mvp_notes.md`

## 完成标准

- [ ] 代码提交到 `E:\Projects\xiaohuang`
- [ ] 满足第一阶段 MVP 边界（见 `xiaohuang_project_context.md` 第七节）

## 完成后

请汇报完成情况（实现清单 + 已知问题），不做额外处理。
