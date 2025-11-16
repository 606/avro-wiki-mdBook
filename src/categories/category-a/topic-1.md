# Topic 1

This is an example topic page demonstrating Obsidian and mdBook compatibility.

## Overview

This page shows how to structure content in a way that works well with both Obsidian and mdBook.

## Markdown Features

### Text Formatting

- **Bold text** for emphasis
- *Italic text* for subtle emphasis
- `Inline code` for code snippets
- ~~Strikethrough~~ for corrections

### Lists

Unordered lists:
- Item 1
- Item 2
  - Nested item A
  - Nested item B
- Item 3

Ordered lists:
1. First step
2. Second step
3. Third step

### Code Blocks

```python
def hello_world():
    """Example Python code"""
    print("Hello from the Avro Wiki!")
    return True
```

```javascript
// Example JavaScript code
function helloWorld() {
    console.log("Hello from the Avro Wiki!");
    return true;
}
```

### Links

Internal links (to other wiki pages):
- Markdown style: [Go to Welcome](../../welcome.md)
- Obsidian style: `[[Welcome]]` (requires preprocessor)

External links:
- [mdBook Documentation](https://rust-lang.github.io/mdBook/)
- [Obsidian](https://obsidian.md/)

### Tables

| Feature | mdBook | Obsidian | Both |
|---------|--------|----------|------|
| Markdown | ✓ | ✓ | ✓ |
| Search | ✓ | ✓ | ✓ |
| Wikilinks | Plugin | ✓ | Config |
| Themes | ✓ | ✓ | ✓ |

### Quotes

> "This is a blockquote. It can be used for important notes or citations."
> 
> — Someone Important

### Horizontal Rules

---

### Task Lists

- [x] Create example page
- [x] Add markdown examples
- [ ] Add more content
- [ ] Review and refine

## Images

You can include images like this:

```markdown
![Alt text](./images/example.png)
```

For images to work:
1. Create an `images/` folder in the category
2. Place images there
3. Reference with relative paths

## Admonitions (Notes/Warnings)

While mdBook doesn't have native admonition support, you can use blockquotes:

> **Note:** This is an important note about something.

> **Warning:** This is a warning about potential issues.

> **Tip:** This is a helpful tip for users.

## LaTeX/Math (if needed)

If you need math equations, you can enable MathJax in `book.toml`:

```markdown
Inline math: $E = mc^2$

Block math:
$$
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}
$$
```

## Metadata (Obsidian Frontmatter)

If your Obsidian notes use frontmatter, mdBook will ignore it by default:

```yaml
---
title: Topic 1
tags: [example, tutorial]
date: 2025-11-16
---
```

You can use a preprocessor to handle frontmatter if needed.

## Backlinks

In Obsidian, backlinks show pages that link to this one. In mdBook:
- You can manually maintain a "Referenced By" section
- Or use a script to generate backlink pages

## Tags

If you use tags in Obsidian:
- Create a [Tags page](../../tags.md) listing all tags
- Or group related pages by tag
- Or use a script to generate tag indices

## Best Practices

For maximum compatibility:

1. **Use relative links**: `./page.md` or `../other/page.md`
2. **Keep filenames simple**: lowercase, hyphens, no spaces
3. **Organize logically**: Use folders/categories effectively
4. **Test in both**: Check pages in Obsidian and mdBook
5. **Standard markdown**: Stick to common markdown features

## Related Topics

- [Topic 2](./topic-2.md)
- [Category B Topics](../category-b/README.md)
- [How to Use This Wiki](../../how-to-use.md)

---

**Category**: [Category A](./README.md)  
**Last Updated**: 2025-11-16
