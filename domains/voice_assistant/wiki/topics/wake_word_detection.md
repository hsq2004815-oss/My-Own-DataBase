# Wake Word Detection (唤醒词检测)

## openWakeWord 解决什么问题？

openWakeWord 是一个开源的唤醒词检测框架，核心解决以下问题：

1. **低成本唤醒词检测**：让开发者无需从零训练模型即可在应用中添加语音唤醒功能。提供预训练的英文唤醒词模型（"alexa", "hey mycroft", "hey jarvis" 等）。
2. **纯合成数据训练**：所有模型均使用 100% TTS 生成的合成语音训练，无需手动收集真实语音数据，极大降低了训练门槛。
3. **跨平台推理**：基于 ONNX Runtime 和 TFLite，支持 Linux/macOS/Windows/Raspberry Pi 等多平台。
4. **可定制的二次验证**：支持训练自定义声纹验证模型作为第二级过滤，减少误触发。

## 核心技术架构

```
音频输入 (16kHz, 16-bit PCM)
  → melspectrogram (ONNX 实现)
  → Google speech_embedding (冻结的预训练特征提取器, Apache-2.0)
  → 分类器 (全连接或 2层 RNN)
  → 推理引擎 (ONNX 或 TFLite)
  → 分数输出 (0-1, 默认阈值 0.5)
```

### 模型设计原则

| 原则 | 说明 |
|------|------|
| 快速但不追求极致轻量 | Raspberry Pi 3 单核可同时运行 15-20 个模型 |
| 足够准确 | 误拒绝率 <5%，误接受率 <0.5次/小时 |
| 架构简洁 | 80ms 帧滑动窗口，每帧输出 0-1 分数 |
| 零手动数据收集 | 100% TTS 合成训练数据 |

### 性能对比

在 "alexa" 和 "hey mycroft" 的测试中，openWakeWord 模型的准确度至少与商业方案 Picovoice Porcupine 相当甚至更好（小样本测试，结论需谨慎对待）。

## 内置功能

- **VAD 集成**：内嵌 Silero VAD，可在非语音噪音时阻止误触发
- **Speex 噪声抑制**：Linux 上支持 Speex 降噪预处理
- **多模型并行**：单进程可同时监听多个唤醒词
- **自定义验证模型**：针对特定用户的声纹二次验证，<5 分钟训练数据即可

## 对小黄项目的意义

### 适合借鉴的部分

| 可借鉴内容 | 用途 |
|------------|------|
| melspectrogram + embedding + classifier 三段式架构 | 小黄唤醒词检测的模型架构蓝本 |
| 自动训练管线 (Google Colab / 本地 notebook) | 训练中文"小黄"唤醒词模型 |
| VAD + 唤醒词 + 重复抑制的控制逻辑 | 减少 MVP 阶段的误触发 |
| 性能评估方法 (Dinner Party Corpus) | 评估小黄唤醒模型的真实表现 |
| 自定义声纹验证模型方案 | 后续优化，减少非目标说话人的误触发 |

### 不适合直接使用的部分

| 内容 | 原因 |
|------|------|
| 现有预训练模型 | 仅支持英文，目标语言是中文 |
| CC BY-NC-SA 模型许可 | 商用场景需注意合规 |
| Google speech_embedding | 基于大量英文语音预训练，对中文的特征提取能力未经验证 |

## Windows 可行性

- Windows 上默认使用 ONNX Runtime（TFLite 不可用）
- 不支持 Speex 噪声抑制（仅 Linux）
- 麦克风采集需 PyAudioWPatch 替代 PyAudio
- 预训练模型下载、推理流程在 Windows 上已验证可用

## 在第一阶段 MVP 中的建议

1. **训练中文唤醒词模型**：使用 openWakeWord 的自动训练管线（Google Colab notebook），用中文 TTS 引擎生成"小黄"、"小黄小黄"等唤醒词语料，快速训练一个基础模型。
2. **架构参考**：直接采用其 80ms 帧滑动窗口 + 阈值判断的推理循环模式。
3. **VAD 集成**：使用其内嵌的 Silero VAD 来减少环境噪音导致的误触发。
4. **暂不引入自定义验证模型**：MVP 阶段保持流程简单，后续迭代再加入。

## 相关资源

- 仓库：https://github.com/dscripka/openWakeWord
- Home Assistant 社区模型合集：https://github.com/fwartner/home-assistant-wakewords-collection
- C++ 移植版：https://github.com/rhasspy/openWakeWord-cpp
- Docker 部署版：https://github.com/dalehumby/openWakeWord-rhasspy
- microWakeWord (微控制器版)：https://github.com/kahrendt/microWakeWord
