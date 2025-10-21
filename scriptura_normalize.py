#!/usr/bin/env python3
"""
Scriptura Markdown Normalizer (v2)
-------------------------------------
Lawful enforcement of blockquote formatting across all Scriptura `.md` files.

Modes:
• Manual (default): Scans every Markdown file in the repository
• Hook-aware: When run via pre-commit, only scans staged files
"""

import os
import subprocess
from pathlib import Path

ROOT = Path(".")
EXTENSIONS = (".md",)
DOUBLE_SPACE = "  "


def get_staged_files():
    """Return a list of staged Markdown files (used by pre-commit mode)."""
    try:
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
            stdout=subprocess.PIPE,
            text=True,
            check=True,
        )
        files = [Path(f.strip()) for f in result.stdout.splitlines()]
        return [f for f in files if f.suffix.lower() in EXTENSIONS and f.exists()]
    except Exception:
        # If not in a git repo or command fails, fallback to manual mode
        return []


def normalize_markdown(file_path: Path):
    """Normalize blockquote lines in a single Markdown file."""
    with file_path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    normalized = []
    in_code_block = False
    modified_lines = []

    for i, line in enumerate(lines):
        stripped = line.rstrip("\n")

        if stripped.strip().startswith("```"):
            in_code_block = not in_code_block
            normalized.append(stripped)
            continue

        if in_code_block:
            normalized.append(stripped)
            continue

        if stripped.lstrip().startswith(">"):
            if not stripped.endswith(DOUBLE_SPACE):
                stripped = stripped.rstrip() + DOUBLE_SPACE
                modified_lines.append(i + 1)

        normalized.append(stripped)

    if not modified_lines:
        return False, []

    with file_path.open("w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(normalized) + "\n")

    return True, modified_lines


def normalize_all_markdown(root: Path):
    """Walk through all Markdown files and normalize them."""
    print(f"🪶 Scanning all Markdown codices under: {root.resolve()}")
    changed_files = []

    for path in root.rglob("*"):
        if path.suffix.lower() in EXTENSIONS:
            changed, lines = normalize_markdown(path)
            if changed:
                changed_files.append((path, lines))
                print(f"✅ Updated {path} (lines {lines})")

    if not changed_files:
        print("✨ All Markdown codices are lawful.")
    else:
        print(f"\n📜 {len(changed_files)} file(s) normalized successfully.")


def main():
    staged_files = get_staged_files()

    if staged_files:
        print("🪶 Hook Mode: Normalizing staged Markdown codices...")
        changed_files = []
        for path in staged_files:
            changed, lines = normalize_markdown(path)
            if changed:
                subprocess.run(["git", "add", str(path)])
                changed_files.append((path, lines))
                print(f"✅ Updated {path} (lines {lines})")

        if not changed_files:
            print("✨ All staged Markdown codices are lawful.")
        else:
            print(f"\n📜 {len(changed_files)} file(s) normalized and restaged.")
    else:
        print("🪶 Manual Mode: No staged files detected — scanning entire codex.")
        normalize_all_markdown(ROOT)


if __name__ == "__main__":
    main()
