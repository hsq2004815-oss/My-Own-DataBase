# 唤醒词与触发指令 —— 小黄第一阶段候选方案

> 生成时间：2026-04-30
> 数据来源：Wake-Word (README/package.json/LICENSE)、FunASR (README/MODEL_LICENSE)、openWakeWord (现有 metadata)

## 一、候选唤醒方案总览

| 方案 | 类型 | 核心技术 | 可训练中文 | 许可 | 适合 MVP |
|------|------|---------|-----------|------|----------|
| openWakeWord 训练管线 | 专用唤醒词模型 | melspectrogram + embedding + classifier (ONNX) | 是 (TTS 合成数据) | Apache 2.0 (代码) | 推荐 |
| FunASR fsmn-kws | 关键词检出 | FSMN / SANM 声学模型 (PyTorch/ONNX) | 可微调 | 模型协议 (署名) | 推荐 |
| Picovoice Porcupine (Wake-Word) | 商业 SDK | 专有唤醒词引擎 | 需 Picovoice 云端训练 | MIT (代码), 专有 (模型) | 不推荐 |
| STT 文本匹配 (VoiceClaw 方案) | 间接方案 | STT → 文本匹配 | N/A | MIT | 不推荐 |

## 二、方案分析

### 2.1 openWakeWord 训练管线（首选）

**来源：** openWakeWord (已入库第一批)

**工作原理：**
1. 用中文 TTS 合成大量"小黄"唤醒词语音数据
2. Google Colab notebook 自动训练流程
3. 生成 ONNX 模型用于推理

**优势：**
- 专用唤醒词模型，精度高、延迟低
- ONNX 格式跨平台 (Windows 原生支持)
- 训练流程成熟 (100% TTS 合成数据管线)
- 架构清晰 (mel + embedding + classifier)

**劣势：**
- 需要额外训练步骤 (需 TTS 生成中文数据)
- Google speech_embedding 对中文适应性未验证
- 预训练模型仅英文，中文需从零开始

**MVP 适配：** 第一推荐。虽然需要训练步骤，但拥有最成熟的训练方法论和最低的推理开销。

### 2.2 FunASR fsmn-kws / sanm-kws（推荐对比评估）

**来源：** FunASR (本次入库)

**工作原理：**
- fsmn-kws: 基于 FSMN (Feedforward Sequential Memory Network) 的关键词检出模型
- sanm-kws: 基于 SANM (Self-Attention Network Memory) 的流式关键词检出
- 支持 4 种模型：fsmn_kws, fsmn_kws_mt, sanm_kws, sanm_kws_streaming
- 输入音频，输出检测到的关键词

**优势：**
- 与 STT 引擎同一生态 (都是 FunASR)，技术栈统一
- 模型极小 (fsmn-kws 仅 0.7M 参数)，适合持续监听
- 支持流式检测 (sanm_kws_streaming)
- 支持微调 (可用自定义中文关键词数据 fine-tune)
- Windows 支持 (FunASR Runtime SDK)
- 5000 小时中文数据预训练

**劣势：**
- 关键词检出功能 2024/09/25 才加入，相对较新
- 针对"小黄"的精度未实际测试
- 微调流程复杂度未确认

**MVP 适配：** 第二推荐。与 FunASR STT 统一技术栈的优势很大，值得与 openWakeWord 训练管线做对比评估。

### 2.3 Picovoice Porcupine / Wake-Word（不推荐）

**来源：** Wake-Word (本次入库)

**工作原理：**
- Picovoice Porcupine 商业 SDK 做唤醒词检测
- 唤醒词模型 (.ppn) 需要通过 Picovoice Console 云端训练或使用预设
- 应用层用 Electron + React 封装

**优势：**
- 工业级精度 (Picovoice 是业界知名语音 AI 公司)
- 提供完整的 Windows 桌面应用参考 (Electron + 系统托盘)
- 开箱即用 (如果有 Picovoice API key)

**劣势：**
- Picovoice 唤醒词模型不可自行离线训练，依赖 Picovoice 云端
- 免费 tier 仅限非商业用途
- 模型格式专有 (.ppn)，不可导出/转换
- 不适合需要完全自主可控的唤醒词方案
- 项目硬编码 "Hey Claude" 场景

**MVP 适配：** 不推荐。唤醒词方案被锁定在 Picovoice 商业 SDK，无法满足自主训练"小黄"中文唤醒词的需求。但 Electron 桌面应用架构值得参考。

### 2.4 STT 文本匹配（不推荐）

**来源：** VoiceClaw (已入库第一批)

**工作原理：**
- 持续运行 STT 引擎 (SenseVoice / faster-whisper)
- 将识别文本与唤醒词做字符串匹配

**优势：**
- 实现简单
- 不依赖额外模型

**劣势：**
- 延迟高 (需完整识别后才能判断)
- 资源消耗大 (持续运行 STT 引擎)
- 误触发率高 (任何包含唤醒词的语音都会触发)
- 不适合持续监听场景

**MVP 适配：** 不推荐。VoiceClaw 文档本身也指出此方案的局限性。

## 三、第一阶段 MVP 推荐

### 主方案：openWakeWord 训练管线

用 openWakeWord 的方法论，配合中文 TTS 合成数据，训练专属"小黄"唤醒词 ONNX 模型。

### 对比评估候选：FunASR fsmn-kws / sanm-kws

作为统一 FunASR 技术栈的替代方案。如果 fsmn-kws 对"小黄"的检测精度能达到要求，可大幅简化整体技术栈（STT + KWS 都在 FunASR 生态内）。

### 评估计划

| 步骤 | 内容 |
|------|------|
| 1 | 用中文 TTS (CosyVoice / ChatTTS / Edge TTS) 生成 1000+ "小黄"语音样本 |
| 2 | 用 fsmn-kws 预训练模型直接测试检出率 (不做微调) |
| 3 | 如果检出率 < 90%，用样本微调 fsmn-kws |
| 4 | 并行用 openWakeWord 训练管线训练 ONNX 模型 |
| 5 | 对比两种方案的延迟、精度、资源消耗，做最终选择 |

## 四、Wake-Word 项目的参考价值

虽然 Picovoice 方案不适合直接使用，但 Wake-Word 项目的以下部分值得参考：

- **Electron 桌面应用架构**：主进程 (语音检测) + 渲染进程 (React UI) 的 IPC 通信模式
- **系统托盘方案**：绿/红图标状态指示、右键菜单控制
- **设置面板 UI**：API key 配置、功能开关、灵敏度调节
- **Windows NSIS 安装器**：专业安装体验

这些可作为小黄悬浮窗和桌面集成的参考，但与唤醒词引擎本身无关。
