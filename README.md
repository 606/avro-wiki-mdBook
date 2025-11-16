# Avro Wiki - mdBook

A comprehensive wiki built with mdBook, designed to handle 15000+ markdown files from Obsidian.

## 📚 Overview

This repository provides a complete mdBook setup optimized for large-scale wikis. It includes:

- ✅ **mdBook configuration** optimized for 15000+ pages
- ✅ **Hierarchical organization** with categories and topics
- ✅ **Obsidian compatibility** for seamless note-taking workflow
- ✅ **Powerful search** across all content
- ✅ **Automation scripts** for managing large wikis
- ✅ **Example content** showing best practices
- ✅ **Complete documentation** for contributors

## 🚀 Quick Start

### Prerequisites

- [mdBook](https://rust-lang.github.io/mdBook/) installed
- Git (for version control)
- Optional: [Obsidian](https://obsidian.md/) for editing

### Installation

```bash
# Clone the repository
git clone https://github.com/606/avro-wiki-mdBook.git
cd avro-wiki-mdBook

# Install mdBook (if not already installed)
cargo install mdbook
# Or download from: https://github.com/rust-lang/mdBook/releases

# Build the wiki
mdbook build

# Serve locally with live reload
mdbook serve --open
```

The wiki will open in your browser at `http://localhost:3000`.

## 📖 Usage

### Adding Content

1. **Create markdown files** in `src/` directory:
   ```
   src/
   ├── categories/
   │   └── your-category/
   │       └── your-page.md
   └── your-page.md
   ```

2. **Update SUMMARY.md** to include new pages in navigation

3. **Test locally**:
   ```bash
   mdbook serve
   ```

4. **Commit and push** your changes

### For Obsidian Users

1. Open this repository in Obsidian as a vault
2. Edit files in `src/` directory
3. Use standard markdown or Obsidian features
4. Build with mdBook when ready to publish

## 🛠️ Automation Scripts

For large wikis (15000+ files), use the included scripts:

### Generate SUMMARY.md
```bash
python3 scripts/generate_summary.py > src/SUMMARY.md
```

### Check for Broken Links
```bash
python3 scripts/check_links.py
```

### Custom Scripts
Add your own scripts in `scripts/` directory for:
- Generating indices
- Compiling tags
- Optimizing images
- Validating content

## 📁 Repository Structure

```
avro-wiki-mdBook/
├── book/                  # Built HTML (gitignored)
├── src/                   # Source markdown files
│   ├── SUMMARY.md        # Table of contents
│   ├── README.md         # Wiki homepage
│   ├── categories/       # Organized content
│   ├── welcome.md
│   ├── how-to-use.md
│   ├── search-tips.md
│   ├── index.md
│   ├── tags.md
│   ├── glossary.md
│   ├── contributing.md
│   ├── license.md
│   └── 404.md
├── scripts/              # Automation scripts
│   ├── generate_summary.py
│   └── check_links.py
├── book.toml            # mdBook configuration
├── .gitignore
└── README.md            # This file
```

## ⚙️ Configuration

The `book.toml` file is pre-configured with:

- Search optimization for large wikis
- Collapsible sidebar sections
- Theme customization
- Git integration
- Performance settings

Modify `book.toml` to customize further.

## 🎯 Features

### For Readers
- **Fast Search**: Find content across 15000+ pages instantly
- **Responsive Design**: Works on desktop and mobile
- **Multiple Themes**: Light and dark modes
- **Keyboard Navigation**: Shortcuts for efficient browsing
- **Print Support**: Export to PDF

### For Contributors
- **Markdown-based**: Write in plain text
- **Git-friendly**: Full version history
- **Obsidian Compatible**: Use your favorite editor
- **Live Reload**: See changes instantly
- **Validation Tools**: Check links and structure

### For Maintainers
- **Automation Scripts**: Generate indices and navigation
- **Scalable**: Handles 15000+ files efficiently
- **Customizable**: Themes, styling, and structure
- **Static Output**: Deploy anywhere (GitHub Pages, Netlify, etc.)

## 🌐 Deployment

### GitHub Pages

1. Build the book:
   ```bash
   mdbook build
   ```

2. The output is in `book/` directory

3. Deploy to GitHub Pages:
   - Use GitHub Actions workflow
   - Or manually copy `book/` to `gh-pages` branch

### Other Platforms

The built wiki (in `book/`) is static HTML and can be deployed to:
- Netlify
- Vercel
- AWS S3
- Any static hosting service

## 📝 Documentation

- [How to Use This Wiki](src/how-to-use.md) - User guide
- [Search Tips](src/search-tips.md) - Effective searching
- [Contributing Guide](src/contributing.md) - How to contribute
- [mdBook Documentation](https://rust-lang.github.io/mdBook/) - Official docs

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](src/contributing.md) for details.

## 📜 License

This project is licensed under the MIT License - see [LICENSE.md](src/license.md) for details.

## 🔧 Troubleshooting

### mdBook Not Found
Install mdBook: `cargo install mdbook` or download from releases

### Build Errors
- Check `book.toml` syntax
- Verify all links in `SUMMARY.md` point to existing files
- Run `python3 scripts/check_links.py` to find broken links

### Search Not Working
- Ensure JavaScript is enabled
- Rebuild the book: `mdbook build`
- Clear browser cache

## 💡 Tips for Large Wikis

1. **Use categories**: Organize content hierarchically
2. **Automate**: Use scripts to generate SUMMARY.md and indices
3. **Test regularly**: Build and check links frequently
4. **Optimize images**: Compress before adding
5. **Split large files**: Keep pages focused and manageable
6. **Use search**: Rely on search instead of complex navigation
7. **Document structure**: Maintain a clear organization scheme

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/606/avro-wiki-mdBook/issues)
- **Discussions**: [GitHub Discussions](https://github.com/606/avro-wiki-mdBook/discussions)
- **mdBook Help**: [mdBook Documentation](https://rust-lang.github.io/mdBook/)

---

**Built with** [mdBook](https://rust-lang.github.io/mdBook/) • **Compatible with** [Obsidian](https://obsidian.md/)