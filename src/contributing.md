# Contributing to the Wiki

Thank you for your interest in contributing to the Avro Wiki! This guide will help you add or update content.

## Quick Start

1. **Fork** the repository on GitHub
2. **Clone** your fork locally
3. **Create** a branch for your changes
4. **Edit** markdown files in the `src/` directory
5. **Test** your changes with `mdbook serve`
6. **Commit** and push your changes
7. **Submit** a pull request

## Setting Up

### Prerequisites

- Git installed on your system
- mdBook installed (see [Installation](#installing-mdbook))
- Text editor (VS Code, Obsidian, vim, etc.)

### Installing mdBook

**Using Cargo (Rust package manager):**
```bash
cargo install mdbook
```

**Or download pre-built binaries:**
- Visit [mdBook releases](https://github.com/rust-lang/mdBook/releases)
- Download for your platform
- Extract and add to your PATH

**Verify installation:**
```bash
mdbook --version
```

### Clone the Repository

```bash
git clone https://github.com/606/avro-wiki-mdBook.git
cd avro-wiki-mdBook
```

## Making Changes

### Creating a New Page

1. **Choose the right location** in `src/`:
   ```
   src/
   ├── categories/
   │   ├── category-a/
   │   ├── category-b/
   │   └── category-c/
   └── your-new-page.md
   ```

2. **Create the markdown file**:
   ```bash
   touch src/categories/category-a/new-topic.md
   ```

3. **Add content** following the [Content Guidelines](#content-guidelines)

4. **Update SUMMARY.md** to include your page:
   ```markdown
   - [Category A](./categories/category-a/README.md)
     - [Topic 1](./categories/category-a/topic-1.md)
     - [New Topic](./categories/category-a/new-topic.md)  ← Add this
   ```

### Editing Existing Pages

1. **Find the file** in `src/`
2. **Make your changes** using markdown
3. **Test locally** (see [Testing](#testing-changes))
4. **Commit** with a descriptive message

### Testing Changes

**Start local server with live reload:**
```bash
mdbook serve --open
```

This will:
- Build the book
- Start a local web server (usually http://localhost:3000)
- Open in your default browser
- Auto-reload when you save changes

**Build without serving:**
```bash
mdbook build
```

Output goes to the `book/` directory.

**Check for errors:**
```bash
mdbook test
```

## Content Guidelines

### File Naming

- Use lowercase letters
- Use hyphens instead of spaces: `my-topic.md`
- Keep names concise but descriptive
- Avoid special characters

### Markdown Style

#### Headings
```markdown
# Page Title (H1 - only one per page)

## Main Section (H2)

### Subsection (H3)

#### Minor Section (H4)
```

#### Links
```markdown
# Relative links (preferred):
[Other Page](./other-page.md)
[Category](../category-a/README.md)

# Absolute links (for external):
[mdBook](https://rust-lang.github.io/mdBook/)
```

#### Code Blocks
````markdown
```language
code here
```
````

Always specify the language for syntax highlighting:
- `python`, `javascript`, `rust`, `bash`, `yaml`, `toml`, etc.

#### Images
```markdown
![Alt text](./images/image.png)

# Store images near the markdown file:
src/categories/category-a/
├── topic.md
└── images/
    └── diagram.png
```

### Page Structure

Recommended structure for wiki pages:

```markdown
# Page Title

Brief introduction (1-2 sentences).

## Overview

What is this page about?

## Main Content

The bulk of your content, organized with headings.

### Subsections

Break content into digestible sections.

## Examples

Concrete examples when applicable.

## See Also

- [Related Page 1](./related-1.md)
- [Related Page 2](./related-2.md)

---

**Category**: [Category Name](./README.md)
**Tags**: #tag1 #tag2
```

### Writing Tips

1. **Be clear and concise**: Get to the point quickly
2. **Use examples**: Show, don't just tell
3. **Link related content**: Help readers discover more
4. **Update dates**: Note when content was last updated
5. **Think about search**: Use terms people will search for

### Obsidian Compatibility

If you're using Obsidian to edit:

#### Wikilinks
Both styles work, but standard markdown is preferred:
```markdown
[[Page Name]]           # Obsidian style
[Page Name](./page.md)  # Standard markdown (preferred)
```

#### Frontmatter
You can use YAML frontmatter, though mdBook ignores it by default:
```yaml
---
title: My Page
tags: [example, tutorial]
date: 2025-11-16
---
```

#### Attachments
Store images and files in subdirectories:
```
src/categories/category-a/
├── README.md
├── topic.md
└── attachments/
    ├── image.png
    └── document.pdf
```

## Large Wiki Best Practices

For wikis with 15000+ files:

### Organization
- **Use categories**: Group related content
- **Limit nesting**: Don't go too deep (3-4 levels max)
- **Consistent naming**: Follow naming conventions
- **Index pages**: Create README.md for each directory

### Automation
- **Generate indices**: Auto-create index pages
- **Extract tags**: Parse and compile tag lists
- **Validate links**: Check for broken links
- **Update SUMMARY**: Script generation of SUMMARY.md

### Performance
- **Optimize images**: Compress before adding
- **Limit file size**: Split large pages
- **Clean builds**: Remove unused files
- **Monitor build time**: Watch for slowdowns

### Maintenance Scripts

Create scripts in `scripts/` directory:

```
scripts/
├── generate_summary.py    # Auto-generate SUMMARY.md
├── generate_index.py      # Create alphabetical index
├── generate_tags.py       # Extract and compile tags
├── check_links.py         # Validate all links
└── optimize_images.sh     # Compress images
```

Example usage:
```bash
# Before building:
python3 scripts/generate_summary.py > src/SUMMARY.md
python3 scripts/generate_index.py > src/alphabetical-index.md
python3 scripts/generate_tags.py > src/tags.md

# Build:
mdbook build
```

## Submitting Changes

### Commit Messages

Write clear commit messages:

```bash
# Good:
git commit -m "Add documentation for API endpoints"
git commit -m "Fix broken link in getting started guide"
git commit -m "Update installation instructions for Windows"

# Not as good:
git commit -m "Update"
git commit -m "Fix stuff"
git commit -m "WIP"
```

### Pull Request Process

1. **Push your branch**:
   ```bash
   git push origin your-branch-name
   ```

2. **Create pull request** on GitHub

3. **Fill in the template**:
   - What changed?
   - Why?
   - Testing done?
   - Related issues?

4. **Wait for review**

5. **Address feedback** if any

6. **Merge** once approved

### Pull Request Checklist

Before submitting:

- [ ] Content follows style guidelines
- [ ] Links are working
- [ ] Images are optimized
- [ ] SUMMARY.md is updated if new pages added
- [ ] Tested locally with `mdbook serve`
- [ ] No build errors or warnings
- [ ] Commit messages are clear

## Getting Help

- **mdBook Documentation**: https://rust-lang.github.io/mdBook/
- **Markdown Guide**: https://www.markdownguide.org/
- **GitHub Issues**: Report problems or suggest features
- **Discussions**: Ask questions on GitHub Discussions

## Code of Conduct

Be respectful and constructive:
- Be welcoming to newcomers
- Provide constructive feedback
- Focus on content, not contributors
- Follow project guidelines

## License

By contributing, you agree that your contributions will be licensed under the same license as this project.

---

Thank you for contributing to the Avro Wiki! 🎉
