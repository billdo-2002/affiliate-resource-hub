"""
TARGETED REPAIR SCRIPT
Fixes specific remaining issues without replacing entire header structure.

Issues to fix:
1. mcp-promotion.html: Missing announce bar (insert before <header)
2. All files: Wrong MCP link (mcp-promotion-playbook.html -> mcp-promotion.html)
3. All files: Add scroll-margin-top to article-section / [id] elements
4. All files: Body text font size / line height (add CSS if missing)
5. guides/general-guide.html: Fix article link hrefs (missing .html extension)
"""

import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

FILES = [
    ('index.html', '', 'index'),
    ('guides.html', '', 'guides'),
    ('mcp-promotion.html', '', 'mcp'),
    ('guides/discord-blueprint.html', '../', 'guide'),
    ('guides/general-guide.html', '../', 'guide'),
    ('guides/tiktok-youtube-shorts.html', '../', 'guide'),
    ('guides/angles/scale-safely-with-margins.html', '../../', 'angle'),
    ('guides/angles/stop-losing-30-profit.html', '../../', 'angle'),
    ('guides/angles/track-profit-like-a-pro.html', '../../', 'angle'),
    ('resources/mcp/reddit-ready-to-post.html', '../../', 'mcp-resource'),
    ('resources/mcp/short-form-video-guidelines.html', '../../', 'mcp-resource'),
    ('resources/mcp/x-twitter-ready-to-post.html', '../../', 'mcp-resource'),
]

ANNOUNCE_BAR = '''<div id="announce-bar">
  <span class="announce-star">&#9733;</span>
  <span>Earn 100% on your first month + 20% recurring for the year. Join 1,000+ affiliates.</span>
  <a href="https://affiliate.trueprofit.io/sign-up" target="_blank">JOIN NOW</a>
  <span class="announce-star">&#9733;</span>
  <button class="close-btn" onclick="document.getElementById('announce-bar').style.display='none'" aria-label="Close">&times;</button>
</div>'''

# CSS to add for article layout fixes
ARTICLE_CSS_FIX = '''
/* =========================================
   ARTICLE LAYOUT FIX - scroll offset + typography
   ========================================= */
.article-section,
h2[id], h3[id], div[id], section[id] {
  scroll-margin-top: 120px;
}
.guide-content {
  font-size: 18px;
  line-height: 1.75;
}
.guide-body {
  display: flex;
  gap: 40px;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px 80px;
}
.guide-body-inner {
  display: flex;
  gap: 40px;
  width: 100%;
}
.guide-content {
  flex: 1;
  min-width: 0;
  max-width: 860px;
}
.guide-sidebar {
  width: 320px;
  flex-shrink: 0;
}
'''

HOOK_PANEL_CSS_FIX = '''
/* =========================================
   HOOK PANEL FIX
   ========================================= */
.hook-panel {
  background: #f0fdf4;
  border-radius: 24px;
  border: 1px solid rgba(15, 23, 42, 0.08);
  padding: 32px;
  display: flex;
  gap: 32px;
  align-items: flex-start;
  margin: 32px 0;
  overflow: hidden;
}
.hook-panel-img {
  flex: 0 0 300px;
  max-width: 300px;
}
.hook-panel-img img {
  width: 100%;
  height: auto;
  border-radius: 12px;
  object-fit: cover;
}
.hook-panel-content {
  flex: 1;
  min-width: 0;
}
@media (max-width: 768px) {
  .hook-panel {
    flex-direction: column;
  }
  .hook-panel-img {
    flex: none;
    max-width: 100%;
  }
}
'''

COPY_BLOCK_CSS_FIX = '''
/* =========================================
   COPY BLOCK FIX
   ========================================= */
.copy-block {
  background: #f8fafc;
  border-radius: 16px;
  padding: 36px 40px;
  position: relative;
  margin: 24px 0;
  border: 1px solid #e2e8f0;
}
.copy-block-header {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 16px;
}
.copy-btn {
  font-family: var(--font, 'Plus Jakarta Sans', sans-serif);
  font-size: 13px;
  font-weight: 600;
  color: #374151;
  background: #fff;
  border: 1.5px solid #d1d5db;
  padding: 6px 14px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.copy-btn:hover {
  border-color: #1d9e75;
  color: #1d9e75;
  background: #f0fdf4;
}
.copy-block p {
  margin: 0 0 16px;
  line-height: 1.7;
  color: #1e293b;
  font-size: 16px;
}
.copy-block p:last-child { margin-bottom: 0; }
.affiliate-link {
  font-family: 'Courier New', monospace;
  background: #d1fae5;
  color: #065f46;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 0.95em;
}
.material-note {
  text-align: center;
  font-style: italic;
  color: #94a3b8;
  font-size: 14px;
  margin-top: 20px;
}
'''

