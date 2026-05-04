# Evals — Minimum Viable Evaluation

## Purpose

Verify that the database actually makes Claude Code / Codex / opencode output better, not just structurally bigger.

## What we evaluate

Not automated benchmarks. Human comparison of two outputs:

1. **Baseline**: Agent output without database access
2. **Database-assisted**: Agent output after following `CLAUDE.md → AGENT_USAGE.md → domain AGENT_USAGE.md → playbook → rules`

## Evaluation criteria

| Dimension | What to check |
|-----------|--------------|
| Domain routing | Did it pick the right domain? |
| Playbook usage | Did it follow the right playbook? |
| Style fit | Does output match my preferences? |
| Less drift | Did it avoid wandering into wrong territory? |
| Engineering detail | Did it include constraints/checks, not just code? |
| Rule reuse | Did it apply existing rules? |
| Uncertainty | Did it state what it doesn't know? |
| Raw avoidance | Did it stay out of raw/ and third-party code? |

## How to run

1. Pick a task from `evals/tasks/second_brain_eval_tasks.jsonl`
2. Run it without database (fresh session, no CLAUDE.md pointing to DataBase)
3. Run it with database (session with CLAUDE.md, API access)
4. Compare outputs against the criteria above
5. Record findings

## Failing an eval

A failed eval is more valuable than no eval. Record:
- What failed
- Why (wrong routing? missing playbook? no rule for this case?)
- What to add or fix
- Do NOT rewrite the whole database because of one failure
