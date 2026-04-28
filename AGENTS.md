# AGENTS.md

Follow `AGENT.md` for this repository.

This file exists because many coding agents automatically look for `AGENTS.md`. The canonical local guidance is in `AGENT.md`, and direct user instructions still override both files.

## Runtime Access Rule

Use the local FastAPI service as the default runtime source for My-Own-DataBase:

```text
http://127.0.0.1:8765
```

When a user says "根据我的数据库", "用我的数据库", "按我的数据库规则", "调用我的数据库", "based on my database", or "use my database", call `GET /health` and then `POST /brief` before doing the task.

GitHub is only for backup, inspection, ChatGPT structure review, and version synchronization. Do not default to GitHub or scan the whole repository for runtime context unless the local API is unavailable and the user explicitly allows file reading.

For UI/frontend/portfolio/landing page tasks that ask for high-end motion, animation, Lottie, visual effects, or advanced interaction, also call `/assets/search` for the motion asset queries listed in `AGENT.md`. Final output must report retrieved asset/chunk ids, usage policy, direct-use versus inspiration-only status, and the CSS/SVG/Canvas/Lottie/video implementation path.
