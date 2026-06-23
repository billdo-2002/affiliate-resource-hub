import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r"c:\Users\khoadnd\Desktop\onboarding hub"
recovered_dir = os.path.join(BASE, "scratch", "recovered_htmls")

def inspect_file(fn):
    path = os.path.join(recovered_dir, fn)
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    print(f"\n=========================================")
    print(f"FILE: {fn} (Size: {len(content)} bytes)")
    print(f"=========================================")
    
    # Title
    title = re.search(r"<title>(.*?)</title>", content)
    print("Title:", title.group(1) if title else "NONE")
    
    # Headings
    headings = re.findall(r"<h[1-6][^>]*>(.*?)</h[1-6]>", content)
    print("Headings:", headings[:15])
    
    # Breadcrumbs
    breadcrumbs = re.findall(r'class="guide-breadcrumb".*?>(.*?)</div>', content, re.DOTALL)
    print("Breadcrumbs:", breadcrumbs)

inspect_file("$R5KLI7G.html")
inspect_file("$RLV5CB3.html")
