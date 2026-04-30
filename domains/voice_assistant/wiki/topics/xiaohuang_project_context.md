# 小黄（XiaoHuang）项目长期上下文文档

> **注意：每个新 Issue 的 Agent 必须先读取本文件，再执行任务。**

---

## 一、小黄长期目标

小黄是一个 **Windows 桌面 AI 助手**，核心能力路径规划如下：

| 阶段 | 能力 | 说明 |
|------|------|------|
| 第一阶段 | 语音唤醒 + 音波悬浮窗 + 单句语音转文字 | 当前阶段，详见下文 |
| 第二阶段 | 单轮语音回复 / TTS | 识别句子后给予一次语音回复 |
| 第三阶段 | 连续语音对话 | 多轮上下文对话，无需反复唤醒 |
| 第四阶段 | 浏览器操作 | 通过 Agent 操控浏览器完成任务 |
| 第五阶段 | 资料下载入库 | 爬虫 + 下载 + 结构化存储 |
| 第六阶段 | opencode 写代码 | 语音驱动代码编写 |
| 第七阶段 | QQ/微信草稿回复 | 社交消息的语音起草与发送 |

**长期愿景：** 从语音唤醒开始，逐步演进为全能的 Windows 桌面 AI 助手。

---

## 二、当前阶段

**当前处于语音唤醒/语音交流预研阶段，不开发完整小黄系统。**

第一阶段唯一目标：

> 说"小黄" → 弹出音波悬浮窗 → 听一句话 → 转文字显示

这是一个最小闭环 MVP，验证语音唤醒 + 语音识别的基础链路。

---

## 三、当前已入库项目

| 项目 | 定位 | 本地路径 | 许可 | 对小黄的价值 |
|------|------|----------|------|-------------|
| openWakeWord | 开源唤醒词检测框架 | `E:\DataBase\domains\voice_assistant\raw\github\repos\openWakeWord` | Apache 2.0 (代码) / CC BY-NC-SA 4.0 (模型) | 唤醒词模型训练方法论 + 推理架构 |
| VoiceClaw | OpenClaw 语音插件 | `E:\DataBase\domains\voice_assistant\raw\github\repos\voiceclaw` | MIT | 语音交互管道架构 + Node.js+Python 双进程通信 |

### openWakeWord 核心摘要

- **架构：** melspectrogram（ONNX） → Google speech_embedding（冻结预训练特征提取器） → 分类器（全连接或 RNN） → 推理引擎（ONNX/TFLite）
- **帧窗口：** 80ms（1280 samples @ 16kHz）
- **内置：** Silero VAD 减少误触发、自定义声纹二次验证、100% TTS 合成数据训练管线
- **Windows：** 默认 ONNX Runtime，不支持 TFLite 和 Speex 降噪

### VoiceClaw 核心摘要

- **架构：** Node.js (TypeScript) 插件逻辑 + Python 子进程 (音频/ML)，JSON-RPC over stdio 通信
- **事件流：** VAD → 唤醒词 → STT → Agent → TTS
- **引擎：** STT 可选 SenseVoice/faster-whisper/OpenAI Whisper，TTS 可选 Edge TTS/Piper
- **唤醒方案：** 基于 STT 文本匹配（非专用唤醒词模型）

---

## 四、当前技术判断

### 关于 openWakeWord

| 结论 | 说明 |
|------|------|
| **不建议直接使用预训练模型** | 现有模型仅支持英文（alexa、hey mycroft 等），目标语言为中文 |
| **建议使用其训练管线** | Google Colab notebook + 中文 TTS 合成数据，训练"小黄"专属唤醒词模型 |
| **建议借鉴架构** | melspectrogram + embedding + classifier 三段式架构直接复用 |
| **注意许可** | 预训练模型为 CC BY-NC-SA 4.0，商用需注意合规 |
| **Google speech_embedding 风险** | 基于大量英文语音预训练，对中文的特征提取能力未经验证 |

### 关于 VoiceClaw

| 结论 | 说明 |
|------|------|
| **不建议直接 fork 成主项目** | 深度耦合 OpenClaw 平台，独立使用改造成本高 |
| **适合作为架构参考** | Node.js + Python 双进程、JSON-RPC over stdio、VAD → Wake Word → STT → Agent → TTS 事件流 |
| **唤醒方案不适用** | 其 STT 文本匹配方案延迟高、资源消耗大，不适合持续监听 |
| **第一阶段建议** | 吸取架构理念独立实现，不直接集成 |

### 互补关系

理想路径：用 openWakeWord 的**方法论**训练中文唤醒词模型（底层），参考 VoiceClaw 的**架构**设计语音交互管道（上层）。

---

## 四 A、第二批已入库项目 (2026-04-30)

