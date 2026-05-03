# Voice Assistant AGENT_USAGE

## Purpose

Use this domain for XiaoHuang voice assistant context, wake word detection, STT/TTS engine selection, desktop voice pipeline design, and Windows voice assistant planning.

## When to Use

- XiaoHuang voice assistant planning
- Wake word, KWS, STT, TTS, VAD, or command trigger design
- Windows desktop voice assistant architecture
- Voice pipeline tradeoff review

## Read First

1. [Voice Assistant README](README.md)
2. [Voice Assistant wiki index](wiki/index.md)
3. [XiaoHuang Project Context](wiki/topics/xiaohuang_project_context.md)
4. [XiaoHuang Voice Pipeline Notes](wiki/topics/xiaohuang_voice_pipeline_notes.md)
5. [Wake Word Trigger Command](wiki/topics/wake_word_trigger_command.md)
6. [STT Engine Comparison](wiki/topics/stt_engine_comparison.md)
7. [TTS Engine Notes](wiki/topics/tts_engine_notes.md)

Raw repos are only reference material. Prefer the distilled wiki notes before reading `raw/github/repos`.

## Task Routing

- Wake word / KWS: wake word trigger and detection topics
- STT choice: STT engine comparison plus FunASR notes
- TTS quick validation: TTS engine notes
- Windows desktop voice assistant: XiaoHuang project context and pipeline notes

## Do Not Use by Default

- raw repo source before distilled wiki notes
- model files or licenses as reusable assets without review

## Output Requirements

- Report which voice pipeline notes affected the result.
- Report engine comparisons and raw-project constraints.
- State uncertainty around license, model availability, and Windows integration.
