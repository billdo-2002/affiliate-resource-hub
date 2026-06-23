import os
import re

filepath = r"c:\Users\khoadnd\Desktop\onboarding hub\scratch\build_angles.py"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's search for how it replaces the article content and sidebar
print("Nesting logic in build_angles.py:")
idx = content.find("def build_page")
if idx != -1:
    print(content[idx:idx+1500])
else:
    print("def build_page not found in build_angles.py")