| 项目 | 定位 | 本地路径 | 许可 | 对小黄的价值 |
|------|------|----------|------|-------------|
| Wake-Word | Electron 唤醒词桌面应用 | `E:\DataBase\domains\voice_assistant\raw\github\repos\Wake-Word` | MIT (代码) / Picovoice 专有 (模型) | Electron 桌面应用架构参考 (系统托盘/设置面板/安装器) |
| FunASR | 阿里端到端语音识别工具包 | `E:\DataBase\domains\voice_assistant\raw\github\repos\FunASR` | MIT (代码) / 模型协议 (模型) | **MVP 核心依赖** — STT + VAD + KWS + 标点恢复 |
| faster-whisper | CTranslate2 加速 Whisper 推理 | `E:\DataBase\domains\voice_assistant\raw\github\repos\faster-whisper` | MIT | STT 备选 + 对标验证 |
| edge-tts | 微软 Edge 在线 TTS 模块 | `E:\DataBase\domains\voice_assistant\raw\github\repos\edge-tts` | LGPLv3 + MIT | 第二阶段 TTS 快速验证方案 |

### Wake-Word 核心摘要

- **架构：** Electron 27 + React 18 + TypeScript 5.3，主进程/渲染进程 IPC
- **唤醒引擎：** Picovoice Porcupine (商业 SDK)，专有 .ppn 模型格式
- **默认唤醒词：** "Hey Claude"，唤醒后自动启动 Cursor IDE 和 Claude CLI
- **Windows：** 专为 Windows 10/11 64-bit 设计，提供 NSIS 安装器
- **VAD/STT/TTS：** 无，纯粹是唤醒词 → 执行命令的桌面工具
- **许可陷阱：** Picovoice 免费 tier 仅限非商业用途，模型不可自行训练

### FunASR 核心摘要

- **组织：** 阿里巴巴 DAMO Academy (Speech Lab)
- **核心模型：** SenseVoiceSmall (234M，中文精度高)，Paraformer-zh (220M，流式/非流式)，Fun-ASR-Nano-2512 (800M，多语言大模型)
- **VAD：** fsmn-vad (0.4M，流式支持)
- **KWS：** fsmn-kws (0.7M)、sanm-kws (2024/09 新增)
- **标点：** ct-punc (290M)
- **部署：** pip 包 / Docker / Windows SDK / ONNX 导出
- **Windows：** 有官方 Windows SDK (funasr-runtime-win-cpu-x64)
- **许可：** 代码 MIT；模型需遵守 MODEL_LICENSE (署名要求)

### faster-whisper 核心摘要

- **组织：** SYSTRAN
- **原理：** 使用 CTranslate2 替代 PyTorch 推理，实现最高 4 倍加速、内存更少
- **模型：** Whisper large-v3 (1550M)，turbo (809M)，distil-large-v3
- **VAD：** 内置 Silero VAD (vad_filter=True)
- **量化：** CPU/GPU 均支持 int8 量化
- **GPU 需求：** CUDA 12 + cuBLAS + cuDNN 9 (Windows 需手动安装)
- **中文精度：** 未专项优化 (Whisper 为多语言通用模型)
- **许可：** 纯 MIT (代码 + 模型)

### edge-tts 核心摘要

- **原理：** 调用 Microsoft Edge 浏览器 Read Aloud TTS 云端 API (WebSocket)
- **中文声音：** 20+ 种 (zh-CN/zh-HK/zh-TW)，推荐 zh-CN-XiaoxiaoNeural
- **输出：** mp3 + SRT 字幕
- **局限：** 必须联网、依赖微软非官方 API、无离线能力
- **许可：** 主体 LGPLv3，srt_composer.py 为 MIT
- **第一阶段：** 不需要 (MVP 不含 TTS)

---

## 五、Agent 分工

| Agent | 职责 | 禁止行为 |
|-------|------|----------|
| **claude code** | 下载 GitHub 项目到 raw 目录 | 不运行 install/build/test，不修改 raw 源码 |
| **open code** | 数据库融入——生成 metadata、wiki、rules 文档 | 不下载新项目，不修改 raw 源码 |
| **Codex** | 开发 `E:\Projects\xiaohuang` 主项目 | 不负责下载项目，不负责数据库融入 |

---

## 六、Multica 使用规则

1. **每个 Issue 都可能是新上下文** —— 新 Agent 不会自动继承之前对话。
2. **新 Issue 必须先读取本文件** —— 所有 Agent 在接手小黄相关 Issue 时，第一步必须读取 `xiaohuang_project_context.md`。
3. **同一任务的修正尽量在原 Issue 里继续评论**，不要反复新建 Issue。
4. **本文件由 open code 维护** —— 有重大进展或方向变更时更新此文档。

---

## 七、第一阶段 MVP 边界

### 必须包含

