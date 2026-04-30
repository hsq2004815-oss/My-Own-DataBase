# TTS 引擎笔记 —— 小黄第二阶段及以后

> 生成时间：2026-04-30
> 数据来源：edge-tts (README/LICENSE/setup.py/examples)
> 注意：第一阶段 MVP **不包含 TTS**，本文档为第二阶段 (单轮语音回复) 及以后的准备工作。

## 一、当前已入库 TTS 相关项目

| 项目 | 类型 | 来源 | 本地路径 | 许可 |
|------|------|------|----------|------|
| edge-tts | 云端 TTS (Python) | 本次入库 | `raw/github/repos/edge-tts` | LGPLv3 + MIT |
| (VoiceClaw 内) Edge TTS | 云端 TTS (集成) | 第一批入库 | `raw/github/repos/voiceclaw` | MIT |

## 二、edge-tts 详细分析

### 2.1 基本信息

- **GitHub：** https://github.com/rany2/edge-tts
- **原理：** 调用 Microsoft Edge 浏览器的 Read Aloud TTS 云端 API (WebSocket 协议)
- **安装：** `pip install edge-tts`
- **CLI 工具：** `edge-tts` (生成 mp3+字幕), `edge-playback` (播放)
- **Python API：** 支持同步和异步模式

### 2.2 中文声音

300+ 声音中，中文相关声音如下 (未全部列出)：

| 声音 ID | 性别 | 语言 |
|---------|------|------|
| zh-CN-XiaoxiaoNeural | Female | 普通话 |
| zh-CN-YunxiNeural | Male | 普通话 |
| zh-CN-YunjianNeural | Male | 普通话 |
| zh-CN-XiaoyiNeural | Female | 普通话 |
| zh-CN-YunyangNeural | Male | 普通话 |
| zh-HK-HiuGaaiNeural | Female | 粤语 |
| zh-HK-HiuMaanNeural | Female | 粤语 |
| zh-HK-WanLungNeural | Male | 粤语 |
| zh-TW-HsiaoChenNeural | Female | 台湾普通话 |
| zh-TW-HsiaoYuNeural | Female | 台湾普通话 |
| zh-TW-YunJheNeural | Male | 台湾普通话 |

**MVP 推荐：** `zh-CN-XiaoxiaoNeural` (女声，自然流畅，最常用的中文声音)

### 2.3 可调参数

- `--rate`：语速 (-50% ~ +100%)
- `--volume`：音量 (-50% ~ +100%)
- `--pitch`：音调 (-50Hz ~ +50Hz)

### 2.4 输出格式

- 音频：mp3
- 字幕：SRT (带时间戳)

### 2.5 核心局限

| 局限 | 影响 |
|------|------|
| 必须联网 | 无网络时完全无法工作 |
| 依赖微软非官方 API | API 可能随时变更或被限制 |
| 无流式音频输出 | 需等待完整 mp3 生成后才能播放 (延迟较高) |
| LGPLv3 许可 | 商业闭源使用需注意合规 (动态链接可满足) |
| 自定义 SSML 受限 | 微软仅允许 `<voice>` + `<prosody>` 标签 |

### 2.6 License 详解

```
src/edge_tts/srt_composer.py → MIT
所有其他文件 → LGPLv3
```

LGPLv3 要求：如果修改了库源码，需要公开修改；如果仅通过 pip 安装后动态链接，对小黄项目的许可无影响。对 MVP 来说，通过 `pip install edge-tts` 使用即可满足 LGPLv3 合规要求。

## 三、第一阶段 MVP 中的 TTS

**第一阶段不包含 TTS。** MVP 链路是：

```
说"小黄" → 音波悬浮窗 → 听一句话 → 转文字显示
```

没有语音回复环节。

## 四、第二阶段 (单轮语音回复) 的 TTS 选择

当第一阶段完成后，第二阶段将加入单轮语音回复，此时需要考虑 TTS 引擎。

### 4.1 候选 TTS 引擎

| 引擎 | 类型 | 中文质量 | 离线 | 许可 | 备注 |
|------|------|---------|------|------|------|
| edge-tts | 云端 | 好 | 否 | LGPLv3 + MIT | 当前唯一已入库 TTS |
| Piper | 本地 | 中 | 是 | MIT | 未入库 (候选) |
| CosyVoice | 本地 | 好 | 是 | Apache 2.0 | 未入库 (候选，阿里) |
| ChatTTS | 本地 | 好 | 是 | CC BY-NC 4.0 | 未入库 (候选，非商用) |

### 4.2 推荐路线

**短期 (MVP 验证阶段)：edge-tts**
- 快速集成，中文声音自然
- 适合 Demo 和功能验证
- 注意联网依赖

**长期 (正式版本)：Piper 或 CosyVoice**
- 完全离线，隐私友好
- 许可更宽松
- 需评估中文声音自然度和推理性能

## 五、未入库但值得关注的 TTS 项目

这些项目尚未下载到 raw 目录，仅供后续参考：

| 项目 | GitHub | 特点 |
|------|--------|------|
| Piper | https://github.com/rhasspy/piper | 本地 TTS (C++), ONNX 导出, 多种语言, MIT |
| CosyVoice | https://github.com/FunAudioLLM/CosyVoice | 阿里开源, 中文 TTS 专项, 零样本声音克隆 |
| ChatTTS | https://github.com/2noise/ChatTTS | 对话式中文 TTS, 韵律自然 |
| Coqui TTS | https://github.com/coqui-ai/TTS | 通用 TTS 框架 (已停止维护) |
| XTTS-v2 | https://github.com/coqui-ai/TTS | 多语言 + 声音克隆 (Coqui 生态) |

## 六、edge-tts 代码使用示例

```python
import edge_tts

# 同步方式
async def main():
    communicate = edge_tts.Communicate(
        "你好，我是小黄。",
        "zh-CN-XiaoxiaoNeural"
    )
    await communicate.save("output.mp3")

# 命令行
# edge-tts --voice zh-CN-XiaoxiaoNeural --text "你好" --write-media output.mp3
```

## 七、结论

- edge-tts 是当前唯一已入库的 TTS 引擎，适合快速验证
- 第一阶段不需要 TTS
- 第二阶段建议先用 edge-tts 跑通流程，再评估离线替代方案
- 长期应入库 Piper 和/或 CosyVoice 作为离线 TTS 候选
