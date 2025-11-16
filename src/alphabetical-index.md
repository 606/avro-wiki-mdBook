# Index

This page serves as an alphabetical index of all major topics in the wiki.

## A

- [Avro Wiki](./README.md)

## B

## C

- [Category A](./categories/category-a/README.md)
- [Category B](./categories/category-b/README.md)
- [Category C](./categories/category-c/README.md)
- [Contributing](./contributing.md)

## D-E

## F-G

- [Glossary](./glossary.md)

## H

- [How to Use This Wiki](./how-to-use.md)

## I-L

## M-O

## P-R

## S

- [Search Tips](./search-tips.md)

## T

- [Tags](./tags.md)

## U-Z

---

## For Large Wikis (15000+ pages)

For a wiki with thousands of pages, consider:

1. **Auto-generate this index** using a script that scans all markdown files
2. **Split into multiple index pages** (A-D, E-H, I-L, M-P, Q-T, U-Z)
3. **Use search instead** - the search feature is often more effective
4. **Create topic-specific indices** - one index per category
5. **Maintain programmatically** - update with each build

## Example Script

```python
#!/usr/bin/env python3
"""Generate index from markdown files"""
import os
from pathlib import Path

def generate_index(src_dir):
    """Scan src directory and generate alphabetical index"""
    index = {}
    for md_file in Path(src_dir).rglob("*.md"):
        if md_file.name == "SUMMARY.md":
            continue
        # Parse title from first heading
        with open(md_file) as f:
            first_line = f.readline().strip()
            if first_line.startswith("# "):
                title = first_line[2:]
                first_letter = title[0].upper()
                if first_letter not in index:
                    index[first_letter] = []
                rel_path = md_file.relative_to(src_dir)
                index[first_letter].append((title, str(rel_path)))
    
    # Generate markdown
    output = "# Index\n\n"
    for letter in sorted(index.keys()):
        output += f"## {letter}\n\n"
        for title, path in sorted(index[letter]):
            output += f"- [{title}](./{path})\n"
        output += "\n"
    
    return output

if __name__ == "__main__":
    import sys
    src_dir = sys.argv[1] if len(sys.argv) > 1 else "src"
    print(generate_index(src_dir))
```

Save this as `scripts/generate_index.py` and run before building:

```bash
python3 scripts/generate_index.py > src/index.md
mdbook build
```
