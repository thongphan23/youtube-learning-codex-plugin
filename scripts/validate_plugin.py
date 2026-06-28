#!/usr/bin/env python3
"""Validate the local YouTube Learning plugin package."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED_SKILLS = [
    "skills/index/SKILL.md",
    "skills/learn-video/SKILL.md",
    "skills/discover-videos/SKILL.md",
]


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    manifest_path = root / ".codex-plugin" / "plugin.json"
    errors: list[str] = []
    if not manifest_path.exists():
        errors.append("Missing .codex-plugin/plugin.json")
    else:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest_name = manifest.get("name")
        if manifest_name not in {root.name, root.parent.name}:
            errors.append("Manifest name must match plugin folder name or cache parent folder name")
        if "[TODO:" in json.dumps(manifest):
            errors.append("Manifest still contains TODO placeholders")
        interface = manifest.get("interface", {})
        if interface.get("brandColor") != "#FF0000":
            errors.append("brandColor must be #FF0000")
        for asset_field in ("composerIcon", "logo"):
            asset = interface.get(asset_field)
            if not isinstance(asset, str) or not (root / asset).exists():
                errors.append(f"Missing asset for {asset_field}: {asset}")
    for skill in REQUIRED_SKILLS:
        path = root / skill
        if not path.exists():
            errors.append(f"Missing {skill}")
        elif "---" not in path.read_text(encoding="utf-8")[:200]:
            errors.append(f"Missing frontmatter in {skill}")
    for reference in [
        "references/source-policy.md",
        "references/output-contracts.md",
        "references/brain2-vault-contract.md",
        "references/quality-rubric.md",
    ]:
        if not (root / reference).exists():
            errors.append(f"Missing {reference}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"OK: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
