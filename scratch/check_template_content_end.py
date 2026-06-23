import os

filepath = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\general-guide.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's search for "Build Your Audience" and print the next 200 chars
idx = content.find("Build Your Audience")
if idx != -1:
    print(content[idx:idx+800])
else:
    print("Build Your Audience not found")
