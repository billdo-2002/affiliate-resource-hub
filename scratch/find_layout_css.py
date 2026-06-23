import os
import re

filepath = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\general-guide.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find all CSS rules for article-layout, article-sidebar, article-shell, article-content
style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
style = style_match.group(1)

for cls in ['.article-layout', '.article-sidebar', '.article-shell', '.article-content']:
    print(f"=== {cls} ===")
    matches = list(re.finditer(re.escape(cls) + r'\s*\{([^}]*)\}', style))
    for i, m in enumerate(matches):
        print(f"  Occurrence {i+1}:")
        print(m.group(0))

# Find media queries containing these classes
print("\n=== Media Queries containing these classes ===")
mq_matches = list(re.finditer(r'@media[^{]*\{([^{}]*\{[^{}]*\}[^{}]*)*\}', style))
for mq in mq_matches:
    mq_text = mq.group(0)
    if any(cls in mq_text for cls in ['.article-layout', '.article-sidebar', '.article-shell', '.article-content']):
        print(mq_text)
