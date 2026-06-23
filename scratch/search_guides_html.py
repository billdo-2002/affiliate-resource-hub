import os

BASE = r"c:\Users\khoadnd\Desktop\onboarding hub"
guides_file = os.path.join(BASE, "guides.html")

with open(guides_file, "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for "general-guide.html"
idx = 0
while True:
    pos = content.find("general-guide.html", idx)
    if pos == -1:
        break
    print(f"\n--- Found general-guide.html at index {pos} ---")
    start = max(0, pos - 200)
    end = min(len(content), pos + 400)
    print(content[start:end])
    idx = pos + 1
