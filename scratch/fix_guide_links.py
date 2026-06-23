"""
Fix the wrong article link hrefs in general-guide.html.
The links should be:
  angles/track-profit-like-a-pro.html (not ../guides/angles/...)
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

path = os.path.join(BASE, 'guides', 'general-guide.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

original = text

# Fix the article-link-row hrefs - they should be relative to guides/ directory
# Wrong: ../guides/angles/track-profit-like-a-pro.html
# Right: angles/track-profit-like-a-pro.html
text = text.replace(
    'href="../guides/angles/track-profit-like-a-pro.html" class="article-link-row"',
    'href="angles/track-profit-like-a-pro.html" class="article-link-row"'
)
text = text.replace(
    'href="../guides/angles/scale-safely-with-margins.html" class="article-link-row"',
    'href="angles/scale-safely-with-margins.html" class="article-link-row"'
)
text = text.replace(
    'href="../guides/angles/stop-losing-30-profit.html" class="article-link-row"',
    'href="angles/stop-losing-30-profit.html" class="article-link-row"'
)

if text != original:
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(text)
    print("Fixed article link hrefs in general-guide.html")
else:
    print("No changes needed")

# Verify
path = os.path.join(BASE, 'guides', 'general-guide.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, line in enumerate(lines, 1):
    if 'article-link-row' in line:
        print("%5d: %s" % (i, line.rstrip()[:120]))