TABLE_CSS_FIX = '''
/* =========================================
   SCRIPT TABLE FIX
   ========================================= */
.table-wrapper {
  overflow-x: auto;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
  margin: 24px 0;
}
.script-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 15px;
  min-width: 700px;
}
.script-table th {
  background: #f1f5f9;
  color: #0f172a;
  font-weight: 600;
  padding: 14px 16px;
  text-align: left;
  border-bottom: 2px solid #e2e8f0;
  white-space: nowrap;
}
.script-table td {
  padding: 14px 16px;
  border-bottom: 1px solid #f1f5f9;
  vertical-align: top;
  line-height: 1.6;
  color: #374151;
}
.script-table tr:last-child td { border-bottom: none; }
.script-table tr:nth-child(even) td { background: #fafafa; }
.script-table tr:hover td { background: #f0fdf4; }
'''

def process_file(rel_path, prefix, page_type):
    path = os.path.join(BASE, rel_path.replace('/', os.sep))
    
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    original = text
    changes = []
    
    # Fix 1: mcp-promotion.html - Add announce bar if missing
    if 'id="announce-bar"' not in text and "id='announce-bar'" not in text:
        # Insert before <header
        header_match = re.search(r'<header\s', text)
        if header_match:
            text = text[:header_match.start()] + ANNOUNCE_BAR + '\n\n' + text[header_match.start():]
            changes.append("Added missing announce bar")
    
    # Fix 2: Fix wrong MCP promotion link
    # mcp-promotion-playbook.html -> mcp-promotion.html
    old_mcp_link = prefix + 'guides/mcp-promotion-playbook.html'
    new_mcp_link = prefix + 'mcp-promotion.html'
    if old_mcp_link in text:
        text = text.replace(old_mcp_link, new_mcp_link)
        changes.append("Fixed MCP promotion link")
    
    # Also fix variant without prefix
    if 'guides/mcp-promotion-playbook.html' in text:
        text = text.replace('guides/mcp-promotion-playbook.html', prefix + 'mcp-promotion.html')
        changes.append("Fixed MCP promotion link (variant)")
    
    # Fix 3: Add scroll-margin-top CSS if guide/article page
    if 'article-section' in text and 'scroll-margin-top' not in text:
        # Add to end of first </style>
        text = text.replace('</style>', ARTICLE_CSS_FIX + '</style>', 1)
        changes.append("Added scroll-margin-top CSS")
    
    # Fix 4: Add hook panel CSS if page has hook panels
    if 'hook-panel' in text and 'hook-panel-img' not in text:
        text = text.replace('</style>', HOOK_PANEL_CSS_FIX + '</style>', 1)
        changes.append("Added hook panel CSS")
    
    # Fix 5: Add copy block CSS if page has copy blocks
    if ('copy-block' in text or 'copy-post' in text.lower()) and 'affiliate-link' not in text:
        text = text.replace('</style>', COPY_BLOCK_CSS_FIX + '</style>', 1)
        changes.append("Added copy block CSS")
    
    # Fix 6: Add table CSS if page has script tables
    if 'script-table' in text and 'table-wrapper' not in text:
        text = text.replace('</style>', TABLE_CSS_FIX + '</style>', 1)
        changes.append("Added script table CSS")
    
    # Fix 7: Fix article link hrefs in general-guide (missing .html)
    if 'general-guide' in rel_path:
        # Fix links like /guides/angles/track-profit-like-a-pro (missing .html)
        text = re.sub(
            r'href="(/guides/angles/[^"]+(?<!\.html))"',
            lambda m: 'href="' + prefix + m.group(1).lstrip('/') + '.html"',
            text
        )
        changes.append("Fixed guide angle link hrefs")
    
    # Fix 8: Fix affiliate link placeholder style in copy blocks
    text = re.sub(
        r'\[your affiliate link\]',
        '<span class="affiliate-link">[your affiliate link]</span>',
        text
    )
    if '[your affiliate link]' in original:
        changes.append("Styled affiliate link placeholder")
    
    if text != original:
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(text)
        return True, changes
    else:
        return False, []


print("=" * 60)
print("TARGETED REPAIR")
print("=" * 60)

for rel_path, prefix, page_type in FILES:
    print("\nProcessing: %s" % rel_path)
    changed, changes = process_file(rel_path, prefix, page_type)
    if changed:
        for c in changes:
            print("  + %s" % c)
    else:
        print("  (no changes needed)")

print("\n" + "=" * 60)
print("Done!")
