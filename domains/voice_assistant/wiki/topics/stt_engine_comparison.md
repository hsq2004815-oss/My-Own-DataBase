# STT 引擎对比 —— 小黄第一阶段候选

> 生成时间：2026-04-30
> 数据来源：FunASR 和 faster-whisper 的 README / docs / setup.py / LICENSE

## 一、候选引擎总览

| 引擎 | 类型 | 中文精度 | 实时/流式 | 模型大小 | 许可 | Windows |
|------|------|---------|----------|---------|------|---------|
| SenseVoiceSmall (FunASR) | 专项中文 + 多语言 | 高 (400000h 中文训练) | 非流式 (离线) | 234M | 模型协议 (署名要求) | 是 (SDK/ONNX) |
| Paraformer-zh-streaming (FunASR) | 专项中文 | 高 (60000h 中文训练) | 流式 (实时) | 220M | 模型协议 (署名要求) | 是 (SDK/ONNX) |
| Fun-ASR-Nano-2512 | 多语言大模型 | 高 (数千万小时训练) | 低延迟实时 | 800M | 模型协议 (署名要求) | 未确认 |
| faster-whisper large-v3 | 通用多语言 | 中 (英文最优，中文未专项) | 非流式 | 1550M | MIT | 是 (需 GPU 库) |
| faster-whisper turbo | 通用多语言 | 中 | 非流式 | 809M | MIT | 是 |
| faster-whisper distil-large-v3 | 通用多语言 (英文优先) | 低 (中文未确认) | 非流式 | 未确认 | MIT | 是 |
| OpenAI Whisper (原始) | 通用多语言 | 中 | 非流式 | 1550M | MIT | 是 |

## 二、关键维度对比

### 2.1 中文识别精度

**SenseVoice (FunASR) 胜出。**

- 用 400000+ 小时中文数据训练
- 支持 7 种中文方言和 26 种地方口音
- 集成 ITN (逆文本正则化) 直接输出可读文本
- 内置情感识别 (SER) 和音频事件检测 (AED)

faster-whisper 基于 OpenAI Whisper 模型，为多语言通用模型，中文精度不如中文专项训练的 SenseVoice。

### 2.2 实时/流式支持

**FunASR 胜出。**

- FunASR 提供 paraformer-zh-streaming 原生流式模型 (600ms 粒度上屏)
- faster-whisper 为离线设计，需要社区项目 (WhisperLive, Whisper-Streaming) 补充实时能力

但第一阶段 MVP 场景是"听一句话 → 转文字"的**离线识别**，不需要流式。流式能力是加分项但非必需。

### 2.3 模型大小与硬件需求

**FunASR 胜出 (小模型资源消耗更低)。**

| 模型 | 参数量 | CPU 内存估算 | GPU VRAM 估算 |
|------|--------|------------|-------------|
| SenseVoiceSmall | 234M | ~1-2GB | ~1-2GB |
| Paraformer-zh | 220M | ~1-2GB | ~1-2GB |
| faster-whisper large-v3 | 1550M | ~3-4GB | ~4.5GB (fp16) |
| faster-whisper turbo | 809M | ~2-3GB | ~3-4GB |

MVP 目标是在普通 Windows 笔记本上运行，FunASR 小模型的资源消耗明显更低。

### 2.4 许可生态

**faster-whisper 胜出。**

- faster-whisper + Whisper 模型：纯 MIT，商业友好
- FunASR 代码 MIT，但模型有独立 MODEL_LICENSE (需署名、禁止诋毁等条款)，商业使用需仔细评估

### 2.5 VAD 集成

**双方持平。**

- FunASR 提供 fsmn-vad (0.4M 参数，流式支持)，与 STT 模型无缝集成
- faster-whisper 内置 Silero VAD (vad_filter=True)，简单易用

### 2.6 Windows 支持

**FunASR 稍优。**

- FunASR 有官方 Windows SDK (funasr-runtime-win-cpu-x64)，专门适配 Windows
- faster-whisper GPU 推理需要手动安装 CUDA 库 (可从 Purfview 项目获取)，CPU 推理直接可用

### 2.7 附加能力

| 能力 | FunASR | faster-whisper |
|------|--------|---------------|
| 标点恢复 | ✅ ct-punc (290M) | ❌ (Whisper 自带基础标点) |
| 说话人分离 | ✅ cam++ (7.2M) | ❌ (需额外工具) |
| 情感识别 | ✅ emotion2vec | ❌ |
| 关键词检出 | ✅ fsmn-kws (0.7M) | ❌ |
| 词级时间戳 | ✅ fa-zh | ✅ (内置) |
| ONNX 导出 | ✅ | ❌ (CTranslate2 自有格式) |

## 三、第一阶段 MVP 推荐

### 首选：FunASR / SenseVoiceSmall

理由：
1. 中文精度最高（关键需求）
2. 模型小，适合普通 Windows 笔记本
3. VAD 和标点恢复都在同一生态内，集成成本低
4. Windows 官方 SDK 支持
5. 可选 fsmn-kws 作为唤醒词检测（统一技术栈）
6. 后续阶段可无缝升级到流式 (paraformer-zh-streaming)

### 备选：faster-whisper

适用于：
1. 对 MIT 许可有明确要求的场景
2. 已有 NVIDIA GPU 的硬件环境
3. 需要多语言支持（不仅仅是中文）
4. 作为 FunASR 的对标验证方案

### 不建议：原始 OpenAI Whisper

faster-whisper 已完全覆盖其能力（更快、内存更少、同样的精度），没有理由使用原始版本。

## 四、集成建议

```
麦克风 → Silero VAD / fsmn-vad (检测语音起始/结束)
       → 截取单句音频 (最长 10s 或 VAD 自动截断)
       → SenseVoiceSmall (语音转文字)
       → ct-punc (标点恢复)
       → 悬浮窗显示
```

如果使用 FunASR 生态，VAD 和 STT 共享同一个 `AutoModel` 调用入口，代码更简洁。
