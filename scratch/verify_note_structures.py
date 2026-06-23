import os
from bs4 import BeautifulSoup

search_dir = r"c:\Users\khoadnd\Desktop\onboarding hub"
files_to_check = [
    r"guides\general-guide.html",
    r"guides\tiktok-youtube-shorts.html",
    r"resources\mcp\reddit-ready-to-post.html",
    r"resources\mcp\x-twitter-ready-to-post.html"
]

print("Verifying note structures...")

for rel_path in files_to_check:
    full_path = os.path.join(search_dir, rel_path)
    if not os.path.exists(full_path):
        continue
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    soup = BeautifulSoup(content, 'html.parser')
    
    # We should have no elements with class 'article-note' or 'common-mistake' in the body
    # (since we renamed them to 'callout-box')
    old_notes = soup.find_all(class_=lambda x: x and any(c in x for c in ['article-note', 'common-mistake']))
    new_callouts = soup.find_all(class_='callout-box')
    
    print(f"File: {rel_path}")
    print(f"  Old note elements: {len(old_notes)}")
    print(f"  New callout elements: {len(new_callouts)}")
    
    # Check that each callout-box contains callout-title, callout-bullets, callout-row, callout-icon, callout-text
    for i, callout in enumerate(new_callouts):
        issues = []
        if not callout.find(class_='callout-title'):
            issues.append("missing callout-title")
        if not callout.find(class_='callout-bullets'):
            issues.append("missing callout-bullets")
        if not callout.find(class_='callout-row'):
            issues.append("missing callout-row")
        if not callout.find(class_='callout-icon'):
            issues.append("missing callout-icon")
        if not callout.find(class_='callout-text'):
            issues.append("missing callout-text")
        
        status = "OK" if not issues else f"FAIL ({', '.join(issues)})"
        print(f"    Callout {i+1} status: {status}")
