import os
import re

filepath = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\general-guide.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
style = style_match.group(1)

matches = list(re.finditer(r'\.article-shell', style))
print(f"Total occurrences of .article-shell in style: {len(matches)}")
for i, m in enumerate(matches):
    start = m.start()
    print(f"  Occurrence {i+1} at index {start}:")
    print(style[max(0, start-100):start+300])
