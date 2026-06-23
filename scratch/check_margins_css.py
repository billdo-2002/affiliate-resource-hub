import os
import re

filepath = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\angles\scale-safely-with-margins.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
style = style_match.group(1)

print("CSS has article-layout:", ".article-layout" in style)
print("HTML has article-layout:", "class=\"article-layout\"" in content)
print("CSS has guide-body-inner:", ".guide-body-inner" in style)
print("HTML has guide-body-inner:", "class=\"guide-body-inner\"" in content)
