# Windows Desktop Tool Playbook

Python desktop tools — Tkinter / PySide / Qt, system tray, single instance, packaging.

## When to use

- Windows desktop utility or launcher
- System tray application
- Voice assistant desktop entry (小黄)
- Local config tool, control panel, or settings UI
- EXE packaging for distribution

## Read first

- `domains/agent_workflow/AGENT_USAGE.md`
- `domains/agent_workflow/wiki/index.md`
- `domains/voice_assistant/AGENT_USAGE.md` (if voice-related)

## Architecture checklist

Every desktop tool must separate:

| Layer | Responsibility |
|-------|---------------|
| UI layer | Tkinter/PySide windows, tray icon, menus |
| Config layer | Read/write user config, separate from defaults |
| Local storage | File paths, SQLite, JSON config — never hardcoded |
| Background service | Long-running logic, wake word listener, API server |
| Single instance | Mutex or socket-based guard against double-launch |
| Shortcuts / hotkey | Global keyboard shortcuts if needed |
| Startup | Windows Startup folder or Task Scheduler registration |
| Logging | File-based logging with rotation |
| Packaging | PyInstaller or equivalent, smoke-tested |

## Windows-specific constraints

- **Path encoding**: Use `pathlib.Path`, not string concatenation. Use forward slashes in Bash/Git Bash, backslashes in PowerShell.
- **PowerShell**: Prefer `-NoProfile` to avoid conda encoding errors.
- **Permissions**: User config in `%APPDATA%`, not Program Files.
- **Antivirus**: PyInstaller output may trigger false positives. Sign if distributing.
- **Default config vs user config**: Ship defaults in source; user overrides in `%APPDATA%/<app>/config.json`.

## Completion verification

- [ ] App launches without errors
- [ ] Tray icon appears, right-click menu works
- [ ] Config persists across restart
- [ ] Second launch brings existing window to front (single instance)
- [ ] Startup registration works
- [ ] Packaged EXE smoke-tests cleanly
- [ ] Log file exists and is readable

## Anti-patterns

- Hardcoded paths (`C:\Users\xxx\...`)
- Config and defaults mixed in one file
- No logging
- No exception recovery — one crash kills everything
- GUI and core logic in the same class
- Packaging without smoke test
- Assuming `python` is on PATH for end users
