# Launch Control, Readiness & Operation Lock Snippet

## Capability

Reliable single-instance desktop app startup with subprocess health monitoring and graceful shutdown.

## Source Pattern

Derived from desktop assistant launch orchestration patterns. Describes the interface shape and control flow, not copied source code.

## Interface Shape

```
LaunchController
  ├── acquire_lock() -> LockResult     # Try to acquire single-instance lock
  ├── release_lock()                   # Release lock on clean shutdown
  ├── is_stale_lock(lock) -> bool      # Detect crashed previous instance
  ├── start_service(name, cmd) -> Proc # Launch a subprocess
  ├── wait_ready(proc, timeout, interval) -> bool  # Poll until service is healthy
  ├── health_check(proc) -> bool       # Check if a managed process is still healthy
  └── shutdown()                       # Graceful shutdown: stop accepting, drain, close, release
```

## Control Flow

1. **Startup guard**: On launch, try to acquire a lock file (e.g. `%TEMP%\app_name.lock`). If lock exists, check if the PID inside is still alive. If alive, exit or activate existing window. If dead, clean up stale lock and proceed.
2. **Service initialization**: Launch dependent services (API server, STT engine, etc.) as subprocesses. For each, poll a readiness endpoint or flag with timeout.
3. **Runtime health**: Periodically check subprocess health. On failure, log, attempt restart (with backoff), and surface status to the user.
4. **Graceful shutdown**: On exit signal (WM_CLOSE, SIGTERM, Ctrl+C), stop accepting new work, drain pending operations, terminate subprocesses in reverse order, release lock file.

## Key Implementation Points

- **Lock file format**: Write PID and start timestamp as JSON. Stale if PID doesn't exist or start time is impossibly old.
- **Readiness polling**: Use exponential backoff up to a max interval. Example: 100ms → 200ms → 400ms → 500ms (cap) until timeout (default 30s).
- **Shutdown ordering**: Reverse of startup order. Services that depend on others must be stopped first.
- **Crash recovery**: On next launch, detect stale lock, log the previous crash, clean up, and start fresh. Do not block the user with a "previous instance crashed" dialog.

## What NOT to Copy

- Do not copy specific subprocess command lines or paths.
- Do not copy application-specific service names or configurations.
- The pattern is the interface shape and control flow, not any specific implementation.

## Related

- Code asset: `launch-control-readiness-pattern.asset.json`
- Adapter: `adapt-launch-control-to-desktop-assistant.md`
