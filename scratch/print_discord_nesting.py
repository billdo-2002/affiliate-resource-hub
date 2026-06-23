import os

filepath = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\discord-blueprint.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's search for "guide-sidebar" and print 500 characters before it
idx = content.find('guide-sidebar')
if idx != -1:
    print(content[idx-500:idx+500])
else:
    print("guide-sidebar not found")
