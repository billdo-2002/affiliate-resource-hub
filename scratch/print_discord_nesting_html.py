import os, re

filepath = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\discord-blueprint.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find all occurrences of "guide-sidebar" in HTML (which starts with <div or similar)
matches = list(re.finditer(r'<[a-z]+[^>]*guide-sidebar', content, re.IGNORECASE))
print(f"Found {len(matches)} tag matches:")
for m in matches:
    start = m.start()
    print(f"  Match at index {start}:")
    print(content[start-500:start+800])
