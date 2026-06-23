import os
from bs4 import BeautifulSoup

path = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\tiktok-youtube-shorts.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()
    
soup = BeautifulSoup(content, 'html.parser')

# Find sentence
sentence_p = None
for p in soup.find_all(['p', 'div']):
    if "One of our partners created this video" in p.get_text():
        sentence_p = p
        break
        
out_lines = []
out_lines.append("=== INTRO SENTENCE PARAGRAPH ===")
if sentence_p:
    out_lines.append(sentence_p.prettify())
else:
    out_lines.append("Not found")
    
# Find video visual container
video_container = soup.find(class_=lambda x: x and any(term in x for term in ['video', 'placeholder', 'frame']))
out_lines.append("\n=== VIDEO VISUAL CONTAINER ===")
if video_container:
    out_lines.append(video_container.prettify())
else:
    img = soup.find('img')
    if img:
        out_lines.append("Found image: " + img.prettify())
        parent = img.parent
        out_lines.append("Parent of image: " + parent.prettify())

with open("scratch/tiktok_details.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))
print("Wrote output to scratch/tiktok_details.txt")
