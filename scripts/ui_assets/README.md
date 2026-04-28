# UI Asset Scripts

Scripts for maintaining `domains/ui_assets`.

## Scripts

- `ingest_assets.py`: copy local files into the asset domain and create baseline metadata.
- `register_collections.py`: register large local libraries as collection-level metadata.
- `enrich_metadata.py`: enrich existing screenshot/video metadata and generate retrieval chunks without moving raw assets.
- `search_assets.py`: search asset metadata using the same ranking helpers as the local API.

## Enrich Metadata

```powershell
python E:\DataBase\scripts\ui_assets\enrich_metadata.py --check
python E:\DataBase\scripts\ui_assets\enrich_metadata.py
```

The enrichment script updates `processed/metadata/*.json` and writes `processed/chunks/*.json`.
It does not move, copy, or modify files under `raw`.

The Lottie Web collection remains collection-level metadata. Enrichment writes
summary chunks for loading animation, micro interaction, hover motion, JSON web
animation, animated icons, and implementation notes. Its `usage_policy` remains
`review_required`; direct commercial use requires license confirmation.

## Search

```powershell
python E:\DataBase\scripts\ui_assets\search_assets.py "lottie loading animation"
python E:\DataBase\scripts\ui_assets\search_assets.py "高级 小动画 hover 微交互"
```
