# Search Tips

Master the search feature to quickly find what you need across 15000+ pages.

## Basic Search

### Quick Search
Press `s` or `/` to focus the search box, then start typing.

### Search as You Type
Results appear instantly - no need to press Enter.

### Preview Snippets
Each result shows a preview of where your search terms appear.

## Search Techniques

### Single Word
```
obsidian
```
Finds pages containing "obsidian"

### Multiple Words (AND)
```
markdown wiki
```
Finds pages containing both "markdown" AND "wiki" (order doesn't matter)

### Exact Phrases
```
"getting started"
```
Use quotes to search for exact phrases

### Case Insensitive
```
MDBOOK
mdbook
MdBook
```
All find the same results - search is case-insensitive

## Advanced Tips

### Use Specific Terms
❌ Too general: `how to use`
✓ More specific: `obsidian wikilinks`

Better terms = better results!

### Try Variations
If you don't find what you need, try:
- Synonyms: "guide" vs "tutorial" vs "documentation"
- Singular/plural: "link" vs "links"
- Different phrasings: "how to install" vs "installation"

### Search for Code
```
fn main()
```
Search works in code blocks too!

### Common vs. Rare Words
The search algorithm gives more weight to:
- Words in **titles** (boost: 2x)
- Words in **headings** (boost: varies)
- Rare words (appear in fewer pages)

## Understanding Results

### Result Ranking
Results are ranked by:
1. **Title matches** - highest priority
2. **Heading matches** - high priority  
3. **Content matches** - standard priority
4. **Term frequency** - how often terms appear
5. **Term rarity** - rarer terms rank higher

### Result Limit
By default, search shows up to **30 results**. If you don't see what you need:
- Make your query more specific
- Try different terms
- Check spelling

### Preview Context
Each result shows:
- Page title
- Matching text snippet (30 words)
- Highlighting of your search terms

## Search Configuration

This wiki's search is configured with:
- Boolean AND: All terms must appear
- Result limit: 30 pages
- Teaser length: 30 words
- Title boost: 2x
- Heading splitting: Level 3

## Performance

### Fast Indexing
- Search index is built during wiki build
- Index loads once on first search
- Subsequent searches are instant

### Large Wiki Optimization
For 15000+ pages:
- Search index is optimized for size
- Only relevant snippets are indexed
- Common words are de-emphasized

## Search Limitations

### What Search Doesn't Find
- Content in images (alt text is searchable)
- Filenames (page titles are searchable)
- Comments in code (if they're not rendered)

### Special Characters
Some characters have special meaning:
- Quotes `"` for exact phrases
- Others are generally treated as spaces

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `s` or `/` | Open search |
| `Esc` | Close search |
| `↓` or `Tab` | Next result |
| `↑` or `Shift+Tab` | Previous result |
| `Enter` | Go to selected result |

## Search Examples

### Example 1: Finding a Topic
**Goal**: Find information about installing mdBook
```
mdbook install
```
or
```
"how to install"
```

### Example 2: Finding Related Pages
**Goal**: Find all pages about configuration
```
configuration
```
Then refine:
```
configuration toml
```

### Example 3: Finding Code Examples
**Goal**: Find Rust code examples
```
rust fn main
```

### Example 4: Finding Recent Topics
**Goal**: Find pages about a recent feature
```
"version 0.4"
```

## Tips for Wiki Maintainers

To improve search results:

1. **Use Descriptive Titles**: Good titles appear in search results
2. **Write Clear Headings**: Headings are weighted higher in search
3. **Use Keywords**: Include terms people will search for
4. **Avoid Duplication**: Unique content ranks better
5. **Add Alt Text**: Make images searchable via alt text

## Mobile Search

On mobile devices:
1. Tap the search icon (🔍)
2. Type your query on the keyboard
3. Tap a result to navigate
4. Swipe down to dismiss search

## Troubleshooting

### No Results Found
- Check spelling
- Try different terms or synonyms
- Search for partial words
- Verify the content exists in the wiki

### Too Many Results
- Add more specific terms
- Use quotes for exact phrases
- Include rare/unique terms

### Wrong Results
- Use more specific terms
- Check for ambiguous terms
- Add context words to clarify meaning

### Search Not Working
- Ensure JavaScript is enabled
- Refresh the page to reload search index
- Check browser console for errors

---

**Pro Tip**: The best way to master search is to use it regularly. The more you search, the better you'll understand what works!
