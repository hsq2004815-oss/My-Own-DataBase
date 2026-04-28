"""Call the local DataBase /brief API and print an agent-friendly summary.

My-Own-DataBase runtime context should come from the local FastAPI service.
GitHub is only for backup, inspection, and version synchronization.
"""

from __future__ import annotations

import argparse
import json
import sys
import textwrap
import urllib.error
import urllib.parse
import urllib.request
from typing import Any


DEFAULT_URL = "http://127.0.0.1:8765/brief"
START_COMMAND = (
    "cd E:\\DataBase\\backend_api\n"
    "python -m uvicorn app.main:app --host 127.0.0.1 --port 8765 --reload"
)


def health_url_for(brief_url: str) -> str:
    parsed = urllib.parse.urlparse(brief_url)
    return urllib.parse.urlunparse((parsed.scheme, parsed.netloc, "/health", "", "", ""))


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


def post_json(url: str, payload: dict[str, Any]) -> dict[str, Any]:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def get_json(url: str) -> dict[str, Any]:
    with urllib.request.urlopen(url, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def chunk_ids(chunks: list[dict[str, Any]]) -> list[str]:
    return [str(chunk.get("chunk_id", "")) for chunk in chunks if chunk.get("chunk_id")]


def asset_ids(assets: list[dict[str, Any]]) -> list[str]:
    return [str(asset.get("asset_id", "")) for asset in assets if asset.get("asset_id")]


def print_list(title: str, items: list[str]) -> None:
    print(title)
    if not items:
        print("- none")
        return
    for item in items:
        print(f"- {item}")


def compact_text(value: str, width: int = 110) -> str:
    return "\n".join(textwrap.wrap(" ".join(value.split()), width=width))


def print_chunk_summary(title: str, chunks: list[dict[str, Any]], show_content: bool) -> None:
    print(title)
    if not chunks:
        print("- none")
        return
    for chunk in chunks:
        chunk_id = chunk.get("chunk_id", "")
        section = chunk.get("section", "")
        source_name = chunk.get("source_name", "")
        print(f"- {chunk_id} [{section}] ({source_name})")
        if show_content:
            content = str(chunk.get("content", ""))
            print(textwrap.indent(compact_text(content[:700]), "  "))


def print_asset_summary(title: str, assets: list[dict[str, Any]], show_content: bool) -> None:
    print(title)
    if not assets:
        print("- none")
        return
    for asset in assets:
        asset_id = asset.get("asset_id", "")
        asset_type = asset.get("asset_type", "")
        usage_policy = asset.get("usage_policy", "")
        file_path = asset.get("file_path", "")
        print(f"- {asset_id} [{asset_type}, {usage_policy}]")
        if file_path:
            print(f"  path: {file_path}")
        if show_content:
            summary = str(asset.get("ai_summary", ""))
            if summary:
                print(textwrap.indent(compact_text(summary[:500]), "  "))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fetch a task brief from the local DataBase API; do not use GitHub as the default runtime source."
    )
    parser.add_argument("task", help="Task description to send to /brief.")
    parser.add_argument("--url", default=DEFAULT_URL, help=f"Brief API URL. Default: {DEFAULT_URL}")
    parser.add_argument("--ui", type=int, default=8, help="UI chunk limit. Default: 8")
    parser.add_argument("--workflow", type=int, default=2, help="Workflow chunk limit. Default: 2")
    parser.add_argument("--automation", type=int, default=0, help="Automation chunk limit. Default: 0")
    parser.add_argument("--assets", type=int, default=10, help="UI asset suggestion limit. Default: 10")
    parser.add_argument("--json", action="store_true", help="Print raw JSON response.")
    parser.add_argument("--content", action="store_true", help="Also print compact chunk content excerpts.")
    args = parser.parse_args()

    payload = {
        "task": args.task,
        "ui_limit": args.ui,
        "workflow_limit": args.workflow,
        "automation_limit": args.automation,
        "asset_limit": args.assets,
    }

    try:
        get_json(health_url_for(args.url))
        result = post_json(args.url, payload)
    except urllib.error.URLError as exc:
        print(f"Failed to call {args.url}: {exc}", file=sys.stderr)
        print("The local database API is not running or not reachable.", file=sys.stderr)
        print("\nStart the API first:\n", file=sys.stderr)
        print(START_COMMAND, file=sys.stderr)
        print("\nDo not fall back to GitHub unless the user explicitly asks.", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    print("DataBase Brief")
    print("=" * 14)
    print(f"Task: {result.get('brief', args.task)}")
    print()
    print_list("UI queries:", result.get("ui_queries", []))
    print()
    print_list("Workflow queries:", result.get("workflow_queries", []))
    print()
    print_list("Automation queries:", result.get("automation_queries", []))
    print()
    print_list("Asset queries:", result.get("asset_queries", []))
    print()
    print_chunk_summary("UI chunks:", result.get("ui_chunks", []), args.content)
    print()
    print_chunk_summary("Workflow chunks:", result.get("workflow_chunks", []), args.content)
    print()
    print_chunk_summary("Automation chunks:", result.get("automation_chunks", []), args.content)
    print()
    print_asset_summary("Asset suggestions:", result.get("asset_suggestions", []), args.content)
    print()
    print_list("Guidance:", result.get("guidance", []))
    print()
    print("Report these chunk_ids in your final handoff:")
    all_ids = (
        chunk_ids(result.get("ui_chunks", []))
        + chunk_ids(result.get("workflow_chunks", []))
        + chunk_ids(result.get("automation_chunks", []))
    )
    for item in all_ids:
        print(f"- {item}")
    print()
    print("Report these asset_ids if you used asset suggestions:")
    for item in asset_ids(result.get("asset_suggestions", [])):
        print(f"- {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
