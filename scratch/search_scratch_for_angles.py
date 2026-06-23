import os

scratch_dir = r"c:\Users\khoadnd\Desktop\onboarding hub\scratch"
target = "track-profit-like-a-pro"

for filename in os.listdir(scratch_dir):
    filepath = os.path.join(scratch_dir, filename)
    if os.path.isfile(filepath) and filename.endswith(('.py', '.ps1', '.txt')):
        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            if target in content:
                print(f"Found in: {filename}")
        except Exception as e:
            print(f"Error reading {filename}: {e}")
