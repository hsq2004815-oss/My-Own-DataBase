"""Enrich UI asset metadata and generate retrieval chunks.

This script updates metadata for already-imported local assets. It never moves
or copies raw files.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
METADATA_DIR = ROOT / "domains" / "ui_assets" / "processed" / "metadata"
CHUNK_DIR = ROOT / "domains" / "ui_assets" / "processed" / "chunks"

SCREENSHOT_TAGS = [
    "dark-cinematic",
    "liquid-glass",
    "floating-navbar",
    "giant-typography",
    "bento-grid",
    "dashboard-preview",
    "editorial-layout",
    "portfolio-inspiration",
    "SaaS-hero",
]

VIDEO_TAGS = [
    "motion-reference",
    "hero-background",
    "ambient-motion",
    "cinematic-loop",
    "glass-refraction",
    "particle-background",
    "gradient-motion",
]

LOTTIE_ASSET_ID = "lottie-web-library-and-demos-b6a4ec55"
LOTTIE_TAGS = [
    "lottie",
    "lottie-animation",
    "small-animation",
    "micro-interaction",
    "loading-animation",
    "hover-motion",
    "button-animation",
    "animated-icon",
    "json-animation",
    "web-ui-motion",
    "lightweight-ui-animation",
]
LOTTIE_USE_CASES = [
    "loading animation",
    "hover motion",
    "micro interaction",
    "json animation reference",
    "web UI motion",
    "button animation",
    "animated icon",
    "lightweight UI animation",
    "小动画",
    "微交互",
    "加载动画",
    "按钮动画",
    "图标动画",
]
LOTTIE_SUMMARIES: list[dict[str, Any]] = [
    {
        "chunk_id": "lottie-loading-animation-summary",
        "title": "Lottie Loading Animation Summary",
        "tags": ["lottie", "loading-animation", "json-animation", "lightweight-ui-animation", "加载动画"],
        "content": "Use this collection as a review_required reference for lightweight loading animations, progress states, skeleton alternatives, empty-state waits, and async feedback. Do not assume direct commercial use until the collection license is checked.",
    },
    {
        "chunk_id": "lottie-micro-interaction-summary",
        "title": "Lottie Micro Interaction Summary",
        "tags": ["lottie", "micro-interaction", "web-ui-motion", "小动画", "微交互"],
        "content": "Use as inspiration for small UI micro interactions: success feedback, subtle state changes, form confirmation, onboarding delight, and compact product moments. Recreate or use only after license review.",
    },
    {
        "chunk_id": "lottie-hover-motion-summary",
        "title": "Lottie Hover Motion Summary",
        "tags": ["lottie", "hover-motion", "button-animation", "web-ui-motion", "按钮动画"],
        "content": "Use as a reference for hover motion on buttons, cards, nav items, feature icons, and premium CTA states. Keep hover animation lightweight, optional, and accessible.",
    },
    {
        "chunk_id": "lottie-json-web-animation-summary",
        "title": "Lottie JSON Web Animation Summary",
        "tags": ["lottie", "json-animation", "web-ui-motion", "lightweight-ui-animation"],
        "content": "Use as collection-level guidance for JSON-driven web UI animation. Prefer lazy loading, reduced-motion handling, bounded file sizes, and license confirmation before direct use.",
    },
    {
        "chunk_id": "lottie-ui-icon-animation-summary",
        "title": "Lottie UI Icon Animation Summary",
        "tags": ["lottie", "animated-icon", "button-animation", "micro-interaction", "图标动画"],
        "content": "Use as inspiration for animated icons in buttons, feature bullets, status badges, empty states, onboarding steps, and product UI affordances. Avoid overuse and do not ship unreviewed assets.",
    },
    {
        "chunk_id": "lottie-implementation-notes-summary",
        "title": "Lottie Implementation Notes Summary",
        "tags": ["lottie", "implementation-notes", "review-required", "web-ui-motion"],
        "content": "Implementation notes: this collection is review_required, individual files are not indexed, and direct commercial use requires license confirmation. Agents may use it as style reference and should recreate equivalent motion with owned JSON, CSS, SVG, Canvas, or generated assets when direct_use is not confirmed.",
    },
]

SCREENSHOT_PROFILES: dict[str, dict[str, list[str] | str]] = {
    "reference 2": {
        "tags": ["liquid-glass", "floating-navbar", "SaaS-hero", "dashboard-preview"],
        "use_cases": ["liquid glass component inspiration", "button kit reference", "glass card system"],
        "summary": "Liquid Glass UI screenshot reference with translucent controls, floating pills, glossy buttons, soft shadows, and glass card surfaces.",
    },
    "reference2": {
        "tags": ["liquid-glass", "floating-navbar", "SaaS-hero", "dashboard-preview"],
        "use_cases": ["liquid glass component inspiration", "button kit reference", "glass card system"],
        "summary": "Liquid Glass screenshot reference for high-end buttons, floating navigation, translucent panels, soft refraction, and premium SaaS UI controls.",
    },
    "reference1 (1)": {
        "tags": ["dark-cinematic", "dashboard-preview", "SaaS-hero"],
        "use_cases": ["dark analytics landing inspiration", "dashboard hero reference"],
        "summary": "Dark cinematic analytics hero screenshot with dashboard preview, glowing CTA, and high-contrast product storytelling.",
    },
    "reference1 (10)": {
        "tags": ["dark-cinematic", "floating-navbar", "dashboard-preview", "SaaS-hero"],
        "use_cases": ["finance SaaS hero", "dashboard preview inspiration"],
        "summary": "Dark cinematic finance SaaS hero with floating navigation, dashboard product preview, glowing orb, and restrained neon accent.",
    },
    "reference1 (11)": {
        "tags": ["dark-cinematic", "giant-typography", "SaaS-hero"],
        "use_cases": ["AI product landing hero", "giant typography hero"],
        "summary": "Premium dark AI landing hero with giant typography, glossy abstract background, floating navbar, and cinematic product mood.",
    },
    "reference1 (12)": {
        "tags": ["dark-cinematic", "giant-typography", "SaaS-hero"],
        "use_cases": ["product leader landing page", "dark SaaS hero"],
        "summary": "Dark SaaS hero screenshot with large editorial headline, blue glass-like 3D background, floating navbar, and clear CTA row.",
    },
    "reference1 (13)": {
        "tags": ["dark-cinematic", "giant-typography", "SaaS-hero"],
        "use_cases": ["growth landing hero", "cinematic dark product page"],
        "summary": "Minimal dark product hero with huge centered type, blue cinematic glow, floating top nav, and restrained CTA hierarchy.",
    },
    "reference1 (14)": {
        "tags": ["dark-cinematic", "editorial-layout", "portfolio-inspiration"],
        "use_cases": ["agency portfolio hero", "cinematic landing cover"],
        "summary": "Dark cinematic agency or portfolio hero with dramatic atmospheric background, editorial serif emphasis, and centered CTA.",
    },
    "reference1 (15)": {
        "tags": ["editorial-layout", "SaaS-hero", "dashboard-preview"],
        "use_cases": ["white editorial SaaS page", "automation product landing"],
        "summary": "White editorial SaaS screenshot with airy composition, product dashboard preview, soft nature backdrop, and restrained black CTA.",
    },
    "reference1 (16)": {
        "tags": ["dark-cinematic", "giant-typography", "portfolio-inspiration"],
        "use_cases": ["security product hero", "bold portfolio composition"],
        "summary": "Dark cinematic security hero with oversized staggered typography, human figure media, and sharp data/security positioning.",
    },
    "reference1 (17)": {
        "tags": ["dark-cinematic", "giant-typography", "portfolio-inspiration"],
        "use_cases": ["security landing hero", "editorial dark composition"],
        "summary": "Dark editorial hero with giant fragmented typography, warm cinematic accent, floating navbar, and security/product narrative.",
    },
    "reference1 (18)": {
        "tags": ["editorial-layout", "portfolio-inspiration", "SaaS-hero"],
        "use_cases": ["city/vision portfolio hero", "future technology landing"],
        "summary": "Editorial technology landing screenshot with scenic media background, understated navbar, strong headline, and portfolio-style CTA.",
    },
    "reference1 (19)": {
        "tags": ["dark-cinematic", "editorial-layout", "portfolio-inspiration"],
        "use_cases": ["AI portfolio hero", "dark editorial landing page"],
        "summary": "Dark editorial AI hero with serif typography, atmospheric illustration, floating nav, and premium portfolio composition.",
    },
    "reference1 (2)": {
        "tags": ["dark-cinematic", "giant-typography", "SaaS-hero"],
        "use_cases": ["dark product hero", "red accent landing page"],
        "summary": "Dark premium product hero with bold centered headline, red abstract motion-like shape, floating navbar, and focused CTA.",
    },
    "reference1 (20)": {
        "tags": ["liquid-glass", "dashboard-preview", "SaaS-hero"],
        "use_cases": ["glass dashboard preview", "technical product hero"],
        "summary": "Light blue glassmorphism product page with translucent hex panels, dashboard-like preview, and operational evaluation positioning.",
    },
    "reference1 (3)": {
        "tags": ["editorial-layout", "SaaS-hero"],
        "use_cases": ["AI cloud landing page", "white SaaS hero"],
        "summary": "White SaaS hero screenshot with clean headline, black CTA, subtle pastel gradient product/media field, and minimal nav.",
    },
    "reference1 (4)": {
        "tags": ["dark-cinematic", "dashboard-preview", "SaaS-hero"],
        "use_cases": ["SEO dashboard hero", "dark SaaS dashboard preview"],
        "summary": "Dark SaaS research landing screenshot with purple gradient glow, dashboard preview strip, floating nav, and premium hero structure.",
    },
    "reference1 (5)": {
        "tags": ["dark-cinematic", "dashboard-preview", "bento-grid", "SaaS-hero"],
        "use_cases": ["research dashboard section", "bento dashboard inspiration"],
        "summary": "Dark dashboard-focused screenshot with purple cards, research panels, bento-like product preview, and premium SaaS structure.",
    },
    "reference1 (6)": {
        "tags": ["dark-cinematic", "dashboard-preview", "SaaS-hero"],
        "use_cases": ["AI reflection app hero", "dark dashboard preview"],
        "summary": "Dark SaaS hero with purple horizon glow, dashboard preview, floating navbar, and premium AI productivity positioning.",
    },
    "reference1 (7)": {
        "tags": ["editorial-layout", "bento-grid", "portfolio-inspiration"],
        "use_cases": ["portfolio case grid", "editorial media layout"],
        "summary": "Light editorial portfolio screenshot with media grid, playful composition, and case-study style layout inspiration.",
    },
    "reference1 (8)": {
        "tags": ["dark-cinematic", "editorial-layout", "portfolio-inspiration"],
        "use_cases": ["language product hero", "cinematic editorial cover"],
        "summary": "Dark cinematic language product hero with globe-like background, minimal nav, editorial headline, and atmospheric layout.",
    },
    "reference1 (9)": {
        "tags": ["dark-cinematic", "dashboard-preview", "portfolio-inspiration"],
        "use_cases": ["performance dashboard hero", "sports/analytics landing"],
        "summary": "Dark teal performance dashboard hero with dynamic media, metric overlays, floating nav, and cinematic product preview.",
    },
}

VIDEO_PROFILES: dict[str, dict[str, list[str] | str]] = {
    "1 (1)": {
        "tags": ["motion-reference", "hero-background", "ambient-motion", "cinematic-loop", "particle-background"],
        "use_cases": ["dark cinematic hero background", "portfolio background motion"],
        "summary": "Dark vortex-like ambient motion reference for cinematic hero backgrounds, portfolio covers, and deep-space particle moods.",
    },
    "1 (6)": {
        "tags": ["motion-reference", "hero-background", "ambient-motion", "cinematic-loop", "particle-background"],
        "use_cases": ["dark cinematic hero background", "portfolio background motion"],
        "summary": "Dark vortex-like ambient loop reference for cinematic hero backgrounds and deep-space premium landing pages.",
    },
    "1 (2)": {
        "tags": ["motion-reference", "hero-background", "ambient-motion", "cinematic-loop", "gradient-motion"],
        "use_cases": ["abstract gradient hero background", "dark landing page atmosphere"],
        "summary": "Abstract dark gradient motion reference with colored light flare, suitable for premium hero backgrounds and cinematic transitions.",
    },
    "1 (3)": {
        "tags": ["motion-reference", "hero-background", "ambient-motion", "cinematic-loop"],
        "use_cases": ["scenic portfolio background", "cinematic editorial hero"],
        "summary": "Cinematic landscape motion reference with atmospheric scene depth for portfolio, AI, and editorial hero backgrounds.",
    },
    "1 (4)": {
        "tags": ["motion-reference", "hero-background", "glass-refraction", "gradient-motion"],
        "use_cases": ["glass product showcase", "liquid glass refraction inspiration"],
        "summary": "Glass refraction motion reference with prism-like object and light beams, useful for Liquid Glass product showcases and premium hero visuals.",
    },
    "1 (5)": {
        "tags": ["motion-reference", "hero-background", "cinematic-loop"],
        "use_cases": ["product device showcase", "robotics hero motion"],
        "summary": "Product showcase motion reference with device/robotic arm composition for premium hardware, robotics, and developer product heroes.",
    },
    "1 (7)": {
        "tags": ["motion-reference", "hero-background", "ambient-motion", "gradient-motion"],
        "use_cases": ["soft abstract background", "ambient hero motion"],
        "summary": "Soft blue abstract gradient motion reference for subtle hero background animation and atmospheric UI sections.",
    },
    "1 (8)": {
        "tags": ["motion-reference", "hero-background", "ambient-motion", "gradient-motion"],
        "use_cases": ["soft abstract background", "ambient hero motion"],
        "summary": "Soft blue abstract gradient loop reference for ambient hero motion and gentle background animation.",
    },
    "1 (9)": {
        "tags": ["motion-reference", "hero-background", "gradient-motion", "cinematic-loop"],
        "use_cases": ["finance hero background", "dark SaaS landing motion"],
        "summary": "Dark finance SaaS hero motion reference with vivid gradient light band, useful for premium product hero backgrounds.",
    },
    "1 (10)": {
        "tags": ["motion-reference", "hero-background", "gradient-motion"],
        "use_cases": ["light SaaS hero background", "soft pastel landing motion"],
        "summary": "Light SaaS hero motion reference with pastel gradient and simple management product composition for clean landing pages.",
    },
    "1 (11)": {
        "tags": ["motion-reference", "hero-background", "ambient-motion", "cinematic-loop"],
        "use_cases": ["scenic portfolio background", "optimistic landing hero"],
        "summary": "Bright scenic hero motion reference with landscape and clouds, useful for optimistic portfolio or product landing backgrounds.",
    },
    "1 (12)": {
        "tags": ["motion-reference", "hero-background", "ambient-motion", "cinematic-loop", "gradient-motion"],
        "use_cases": ["dark SaaS video hero", "blue abstract product background"],
        "summary": "Dark SaaS video hero reference with blue abstract glass-like background and product-leadership landing composition.",
    },
    "1 (13)": {
        "tags": ["motion-reference", "hero-background", "particle-background", "cinematic-loop"],
        "use_cases": ["finance/asset hero background", "particle landing motion"],
        "summary": "Dark asset/finance hero motion reference with floating coin-like particles, useful for cinematic finance landing backgrounds.",
    },
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def uniq(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        normalized = str(item).strip()
        if normalized and normalized not in seen:
            seen.add(normalized)
            result.append(normalized)
    return result


def profile_for(record: dict[str, Any]) -> dict[str, list[str] | str] | None:
    files = record.get("files") if isinstance(record.get("files"), dict) else {}
    file_path = Path(str(files.get("file_path", "")))
    name = file_path.stem
    asset_type = record.get("asset_type")
    if asset_type == "motion_reference":
        return VIDEO_PROFILES.get(name)
    if asset_type == "screenshot_reference":
        for prefix, profile in SCREENSHOT_PROFILES.items():
            if name.startswith(prefix):
                return profile
    return None


def is_lottie_collection(record: dict[str, Any]) -> bool:
    return record.get("asset_id") == LOTTIE_ASSET_ID


def usage_notes(policy: str) -> list[str]:
    if policy == "inspiration_only":
        return [
            "Usage policy: inspiration_only. Use this asset only as visual reference; do not copy the screenshot or video into a project.",
            "When no direct_use asset is available, recreate the style with original CSS, SVG, Canvas, WebGL, or generated implementation assets.",
        ]
    if policy == "review_required":
        return [
            "Usage policy: review_required. Inspect source and license before direct use.",
            "Prefer recreating the style with original CSS, SVG, Canvas, or project-owned media until usage rights are confirmed.",
        ]
    if policy == "direct_use":
        return ["Usage policy: direct_use. Still preserve attribution and project licensing notes where applicable."]
    return ["Usage policy is not direct_use; treat as reference unless rights are explicitly confirmed."]


def enrich_record(record: dict[str, Any]) -> bool:
    if is_lottie_collection(record):
        policy = str(record.get("usage_policy", "unknown"))
        record["style_tags"] = uniq(list(record.get("style_tags") or []) + LOTTIE_TAGS)
        record["use_cases"] = uniq(list(record.get("use_cases") or []) + LOTTIE_USE_CASES)
        record["avoid_when"] = uniq(
            list(record.get("avoid_when") or [])
            + [
                "Do not default to direct commercial use; usage_policy is review_required.",
                "Do not index or ship individual Lottie files until license and source are reviewed.",
                "Avoid heavy or distracting animation for core reading and task flows.",
                "Respect prefers-reduced-motion and provide a static fallback.",
            ]
        )
        record["implementation_notes"] = uniq(
            list(record.get("implementation_notes") or [])
            + usage_notes(policy)
            + [
                "Keep this as collection-level metadata; do not split all files unless a later task needs per-file curation.",
                "Use Lottie for compact loading states, animated icons, hover feedback, and micro interactions.",
                "Lazy-load animations and cap loop counts for UI affordances.",
                "Provide reduced-motion fallbacks and avoid animation as the only state indicator.",
                "When direct_use is not confirmed, recreate the motion with owned Lottie JSON, CSS, SVG, Canvas, or generated assets.",
            ]
        )
        quality = record.get("quality") if isinstance(record.get("quality"), dict) else {}
        quality["curation_status"] = "reviewed"
        quality["notes"] = "Collection-level Lottie metadata enriched for retrieval; individual files are still not indexed."
        record["quality"] = quality
        retrieval = record.get("retrieval") if isinstance(record.get("retrieval"), dict) else {}
        retrieval["ai_summary"] = (
            "Review-required Lottie Web library and demos collection for loading animation, hover motion, "
            "micro interaction, JSON web animation, button animation, animated icon, and lightweight web UI motion inspiration. "
            "Use as style reference only until license is confirmed; recreate with owned CSS/SVG/Canvas/Lottie assets when direct_use is not available."
        )
        retrieval["prompt_tags"] = uniq(list(retrieval.get("prompt_tags") or []) + LOTTIE_TAGS + LOTTIE_USE_CASES)
        retrieval["negative_prompt_tags"] = uniq(
            list(retrieval.get("negative_prompt_tags") or [])
            + ["direct-commercial-use-without-license", "unreviewed-lottie-file", "excessive-animation"]
        )
        record["retrieval"] = retrieval
        return True

    profile = profile_for(record)
    if profile is None:
        return False

    asset_type = str(record.get("asset_type", ""))
    policy = str(record.get("usage_policy", "unknown"))
    files = record.get("files") if isinstance(record.get("files"), dict) else {}
    file_path = Path(str(files.get("file_path", "")))
    base_tags = VIDEO_TAGS if asset_type == "motion_reference" else SCREENSHOT_TAGS
    profile_tags = list(profile.get("tags", [])) if isinstance(profile.get("tags"), list) else []
    profile_use_cases = list(profile.get("use_cases", [])) if isinstance(profile.get("use_cases"), list) else []

    record["style_tags"] = uniq(list(record.get("style_tags") or []) + profile_tags)
    record["use_cases"] = uniq(list(record.get("use_cases") or []) + profile_use_cases)
    record["avoid_when"] = uniq(
        list(record.get("avoid_when") or [])
        + [
            "Do not copy this reference asset into deliverables when usage_policy is inspiration_only.",
            "Do not treat reference screenshots or videos as licensed product assets.",
        ]
    )
    record["implementation_notes"] = uniq(
        list(record.get("implementation_notes") or [])
        + usage_notes(policy)
        + [
            "Use the tags as style retrieval hints, then build original UI/material/motion in the target project.",
            "For Liquid Glass styles, recreate with backdrop-filter, translucent layers, gradient rim borders, and contrast-safe text.",
            "For video/background inspiration, recreate with original gradients, particles, Canvas/WebGL, or licensed/generated media.",
        ]
    )
    quality = record.get("quality") if isinstance(record.get("quality"), dict) else {}
    quality["curation_status"] = "reviewed"
    quality["notes"] = "Enriched for style retrieval. Asset remains governed by usage_policy."
    record["quality"] = quality

    retrieval = record.get("retrieval") if isinstance(record.get("retrieval"), dict) else {}
    summary = str(profile.get("summary", "")).strip()
    policy_text = (
        "This is inspiration_only: use it as reference only and recreate the style with original CSS/SVG/Canvas/media."
        if policy == "inspiration_only"
        else "Review license and source before direct use."
    )
    retrieval["ai_summary"] = f"{summary} {policy_text}"
    retrieval["prompt_tags"] = uniq(
        list(retrieval.get("prompt_tags") or [])
        + profile_tags
        + base_tags
        + [asset_type.replace("_", "-"), file_path.stem.lower()]
    )
    retrieval["negative_prompt_tags"] = uniq(
        list(retrieval.get("negative_prompt_tags") or [])
        + ["copy-asset-directly", "unlicensed-direct-use", "brand-copying"]
    )
    record["retrieval"] = retrieval
    return True


def chunk_for(record: dict[str, Any]) -> dict[str, Any]:
    retrieval = record.get("retrieval") if isinstance(record.get("retrieval"), dict) else {}
    files = record.get("files") if isinstance(record.get("files"), dict) else {}
    content = "\n".join(
        [
            f"# {record['asset_id']} asset retrieval chunk",
            f"Asset type: {record.get('asset_type', '')}",
            f"Usage policy: {record.get('usage_policy', '')}",
            f"File path: {files.get('file_path', '')}",
            f"Style tags: {', '.join(record.get('style_tags', []))}",
            f"Use cases: {', '.join(record.get('use_cases', []))}",
            f"Implementation notes: {' '.join(record.get('implementation_notes', []))}",
            f"Summary: {retrieval.get('ai_summary', '')}",
        ]
    )
    return {
        "chunk_id": f"{record['asset_id']}-asset-summary",
        "asset_id": record["asset_id"],
        "asset_type": record.get("asset_type", ""),
        "usage_policy": record.get("usage_policy", ""),
        "content": content,
        "metadata": {
            "style_tags": record.get("style_tags", []),
            "use_cases": record.get("use_cases", []),
            "prompt_tags": retrieval.get("prompt_tags", []),
        },
    }


def lottie_chunks(record: dict[str, Any]) -> list[dict[str, Any]]:
    retrieval = record.get("retrieval") if isinstance(record.get("retrieval"), dict) else {}
    files = record.get("files") if isinstance(record.get("files"), dict) else {}
    chunks: list[dict[str, Any]] = []
    for item in LOTTIE_SUMMARIES:
        content = "\n".join(
            [
                f"# {item['title']}",
                f"Asset id: {record['asset_id']}",
                f"Asset type: {record.get('asset_type', '')}",
                f"Usage policy: {record.get('usage_policy', '')}",
                f"File path: {files.get('file_path', '')}",
                f"Style tags: {', '.join(record.get('style_tags', []))}",
                f"Use cases: {', '.join(record.get('use_cases', []))}",
                f"Summary: {item['content']}",
                f"Collection summary: {retrieval.get('ai_summary', '')}",
            ]
        )
        chunks.append(
            {
                "chunk_id": item["chunk_id"],
                "asset_id": record["asset_id"],
                "asset_type": record.get("asset_type", ""),
                "usage_policy": record.get("usage_policy", ""),
                "content": content,
                "metadata": {
                    "style_tags": uniq(list(record.get("style_tags", [])) + list(item["tags"])),
                    "use_cases": record.get("use_cases", []),
                    "prompt_tags": uniq(list(retrieval.get("prompt_tags", [])) + list(item["tags"])),
                },
            }
        )
    return chunks


def main() -> int:
    parser = argparse.ArgumentParser(description="Enrich UI asset metadata and generate asset chunks.")
    parser.add_argument("--check", action="store_true", help="Validate and report without writing files.")
    args = parser.parse_args()

    metadata_files = sorted(path for path in METADATA_DIR.glob("*.json") if path.name != ".gitkeep")
    chunks: list[dict[str, Any]] = []
    enriched = 0
    for path in metadata_files:
        record = load_json(path)
        if not isinstance(record, dict) or not record.get("asset_id"):
            continue
        changed = enrich_record(record)
        if changed:
            enriched += 1
            if not args.check:
                write_json(path, record)
        if record.get("asset_type") in {"screenshot_reference", "motion_reference"}:
            chunks.append(chunk_for(record))
        elif is_lottie_collection(record):
            chunks.extend(lottie_chunks(record))

    if not args.check:
        CHUNK_DIR.mkdir(parents=True, exist_ok=True)
        for chunk in chunks:
            filename = chunk["asset_id"]
            if not str(chunk["chunk_id"]).endswith("-asset-summary"):
                filename = chunk["chunk_id"]
            write_json(CHUNK_DIR / f"{filename}.json", chunk)
        write_json(CHUNK_DIR / "all_asset_chunks.json", chunks)

    action = "would enrich" if args.check else "enriched"
    print(f"{action} {enriched} metadata record(s)")
    print(f"{'would write' if args.check else 'wrote'} {len(chunks)} asset chunk(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
