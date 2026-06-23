import os
from bs4 import BeautifulSoup

search_dir = r"c:\Users\khoadnd\Desktop\onboarding hub"
path = os.path.join(search_dir, r"guides\general-guide.html")

with open(path, "r", encoding="utf-8") as f:
    content = f.read()
    
soup = BeautifulSoup(content, 'html.parser')
style = soup.find('style')
if style:
    with open("scratch/general_guide_style.css", "w", encoding="utf-8") as out:
        out.write(style.string or "")
    print("Wrote style tag to scratch/general_guide_style.css")
else:
    print("No style tag found in general-guide.html")
