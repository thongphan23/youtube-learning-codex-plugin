#!/usr/bin/env python3
"""Small local helpers for the YouTube Learning Codex plugin."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path
from typing import Any


YOUTUBE_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")


def video_id_from_url(value: str) -> str:
    value = value.strip()
    if YOUTUBE_ID_RE.match(value):
        return value
    parsed = urllib.parse.urlparse(value)
    host = parsed.netloc.lower()
    if host.endswith("youtu.be"):
        candidate = parsed.path.strip("/").split("/")[0]
        if YOUTUBE_ID_RE.match(candidate):
            return candidate
    if "youtube.com" in host:
        query_id = urllib.parse.parse_qs(parsed.query).get("v", [""])[0]
        if YOUTUBE_ID_RE.match(query_id):
            return query_id
        parts = [part for part in parsed.path.split("/") if part]
        for marker in ("shorts", "embed", "live"):
            if marker in parts:
                index = parts.index(marker)
                if len(parts) > index + 1 and YOUTUBE_ID_RE.match(parts[index + 1]):
                    return parts[index + 1]
    raise SystemExit(f"Could not extract a YouTube video id from: {value}")


def canonical_watch_url(value: str) -> str:
    return f"https://www.youtube.com/watch?v={video_id_from_url(value)}"


def fetch_json(url: str) -> Any:
    request = urllib.request.Request(url, headers={"User-Agent": "youtube-learning-codex-plugin/0.1"})
    with urllib.request.urlopen(request, timeout=15) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return json.loads(response.read().decode(charset))


def cmd_oembed(args: argparse.Namespace) -> int:
    video_url = canonical_watch_url(args.url)
    endpoint = "https://www.youtube.com/oembed?" + urllib.parse.urlencode(
        {"url": video_url, "format": "json"}
    )
    payload = fetch_json(endpoint)
    output = {
        "url": video_url,
        "title": payload.get("title"),
        "author_name": payload.get("author_name"),
        "author_url": payload.get("author_url"),
        "thumbnail_url": payload.get("thumbnail_url"),
        "provider_name": payload.get("provider_name"),
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0


def cmd_extract_id(args: argparse.Namespace) -> int:
    print(video_id_from_url(args.url))
    return 0


def cmd_scaffold(args: argparse.Namespace) -> int:
    root = Path(args.root).expanduser()
    slug = re.sub(r"[^a-z0-9]+", "-", args.slug.lower()).strip("-")
    if not slug:
        raise SystemExit("Slug must contain at least one letter or digit.")
    target = root / slug
    files = {
        "source.md": "# Source\n\n",
        "speaker-profile.md": "# Speaker Profile\n\n",
        "worldview-analysis.md": "# Worldview Analysis\n\n",
        "brain2-check.md": "# Brain2 Check\n\n",
        "application.md": "# Application\n\n",
        "qa.md": f"# QA\n\nCreated: {date.today().isoformat()}\n\n",
    }
    target.mkdir(parents=True, exist_ok=True)
    for name, content in files.items():
        path = target / name
        if not path.exists():
            path.write_text(content, encoding="utf-8")
    print(str(target))
    return 0


def cmd_validate_library(args: argparse.Namespace) -> int:
    path = Path(args.path).expanduser()
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise SystemExit("Library must be a JSON array.")
    seen: set[str] = set()
    errors: list[str] = []
    for index, item in enumerate(payload):
        if not isinstance(item, dict):
            errors.append(f"[{index}] item is not an object")
            continue
        url = item.get("url")
        title = item.get("title")
        channel = item.get("channel")
        if not isinstance(url, str) or "youtube.com/watch?v=" not in canonical_watch_url(url):
            errors.append(f"[{index}] invalid YouTube watch URL")
        else:
            normalized = canonical_watch_url(url)
            if normalized in seen:
                errors.append(f"[{index}] duplicate URL: {normalized}")
            seen.add(normalized)
        if not isinstance(title, str) or not title.strip():
            errors.append(f"[{index}] missing title")
        if not isinstance(channel, str) or not channel.strip():
            errors.append(f"[{index}] missing channel")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"OK: {len(payload)} video entries")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="YouTube Learning helper CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    extract = sub.add_parser("extract-id", help="Extract a YouTube video id")
    extract.add_argument("url")
    extract.set_defaults(func=cmd_extract_id)

    oembed = sub.add_parser("oembed", help="Fetch YouTube oEmbed metadata")
    oembed.add_argument("url")
    oembed.set_defaults(func=cmd_oembed)

    scaffold = sub.add_parser("scaffold", help="Create a run folder for a serious learning pass")
    scaffold.add_argument("slug")
    scaffold.add_argument("--root", default="/Users/rio/content/youtube-learning")
    scaffold.set_defaults(func=cmd_scaffold)

    validate = sub.add_parser("validate-library", help="Validate a video library JSON file")
    validate.add_argument("path")
    validate.set_defaults(func=cmd_validate_library)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
