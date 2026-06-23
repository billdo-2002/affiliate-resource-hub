import os

BASE = r"c:\Users\khoadnd\Desktop\onboarding hub"
tail_file = os.path.join(BASE, "latest_tail.txt")

if not os.path.exists(tail_file):
    print("latest_tail.txt does not exist!")
    exit(1)

with open(tail_file, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

print(f"latest_tail.txt size: {len(content)} bytes")

# Let's search for "discord 1.webp" and extract surrounding text
idx = 0
while True:
    pos = content.find("discord 1.webp", idx)
    if pos == -1:
        break
    print(f"\n--- Found occurrence of discord 1.webp at index {pos} ---")
    start = max(0, pos - 2000)
    end = min(len(content), pos + 4000)
    snippet = content[start:end]
    print(snippet[:1500])
    # Let's write the snippet to a separate file to inspect it
    with open(f"scratch/found_discord_snippet_{pos}.txt", "w", encoding="utf-8") as out:
        out.write(snippet)
    idx = pos + 1
