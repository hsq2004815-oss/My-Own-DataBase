# Code Asset Reuse Rules

These rules supplement the existing agent workflow rules. They govern how agents find, evaluate, and reuse code assets from the database.

## What Code Assets Are

Code assets are structured, indexed records of reusable code capabilities stored under `processed/code_assets/`, with supporting `wiki/snippets/` and `wiki/adapters/` documentation. They are a **processed/wiki layer** asset — not raw source code.

Code assets do NOT replace existing `rules/`, `wiki/`, or `references/`. They sit alongside them as an additional lookup layer for when the task involves reusing code patterns, modules, or libraries across projects.

## Agent Lookup Order

When a task involves reusing code capabilities (launch control, settings UI, LLM routing, healthcheck, etc.), the agent MUST follow this order:

1. **Index first**: Check `wiki/indexes/code-assets-global-index.md` for relevant capability entries.
2. **Code assets second**: Read matching `processed/code_assets/*.asset.json` records for structured metadata, reuse level, and risks.
3. **Snippets/adapters third**: Read `wiki/snippets/` and `wiki/adapters/` for implementation guidance and adapter plans.
4. **Existing rules/wiki fourth**: Cross-reference with domain `rules/` and `wiki/` for additional constraints.

Do NOT default to scanning `raw/` for code reuse. `raw/` remains raw input material, not default agent context.

## Pre-Reuse Checks

Before reusing any code asset, the agent MUST verify:

1. **License**: Is the license clear and compatible? GPL/AGPL and no-license code MUST NOT be marked for direct use or code copying.
2. **Dependencies**: Are dependencies controlled and compatible with the target project?
3. **Windows compatibility**: Does the asset work on Windows if the target is Windows?
4. **Adapter layer**: Does the asset need an adapter? Will the adapter pollute the main pipeline?
5. **Tests**: Are tests defined? Can they be written before integration?
6. **Real verification**: Has the asset been verified in a real project context?

## Reuse Level Decision Tree

```
Can it be used as a pip/npm dependency directly?
  YES → direct_dependency (e.g. FastAPI, playwright, pystray)
  NO  → Is the pattern clear enough to reimplement?
           YES → implementation_pattern
           NO  → Can a small module be extracted with clear boundaries?
                    YES → extractable_module (check license first)
                    NO  → research_only
```

## Reuse Policy Decision Tree

```
Is license permissive (MIT, Apache-2.0, BSD)?
  YES → Can it be a direct dependency? → direct_use_allowed
        Needs wrapping? → adapter_required
  NO  → Is license GPL/AGPL or absent?
          YES → do_not_copy_code (or research_only)
          NO  → license_review_required
```

## What NOT to Do

- Do NOT copy large blocks of raw source code into wiki or code asset records.
- Do NOT mark GPL/AGPL or unlicensed code as `direct_use_allowed` or `extractable_module`.
- Do NOT skip the adapter layer assessment — even a good pattern can pollute the main pipeline if wired in directly.
- Do NOT treat code assets as the only source of truth; always cross-reference with domain rules.
- Do NOT scan entire `raw/` directories to find code assets; use indexes first.

## Relationship to Existing Rules

- `raw/` → original sources, not default context.
- `processed/code_assets/` → structured code capability records (this layer).
- `wiki/snippets/` → human-readable pattern descriptions.
- `wiki/adapters/` → integration plans for target projects.
- `wiki/indexes/` → capability-based lookup for agents.
- `rules/` → domain-level engineering rules (unchanged).
- `wiki/topics/` → domain-level topic summaries (unchanged).
- `references/` → domain-level reference JSON (unchanged).

This layer adds code reuse guidance without modifying or replacing any existing layer.

---

## Related Knowledge

### Belongs To
- [Agent Workflow AGENT_USAGE](../AGENT_USAGE.md)
- [Agent Workflow Wiki Index](../wiki/index.md)

### Related Rules
- [Code Assets Global Index](../wiki/indexes/code-assets-global-index.md)
- [Code Asset Intake Checklist](../wiki/checklists/code-asset-intake-checklist.md)
- [Code Asset Record Template](../wiki/templates/code-asset-record-template.md)