| 组件 | 说明 |
|------|------|
| 唤醒词"小黄" | 训练好的中文唤醒词 ONNX 模型 |
| 音波悬浮窗 | 实时波形可视化，唤醒时高亮动画 |
| 正在听状态 | 悬浮窗反馈当前处于录音状态 |
| 识别一句话 | 唤醒后录制用户语音（最长 10 秒或 VAD 自动截断） |
| 显示转写文字 | STT 转写结果展示在悬浮窗上 |

### 明确不包含

- OpenCLI / Browser 操作
- opencode 调用
- QQ / 微信集成
- 爬虫 / 资料下载
- 完整任务调度系统
- 多轮对话
- 复杂 Agent 能力

### MVP 建议技术栈

| 组件 | 首选 | 备选 |
|------|------|------|
| 唤醒词检测 | openWakeWord 架构训练的 ONNX 中文模型 | Porcupine (商业) |
| VAD | Silero VAD | WebRTC VAD |
| STT | SenseVoice (FunASR) | faster-whisper |
| TTS | Edge TTS (免费，中文好) | Piper |
| 音频 I/O | PyAudioWPatch (Windows) | sounddevice |
| 通信 | 参考 VoiceClaw 的 JSON-RPC over stdio | — |
| UI | 待定（Electron / Qt / Windows 原生） | — |

### 关键风险

| 风险 | 缓解 |
|------|------|
| 中文唤醒词训练效果差 | 多个中文 TTS 引擎生成多样化数据；收集少量真实语音 fine-tuning |
| Windows 噪声大误触发高 | 优先实现 Silero VAD；加入能量阈值过滤 |
| Google speech_embedding 对中文不适应 | 先用其 pipeline 训练测试；必要时探索 WavLM / chinese-hubert |
| ONNX 推理性能不足 | 量化模型；考虑模型剪枝 |
| TTS 合成训练数据版权 | 使用开源可商用 TTS（CosyVoice-300M、ChatTTS） |

---

## 八、后续候选项目收集顺序

### 第一批已完成 ✅

- openWakeWord：唤醒词检测参考
- VoiceClaw：语音插件和事件管道参考

### 第二批已完成 ✅

- Wake-Word：Electron 桌面应用架构参考
- FunASR / SenseVoice：中文 STT 引擎 + VAD + KWS + 标点
- faster-whisper：轻量级 STT 引擎备选
- edge-tts：免费中文 TTS 引擎 (第二阶段用)

### 后续建议 📋

| 优先级 | 项目 | 用途 |
|--------|------|------|
| 中 | Piper | 本地离线 TTS 引擎 |
| 中 | CosyVoice | 中文 TTS + 声音克隆 |
| 中 | Alice | 语音助手参考 |
| 中 | OpenClaw Assistant | Agent 框架参考 |
| 低 | ChatTTS | 对话式中文 TTS |
| 低 | PersonaPlex | 多角色 Agent 参考 |
| 低 | Moshi | 对话 AI 参考 |
| 低 | 闪电说产品参考 | 竞品分析 |

---

## 九、给未来 Agent 的默认开场要求

> **请先读取 `E:\DataBase\domains\voice_assistant\wiki\topics\xiaohuang_project_context.md`，确认小黄项目当前阶段、已有资源和技术边界，再执行本 Issue。**
>
> 如需了解详细技术分析，可进一步读取：
> - `wiki/topics/wake_word_detection.md`（唤醒词检测技术分析）
> - `wiki/topics/openclaw_voice_plugin.md`（VoiceClaw 语音插件分析）
> - `wiki/topics/xiaohuang_voice_wake_mvp_notes.md`（MVP 建议路线）
> - `wiki/topics/stt_engine_comparison.md`（STT 引擎对比：FunASR vs faster-whisper）
> - `wiki/topics/wake_word_trigger_command.md`（唤醒词候选方案分析）
> - `wiki/topics/tts_engine_notes.md`（TTS 引擎笔记：edge-tts 及其他）
> - `wiki/topics/xiaohuang_voice_pipeline_notes.md`（第二批入库综合分析）
> - `processed/metadata/openWakeWord.metadata.json`（openWakeWord 结构化元数据）
> - `processed/metadata/voiceclaw.metadata.json`（VoiceClaw 结构化元数据）
> - `processed/metadata/Wake-Word.metadata.json`（Wake-Word 结构化元数据）
> - `processed/metadata/FunASR.metadata.json`（FunASR 结构化元数据）
> - `processed/metadata/faster-whisper.metadata.json`（faster-whisper 结构化元数据）
> - `processed/metadata/edge-tts.metadata.json`（edge-tts 结构化元数据）
> - `../dev_tools/rules/github_import_rules.md`（GitHub 导入规范）

---

*本文档由 open code 生成与更新，最后更新：2026-04-30 (第二批入库)*
*维护者：open code（数据库融入 Agent）*
