#!/usr/bin/env python3
"""
Scriptura Pre-Commit Markdown Normalizer
----------------------------------------
A lawful pre-commit hook that enforces Scriptura formatting standards
before any Git commit is finalized.

Features:
• Checks all staged .md files (only those being committed)
• Adds double spaces to all blockquote lines (`>`) unless inside code fences
• Automatically restages modified files so commit proceeds cleanly
• Provides summary of all normalized lines
"""

import subprocess
from pathlib import Path

DOUBLE_SPACE = "  "
EXTENSIONS = (".md",)

def get_staged_files():
    """Return a list of staged markdown files."""
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
        stdout=subprocess.PIPE,
        text=True
    )
    files = [Path(f.strip()) for f in result.stdout.splitlines()]
    return [f for f in files if f.suffix.lower() in EXTENSIONS and f.exists()]

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

def main():
    print("🪶 Scriptura Pre-Commit Normalizer: Checking Markdown codices...")
    staged_files = get_staged_files()
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

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
