"""Import local UI assets into the ui_assets domain.

The script copies files from a source directory, classifies them by extension
and filename hints, and creates JSON metadata records. It intentionally defaults
to usage_policy=review_required so unknown web downloads are not treated as
direct-use project assets.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DOMAIN_ROOT = ROOT / "domains" / "ui_assets"
RAW_ROOT = DOMAIN_ROOT / "raw"
METADATA_DIR = DOMAIN_ROOT / "processed" / "metadata"
IMPORT_LOG = DOMAIN_ROOT / "registry" / "import_log.jsonl"

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif", ".bmp", ".tif", ".tiff"}
VIDEO_EXTENSIONS = {".mp4", ".webm", ".mov", ".m4v", ".avi"}
VECTOR_EXTENSIONS = {".svg"}
CODE_EXTENSIONS = {".html", ".css", ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte"}
DESIGN_EXTENSIONS = {".fig", ".sketch", ".xd", ".psd", ".ai"}
FONT_EXTENSIONS = {".woff", ".woff2", ".ttf", ".otf", ".eot"}
DEFAULT_EXCLUDE_DIRS = {
    ".git",
    "node_modules",
    ".next",
    "dist",
    "build",
    ".cache",
    "__pycache__",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha1_file(path: Path) -> str:
    digest = hashlib.sha1()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", value).strip("-")
    return value or "asset"


def infer_tags(name: str) -> list[str]:
    lower = name.lower()
    mapping = {
        "liquid-glass": ["liquid", "glass", "玻璃"],
        "aurora": ["aurora", "极光"],
        "caustics": ["caustic", "caustics", "水纹", "折射"],
        "data-current": ["data", "particle", "particles", "数据流", "粒子"],
        "dark": ["dark", "black", "暗色", "黑色"],
        "neon": ["neon", "glow", "霓虹", "发光"],
        "premium": ["premium", "luxury", "高级"],
        "dashboard": ["dashboard", "仪表盘", "看板"],
        "modal": ["modal", "dialog", "弹窗"],
        "button": ["button", "btn", "按钮"],
        "toast": ["toast", "notification", "通知"],
        "texture": ["texture", "noise", "grain", "纹理"],
    }
    tags = []
    for tag, needles in mapping.items():
        if any(needle in lower for needle in needles):
            tags.append(tag)
    return tags


def classify_asset(path: Path) -> tuple[str, str]:
    lower = path.stem.lower()
    ext = path.suffix.lower()

    background_hints = (
        "bg",
        "background",
        "backdrop",
        "hero",
        "scene",
        "aurora",
        "caustic",
        "water",
        "particle",
        "dataflow",
        "data-current",
        "背景",
        "极光",
        "水纹",
        "粒子",
        "数据流",
    )
    texture_hints = ("texture", "noise", "grain", "pattern", "纹理", "噪声")
    control_hints = ("button", "btn", "toggle", "input", "control", "按钮", "控件")
    surface_hints = ("card", "panel", "window", "modal", "dialog", "surface", "窗口", "卡片", "弹窗")
    icon_hints = ("icon", "logo", "glyph", "图标")
    screenshot_hints = ("screenshot", "screen", "reference", "inspiration", "shot", "截图", "参考")

    def has_any(words: tuple[str, ...]) -> bool:
        return any(word in lower for word in words)

    if ext in VIDEO_EXTENSIONS:
        if has_any(background_hints):
            return "background_video", "backgrounds"
        return "motion_reference", "videos"
    if ext in IMAGE_EXTENSIONS:
        if has_any(texture_hints):
            return "texture", "textures"
        if has_any(control_hints):
            return "control", "controls"
        if has_any(surface_hints):
            return "surface", "surfaces"
        if has_any(icon_hints):
            return "icon", "icons"
        if has_any(screenshot_hints):
            return "screenshot_reference", "screenshots"
        if has_any(background_hints):
            return "background_image", "backgrounds"
        return "screenshot_reference", "images"
    if ext in VECTOR_EXTENSIONS:
        if has_any(background_hints):
            return "background_image", "backgrounds"
        if has_any(icon_hints):
            return "icon", "icons"
        if has_any(control_hints):
            return "control", "controls"
        if has_any(surface_hints):
            return "surface", "surfaces"
        return "component_code", "components"
    if ext in CODE_EXTENSIONS:
        return "component_code", "components"
    if ext in FONT_EXTENSIONS:
        return "font", "fonts"
    if ext in DESIGN_EXTENSIONS:
        return "design_file", "design_files"
    return "unknown", "unknown"


def unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    index = 2
    while True:
        candidate = parent / f"{stem}-{index}{suffix}"
        if not candidate.exists():
            return candidate
        index += 1


def iter_files(source: Path, exclude_dirs: set[str], include_ext: set[str] | None) -> list[Path]:
    files: list[Path] = []
    for path in sorted(source.rglob("*")):
        if not path.is_file():
            continue
        parts = set(path.relative_to(source).parts[:-1])
        if parts & exclude_dirs:
            continue
        if include_ext is not None and path.suffix.lower() not in include_ext:
            continue
        files.append(path)
    return files


def build_metadata(
    source_path: Path,
    copied_path: Path,
    asset_type: str,
    usage_policy: str,
    digest: str,
    source_name: str,
    source_url: str,
    license_label: str,
    license_notes: str,
) -> dict[str, Any]:
    tags = infer_tags(source_path.name)
    asset_id = f"{slugify(source_path.stem)}-{digest[:8]}"
    summary_tags = ", ".join(tags) if tags else asset_type.replace("_", " ")
    return {
        "asset_id": asset_id,
        "domain": "ui_assets",
        "asset_type": asset_type,
        "usage_policy": usage_policy,
        "files": {
            "file_path": str(copied_path),
            "preview_path": "",
            "original_path": str(source_path),
            "sha1": digest,
            "size_bytes": source_path.stat().st_size,
            "extension": source_path.suffix.lower(),
        },
        "source": {
            "name": source_name,
            "url": source_url,
            "captured_at": utc_now(),
            "notes": "Imported by scripts/ui_assets/ingest_assets.py",
        },
        "license": {
            "label": license_label,
            "notes": license_notes,
        },
        "style_tags": tags,
        "use_cases": [],
        "avoid_when": [],
        "implementation_notes": [],
        "quality": {
            "curation_status": "new",
            "notes": "Review usage_policy and license before direct project use.",
        },
        "retrieval": {
            "ai_summary": f"{asset_type.replace('_', ' ')} asset for {summary_tags}. Review usage policy before use.",
            "prompt_tags": tags + [asset_type.replace("_", "-")],
            "negative_prompt_tags": [],
        },
    }


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def append_log(event: dict[str, Any]) -> None:
    IMPORT_LOG.parent.mkdir(parents=True, exist_ok=True)
    with IMPORT_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False, separators=(",", ":")) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Import local UI assets into E:\\DataBase\\domains\\ui_assets.")
    parser.add_argument("source", type=Path, help="Folder containing downloaded or generated assets.")
    parser.add_argument(
        "--usage-policy",
        choices=["direct_use", "inspiration_only", "internal_reference", "review_required", "unknown"],
        default="review_required",
    )
    parser.add_argument("--source-name", default="local import")
    parser.add_argument("--source-url", default="")
    parser.add_argument("--license", default="review required")
    parser.add_argument("--license-notes", default="Review license before using this asset in a project.")
    parser.add_argument(
        "--include-ext",
        default="",
        help="Comma-separated extension allowlist, for example .mp4,.webm,.png",
    )
    parser.add_argument(
        "--exclude-dir",
        action="append",
        default=[],
        help="Directory name to skip. Can be repeated. Defaults include .git, node_modules, dist, build.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print planned imports without copying files.")
    args = parser.parse_args()

    source = args.source.resolve()
    if not source.exists() or not source.is_dir():
        raise SystemExit(f"Source folder not found or not a directory: {source}")

    include_ext = None
    if args.include_ext.strip():
        include_ext = {
            item.strip().lower() if item.strip().startswith(".") else f".{item.strip().lower()}"
            for item in args.include_ext.split(",")
            if item.strip()
        }
    exclude_dirs = DEFAULT_EXCLUDE_DIRS | set(args.exclude_dir)
    files = iter_files(source, exclude_dirs=exclude_dirs, include_ext=include_ext)
    if not files:
        raise SystemExit(f"No files found under {source}")

    imported = 0
    for path in files:
        asset_type, bucket = classify_asset(path)
        digest = sha1_file(path)
        destination_dir = RAW_ROOT / args.usage_policy / bucket
        destination = unique_path(destination_dir / path.name)
        metadata = build_metadata(
            source_path=path,
            copied_path=destination,
            asset_type=asset_type,
            usage_policy=args.usage_policy,
            digest=digest,
            source_name=args.source_name,
            source_url=args.source_url,
            license_label=args.license,
            license_notes=args.license_notes,
        )
        metadata_path = METADATA_DIR / f"{metadata['asset_id']}.json"

        if args.dry_run:
            print(f"[dry-run] {path} -> {destination} ({asset_type})")
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, destination)
        write_json(metadata_path, metadata)
        append_log(
            {
                "imported_at": utc_now(),
                "asset_id": metadata["asset_id"],
                "source_path": str(path),
                "file_path": str(destination),
                "metadata_path": str(metadata_path),
                "asset_type": asset_type,
                "usage_policy": args.usage_policy,
            }
        )
        imported += 1
        print(f"imported {metadata['asset_id']} -> {destination}")

    action = "planned" if args.dry_run else "imported"
    print(f"{action} {len(files) if args.dry_run else imported} asset(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
