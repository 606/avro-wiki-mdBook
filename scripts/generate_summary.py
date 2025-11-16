#!/usr/bin/env python3
"""
Generate SUMMARY.md from filesystem structure.

This script automatically creates a SUMMARY.md file by scanning the src/ directory.
Useful for wikis with many files where manual SUMMARY.md maintenance is impractical.

Usage:
    python3 scripts/generate_summary.py > src/SUMMARY.md
    python3 scripts/generate_summary.py --dry-run  # Preview without writing
"""

import os
import sys
from pathlib import Path
from typing import List, Tuple


def get_title_from_file(file_path: Path) -> str:
    """Extract title from first H1 heading in markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('# '):
                    return line[2:].strip()
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}", file=sys.stderr)
    
    # Fallback to filename
    return file_path.stem.replace('-', ' ').replace('_', ' ').title()


def should_skip(path: Path) -> bool:
    """Check if a file or directory should be skipped."""
    skip_names = {
        'SUMMARY.md', 'summary.md',
        '.git', '.github', '.obsidian',
        '__pycache__', 'node_modules',
        '.DS_Store', 'Thumbs.db'
    }
    return path.name in skip_names or path.name.startswith('.')


def scan_directory(directory: Path, base_path: Path, level: int = 0) -> List[Tuple[str, str, int]]:
    """
    Recursively scan directory and return list of (title, path, level) tuples.
    
    Args:
        directory: Directory to scan
        base_path: Base path for calculating relative paths
        level: Current nesting level
    
    Returns:
        List of (title, relative_path, level) tuples
    """
    items = []
    
    # Get all items in directory
    try:
        dir_items = sorted(directory.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
    except PermissionError:
        return items
    
    # Process README.md first if it exists
    readme_path = directory / 'README.md'
    if readme_path.exists() and not should_skip(readme_path):
        title = get_title_from_file(readme_path)
        rel_path = readme_path.relative_to(base_path)
        items.append((title, str(rel_path), level))
    
    # Process other files and directories
    for item in dir_items:
        if should_skip(item):
            continue
        
        if item.is_dir():
            # Recursively process subdirectory
            subitems = scan_directory(item, base_path, level + 1)
            items.extend(subitems)
        elif item.suffix == '.md' and item.name != 'README.md':
            title = get_title_from_file(item)
            rel_path = item.relative_to(base_path)
            items.append((title, str(rel_path), level))
    
    return items


def generate_summary(src_dir: Path) -> str:
    """Generate SUMMARY.md content from src directory structure."""
    
    output = ["# Summary\n"]
    
    # Introduction (README.md at root)
    readme = src_dir / 'README.md'
    if readme.exists():
        title = get_title_from_file(readme)
        output.append(f"[{title}](./README.md)\n")
        output.append("\n---\n")
    
    # Add static "Getting Started" section
    getting_started = [
        ('Welcome', 'welcome.md'),
        ('How to Use This Wiki', 'how-to-use.md'),
        ('Search Tips', 'search-tips.md')
    ]
    
    output.append("\n# Getting Started\n\n")
    for title, path in getting_started:
        file_path = src_dir / path
        if file_path.exists():
            output.append(f"- [{title}](./{path})\n")
    
    output.append("\n---\n")
    
    # Scan categories directory
    categories_dir = src_dir / 'categories'
    if categories_dir.exists() and categories_dir.is_dir():
        output.append("\n# Wiki Content\n\n")
        
        # Get all categories
        categories = sorted([d for d in categories_dir.iterdir() 
                           if d.is_dir() and not should_skip(d)])
        
        for category in categories:
            # Scan category
            items = scan_directory(category, src_dir, level=0)
            
            if items:
                for title, path, level in items:
                    indent = "  " * level
                    output.append(f"{indent}- [{title}](./{path})\n")
    
    # Add static reference section
    output.append("\n---\n")
    output.append("\n# Reference\n\n")
    
    reference_pages = [
        ('Index', 'index.md'),
        ('Tags', 'tags.md'),
        ('Glossary', 'glossary.md')
    ]
    
    for title, path in reference_pages:
        file_path = src_dir / path
        if file_path.exists():
            output.append(f"- [{title}](./{path})\n")
    
    # Add static additional resources section
    output.append("\n---\n")
    output.append("\n# Additional Resources\n\n")
    
    additional = [
        ('Contributing', 'contributing.md'),
        ('License', 'license.md')
    ]
    
    for title, path in additional:
        file_path = src_dir / path
        if file_path.exists():
            output.append(f"- [{title}](./{path})\n")
    
    return ''.join(output)


def main():
    """Main entry point."""
    # Check for dry-run flag
    dry_run = '--dry-run' in sys.argv or '-n' in sys.argv
    
    # Determine src directory
    if len(sys.argv) > 1 and not sys.argv[1].startswith('-'):
        src_dir = Path(sys.argv[1])
    else:
        # Assume we're in the project root
        src_dir = Path('src')
    
    if not src_dir.exists():
        print(f"Error: {src_dir} does not exist", file=sys.stderr)
        sys.exit(1)
    
    # Generate summary
    summary = generate_summary(src_dir)
    
    if dry_run:
        print("=== DRY RUN - Preview of SUMMARY.md ===", file=sys.stderr)
        print(summary)
        print("\n=== End of preview ===", file=sys.stderr)
    else:
        print(summary)


if __name__ == '__main__':
    main()
