import os

search_dir = r"c:\Users\khoadnd\Desktop\onboarding hub"
files = [
    r"guides\general-guide.html",
    r"guides\tiktok-youtube-shorts.html"
]

for rel in files:
    path = os.path.join(search_dir, rel)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace multiplication sign × with &times;
        if "×" in content:
            content = content.replace("×", "&times;")
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Replaced times symbol in {rel}")
        else:
            print(f"No times symbol found in {rel}")
