import os
import re

BASE = r"c:\Users\khoadnd\Desktop\onboarding hub"

def inspect_restored(filename):
    path = os.path.join(BASE, "scratch", "restored_pages", filename)
    if not os.path.exists(path):
        print(f"{filename} does not exist!")
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    print(f"\n=========================================")
    print(f"Inspecting {filename} (Size: {len(content)} bytes)")
    print(f"=========================================")
    
    # Let's search for image tags
    imgs = re.findall(r'<img [^>]*src=["\']([^"\']+)["\'][^>]*>', content)
    print("Found images:", set(imgs))
    
    # Search for headings
    headings = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', content)
    print("Found headings (first 10):", headings[:10])

inspect_restored("discord-blueprint.html")
inspect_restored("tiktok-youtube-shorts.html")
inspect_restored("general-guide.html")
