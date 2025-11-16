# How to Use This Wiki

This guide will help you make the most of this wiki's features.

## Navigation

### Sidebar Navigation
The sidebar on the left shows the wiki's structure:
- Click on any item to go to that page
- Click on category headers to expand/collapse sections
- The current page is highlighted

### Breadcrumbs
At the top of each page, you'll see the path to the current page, helping you understand where you are in the wiki structure.

### Previous/Next Buttons
At the bottom of each page, use the arrow buttons to navigate sequentially through the wiki.

## Search

### Basic Search
1. Click the search icon (🔍) or press `s` or `/`
2. Type your search query
3. Results appear instantly as you type
4. Click any result to jump to that page

### Search Tips
- Search looks through **all pages** and their content
- Results show a preview of matching text
- More specific queries give better results
- See [Search Tips](./search-tips.md) for advanced techniques

## Reading Content

### Markdown Features
This wiki supports full markdown syntax:

- **Bold text**: `**bold**` → **bold**
- *Italic text*: `*italic*` → *italic*
- `Code`: `` `code` `` → `code`
- [Links](./welcome.md): `[text](url)` → [text](url)
- Lists, tables, images, and more

### Code Blocks
```rust
fn main() {
    println!("Code blocks support syntax highlighting!");
}
```

### Tables
| Feature | Supported |
|---------|-----------|
| Search  | ✓         |
| Mobile  | ✓         |
| Export  | ✓         |

## Obsidian Integration

If you're using Obsidian to edit this wiki:

### Internal Links
- Obsidian-style links: `[[Page Name]]`
- Standard markdown: `[Page Name](./page-name.md)`
- Both work in the wiki!

### Attachments
- Place images in a subdirectory (e.g., `images/`)
- Reference them: `![Alt text](./images/image.png)`

### Tags
While Obsidian tags (`#tag`) won't be automatically indexed, you can:
- Create a [Tags](./tags.md) page
- List pages by tag manually
- Or use custom scripts to generate tag indices

## Editing Content

### On GitHub
1. Click the edit button (✏️) on any page
2. This opens the file on GitHub
3. Make your changes
4. Submit a pull request

### Locally
1. Clone the repository
2. Edit markdown files in the `src/` directory
3. Test with `mdbook serve`
4. Commit and push your changes

## Exporting

### Print to PDF
1. Click the print button (🖨️) in the top right
2. Use your browser's print function
3. Select "Save as PDF"

### View Source
Click the source code icon to see the markdown source of any page.

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `s` or `/` | Focus search |
| `←` | Previous page |
| `→` | Next page |
| `Esc` | Close search/sidebar |

## Mobile Usage

The wiki is fully responsive:
- Tap the menu icon (☰) to open the sidebar
- Swipe left/right to navigate pages
- All features work on mobile browsers

## Troubleshooting

### Page Not Found
- Check spelling in the URL
- Use search to find the page
- The page may have been moved or renamed

### Search Not Working
- Ensure JavaScript is enabled
- Try refreshing the page
- Search index loads on first visit

### Images Not Loading
- Check the image path is correct
- Ensure images are in the `src/` directory
- Use relative paths: `./images/image.png`

## Advanced Features

### Custom Styling
The wiki supports custom CSS for advanced users.

### Themes
Switch between light and dark themes using the theme selector (🎨).

### Multi-language
While currently in English, mdBook supports multiple languages.

---

For more help, see the [mdBook Documentation](https://rust-lang.github.io/mdBook/).
