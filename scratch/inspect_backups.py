import os
import re
import sys

# Configure stdout to use utf-8 to avoid encoding errors on Windows console
sys.stdout.reconfigure(encoding='utf-8')

BASE = r"c:\Users\khoadnd\Desktop\onboarding hub"

def inspect_backup(filename):
    path = os.path.join(BASE, "scratch", "recovered_htmls", filename)
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    title_match = re.search(r"<title>(.*?)</title>", content)
    title = title_match.group(1) if title_match else "No Title"
    
    print(f"{filename}: Title='{title}' | Size={len(content)} bytes")
    
    # Check for some keywords
    for word in ["Discord", "Short-Form", "TikTok", "General Affiliate", "Ready-to-Post"]:
        if word.lower() in content.lower():
            print(f"  - Contains word: {word}")

for fn in os.listdir(os.path.join(BASE, "scratch", "recovered_htmls")):
    if fn.startswith("$R") and fn.endswith(".html"):
        try:
            inspect_backup(fn)
        except Exception as e:
            print(f"Error inspecting {fn}: {e}")
