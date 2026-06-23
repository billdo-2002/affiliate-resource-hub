import os

# We will search the onboarding hub directory for mentions of discord text
workspace_dir = r"c:\Users\khoadnd\Desktop\onboarding hub"
search_terms = [
    "Promoting TrueProfit on Discord",
    "Example 1: Educational / Problem-First Post",
    "discord 1.webp",
    "If you already own a Discord server"
]

print("Searching workspace...")
for root, dirs, files in os.walk(workspace_dir):
    for fn in files:
        if fn.endswith((".py", ".txt", ".md", ".json", ".html", ".js", ".ps1")):
            path = os.path.join(root, fn)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                for term in search_terms:
                    if term in content:
                        print(f"Found '{term}' in {path} (relative: {os.path.relpath(path, workspace_dir)})")
            except:
                pass

print("Searching App Data Directory...")
appdata_dir = r"C:\Users\khoadnd\.gemini\antigravity-ide"
for root, dirs, files in os.walk(appdata_dir):
    for fn in files:
        if fn.endswith((".jsonl", ".json", ".txt", ".md")):
            path = os.path.join(root, fn)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                for term in search_terms:
                    if term in content:
                        print(f"Found '{term}' in {path}")
            except:
                pass
