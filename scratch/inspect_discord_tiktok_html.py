import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r"c:\Users\khoadnd\Desktop\onboarding hub"
candidate_path = os.path.join(BASE, "scratch", "recovered_htmls", "$R5KLI7G.html")

with open(candidate_path, "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# Let's search for the text "Promoting on Discord"
print("Positions of 'Discord':")
for m in re.finditer(r"Discord", html, re.IGNORECASE):
    print(f"  Index {m.start()}: {html[m.start():m.start()+100]}")

# Let's write the sections out to files
# Section 2 starts around 'Promoting on Discord'
# Let's find '<h2' or '<h3' or '<div' around that
print("\n--- HTML structure of Discord section ---")
pos_discord = html.find("2. Promoting on Discord")
if pos_discord != -1:
    start_idx = html.rfind("<div", 0, pos_discord)
    if start_idx == -1:
        start_idx = pos_discord - 200
    end_idx = html.find("3. Short-Form Video Strategy", pos_discord)
    if end_idx == -1:
        end_idx = pos_discord + 15000
    else:
        end_idx = html.rfind("<div", start_idx, end_idx)
    
    discord_section = html[start_idx:end_idx]
    with open("scratch/discord_section_extracted.html", "w", encoding="utf-8") as out:
        out.write(discord_section)
    print(f"Saved Discord section to scratch/discord_section_extracted.html ({len(discord_section)} bytes)")

# Section 3 starts around 'Short-Form Video Strategy'
pos_video = html.find("3. Short-Form Video Strategy")
if pos_video != -1:
    start_idx = html.rfind("<div", 0, pos_video)
    if start_idx == -1:
        start_idx = pos_video - 200
    end_idx = html.find("Resources", pos_video) # or next section
    if end_idx == -1:
        end_idx = pos_video + 25000
    else:
        end_idx = html.rfind("<div", start_idx, end_idx)
        
    video_section = html[start_idx:end_idx]
    with open("scratch/video_section_extracted.html", "w", encoding="utf-8") as out:
        out.write(video_section)
    print(f"Saved Video section to scratch/video_section_extracted.html ({len(video_section)} bytes)")

