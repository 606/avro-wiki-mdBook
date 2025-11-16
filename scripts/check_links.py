#!/usr/bin/env python3
"""
Check for broken links in markdown files.

This script scans all markdown files and verifies that internal links point to existing files.
Useful for maintaining link integrity in large wikis.

Usage:
    python3 scripts/check_links.py
    python3 scripts/check_links.py src/  # Specify directory
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple, Set


def extract_links(content: str, file_path: Path) -> List[Tuple[str, int]]:
    """
    Extract markdown links from content.
    
    Returns list of (link_target, line_number) tuples.
    """
    links = []
    
    # Match markdown links: [text](url)
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    
    for line_num, line in enumerate(content.split('\n'), 1):
        for match in re.finditer(pattern, line):
            link = match.group(2)
            # Only check relative links (internal)
            if not link.startswith(('http://', 'https://', 'mailto:', '#')):
                links.append((link, line_num))
    
    return links


def resolve_link(link: str, source_file: Path, src_dir: Path) -> Path:
    """
    Resolve a relative link to an absolute path.
    
    Args:
        link: The link target (e.g., './page.md', '../other.md')
        source_file: The file containing the link
        src_dir: The src directory root
    
    Returns:
        Resolved absolute path
    """
    # Remove anchor if present
    if '#' in link:
        link = link.split('#')[0]
    
    # Skip empty links (pure anchors)
    if not link:
        return None
    
    # Resolve relative to the source file's directory
    source_dir = source_file.parent
    target = (source_dir / link).resolve()
    
    return target


def check_file(file_path: Path, src_dir: Path) -> List[Tuple[str, int, str]]:
    """
    Check a single markdown file for broken links.
    
    Returns list of (file, line, link) tuples for broken links.
    """
    broken = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}", file=sys.stderr)
        return broken
    
    links = extract_links(content, file_path)
    
    for link, line_num in links:
        target = resolve_link(link, file_path, src_dir)
        
        if target is None:
            # Pure anchor link, skip
            continue
        
        if not target.exists():
            rel_file = file_path.relative_to(src_dir)
            broken.append((str(rel_file), line_num, link))
    
    return broken


def check_all_links(src_dir: Path) -> int:
    """
    Check all markdown files in src_dir for broken links.
    
    Returns number of broken links found.
    """
    broken_count = 0
    
    # Find all markdown files
    md_files = list(src_dir.rglob('*.md'))
    
    print(f"Checking {len(md_files)} markdown files...\n")
    
    all_broken = []
    
    for md_file in md_files:
        broken = check_file(md_file, src_dir)
        if broken:
            all_broken.extend(broken)
    
    if all_broken:
        print("❌ Found broken links:\n")
        for file, line, link in sorted(all_broken):
            print(f"  {file}:{line} -> {link}")
            broken_count += 1
        print(f"\nTotal: {broken_count} broken link(s)")
    else:
        print("✅ No broken links found!")
    
    return broken_count


def main():
    """Main entry point."""
    # Determine src directory
    if len(sys.argv) > 1:
        src_dir = Path(sys.argv[1])
    else:
        src_dir = Path('src')
    
    if not src_dir.exists():
        print(f"Error: {src_dir} does not exist", file=sys.stderr)
        sys.exit(1)
    
    if not src_dir.is_dir():
        print(f"Error: {src_dir} is not a directory", file=sys.stderr)
        sys.exit(1)
    
    # Check links
    broken_count = check_all_links(src_dir)
    
    # Exit with error code if broken links found
    sys.exit(1 if broken_count > 0 else 0)


if __name__ == '__main__':
    main()
