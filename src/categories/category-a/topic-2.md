# Topic 2

This is another example topic page showing different content types.

## Overview

This page demonstrates additional markdown features and content organization patterns useful for a large wiki.

## Diagrams (Text-based)

### Flow Diagrams

You can use ASCII art for simple diagrams:

```
┌─────────────┐
│   Start     │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Process A  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Process B  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│     End     │
└─────────────┘
```

### Hierarchy

```
Wiki Root
├── Category A
│   ├── Topic 1
│   ├── Topic 2
│   └── Topic 3
├── Category B
│   ├── Topic 1
│   └── Topic 2
└── Category C
    └── Topic 1
```

## Nested Content

### Deep Nesting Example

#### Level 4 Heading
Content under level 4.

##### Level 5 Heading
Content under level 5.

###### Level 6 Heading
Content under level 6 (deepest level in markdown).

## Multiple Code Languages

### Python
```python
class WikiPage:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    def render(self):
        return f"# {self.title}\n\n{self.content}"
```

### JavaScript
```javascript
class WikiPage {
    constructor(title, content) {
        this.title = title;
        this.content = content;
    }
    
    render() {
        return `# ${this.title}\n\n${this.content}`;
    }
}
```

### Rust
```rust
struct WikiPage {
    title: String,
    content: String,
}

impl WikiPage {
    fn new(title: String, content: String) -> Self {
        WikiPage { title, content }
    }
    
    fn render(&self) -> String {
        format!("# {}\n\n{}", self.title, self.content)
    }
}
```

### Shell/Bash
```bash
#!/bin/bash
# Build the wiki
echo "Building wiki..."
mdbook build

# Serve locally
echo "Starting local server..."
mdbook serve --open
```

## Definition Lists

While not native to all markdown flavors, you can create definition lists:

**Term 1**
: Definition of term 1

**Term 2**
: Definition of term 2
: Additional definition for term 2

## Footnotes

Some markdown processors support footnotes[^1], but mdBook doesn't natively.

Instead, use manual references:

See reference [1] for more information.

---

References:
1. [mdBook Guide](https://rust-lang.github.io/mdBook/)

## Collapsible Content

HTML details/summary works in most markdown:

<details>
<summary>Click to expand</summary>

This content is hidden by default and can be revealed by clicking.

- Hidden item 1
- Hidden item 2
- Hidden item 3

</details>

## Alerts/Callouts

### Information
> ℹ️ **Information**
> 
> This is an informational callout.

### Success
> ✅ **Success**
> 
> This indicates a successful operation or positive outcome.

### Warning
> ⚠️ **Warning**
> 
> This is a warning about something important.

### Error
> ❌ **Error**
> 
> This indicates an error or problem.

### Tip
> 💡 **Tip**
> 
> This is a helpful tip or best practice.

## File Paths and Commands

When documenting paths or commands:

**File paths:**
- Linux/Mac: `/home/user/wiki/src/README.md`
- Windows: `C:\Users\user\wiki\src\README.md`

**Commands:**
```bash
# Install mdBook
cargo install mdbook

# Build the book
mdbook build

# Serve with live reload
mdbook serve
```

## Cross-References

### Within This Category
- [Topic 1](./topic-1.md) - Basic markdown examples
- [Category A Home](./README.md) - Category overview

### To Other Categories
- [Category B](../category-b/README.md)
- [Category C](../category-c/README.md)

### To Main Pages
- [Home](../../README.md)
- [Welcome](../../welcome.md)
- [How to Use](../../how-to-use.md)

## Search Optimization

To make this page more searchable:
- Use clear, descriptive headings
- Include relevant keywords naturally
- Provide good page title
- Use synonyms for important concepts

Keywords for this page: example, template, markdown, formatting, code, diagrams

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-11-16 | Initial creation |

## Metadata

- **Category**: Category A
- **Tags**: example, tutorial, markdown, formatting
- **Difficulty**: Beginner
- **Estimated Reading Time**: 5 minutes

---

[← Previous: Topic 1](./topic-1.md) | [Category A Home](./README.md)

