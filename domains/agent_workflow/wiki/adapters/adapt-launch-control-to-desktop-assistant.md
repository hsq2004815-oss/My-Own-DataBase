# Adapter: Launch Control → Desktop Assistant

## Target

Adapt the launch-control-readiness pattern to any desktop assistant, Windows tray tool, or long-running agent application.

## Source Asset

- `launch-control-readiness-pattern` (implementation_pattern, adapter_required)

## Adapter Design

### Where to Put It

Create a single-file adapter in the target project:

```
src/<project>/launch_controller.py    # Generic launch orchestration
```

This adapter should NOT be mixed into the main application logic. It is a standalone orchestration layer that imports and coordinates other services.

### What the Adapter Provides

```
class LaunchController:
    """Generic desktop app launch orchestrator."""

    def __init__(self, app_name: str, lock_dir: str | None = None):
        """
        app_name: used for lock file naming and log prefix
        lock_dir: directory for lock file (default: %TEMP% or /tmp)
        """

    def acquire_lock(self) -> bool:
        """Try to acquire single-instance lock. Returns False if another instance is alive."""

    def release_lock(self) -> None:
        """Release the lock file. Call in finally block."""

    def start_services(self, services: list[ServiceConfig]) -> list[subprocess.Popen]:
        """Start named services from config. Returns list of process handles."""

    def wait_all_ready(self, procs: list[subprocess.Popen], timeout: float = 30.0) -> bool:
        """Poll all services until ready or timeout. Returns True if all ready."""

    def monitor_health(self, procs: list[subprocess.Popen], on_unhealthy: Callable) -> None:
        """Start background health monitor. Calls on_unhealthy(service_name, proc) on failure."""

    def shutdown(self, procs: list[subprocess.Popen]) -> None:
        """Graceful shutdown: reverse-order terminate, wait, kill, release lock."""
```

### Integration Points

| Project Type | Where to Wire In |
|-------------|-----------------|
| Desktop tray app | `main()` before `pystray.run()` |
| Voice assistant | `voice_overlay.py` main orchestration |
| Windows automation tool | Entry point before scheduling loop |
| Backend API server | `app/main.py` lifespan context manager |

### Will It Pollute the Main Pipeline?

**No**, if the adapter stays as a separate file imported only at the entry point. The main application logic (config, LLM, voice, UI) should not import or depend on `launch_controller.py`. The dependency direction is: entry point → launch controller → services.

### Testing the Adapter

1. **Unit tests** (no real subprocess):
   - Lock acquire/release with temp directory
   - Stale lock detection with fake PID
   - Service config validation

2. **Integration tests** (real subprocess):
   - Start a dummy HTTP server, poll `/health`, verify ready
   - Kill a subprocess, verify health monitor fires callback
   - Shutdown with active subprocess, verify clean exit
   - Launch twice, verify second instance detects lock

3. **Real verification**:
   - Run on target Windows version with actual services
   - Test crash recovery: kill process, restart, verify lock cleanup
   - Test with antivirus that may block lock file creation

### Rollback Plan

- The adapter is a single file with a clear interface. To roll back, remove the import from the entry point and delete the file.
- No changes to other services are required.
- Lock file is in %TEMP% and will be cleaned up on next reboot even if the adapter is removed.

### Risks

- Lock file directory may not be writable on locked-down enterprise Windows. Fall back to a user-local app data directory.
- Some antivirus software flags lock files in %TEMP%. Consider using `%LOCALAPPDATA%\<app_name>\lock` instead.
- Subprocess termination on Windows can hang indefinitely. Always use a kill timeout after graceful close.

## Related

- Snippet: `launch-control-readiness-operation-lock.md`
- Code asset: `launch-control-readiness-pattern.asset.json`
