import os

filepath = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\general-guide.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

print("Contains 'Right Column: Sticky Sidebar':", 'Right Column: Sticky Sidebar' in content)
print("Contains 'guide-sidebar':", 'guide-sidebar' in content)
print("Contains 'article-sidebar':", 'article-sidebar' in content)
