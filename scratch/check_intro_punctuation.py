import os

path = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\tiktok-youtube-shorts.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
    
# Find paragraph with "One of our partners"
start_idx = content.find("One of our partners")
if start_idx != -1:
    # Print 100 characters before and after
    print(content[start_idx-50:start_idx+150])
else:
    print("Not found")
