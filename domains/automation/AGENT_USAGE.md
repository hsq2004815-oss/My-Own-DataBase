# Automation AGENT_USAGE

## Purpose

Use this domain for browser automation, Playwright, Chrome CDP, persistent browser sessions, upload flows, screenshots, iframe/modal handling, selector strategy, and browser QA.

## When to Use

- Browser automation or RPA tasks
- Upload, iframe, modal, selector, or CDP debugging
- Persistent logged-in browser sessions
- Screenshot or browser QA verification

## Read First

1. [Automation wiki index](wiki/index.md)
2. [Browser Automation RPA Playbook](playbooks/browser-automation-rpa-playbook.md)
3. [Persistent Browser Daemon for Agent QA](wiki/topics/persistent-browser-daemon-for-agent-qa.md)
4. [Browser QA with Persistent Session](wiki/patterns/browser-qa-with-persistent-session.md)
5. [Automation README](README.md)

## Task Routing

- Need logged-in browser state: persistent browser daemon topic
- Need visual or interaction verification: browser QA pattern
- Need upload/iframe/modal troubleshooting: automation domain first, then task-specific code

## Do Not Use by Default

- automation context for ordinary UI design tasks
- raw browser state assumptions without verification

## Output Requirements

- Report selectors.
- Report browser/session assumptions.
- Report verification performed and any remaining manual steps.
