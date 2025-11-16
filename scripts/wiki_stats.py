#!/usr/bin/env python3
"""
Wiki statistics generator.

This script analyzes the wiki and provides statistics about:
- Number of files
- Total word count
- Average page length
- Categories and topics
- Link count

Usage:
    python3 scripts/wiki_stats.py
"""

import os
import re
from pathlib import Path
from collections import defaultdict


def count_words(content):
    """Count words in markdown content, excluding frontmatter and code blocks."""
    # Remove frontmatter
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
    
    # Remove code blocks
    content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    
    # Remove inline code
    content = re.sub(r'`[^`]+`', '', content)
    
    # Remove markdown links but keep text
    content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)
    
    # Remove HTML tags
    content = re.sub(r'<[^>]+>', '', content)
    
    # Count words
    words = content.split()
    return len(words)


def extract_links(content):
    """Extract all markdown links from content."""
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    return re.findall(pattern, content)


def analyze_wiki(src_dir):
    """Analyze the wiki and return statistics."""
    stats = {
        'total_files': 0,
        'total_words': 0,
        'total_links': 0,
        'categories': defaultdict(int),
        'files_by_size': [],
        'internal_links': 0,
        'external_links': 0,
    }
    
    # Find all markdown files
    for md_file in Path(src_dir).rglob('*.md'):
        # Skip SUMMARY.md
        if md_file.name == 'SUMMARY.md':
            continue
        
        stats['total_files'] += 1
        
        # Read file
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Warning: Could not read {md_file}: {e}")
            continue
        
        # Count words
        words = count_words(content)
        stats['total_words'] += words
        
        # Track file size
        rel_path = md_file.relative_to(src_dir)
        stats['files_by_size'].append((str(rel_path), words))
        
        # Count links
        links = extract_links(content)
        stats['total_links'] += len(links)
        
        for _, link in links:
            if link.startswith(('http://', 'https://')):
                stats['external_links'] += 1
            else:
                stats['internal_links'] += 1
        
        # Track categories
        if 'categories' in str(md_file):
            parts = md_file.parts
            if 'categories' in parts:
                cat_idx = parts.index('categories')
                if cat_idx + 1 < len(parts):
                    category = parts[cat_idx + 1]
                    stats['categories'][category] += 1
    
    return stats


def print_stats(stats):
    """Print statistics in a readable format."""
    print("📊 Wiki Statistics")
    print("=" * 60)
    print()
    
    print("📄 Files")
    print(f"  Total markdown files: {stats['total_files']}")
    print()
    
    print("📝 Content")
    print(f"  Total words: {stats['total_words']:,}")
    if stats['total_files'] > 0:
        avg_words = stats['total_words'] / stats['total_files']
        print(f"  Average words per page: {avg_words:.0f}")
    print()
    
    print("🔗 Links")
    print(f"  Total links: {stats['total_links']}")
    print(f"  Internal links: {stats['internal_links']}")
    print(f"  External links: {stats['external_links']}")
    print()
    
    if stats['categories']:
        print("📁 Categories")
        for category, count in sorted(stats['categories'].items()):
            print(f"  {category}: {count} files")
        print()
    
    # Top 10 largest files
    if stats['files_by_size']:
        print("📏 Largest Pages (by word count)")
        sorted_files = sorted(stats['files_by_size'], key=lambda x: x[1], reverse=True)
        for path, words in sorted_files[:10]:
            print(f"  {words:4d} words - {path}")
        print()
    
    # Estimated reading time (assuming 200 words per minute)
    if stats['total_words'] > 0:
        reading_time = stats['total_words'] / 200
        hours = int(reading_time / 60)
        minutes = int(reading_time % 60)
        print("⏱️  Estimated Reading Time")
        if hours > 0:
            print(f"  Entire wiki: ~{hours}h {minutes}m")
        else:
            print(f"  Entire wiki: ~{minutes}m")
        print()
    
    print("=" * 60)


def main():
    """Main entry point."""
    import sys
    
    # Determine src directory
    if len(sys.argv) > 1:
        src_dir = Path(sys.argv[1])
    else:
        src_dir = Path('src')
    
    if not src_dir.exists():
        print(f"Error: {src_dir} does not exist")
        sys.exit(1)
    
    # Analyze wiki
    stats = analyze_wiki(src_dir)
    
    # Print statistics
    print_stats(stats)


if __name__ == '__main__':
    main()
