# 小黄语音唤醒 MVP 笔记

> 整合 openWakeWord 和 VoiceClaw 的分析，推导"小黄"第一阶段语音唤醒 MVP 的建议路线。

## 当前已有原材料

| 项目 | 定位 | 许可 | 对小黄的意义 |
|------|------|------|-------------|
| openWakeWord | 开源唤醒词检测库 | Apache 2.0 (代码) / CC BY-NC-SA 4.0 (模型) | 唤醒词模型训练方法论 + 推理架构参考 |
| VoiceClaw | OpenClaw 语音插件 | MIT | 语音交互管道架构参考 + 双进程通信模式 |

## 小黄第一阶段应该做什么？

### 目标边界

**只做：小黄唤醒 → 音波悬浮窗 → 开始听一句话**

不接：
- 浏览器操控
- QQ/微信
- opencode
- 爬虫
- 多轮对话
- 复杂 Agent 能力

### 建议路线

```
Phase 1: 唤醒词检测 (核心)
├── 1.1 使用 openWakeWord 训练管线训练中文"小黄"唤醒模型
│   ├── 工具: Google Colab + 中文 TTS (如 CosyVoice/Bark/ChatTTS)
│   ├── 训练数据: ~5000+ 句 "小黄" / "小黄小黄" 合成语音
│   ├── 负样本: 中文对话、音乐、环境噪音 (~数千小时)
│   └── 输出: ONNX 模型 (优先 ONNX, Windows 兼容性好)
│
├── 1.2 实现本地推理循环
│   ├── 音频输入: PyAudioWPatch (Windows) / PyAudio (Linux/Mac)
│   ├── 采样率: 16kHz, 16-bit PCM mono
│   ├── 帧大小: 80ms (1280 samples)，与 openWakeWord 一致
│   ├── 推理引擎: ONNX Runtime
│   └── 阈值: 0.5 (初始值, 后续根据实测调优)
│
├── 1.3 加入 VAD 减少误触发
│   ├── 方案: Silero VAD (openWakeWord 已内嵌, VoiceClaw 也用)
│   ├── 作用: 非语音噪音时不触发唤醒词检测
│   └── 阈值: 0.5 (初始值)
│
└── 1.4 (可选优化) 自定义声纹验证模型
    ├── 前提: 有足够的个人语音样本
    ├── 作用: 只响应特定说话人的"小黄"
    └── 方法: openWakeWord 的 train_custom_verifier

Phase 2: 音波悬浮窗 (UI 反馈)
├── 2.1 音频可视化
│   ├── 实时波形/频谱显示
│   ├── 未唤醒: 半透明/暗色
│   └── 唤醒时: 高亮/动画反馈
│
└── 2.2 技术选型
    ├── 方案 A: Electron 悬浮窗 (与 Node.js 生态一致)
    ├── 方案 B: Python Qt/Tkinter 悬浮窗
    └── 方案 C: Windows 原生 API (仅 Windows)

Phase 3: "开始听一句话"
├── 3.1 唤醒后录音
│   ├── 唤醒后开始录音（如最长 10 秒）
│   ├── VAD 检测静音自动停止
│   └── 保存为临时 WAV 文件
│
├── 3.2 语音识别 (STT)
│   ├── 方案 A: SenseVoice (FunASR, 中文效果好)
│   ├── 方案 B: faster-whisper (轻量)
│   ├── 方案 C: OpenAI Whisper API (依赖网络)
│   └── MVP 建议: SenseVoice + Edge TTS (VoiceClaw 已验证的组合)
│
└── 3.3 一句话结束 → 回到待唤醒状态
```

## openWakeWord 直接借鉴清单

| 可借鉴内容 | 实现方式 | 优先级 |
|-----------|----------|--------|
| 三段式模型架构 | melspectrogram + speech_embedding + classifier | P0 |
| 自动训练管线 | Google Colab notebook 训练流程 | P0 |
| 推理循环模式 | 80ms 帧滑动窗口 | P0 |
| VAD 集成 | Silero VAD 内嵌 | P0 |
| 重复抑制逻辑 | v0.6.0 新增的重复检测控制 | P1 |
| 自定义验证模型 | 声纹二次验证 | P2 (MVP 后) |
| Speex 噪声抑制 | Linux only, MVP 可跳过 | P2 (MVP 后) |

## VoiceClaw 直接借鉴清单

| 可借鉴内容 | 实现方式 | 优先级 |
|-----------|----------|--------|
| 双进程架构 | Node.js (服务) + Python (音频/ML) | P1 |
| JSON-RPC over stdio | 零依赖 IPC 通信 | P1 |
| 事件流管道 | wake_word → speech_start → utterance | P1 |
| 插件配置 schema | openclaw.yaml 风格声明式配置 | P1 |
| Edge TTS | Windows 可用, 中文语音质量可接受 | P0 |
| SenseVoice | FunASR, 中文识别效果好 | P0 |

## 关键风险与缓解

| 风险 | 缓解措施 |
|------|----------|
| 中文唤醒词训练效果差 | 用多个中文 TTS 引擎生成多样化训练数据；收集少量真实语音做 fine-tuning |
| Windows 上噪声大导致误触发高 | 优先实现 VAD；考虑加入简单的能量阈值过滤 |
| Google speech_embedding 对中文不适应 | 先用它的 pipeline 训练测试；如果不适应，探索中文预训练语音模型 (如 WavLM/chinese-hubert) |
| ONNX 模型推理性能不足 | 使用 ONNX 量化；考虑模型剪枝 |
| 训练数据版权（TTS 合成语音） | 使用开源可商用的 TTS 引擎 (CosyVoice-300M, ChatTTS)；检查各 TTS 引擎的许可条款 |

## MVP 技术选型总结

| 组件 | MVP 建议 | 备选方案 |
|------|---------|----------|
| 唤醒词检测 | openWakeWord 架构训练的 ONNX 模型 | Porcupine (商业) |
| 语音活动检测 | Silero VAD | WebRTC VAD |
| 语音识别 | SenseVoice (FunASR) | faster-whisper |
| 语音合成 | Edge TTS (免费, 中文好) | Piper |
| 音频 I/O | PyAudioWPatch (Windows) | sounddevice |
| 进程架构 | Python 独立进程 | Node.js+Python 双进程 |
| UI 框架 | 待定 (Electron/Qt/原生) | - |

## 何时不应该直接使用这两个项目？

1. **不要直接用 openWakeWord 预训练模型**：因为它们是英文的，对"小黄"无效。
2. **不要直接用 VoiceClaw 代码**：因为与 OpenClaw 紧耦合，独立使用改造成本高。
3. **不要跳过训练直接拼凑**：没有经过良好训练的中文唤醒词模型，MVP 体验会很差。

正确的使用方式：
- 用 openWakeWord 的**方法论和工具**训练自己的中文模型
- 用 VoiceClaw 的**架构理念**设计自己的语音交互管道
- 两者结合 = 小黄语音唤醒 MVP 的技术基础
