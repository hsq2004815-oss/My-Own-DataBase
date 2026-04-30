# OpenClaw Voice Plugin (VoiceClaw)

## VoiceClaw 解决什么问题？

VoiceClaw 是 OpenClaw 平台的标准语音助手插件，它将唤醒词检测、语音识别(STT)、语音合成(TTS)整合为一个可插拔的插件，解决以下问题：

1. **为 OpenClaw 添加语音交互能力**：让 OpenClaw 用户可以通过语音而非文字与 Agent 交互。
2. **插件化语音入口**：作为标准 OpenClaw 插件，通过 `openclaw.plugin.json` 清单定义，支持通过配置文件灵活切换 STT/TTS 引擎。
3. **双进程异构架构**：Node.js 负责插件逻辑和 Agent 通信，Python 负责音频采集和 ML 推理，通过 JSON-RPC over stdio 桥接。
4. **完整的语音交互管道**：VAD → 唤醒词 → 录音 → STT → Agent 处理 → TTS 播报。

## 核心技术架构

```
┌──────────────────────────────────────────────────────┐
│                    OpenClaw                           │
│  ┌─────────────────────────────────────────────────┐ │
│  │  VoiceClaw Plugin (Node.js / TypeScript)         │ │
│  │  ├── index.ts      (entry, register everything)  │ │
│  │  ├── service.ts    (background mic service)       │ │
│  │  ├── bridge.ts     (Python child_process IPC)     │ │
│  │  ├── commands.ts   (/voiceclaw start|stop|status) │ │
│  │  ├── gateway-methods.ts (RPC config/status)       │ │
│  │  └── tools.ts      (voice_speak agent tool)       │ │
│  └──────────┬──────────────────────────────────────┘ │
│             │ JSON-RPC over stdio                     │
│  ┌──────────▼──────────────────────────────────────┐ │
│  │  Python (audio/ml)                               │ │
│  │  ├── vad.py       (Silero VAD)                    │ │
│  │  ├── stt.py       (SenseVoice/Whisper)            │ │
│  │  ├── tts.py       (Edge TTS/Piper/say)            │ │
│  │  ├── audio.py     (PyAudio mic/playback)          │ │
│  │  └── server.py    (JSON-RPC server entry)         │ │
│  └──────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────┘
```

## 事件流（端到端）

```
用户说 "Hey Claw"
  → AudioManager 持续监听
  → Silero VAD 检测到语音 → 录制语音段
  → STT 转写 → 匹配唤醒词
  → emit("wake_word") → JSON-RPC → Node.js
  → 继续录制 → STT 转写用户指令
  → emit("utterance", {text}) → Agent 处理
  → Agent 调用 voice_speak 工具 → JSON-RPC → Python
  → TTS 引擎 → 扬声器播放
```

## 配置灵活性

| 组件 | 可选引擎 | 默认值 |
|------|----------|--------|
| STT | sensevoice, faster-whisper, whisper | sensevoice |
| TTS | edge-tts, piper, say | edge-tts |
| VAD | Silero (唯一) | threshold=0.5 |
| 唤醒词 | 可配置任意文本 | "미르야" (韩语) |

## 对小黄项目的意义

### 高度可借鉴的架构模式

VoiceClaw 的架构设计是小黄语音插件最直接的参考：

1. **双进程模式**：Node.js 处理插件逻辑和 Agent 通信 → Python 处理音频和 ML。这种分离让 Node.js 生态和 Python ML 生态各司其职。
2. **JSON-RPC over stdio**：零依赖的进程间通信，无需 HTTP 端口管理，比 WebSocket/HTTP 更简单可靠。
3. **插件声明式配置**：通过 `openclaw.plugin.json` 和 `openclaw.yaml` 统一管理配置，支持热更新。
4. **事件驱动架构**：wake_word → speech_start → utterance → agent_response → tts.speak，事件链清晰。

### 不适合直接使用的部分

| 内容 | 原因 |
|------|------|
| 整个插件代码 | 强依赖 OpenClaw 平台 API，独立使用需大量改写 |
| 唤醒词检测方案 | 是基于 STT 文本匹配而非专用唤醒词模型，延迟高、资源消耗大，不适合持续监听 |
| 韩语默认配置 | 需全部替换为中文配置 |

## Windows 可行性

- Node.js/TypeScript 部分完全跨平台
- Python 依赖在 Windows 上基本可用（PyTorch 官方支持，Edge TTS 纯 Python）
- PyAudio 需用 PyAudioWPatch
- Piper TTS 在 Windows 上的二进制可用性需单独验证

## 与 openWakeWord 的关系

| 维度 | openWakeWord | VoiceClaw |
|------|-------------|-----------|
| 定位 | 底层唤醒词检测库 | 上层 OpenClaw 语音插件 |
| 关注点 | 唤醒词模型训练与推理 | 完整语音交互管道 |
| 技术栈 | 纯 Python | TypeScript + Python (子进程) |
| 唤醒词方案 | 专用 melspectrogram + embedding + classifier | 基于 STT 文本匹配 |
| 对小黄的角色 | 提供唤醒词检测的底层能力 | 提供语音插件的上层架构 |

**互补关系**：理想情况下，小黄应该用 openWakeWord 的架构训练中文唤醒词模型（底层），然后参考 VoiceClaw 的插件架构设计语音交互管道（上层）。

## 在第一阶段 MVP 中的建议

1. **参考架构**：重点学习其 Node.js+Python 双进程模式、JSON-RPC 通信、事件流设计。
2. **不直接集成**：因为 VoiceClaw 与 OpenClaw 紧耦合，小黄如果不是基于 OpenClaw 构建，直接集成成本高。
3. **唤醒词替换**：小黄应采用 openWakeWord 式的专用唤醒词检测，而非 VoiceClaw 的 STT 文本匹配方案（后者延迟高、持续监听资源消耗大）。

## 相关资源

- 仓库：https://github.com/muin-company/voiceclaw
- 作者：MUIN Company (https://muin.company)
- 许可：MIT
- 当前版本：v0.1.0
