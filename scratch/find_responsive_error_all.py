import os

BASE = r"c:\Users\khoadnd\Desktop\onboarding hub"
files_to_check = [
    os.path.join(BASE, "guides", "general-guide.html"),
    os.path.join(BASE, "guides", "discord-blueprint.html"),
    os.path.join(BASE, "guides", "tiktok-youtube-shorts.html"),
    os.path.join(BASE, "guides", "angles", "track-profit-like-a-pro.html"),
    os.path.join(BASE, "guides", "angles", "scale-safely-with-margins.html"),
    os.path.join(BASE, "guides", "angles", "stop-losing-30-profit.html")
]

for filepath in files_to_check:
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Check if the unclosed media query is present
        unclosed = "@media (max-width: 1024px) {\n  .guide-hero-inner { grid-template-columns: 1fr; gap: 48px; }\n@media (max-width: 1100px) {"
        # Normalize spaces/newlines for comparison
        content_norm = content.replace("\r\n", "\n")
        unclosed_norm = unclosed.replace("\r\n", "\n")
        
        print(f"File: {os.path.basename(filepath)}")
        print(f"  Unclosed block found: {unclosed_norm in content_norm}")
