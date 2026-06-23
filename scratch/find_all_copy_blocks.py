import re
import os

files = [
    r"c:\Users\khoadnd\Desktop\onboarding hub\resources\mcp\x-twitter-ready-to-post.html",
    r"c:\Users\khoadnd\Desktop\onboarding hub\resources\mcp\reddit-ready-to-post.html"
]

for file_path in files:
    print(f"==================================================")
    print(f"FILE: {os.path.basename(file_path)}")
    print(f"==================================================")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = re.finditer(r'<div class="article-example-block"', content)
    for i, m in enumerate(matches):
        start = m.start()
        # Find corresponding closing div for class="article-example-block"
        # We can scan forward matching braces or just find the closing tag
        # For simplicity, let's grab up to 1500 chars which covers the block
        snippet = content[start:start+1800]
        # Let's truncate after the closing block div
        end_idx = snippet.find('</div>\n    \n    <p')
        if end_idx == -1:
            end_idx = snippet.find('</div>\n\n')
        if end_idx == -1:
            end_idx = 1500
        else:
            end_idx += 6
        print(f"BLOCK {i+1}:")
        print(snippet[:end_idx])
        print("--------------------------------------------------")
