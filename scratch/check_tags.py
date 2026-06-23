import os
import re

filepath = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\general-guide.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all style tags
style_tags = list(re.finditer(r'<style[^>]*>', content, re.IGNORECASE))
print(f"Total style tags: {len(style_tags)}")
for i, m in enumerate(style_tags):
    print(f"  Style tag {i+1}: {m.group(0)} at position {m.start()}")

# Find all link tags
link_tags = list(re.finditer(r'<link[^>]*>', content, re.IGNORECASE))
print(f"Total link tags: {len(link_tags)}")
for i, m in enumerate(link_tags):
    print(f"  Link tag {i+1}: {m.group(0)}")
