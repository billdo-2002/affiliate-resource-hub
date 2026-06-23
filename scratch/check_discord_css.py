import os
import re

filepath = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\discord-blueprint.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
style = style_match.group(1)

for cls in ['.guide-body-inner', '.guide-sidebar', '.guide-content']:
    print(f"=== {cls} ===")
    matches = list(re.finditer(re.escape(cls) + r'\s*\{([^}]*)\}', style))
    for i, m in enumerate(matches):
        print(f"  Occurrence {i+1} at index {m.start()}:")
        print(m.group(0))

print("\n=== Media queries with guide-body-inner or guide-sidebar ===")
mq_matches = list(re.finditer(r'@media[^{]*\{([^{}]*\{[^{}]*\}[^{}]*)*\}', style))
for mq in mq_matches:
    mq_text = mq.group(0)
    if any(cls in mq_text for cls in ['.guide-body-inner', '.guide-sidebar']):
        print(mq_text)
