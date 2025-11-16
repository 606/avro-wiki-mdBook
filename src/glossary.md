# Glossary

A glossary of terms used throughout this wiki.

## A

**Avro**
: Apache Avro - a data serialization system (if that's what this wiki is about)

**Automation**
: Using scripts and tools to automatically maintain the wiki structure and content.

## B

**Backlink**
: A link from another page pointing to the current page. Helps discover related content.

**Book**
: In mdBook terminology, the entire collection of pages that make up the wiki.

**Build**
: The process of converting markdown source files into HTML output.

## C

**Category**
: A top-level organizational unit for grouping related topics.

**Cross-reference**
: Links between related pages in the wiki.

## D

**Deploy**
: Publishing the built wiki to a web server or hosting platform.

## E

**Edit URL**
: Link that allows users to suggest changes to a page via GitHub.

## F

**Frontmatter**
: YAML metadata at the beginning of a markdown file, used by Obsidian and some other tools.

## G

**Git**
: Version control system used to track changes to the wiki.

**GitHub**
: Platform hosting the wiki's source code.

## H

**HTML**
: HyperText Markup Language - the output format after building the wiki.

## I

**Index**
: Alphabetical listing of all pages in the wiki.

**Internal Link**
: A link from one wiki page to another wiki page.

## L

**Live Reload**
: Feature that automatically refreshes the browser when source files change.

## M

**Markdown**
: Lightweight markup language used to write wiki pages.

**mdBook**
: The static site generator used to build this wiki.

## N

**Navigation**
: Moving between pages using the sidebar, links, or search.

## O

**Obsidian**
: A markdown editor and personal knowledge base application.

## P

**Preprocessor**
: A plugin that modifies markdown content before it's rendered to HTML.

**Pull Request**
: A proposed change to the wiki submitted via GitHub.

## R

**Relative Link**
: A link using a relative path (e.g., `./page.md`) rather than an absolute URL.

**Renderer**
: Component that converts markdown to HTML.

## S

**Search**
: Feature to find content across all wiki pages.

**SUMMARY.md**
: The file that defines the wiki's table of contents and navigation structure.

**Static Site**
: A website consisting of pre-generated HTML files (no server-side processing required).

## T

**Table of Contents (TOC)**
: The hierarchical outline of the wiki's structure.

**Tag**
: A keyword or label used to categorize and find related content.

**Theme**
: Visual appearance of the wiki (light, dark, etc.).

**Topic**
: A specific page or subject within a category.

## V

**Version Control**
: System for tracking changes to files over time (Git).

## W

**Wikilink**
: A link style using double brackets `[[Page Name]]`, popular in Obsidian.

## X-Z

---

## For Maintainers

### Adding Terms

To add a term to this glossary:

1. Choose the appropriate alphabetical section
2. Use this format:
   ```markdown
   **Term**
   : Definition of the term.
   ```
3. Keep definitions concise but complete
4. Add cross-references to related terms when relevant

### Auto-generating Glossary

For large wikis, consider:

1. **Extract from frontmatter**: If pages define terms
2. **Parse definition lists**: Collect definitions from all pages
3. **Maintain separately**: Keep a dedicated glossary file

Example script:

```python
#!/usr/bin/env python3
"""Extract glossary terms from markdown files"""
import re
from pathlib import Path

def extract_definitions(file_path):
    """Extract definition list entries from markdown"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match **Term**: Definition pattern
    pattern = r'\*\*([^*]+)\*\*\s*:\s*(.+?)(?=\n\n|\n\*\*|$)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    return [(term.strip(), defn.strip()) for term, defn in matches]

def generate_glossary(src_dir):
    """Compile glossary from all markdown files"""
    terms = {}
    
    for md_file in Path(src_dir).rglob("*.md"):
        if md_file.name == "glossary.md":
            continue
        
        definitions = extract_definitions(md_file)
        for term, defn in definitions:
            if term not in terms:
                terms[term] = defn
    
    # Sort by first letter
    by_letter = {}
    for term in sorted(terms.keys(), key=str.lower):
        first = term[0].upper()
        if first not in by_letter:
            by_letter[first] = []
        by_letter[first].append((term, terms[term]))
    
    # Generate markdown
    output = "# Glossary\n\n"
    for letter in sorted(by_letter.keys()):
        output += f"## {letter}\n\n"
        for term, defn in by_letter[letter]:
            output += f"**{term}**\n: {defn}\n\n"
    
    return output
```

### Style Guide

- **Capitalize terms**: Use proper capitalization
- **Be concise**: Keep definitions brief but complete
- **Add context**: Mention how the term relates to this wiki
- **Link related terms**: Cross-reference when helpful
- **Avoid jargon**: Define technical terms in plain language

---

**See Also**: [Alphabetical Index](./alphabetical-index.md), [Tags](./tags.md)
