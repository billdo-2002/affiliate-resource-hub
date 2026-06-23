import os

BASE = r"c:\Users\khoadnd\Desktop\onboarding hub"
scratch_dir = os.path.join(BASE, "scratch")

search_terms = ["discord-blueprint.html", "tiktok-youtube-shorts.html"]

for fn in os.listdir(scratch_dir):
    path = os.path.join(scratch_dir, fn)
    if os.path.isdir(path):
        continue
    if fn.endswith((".py", ".txt", ".md", ".json", ".ps1")):
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            for term in search_terms:
                if term in content:
                    # count occurrences
                    count = content.count(term)
                    print(f"Found '{term}' {count} times in scratch/{fn}")
        except Exception as e:
            pass
