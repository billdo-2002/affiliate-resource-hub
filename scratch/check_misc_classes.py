import os
from bs4 import BeautifulSoup

search_dir = r"c:\Users\khoadnd\Desktop\onboarding hub"
html_files = []

for root, dirs, files in os.walk(search_dir):
    for f in files:
        if f.endswith(".html") and ".gemini" not in root:
            html_files.append(os.path.join(root, f))

out_lines = []

for path in html_files:
    rel_path = os.path.relpath(path, search_dir)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    body = soup.body
    if not body:
        continue
    
    found_elms = []
    # Search for classes containing these names
    for tag in body.find_all(True):
        classes = tag.get('class', [])
        for c in classes:
            c_lower = c.lower()
            if any(term in c_lower for term in ['alert', 'error', 'danger', 'success', 'notice', 'highlight', 'callout', 'recap']):
                found_elms.append((tag.name, classes, tag.get_text(strip=True)[:100]))
                break
                
    if found_elms:
        out_lines.append(f"FILE: {rel_path}")
        for i, (name, classes, text) in enumerate(found_elms):
            out_lines.append(f"  {i+1}. Tag: <{name}>, Classes: {classes}, Text: {text}...")

with open("scratch/misc_callouts_report.txt", "w", encoding="utf-8") as out:
    out.write("\n".join(out_lines))
print("Wrote misc callouts to scratch/misc_callouts_report.txt")
