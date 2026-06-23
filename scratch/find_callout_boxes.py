import os
import re

search_dir = r"c:\Users\khoadnd\Desktop\onboarding hub"
matches = {}

for root, dirs, files in os.walk(search_dir):
    for f in files:
        if f.endswith(".html") and ".gemini" not in root:
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
                
            # Search for note/callout box classes
            # Classes like class="article-note...", class="common-mistake..."
            found = []
            lines = content.splitlines()
            for idx, line in enumerate(lines):
                if any(x in line for x in ['class="article-note', 'class="common-mistake']):
                    # Capture surrounding block
                    start = max(0, idx - 1)
                    end = min(len(lines), idx + 10)
                    snippet = "\n".join(f"{start + i + 1}: {lines[start+i]}" for i in range(end - start))
                    found.append(snippet)
            if found:
                matches[os.path.relpath(path, search_dir)] = found

for k, v in matches.items():
    print(f"\n==================================================")
    print(f"FILE: {k}")
    print(f"==================================================")
    for idx, snip in enumerate(v):
        print(f"--- MATCH {idx+1} ---")
        print(snip)
