# Query Derivation Engine Interface Snippet

## Capability

Derive structured search queries from natural language task descriptions using rule-based keyword matching.

## Interface Shape

```
QueryDerivationEngine
  ├── add_rules(domain: str, rules: list[tuple[tuple[str,...], str]]) -> None
  ├── add_synonyms(synonyms: dict[str, str]) -> None
  ├── normalize(text: str) -> str
  ├── derive(task: str, domain: str) -> list[str]
  ├── derive_all(task: str, domains: list[str]) -> dict[str, list[str]]
  └── set_defaults(domain: str, defaults: list[str]) -> None
```

## Key Implementation Points

- **Trigger matching**: case-insensitive substring match. Each rule is `((trigger1, trigger2, ...), query_string)`. If any trigger is found in the task text, the query string is included.
- **Synonym expansion**: before rule matching, normalize the task text by replacing known synonyms (e.g. "玻璃拟态" → "liquid glass").
- **Deduplication**: preserve insertion order, case-insensitive dedup.
- **Defaults**: if no rules match for a domain, return domain-specific defaults.
- **Cap**: maximum 5 derived queries per domain to avoid search explosion.

## What NOT to Copy

- Do not copy specific query rules or trigger terms — they are domain-specific.
- Do not copy synonym dictionaries — build your own for your domain.
- The pattern is the pipeline: normalize → match triggers → dedupe → cap → fallback defaults.

## Related

- Code asset: `query-derivation-engine.asset.json`
