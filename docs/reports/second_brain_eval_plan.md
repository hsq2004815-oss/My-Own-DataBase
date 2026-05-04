# Second Brain Eval Plan

## Why now

The database has enough structure (domains, rules, playbooks, API, SQLite retrieval). The next step is verifying it actually improves agent output, not just looks organized.

## Why not automated

- The criteria are qualitative: style fit, engineering judgment, uncertainty awareness
- Automated scoring would require a second LLM judge, adding complexity and cost
- Manual comparison of 10 tasks is fast and gives direct feedback on what to fix

## How to execute

1. Run each of the 10 tasks in `evals/tasks/second_brain_eval_tasks.jsonl`
2. For each task, produce two outputs:
   - **Without database**: fresh agent session, no CLAUDE.md pointing to DataBase
   - **With database**: agent session with CLAUDE.md, API access, `use-local-database-for-task-playbook`
3. Compare against the criteria in `evals/README.md`
4. Record: task_id, passed/failed dimensions, what to fix

## Recording failures

| Failure type | Action |
|-------------|--------|
| Wrong domain routing | Fix routing table in playbook or AGENT_USAGE |
| Wrong playbook selection | Add or clarify playbook trigger conditions |
| No rule reuse | Add missing rule or improve retrieval |
| Wrong style default | Add aesthetic rule or clarify existing one |
| API assumed non-existent feature | Add to `api_domain_capability_boundary.md` |
| Raw contamination | Add guard to AGENT_USAGE or playbook |

## What counts as "database helps"

- Output includes engineering constraints, not just code
- Output matches documented preferences (not generic defaults)
- Output uses existing rules and reports which ones
- Output states what it doesn't know
- Agent avoids raw/ third-party code for ordinary tasks

## Next after evals

- Fix the top 3 failure patterns
- Re-run affected tasks
- Only then consider new domains or major expansion
