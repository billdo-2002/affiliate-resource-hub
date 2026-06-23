import re

files = [
    r"c:\Users\khoadnd\Desktop\onboarding hub\resources\mcp\x-twitter-ready-to-post.html",
    r"c:\Users\khoadnd\Desktop\onboarding hub\resources\mcp\reddit-ready-to-post.html"
]

for fpath in files:
    print(f"\nFILE: {fpath}")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # search for class rules in style block
    rules = re.findall(r'\.article-example-block\s*\{[^}]*\}|\.copy-content\s*\{[^}]*\}|\.copy-post-btn\s*\{[^}]*\}', content)
    for rule in rules:
        print("  ", rule)
