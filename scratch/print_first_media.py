import os
import re

filepath = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\general-guide.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
style = style_match.group(1)

print(style[32730:34115])
