"""
Remove the redundant guide-body CSS that was added by our repair script,
since the original CSS already has the correct layout definitions.
The issue: our ARTICLE_CSS_FIX block added duplicate/conflicting CSS.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

# The CSS block we added in targeted_repair.py
ARTICLE_CSS_FIX_TO_REMOVE = '''
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

# Replace with a MINIMAL fix that only adds scroll-margin-top
# (which is all that's needed - the layout CSS already exists)
MINIMAL_SCROLL_FIX = '''
/* =========================================
   SCROLL OFFSET FIX - prevent content hiding under sticky header
   ========================================= */
.article-section,
h2[id], h3[id], div[id], section[id] {
  scroll-margin-top: 120px;
}
'''

HTML_FILES = [
    'guides/discord-blueprint.html',
    'guides/general-guide.html',
    'guides/tiktok-youtube-shorts.html',
    'guides/angles/scale-safely-with-margins.html',
    'guides/angles/stop-losing-30-profit.html',
    'guides/angles/track-profit-like-a-pro.html',
    'resources/mcp/reddit-ready-to-post.html',
    'resources/mcp/short-form-video-guidelines.html',
    'resources/mcp/x-twitter-ready-to-post.html',
]

for rel_path in HTML_FILES:
    path = os.path.join(BASE, rel_path.replace('/', os.sep))
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    original = text
    
    if ARTICLE_CSS_FIX_TO_REMOVE.strip() in text:
        text = text.replace(ARTICLE_CSS_FIX_TO_REMOVE.strip(), MINIMAL_SCROLL_FIX.strip())
        print("Fixed CSS in: %s" % rel_path)
    else:
        # Try to find and clean up any variant
        # The CSS may have slight differences in whitespace
        if 'display: flex;\n  gap: 40px;\n  max-width: 1200px;' in text:
            # More targeted removal
            print("Variant CSS found in: %s - needs manual check" % rel_path)
        else:
            print("No redundant CSS found in: %s" % rel_path)
    
    if text != original:
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(text)

print("\nDone!")
