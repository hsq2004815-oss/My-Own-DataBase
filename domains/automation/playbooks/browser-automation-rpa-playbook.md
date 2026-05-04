# Browser Automation / RPA Playbook

Playwright, Selenium, Puppeteer — file upload, iframe, modal, navigation patterns.

## When to use

- Browser automation, web scraping, RPA, form filling, file upload
- CDP-based debugging, screenshot verification, login-state browser
- User mentions "自动化", "浏览器", "上传", "爬取", "Playwright", "Selenium", "截图验证"

## Read first

- `domains/automation/AGENT_USAGE.md`
- `domains/automation/wiki/topics/persistent-browser-daemon-for-agent-qa.md`
- `domains/automation/wiki/patterns/browser-qa-with-persistent-session.md`

## Preflight checklist

- [ ] Is the target site accessible?
- [ ] Is login state needed?
- [ ] Are there overlays, modals, or system dialogs expected?
- [ ] Is the flow repeatable, or is it one-shot?

## Selector strategy

Priority order:
1. `role` / `aria-label` / `data-testid`
2. `text=` selectors (stable across layout changes)
3. CSS selectors (id > class > nested)
4. Never: fixed coordinates, nth-child with fragile indices

If a click fails:
- Check if a toast, modal, or overlay is blocking
- Wait for element to be visible AND enabled
- Scroll into view before clicking

## Upload strategy

Separate upload into stages:
1. **File selection** — `setInputFiles()` or file chooser dialog
2. **Upload trigger** — click the upload button
3. **Transfer confirmation** — wait for progress bar or status text change
4. **Server acknowledgement** — wait for success response in network or DOM
5. **Page state refresh** — confirm the uploaded file appears in the UI

Do NOT assume upload is done after `setInputFiles()` or button click alone.

## iframe / modal / overlay strategy

- Switch to iframe context before interacting inside it
- Switch back after
- For modals: wait for backdrop, then target modal content
- System dialogs (QQ notifications, Windows alerts) can steal focus — expect them

## URL navigation strategy

- URL-based navigation is more stable than click chains
- Not every flow can be URL-encoded (multi-step wizards, file uploads)
- Prefer URL when possible; fall back to selector chains when necessary

## Retry / timeout / logging

Every automation must have:
- Per-action timeout (default: 30s)
- Retry on transient failure (max 3 attempts)
- Screenshot on failure
- Structured log of each step: action, target, result, duration

## Completion verification

After the automation finishes:
- [ ] Did every step complete or log a clear failure?
- [ ] Was page state verified after each action?
- [ ] Are screenshots saved for debug?
- [ ] Did the automation stop cleanly (browser closed, no orphan processes)?

## Anti-patterns

- Fixed coordinates for clicks
- `page.waitForTimeout(5000)` as a substitute for proper `waitForSelector()`
- Silent failure — action says "done" but page state unchanged
- No retry, no timeout, no screenshot
- Treating file select as upload completion
- Ignoring overlays and modals
