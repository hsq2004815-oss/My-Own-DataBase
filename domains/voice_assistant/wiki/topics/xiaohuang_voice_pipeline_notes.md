# 小黄语音管道笔记 —— 第二批入库项目综合分析

> 生成时间：2026-04-30
> 基于第二批入库项目：Wake-Word / FunASR / faster-whisper / edge-tts
> 结合第一批：openWakeWord / VoiceClaw

## 一、管道路线图更新

### 第一阶段 MVP (不变)

```
说"小黄" → 唤醒词检测 → 音波悬浮窗弹出 → 听一句话 (VAD 截断) → STT 转文字 → 悬浮窗显示
```

### 技术选型更新

| 组件 | 首选 (更新后) | 备选 | 来源 |
|------|-------------|------|------|
| 唤醒词检测 | openWakeWord 训练管线 (主) / FunASR fsmn-kws (对比评估) | Picovoice (不推荐) | 第一批+第二批 |
| VAD | FunASR fsmn-vad (推荐, 与 STT 同生态) | Silero VAD | 第二批 (FunASR) |
| STT | FunASR SenseVoiceSmall (主推荐) | faster-whisper turbo | 第二批 |
| TTS | edge-tts (第二阶段用) | Piper / CosyVoice (待入库) | 第二批 |
| 音频 I/O | PyAudioWPatch (Windows) | sounddevice | 第一批 |
| 通信 | JSON-RPC over stdio | — | 第一批 (VoiceClaw) |
| UI | Electron (参考 Wake-Word) | Qt / Windows 原生 | 第二批 (Wake-Word) |

## 二、关键技术判断

### 2.1 唤醒词检测：双轨评估

**主方案：** openWakeWord 训练管线
- 优势：完整的训练方法论、ONNX 推理、低资源消耗
- 风险：Google speech_embedding 对中文的适应性未验证

**对比方案：** FunASR fsmn-kws
- 优势：与 STT 统一技术栈、5000h 中文预训练、模型极小 (0.7M)
- 风险：功能较新 (2024/09)、对"小黄"的精度未知

**决策：** 两种方案并行评估，用同一批中文合成数据测试，选精度和延迟最优的方案。

如果 fsmn-kws 精度达标，强烈建议选择它——因为可以统一到 FunASR 生态（一个 `funasr.AutoModel` 同时加载 KWS + VAD + STT），大幅降低集成复杂度。

### 2.2 STT：FunASR SenseVoiceSmall 为首选

**核心理由：** 中文精度最高、模型较小 (234M)、Windows 官方支持、与 VAD/标点/KWS 同生态。

**备选场景：**
- 需要纯 MIT 许可 → faster-whisper
- 有多语言需求 (不止中文) → faster-whisper large-v3
- 有 GPU 且追求更低延迟 → faster-whisper + batched inference

**不建议：** 原始 openai/whisper (faster-whisper 已完全覆盖)

### 2.3 VAD：FunASR fsmn-vad

与 SenseVoiceSmall 同生态，可以直接在 `AutoModel` 中通过 `vad_model="fsmn-vad"` 参数开启。支持流式和非流式模式，0.4M 参数极轻量。

### 2.4 TTS：第一阶段不需要

edge-tts 作为第二阶段快速验证方案。长期应入库 Piper 或 CosyVoice 作为离线替代。

### 2.5 桌面 UI：Wake-Word 提供 Electron 参考

Wake-Word 展示了一个完整的 Electron + React + TypeScript 桌面应用架构（系统托盘、设置面板、NSIS 安装器），可作为小黄悬浮窗的技术参考。但小黄不需要启动 Cursor/Claude 等 IDE 功能。

## 三、建议的技术栈架构

```
┌─────────────────────────────────────────────────────┐
│                    Electron 桌面壳                     │
│  ┌───────────────────────────────────────────────┐  │
│  │              React UI (悬浮窗)                  │  │
│  │   音波动画 / 识别文字显示 / 状态指示              │  │
│  └───────────────────────────────────────────────┘  │
│                        │ IPC                         │
│  ┌───────────────────────────────────────────────┐  │
│  │        Node.js 主进程 (语音管道控制)             │  │
│  └───────────────────────────────────────────────┘  │
│                        │ JSON-RPC over stdio          │
│  ┌───────────────────────────────────────────────┐  │
│  │           Python 子进程 (音频/ML)                │  │
│  │                                                │  │
│  │  ┌──────────┐  ┌──────────┐  ┌─────────────┐  │  │
│  │  │ KWS/唤醒词 │→│ fsmn-vad │→│ SenseVoice  │  │  │
│  │  │ fsmn-kws │  │ (0.4M)   │  │ Small (234M)│  │  │
│  │  └──────────┘  └──────────┘  └─────────────┘  │  │
│  │                                                │  │
│  │  音频采集：PyAudioWPatch (麦克风)                │  │
│  └───────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

全部 ML 组件在 FunASR 生态内，通过统一的 `funasr.AutoModel` 管理，大幅降低集成和维护成本。

## 四、各项目的具体角色

| 项目 | 入库批次 | 角色 |
|------|---------|------|
| openWakeWord | 第一批 | 唤醒词训练方法论 + 推理架构参考 + 对比评估候选 |
| VoiceClaw | 第一批 | 双进程通信架构参考 + 事件管道设计参考 |
| Wake-Word | 第二批 | Electron 桌面应用架构参考 (系统托盘/设置面板/安装器) |
| FunASR | 第二批 | **MVP 核心依赖** (STT + VAD + KWS + 标点) |
| faster-whisper | 第二批 | STT 备选 + 对标验证 |
| edge-tts | 第二批 | 第二阶段 TTS 快速验证方案 |

## 五、下一步行动建议

1. **验证 FunASR 中文精度：** 在 Windows 上安装 FunASR，用 SenseVoiceSmall 测试几句中文语音的实际识别效果
2. **测试 fsmn-kws 检出率：** 用 TTS 生成若干"小黄"音频，测试 fsmn-kws 的检出率
3. **对比评估：** fsmn-kws vs openWakeWord 训练管线，选出最优唤醒方案
4. **搭建最小管道：** PyAudioWPatch 录音 → fsmn-vad → SenseVoiceSmall → 打印结果
5. **入库 Piper/CosyVoice：** 为第二阶段 TTS 做准备
