# UI Asset Scripts

Scripts for maintaining `domains/ui_assets`.

## Scripts

- `ingest_assets.py`: copy local files into the asset domain and create baseline metadata.
- `register_collections.py`: register large local libraries as collection-level metadata.
- `enrich_metadata.py`: enrich existing screenshot/video metadata and generate retrieval chunks without moving raw assets.

## Enrich Metadata

```powershell
python E:\DataBase\scripts\ui_assets\enrich_metadata.py --check
python E:\DataBase\scripts\ui_assets\enrich_metadata.py
```

The enrichment script updates `processed/metadata/*.json` and writes `processed/chunks/*.json`.
It does not move, copy, or modify files under `raw`.
