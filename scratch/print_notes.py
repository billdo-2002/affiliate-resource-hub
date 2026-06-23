import os
from bs4 import BeautifulSoup

search_dir = r"c:\Users\khoadnd\Desktop\onboarding hub"
files_to_check = [
    r"guides\general-guide.html",
    r"guides\tiktok-youtube-shorts.html",
    r"resources\mcp\reddit-ready-to-post.html",
    r"resources\mcp\x-twitter-ready-to-post.html"
]

out_lines = []

for rel_path in files_to_check:
    full_path = os.path.join(search_dir, rel_path)
    if not os.path.exists(full_path):
        continue
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    soup = BeautifulSoup(content, 'html.parser')
    notes = soup.find_all(class_=lambda x: x and any(c in x for c in ['article-note', 'common-mistake']))
    
    out_lines.append(f"==================================================")
    out_lines.append(f"FILE: {rel_path}")
    out_lines.append(f"==================================================")
    for idx, note in enumerate(notes):
        out_lines.append(f"--- NOTE {idx+1} (Classes: {note.get('class')}) ---")
        out_lines.append(str(note))
        out_lines.append("")

with open("scratch/all_callouts_extracted.txt", "w", encoding="utf-8") as out_f:
    out_f.write("\n".join(out_lines))
print("Wrote callouts to scratch/all_callouts_extracted.txt")
