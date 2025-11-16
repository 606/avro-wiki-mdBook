# Quick Start: Adding Your Obsidian Notes

This guide helps you quickly add your existing Obsidian notes to this wiki.

## Option 1: Copy Notes to src/ Directory

### Step 1: Organize Your Notes

Copy your Obsidian notes into the `src/` directory:

```bash
# Example structure:
src/
├── README.md (keep this)
├── SUMMARY.md (will update)
├── your-notes/
│   ├── note1.md
│   ├── note2.md
│   └── subfolder/
│       └── note3.md
```

### Step 2: Generate SUMMARY.md

Use the automation script to generate navigation:

```bash
python3 scripts/generate_summary.py > src/SUMMARY.md
```

Or manually edit `src/SUMMARY.md` to add your notes.

### Step 3: Build and Test

```bash
mdbook serve --open
```

This opens the wiki in your browser with live reload.

### Step 4: Commit

```bash
git add .
git commit -m "Add my Obsidian notes"
git push
```

## Option 2: Use This Repo as Obsidian Vault

### Step 1: Open in Obsidian

1. Open Obsidian
2. Click "Open folder as vault"
3. Select the `src/` directory of this repository

### Step 2: Edit Notes

- Edit existing notes
- Create new notes
- Use all Obsidian features (tags, links, etc.)

### Step 3: Build

From the repository root:

```bash
mdbook build
```

### Step 4: Preview

```bash
mdbook serve --open
```

## Handling Large Numbers of Files (15000+)

### Organize by Categories

Create a structure like:

```
src/
├── SUMMARY.md
├── README.md
├── programming/
│   ├── python/
│   ├── rust/
│   └── javascript/
├── documentation/
├── projects/
└── reference/
```

### Auto-generate SUMMARY.md

For thousands of files, manual SUMMARY.md is impractical:

```bash
# Generate from filesystem structure
python3 scripts/generate_summary.py > src/SUMMARY.md

# Review the output
cat src/SUMMARY.md

# Build
mdbook build
```

### Performance Tips

1. **Use categories**: Don't put all 15000 files in one directory
2. **Limit nesting**: 3-4 levels deep maximum
3. **Split large files**: Break down very large documents
4. **Optimize images**: Compress images before adding
5. **Use search**: Rely on search instead of listing everything in SUMMARY.md

## Converting Obsidian Links

### Wikilinks to Markdown Links

If you use Obsidian wikilinks (`[[Page]]`), you have options:

#### Option 1: Keep Using Wikilinks

mdBook can handle wikilinks with a preprocessor. Add to `book.toml`:

```toml
[preprocessor.links]
# This will process Obsidian-style links
```

#### Option 2: Convert to Standard Markdown

Use a script to convert:

```bash
# Find all wikilinks
grep -r "\[\[" src/ --include="*.md"

# Convert manually or with a script
# [[Page Name]] -> [Page Name](./page-name.md)
```

#### Option 3: Use Both

Standard markdown links work in both Obsidian and mdBook.

## Handling Frontmatter

Obsidian frontmatter is preserved but not processed by default:

```yaml
---
title: My Page
tags: [tag1, tag2]
date: 2025-11-16
---
```

mdBook will ignore frontmatter, but you can:
- Use a preprocessor to extract and process it
- Use scripts to generate indices from frontmatter
- See `scripts/` directory for examples

## Handling Attachments

### Images

Place images near your markdown files:

```
src/
├── my-category/
│   ├── note.md
│   └── images/
│       ├── diagram.png
│       └── photo.jpg
```

Reference in markdown:

```markdown
![Description](./images/diagram.png)
```

### Other Files

For PDFs, videos, etc.:

```
src/
├── my-category/
│   ├── note.md
│   └── attachments/
│       ├── document.pdf
│       └── video.mp4
```

Link in markdown:

```markdown
[Download PDF](./attachments/document.pdf)
```

## Batch Operations

### Copy 15000+ Files

```bash
# From your Obsidian vault
cp -r /path/to/obsidian/vault/* /path/to/avro-wiki-mdBook/src/

# Generate SUMMARY.md
cd /path/to/avro-wiki-mdBook
python3 scripts/generate_summary.py > src/SUMMARY.md

# Build
mdbook build
```

### Check for Issues

```bash
# Check for broken links
python3 scripts/check_links.py

# Build and check for errors
mdbook build
```

### Validate Structure

```bash
# Make sure all files are reachable
make validate
```

## Common Issues

### Build Errors

**Problem**: SUMMARY.md references missing files

**Solution**: 
```bash
# Check what's referenced
cat src/SUMMARY.md

# Regenerate from actual files
python3 scripts/generate_summary.py > src/SUMMARY.md
```

### Broken Links

**Problem**: Internal links don't work

**Solution**:
```bash
# Find broken links
python3 scripts/check_links.py

# Fix manually or use relative paths
```

### Images Not Loading

**Problem**: Images don't appear in built wiki

**Solution**:
- Use relative paths: `./images/pic.png`
- Ensure images are in `src/` directory
- Check file paths match markdown references

### Slow Build

**Problem**: Building takes too long with many files

**Solution**:
- Organize files into categories
- Avoid deep nesting
- Consider splitting the wiki into multiple books

## Next Steps

1. **Read the docs**: 
   - [How to Use](./how-to-use.md)
   - [Contributing](./contributing.md)
   - [Search Tips](./search-tips.md)

2. **Customize**:
   - Edit `book.toml` for your needs
   - Customize theme and styling
   - Add custom CSS

3. **Deploy**:
   - See [README.md](../README.md) for deployment options
   - GitHub Pages, Netlify, or other hosting

4. **Automate**:
   - Set up pre-commit hooks
   - Use GitHub Actions
   - Create custom scripts

## Getting Help

- Check [Contributing Guide](./contributing.md)
- Review [mdBook Documentation](https://rust-lang.github.io/mdBook/)
- Search existing issues on GitHub

---

**Ready to start?** Copy your notes, run the scripts, and build your wiki! 🚀
