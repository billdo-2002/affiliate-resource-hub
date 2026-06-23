import os

path = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\tiktok-youtube-shorts.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update text to remove period: "commission. ?" -> "commission?"
old_p = '<p class="article-p video-intro-line">One of our partners created this video, and it earns him hundreds in monthly commission. ?</p>'
new_p = '<p class="article-p video-intro-line">One of our partners created this video, and it earns him hundreds in monthly commission?</p>'

# Normalize newlines to make sure it matches
content_norm = content.replace("\r\n", "\n")
old_p_norm = old_p.replace("\r\n", "\n")

if old_p_norm in content_norm:
    content_norm = content_norm.replace(old_p_norm, new_p)
    print("Updated intro sentence text in HTML.")
else:
    # Try literal match of the text itself
    old_text = "One of our partners created this video, and it earns him hundreds in monthly commission. ?"
    new_text = "One of our partners created this video, and it earns him hundreds in monthly commission?"
    if old_text in content_norm:
        content_norm = content_norm.replace(old_text, new_text)
        print("Updated intro sentence text directly (fallback).")
    else:
        print("[WARNING] Could not find the intro sentence text.")

# 2. Update CSS to remove font-size: 19px; from .video-intro-line
old_css_part = """@media (min-width: 1024px) {
  .video-intro-line {
    white-space: nowrap;
    font-size: 19px;
  }
}"""

new_css_part = """@media (min-width: 1024px) {
  .video-intro-line {
    white-space: nowrap;
  }
}"""

old_css_norm = old_css_part.replace("\r\n", "\n")

if old_css_norm in content_norm:
    content_norm = content_norm.replace(old_css_norm, new_css_part)
    print("Updated intro line CSS rules.")
else:
    # Fallback with different spaces
    import re
    content_norm, count = re.subn(r'font-size\s*:\s*19px\s*;', '', content_norm)
    print(f"Removed font-size rule using regex: {count} matches.")

with open(path, "w", encoding="utf-8") as f:
    f.write(content_norm.replace("\n", "\r\n"))
print("Saved final updates.")
