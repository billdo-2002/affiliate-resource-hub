import os
import re

filepath = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\general-guide.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
style = style_match.group(1)

# Check for non-ASCII characters or weird control chars
weird_chars = []
for idx, char in enumerate(style):
    o = ord(char)
    if o < 32 and char not in ['\n', '\r', '\t']:
        weird_chars.append((idx, o, char))
    elif o > 127:
        # Non-ASCII is generally fine (like smart quotes, arrows, etc.), but let's print them just in case
        pass

print(f"Weird control characters found: {len(weird_chars)}")
for idx, o, char in weird_chars:
    print(f"  At char {idx}: code {o} ({repr(char)})")
