import os
import re

filepath = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\general-guide.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find ".article-shell" and print 50 chars before and 100 chars after as a list of character codes
idx = content.find('.article-shell')
if idx != -1:
    sub = content[idx-100:idx+150]
    print(f"Index: {idx}")
    print("Subtext:")
    print(repr(sub))
    print("Char codes:")
    print([ord(c) for c in sub])
else:
    print(".article-shell not found in content!")
