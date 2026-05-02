# Adapter: Multi-Domain Knowledge Retrieval → New Domain

## Target

Adapt the multi-domain knowledge retrieval API pattern to add a new knowledge domain to an existing retrieval service.

## Source Asset

- `multi-domain-knowledge-retrieval-api` (extractable_module, adapter_required)

## Adapter Checklist

### 1. Define the Chunk Model

Create a Pydantic model for your new domain's chunks:

```python
class NewDomainChunkResult(BaseModel):
    chunk_id: str
    title: str
    content: str
    # ... domain-specific fields
```

### 2. Create the Database

Follow the index builder pipeline pattern:
- Define chunk JSONL schema
- Add validation rules (required fields, enums, secret detection)
- Run --dry-run → fix errors → --write with --backup

### 3. Add Connect Function

```python
NEW_DOMAIN_DB_PATH = ROOT / "runtime" / "db" / "sqlite" / "new_domain" / "new_domain_references.db"

def connect_new_domain() -> sqlite3.Connection:
    return connect_db(NEW_DOMAIN_DB_PATH, "New domain DB not found. Run build script first.")
```

### 4. Add Search Functions

Implement the three-strategy search: FTS5 → LIKE → multi-term LIKE. Reuse the existing search utility functions or implement domain-specific ones if the schema differs significantly.

### 5. Add Scoring Function

Define `new_domain_chunk_score(chunk, query, query_index)` with domain-appropriate weights. Reuse the shared scoring infrastructure (SECTION_PRIORITY, etc.) where applicable.

### 6. Add Query Derivation Rules

Add a `NEW_DOMAIN_QUERY_RULES` list and context terms for auto-detection:

```python
NEW_DOMAIN_QUERY_RULES = [
    (("trigger1", "触发词1"), "search query string"),
    ...
]
```

### 7. Add API Endpoints

```python
@app.get("/new_domain/search", response_model=list[NewDomainChunkResult])
def search_new_domain(q: str, limit: int = 5) -> list[NewDomainChunkResult]:
    ...
```

### 8. Update /brief

Add `new_domain_limit` to BriefRequest, add new domain search to build_brief_response(), update guidance messages.

### 9. Update /health

Add new domain DB path, existence check, and chunk count to the health response.

### Will It Pollute the Main Pipeline?

**No**, if each domain is added as an independent module. The pattern isolates domain-specific logic behind:
- Separate DB paths and connect functions
- Separate Pydantic models
- Separate search/score/merge functions
- Separate query derivation rules

The shared infrastructure (connect_db, ranked merge, API logging) is domain-agnostic.

### Testing the New Domain

1. **Search tests**: Run validation harness (search-validation-test-harness) with domain-specific test cases.
2. **API tests**: Verify new endpoints return correct response models.
3. **Brief tests**: Verify /brief returns new domain chunks when task triggers match.
4. **Health tests**: Verify /health reports new domain DB status.

### Rollback Plan

- Remove the new domain's endpoint functions and BriefRequest field.
- Delete the new domain's SQLite DB.
- The rest of the API continues to work unchanged.
