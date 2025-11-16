# Tags

This page organizes content by tags/topics for easy discovery.

## About Tags

Tags help you find related content across different categories. This page lists all tags and the pages associated with them.

## Using Tags

- Click on a tag to jump to the list of pages with that tag
- Pages can have multiple tags
- Tags are maintained manually or via scripts

---

## Tag Index

### #example
Pages demonstrating examples and templates:
- [Topic 1](./categories/category-a/topic-1.md)
- [Topic 2](./categories/category-a/topic-2.md)

### #tutorial
Step-by-step guides and tutorials:
- [How to Use This Wiki](./how-to-use.md)
- [Search Tips](./search-tips.md)

### #reference
Reference documentation:
- [Glossary](./glossary.md)
- [Alphabetical Index](./alphabetical-index.md)

### #getting-started
Resources for new users:
- [Welcome](./welcome.md)
- [How to Use This Wiki](./how-to-use.md)

### #markdown
Markdown formatting and syntax:
- [Topic 1](./categories/category-a/topic-1.md)
- [Topic 2](./categories/category-a/topic-2.md)

### #configuration
Setup and configuration:
- [Contributing](./contributing.md)

---

## For Large Wikis

### Auto-generating Tags

For 15000+ pages, manually maintaining tags isn't practical. Consider:

#### Option 1: Parse Obsidian Frontmatter

If your Obsidian notes use frontmatter:

```yaml
---
tags: [example, tutorial]
---
```

Create a script to extract tags:

```python
#!/usr/bin/env python3
"""Extract tags from markdown frontmatter"""
import os
import re
from pathlib import Path
from collections import defaultdict

def extract_tags(file_path):
    """Extract tags from YAML frontmatter"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match YAML frontmatter
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return []
    
    frontmatter = match.group(1)
    
    # Extract tags
    tags_match = re.search(r'tags:\s*\[(.*?)\]', frontmatter)
    if tags_match:
        tags_str = tags_match.group(1)
        return [tag.strip().strip('"\'') for tag in tags_str.split(',')]
    
    return []

def generate_tag_index(src_dir):
    """Generate tag index from all markdown files"""
    tag_pages = defaultdict(list)
    
    for md_file in Path(src_dir).rglob("*.md"):
        if md_file.name in ["SUMMARY.md", "tags.md"]:
            continue
        
        tags = extract_tags(md_file)
        if tags:
            # Get title
            with open(md_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith('# '):
                        title = line[2:].strip()
                        break
                else:
                    title = md_file.stem
            
            rel_path = md_file.relative_to(src_dir)
            for tag in tags:
                tag_pages[tag].append((title, str(rel_path)))
    
    # Generate markdown
    output = "# Tags\n\n"
    output += "This page organizes content by tags/topics.\n\n"
    output += "---\n\n"
    output += "## Tag Index\n\n"
    
    for tag in sorted(tag_pages.keys()):
        output += f"### #{tag}\n\n"
        for title, path in sorted(tag_pages[tag]):
            output += f"- [{title}](./{path})\n"
        output += "\n"
    
    return output

if __name__ == "__main__":
    import sys
    src_dir = sys.argv[1] if len(sys.argv) > 1 else "src"
    print(generate_tag_index(src_dir))
```

#### Option 2: Parse Inline Tags

If you use inline tags like `#tag` in your content:

```python
def extract_inline_tags(content):
    """Extract #hashtags from content"""
    # Match #tag (but not in code blocks)
    # This is a simplified version
    tags = re.findall(r'(?:^|\s)#([a-zA-Z][\w-]*)', content)
    return tags
```

#### Option 3: Use a Preprocessor

Create an mdBook preprocessor to handle tags automatically:
- Extracts tags during build
- Generates tag pages dynamically
- Updates tag index

### Tag Organization Strategies

For large wikis:

1. **Hierarchical Tags**: Use paths like `category/subcategory`
   - Example: `programming/python`, `programming/rust`

2. **Tag Aliases**: Map multiple tags to canonical forms
   - Example: `js`, `javascript` → `javascript`

3. **Tag Limits**: Limit tags per page (e.g., 3-5 max)
   - Keeps tagging focused and meaningful

4. **Tag Guidelines**: Document tagging conventions
   - When to create new tags
   - How to name tags
   - Tag hierarchy

### Performance Considerations

- Generate tag pages during build, not at runtime
- Consider splitting into multiple tag pages if needed
- Use search for finding tagged content quickly

---

## Adding Tags to Your Pages

### In Frontmatter (Obsidian)
```yaml
---
tags: [example, tutorial, getting-started]
---
```

### In Content
Add a "Tags" section at the bottom of your page:

```markdown
---

**Tags**: #example #tutorial #getting-started
```

### Update This Page

After adding tags to pages:
1. Run the tag generation script
2. Rebuild the wiki
3. Verify tags appear correctly

---

**Tip**: For 15000+ pages, automation is essential. Set up a pre-build hook to regenerate the tag index automatically.
