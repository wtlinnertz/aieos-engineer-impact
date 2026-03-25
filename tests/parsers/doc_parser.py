"""Markdown document parser for extracting structured data from framework files."""

from __future__ import annotations

import re


def extract_headings(content: str) -> list[tuple[int, str]]:
    """Return list of (level, heading_text) for all Markdown headings."""
    results = []
    for line in content.splitlines():
        m = re.match(r"^(#{1,6})\s+(.+)$", line)
        if m:
            results.append((len(m.group(1)), m.group(2).strip()))
    return results


def extract_tables(content: str) -> list[list[list[str]]]:
    """Return list of parsed Markdown tables.

    Each table is a list of rows (including header), each row is a list of
    cell strings with leading/trailing whitespace stripped.
    The separator row (containing dashes) is excluded.
    """
    tables: list[list[list[str]]] = []
    current_table: list[list[str]] = []

    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            # Skip separator rows (all dashes/colons/spaces)
            if all(re.match(r"^[-:\s]+$", c) for c in cells):
                continue
            current_table.append(cells)
        else:
            if current_table:
                tables.append(current_table)
                current_table = []
    if current_table:
        tables.append(current_table)

    return tables


def extract_code_blocks(content: str) -> list[str]:
    """Return content of all fenced code blocks."""
    blocks: list[str] = []
    in_block = False
    current: list[str] = []

    for line in content.splitlines():
        if line.strip().startswith("```"):
            if in_block:
                blocks.append("\n".join(current))
                current = []
                in_block = False
            else:
                in_block = True
        elif in_block:
            current.append(line)

    return blocks


def extract_file_references(content: str) -> list[str]:
    """Find all backtick-quoted file paths ending in .md or similar."""
    return re.findall(r"`([^`]+\.(?:md|py|json|yaml|yml|sh))`", content)


def find_section(content: str, heading: str) -> str | None:
    """Extract the text of a section by heading name (to next same-level heading).

    Returns None if heading not found.
    """
    lines = content.splitlines()
    start_idx = None
    heading_level = None

    for i, line in enumerate(lines):
        m = re.match(r"^(#{1,6})\s+(.+)$", line)
        if m and m.group(2).strip() == heading:
            start_idx = i + 1
            heading_level = len(m.group(1))
            break

    if start_idx is None:
        return None

    end_idx = len(lines)
    for i in range(start_idx, len(lines)):
        m = re.match(r"^(#{1,6})\s+", lines[i])
        if m and len(m.group(1)) <= heading_level:
            end_idx = i
            break

    return "\n".join(lines[start_idx:end_idx]).strip()
