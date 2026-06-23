import os
import re
from bs4 import BeautifulSoup

search_dir = r"c:\Users\khoadnd\Desktop\onboarding hub"
html_files = []

for root, dirs, files in os.walk(search_dir):
    for f in files:
        if f.endswith(".html") and ".gemini" not in root:
            html_files.append(os.path.join(root, f))

output_lines = []
output_lines.append(f"Found {len(html_files)} HTML files to inspect.")

for path in html_files:
    rel_path = os.path.relpath(path, search_dir)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Let's find divs that have class containing 'article-note' or 'common-mistake' or other note classes
    notes = soup.find_all(class_=lambda x: x and any(c in x for c in ['article-note', 'common-mistake']))
    
    if notes:
        output_lines.append(f"\n==================================================")
        output_lines.append(f"FILE: {rel_path} ({len(notes)} notes)")
        output_lines.append(f"==================================================")
        for i, note in enumerate(notes):
            output_lines.append(f"--- NOTE {i+1} ---")
            output_lines.append(f"Tag: {note.name}, Classes: {note.get('class')}")
            output_lines.append(note.prettify())

with open("scratch/notes_report.txt", "w", encoding="utf-8") as out:
    out.write("\n".join(output_lines))
print("Wrote notes to scratch/notes_report.txt")
