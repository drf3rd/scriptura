#!/usr/bin/env python3
"""
update_versions.py — auto-generate versions.json from Git tags.
"""

import json, subprocess, datetime

def get_tags():
    tags = (
        subprocess.check_output(["git", "tag", "--list"])
        .decode("utf-8")
        .strip()
        .splitlines()
    )
    return [t for t in tags if t]

def build_versions_json(tags):
    tags_sorted = sorted(tags, reverse=True)
    latest = tags_sorted[0] if tags_sorted else None
    now = datetime.date.today().isoformat()

    data = {
        "generated": now,
        "default_version": latest,
        "include_archive": False,
        "available_versions": {},
        "archived_versions": {},
    }

    for tag in tags_sorted:
        status = "stable" if tag == latest else "archived"
        summary = f"Auto-generated entry for {tag}"
        path = "." if tag == latest else f"versions/{tag}/"
        bucket = "available_versions" if tag == latest else "archived_versions"
        data[bucket][tag] = {"path": path, "status": status, "summary": summary}

    return data

if __name__ == "__main__":
    tags = get_tags()
    versions = build_versions_json(tags)
    with open("versions.json", "w") as f:
        json.dump(versions, f, indent=2)
    print(f"✅ Generated versions.json with {len(tags)} tags.")
