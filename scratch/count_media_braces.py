import os
import re

filepath = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\general-guide.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
style = style_match.group(1)

# Find @media (min-width: 1024px)
m = re.search(r'@media\s*\(min-width:\s*1024px\)', style)
if m:
    start = m.start()
    # Find matching closing brace
    depth = 0
    sub = style[start:]
    for idx, char in enumerate(sub):
        if char == '{':
            depth += 1
        elif char == '}':
            depth -= 1
            if depth == 0:
                print(f"Matched closing brace at offset {idx} inside @media:")
                print(sub[:idx+1])
                break
else:
    print("@media (min-width: 1024px) not found")
