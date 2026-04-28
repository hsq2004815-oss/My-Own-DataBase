"""Search UI asset metadata using the same ranking as the local API."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend_api.app.main import search_assets_records  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Search UI asset metadata.")
    parser.add_argument("query", help="Search query, for example: lottie loading animation")
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--asset-type", default="")
    parser.add_argument("--usage-policy", default="")
    args = parser.parse_args()

    rows = search_assets_records(
        q=args.query,
        limit=args.limit,
        asset_type=args.asset_type or None,
        usage_policy=args.usage_policy or None,
    )
    if not rows:
        print("No results")
        return 0

    for index, row in enumerate(rows, start=1):
        print(f"[{index}] {row.asset_id} | {row.asset_type} | {row.usage_policy}")
        if row.style_tags:
            print(f"tags: {', '.join(row.style_tags[:12])}")
        if row.use_cases:
            print(f"use_cases: {', '.join(row.use_cases[:8])}")
        print(row.ai_summary[:520])
        if row.file_path:
            print(f"path: {row.file_path}")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
