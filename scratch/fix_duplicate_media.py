import os

path = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\tiktok-youtube-shorts.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Normalize lines to simplify replacement
content_norm = content.replace("\r\n", "\n")

# Target block to remove
target = """@media (max-width: 1023px) {
  .video-intro-line {
    white-space: normal;
  }
}"""

target_norm = target.replace("\r\n", "\n")

if target_norm in content_norm:
    content_norm = content_norm.replace(target_norm, "")
    print("Removed duplicate @media (max-width: 1023px) block.")
else:
    # Let's try matching with flex whitespace
    import re
    content_norm, count = re.subn(r'@media\s*\(\s*max-width\s*:\s*1023px\s*\)\s*\{\s*\.video-intro-line\s*\{\s*white-space\s*:\s*normal\s*;\s*\}\s*\}', '', content_norm)
    print(f"Removed using regex: {count} matches.")

# Write back with Windows newlines
with open(path, "w", encoding="utf-8") as f:
    f.write(content_norm.replace("\n", "\r\n"))
print("Saved clean file.")
