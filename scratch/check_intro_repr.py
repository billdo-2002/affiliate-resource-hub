import os

path = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\tiktok-youtube-shorts.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
    
# Find paragraph with "One of our partners"
start_idx = content.find("One of our partners")
if start_idx != -1:
    chunk = content[start_idx-20:start_idx+120]
    with open("scratch/repr.txt", "w") as out:
        out.write(repr(chunk))
    print("Wrote repr to scratch/repr.txt")
else:
    print("Not found")
