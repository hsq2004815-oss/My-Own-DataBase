# Voice Assistant Domain

语音助手领域数据库 —— 小黄（XiaoHuang）语音交互能力的知识沉淀和项目参考。

## 目录结构

```
voice_assistant/
├── raw/                        # 原始下载的开源项目 (只读, 不修改)
│   └── github/
│       └── repos/
│           ├── openWakeWord/    # 开源唤醒词检测库
│           ├── voiceclaw/       # OpenClaw 语音助手插件
│           ├── Wake-Word/       # Electron 唤醒词桌面应用 (Picovoice)
│           ├── FunASR/          # 阿里端到端语音识别工具包
│           ├── faster-whisper/  # CTranslate2 加速 Whisper 推理
│           └── edge-tts/        # 微软 Edge 在线 TTS Python 模块
├── processed/                   # 结构化元数据
│   └── metadata/
│       ├── openWakeWord.metadata.json
│       ├── voiceclaw.metadata.json
│       ├── Wake-Word.metadata.json
│       ├── FunASR.metadata.json
│       ├── faster-whisper.metadata.json
│       └── edge-tts.metadata.json
├── wiki/                        # 领域知识文档
│   └── topics/
│       ├── wake_word_detection.md
│       ├── openclaw_voice_plugin.md
│       ├── xiaohuang_voice_wake_mvp_notes.md
│       ├── xiaohuang_project_context.md
│       ├── stt_engine_comparison.md
│       ├── wake_word_trigger_command.md
│       ├── tts_engine_notes.md
│       └── xiaohuang_voice_pipeline_notes.md
└── README.md
```

## 项目概览

### 第一批 (语音唤醒 + 管道架构)

| 项目 | 定位 | 许可 | 对小黄的价值 |
|------|------|------|-------------|
| openWakeWord | 唤醒词检测框架 | Apache 2.0 / CC BY-NC-SA 4.0 | 模型训练方法论 + 推理架构 |
| VoiceClaw | OpenClaw 语音插件 | MIT | 语音交互管道架构 + 双进程通信 |

### 第二批 (STT / 唤醒 / TTS 引擎)

| 项目 | 定位 | 许可 | 对小黄的价值 |
|------|------|------|-------------|
| Wake-Word | Electron 唤醒词桌面应用 | MIT (代码) / Picovoice 专有 (模型) | Electron 桌面应用架构参考 |
| FunASR | 端到端语音识别工具包 | MIT (代码) / 模型协议 (模型) | **MVP 核心** — STT + VAD + KWS + 标点 |
| faster-whisper | CTranslate2 加速 Whisper | MIT | STT 备选 + 对标验证 |
| edge-tts | Edge 在线 TTS 模块 | LGPLv3 + MIT | 第二阶段 TTS 快速验证方案 |

## 快速导航

### 架构与规划
- [小黄项目长期上下文](wiki/topics/xiaohuang_project_context.md)
- [小黄语音管道综合分析 (第二批)](wiki/topics/xiaohuang_voice_pipeline_notes.md)
- [小黄语音唤醒 MVP 建议路线](wiki/topics/xiaohuang_voice_wake_mvp_notes.md)

### 技术分析
- [唤醒词与触发指令方案](wiki/topics/wake_word_trigger_command.md)
- [STT 引擎对比](wiki/topics/stt_engine_comparison.md)
- [TTS 引擎笔记](wiki/topics/tts_engine_notes.md)
- [唤醒词检测技术分析](wiki/topics/wake_word_detection.md)
- [OpenClaw 语音插件分析](wiki/topics/openclaw_voice_plugin.md)
