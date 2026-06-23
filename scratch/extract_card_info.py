import os

BASE = r"c:\Users\khoadnd\Desktop\onboarding hub"
guides_file = os.path.join(BASE, "guides.html")

with open(guides_file, "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for "Discord &amp; Community Blueprint"
pos = content.find("Discord &amp; Community Blueprint")
if pos != -1:
    print("\n--- Found Discord Card ---")
    start = max(0, pos - 400)
    end = min(len(content), pos + 1000)
    print(content[start:end])

# Let's search for "TikTok &amp; YouTube Shorts" (skip first in mega menu, find second)
pos2 = content.find("TikTok &amp; YouTube Shorts")
# Find next
pos2 = content.find("TikTok &amp; YouTube Shorts", pos2 + 100)
if pos2 != -1:
    print("\n--- Found TikTok Card ---")
    start = max(0, pos2 - 400)
    end = min(len(content), pos2 + 1000)
    print(content[start:end])
