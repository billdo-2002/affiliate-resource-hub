import os

path = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\tiktok-youtube-shorts.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Mistake Callout CSS
old_callout_css = """.callout-box.warning,
.callout-box.mistake {
  border-left-color: #f97316;
}
.callout-box.warning .callout-title,
.callout-box.mistake .callout-title {
  color: #ea580c;
}
.callout-box.warning .callout-icon,
.callout-box.mistake .callout-icon {
  border-color: #f97316;
  color: #f97316;
}"""

new_callout_css = """.callout-box.warning {
  border-left-color: #f97316;
}
.callout-box.warning .callout-title {
  color: #ea580c;
}
.callout-box.warning .callout-icon {
  border-color: #f97316;
  color: #f97316;
}
.callout-box.mistake {
  border-left-color: #EF4444;
}
.callout-box.mistake .callout-title {
  color: #EF4444;
}
.callout-box.mistake .callout-icon {
  border-color: #EF4444;
  color: #EF4444;
}"""

if old_callout_css in content:
    content = content.replace(old_callout_css, new_callout_css)
    print("Updated mistake callout CSS colors.")
else:
    # Try with \r\n normalized
    old_callout_css_norm = old_callout_css.replace("\r\n", "\n")
    content_norm = content.replace("\r\n", "\n")
    if old_callout_css_norm in content_norm:
        content_norm = content_norm.replace(old_callout_css_norm, new_callout_css)
        content = content_norm
        print("Updated mistake callout CSS colors (normalized newlines).")
    else:
        print("[WARNING] Could not find old callout CSS block.")

# 2. Update Video Placeholder CSS to represent an iPhone mockup
old_video_css = """.tiktok-video-placeholder {
  display: block;
  position: relative;
  width: 280px; /* width: 260320px desktop */
  aspect-ratio: 9 / 16;
  border-radius: 24px;
  overflow: hidden;
  border: 1px solid rgba(15, 23, 42, 0.12);
  box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
  margin: 32px auto 16px;
  background: #000;
}"""

new_video_css = """.tiktok-video-placeholder {
  display: block;
  position: relative;
  width: 300px;
  aspect-ratio: 9 / 16;
  border-radius: 36px;
  border: 10px solid #1e293b;
  box-shadow: 0 20px 40px rgba(15, 23, 42, 0.15), inset 0 0 10px rgba(0,0,0,0.5);
  overflow: hidden;
  margin: 36px auto 18px;
  background: #000;
}"""

# Normalization step for comment box / replacement
old_video_css_norm = old_video_css.replace("\r\n", "\n").replace("260320px", "260–320px")
content_norm = content.replace("\r\n", "\n")
if old_video_css_norm in content_norm:
    content_norm = content_norm.replace(old_video_css_norm, new_video_css)
    content = content_norm
    print("Updated video placeholder to iPhone mockup style.")
else:
    # Let's try raw replace if no encoding character match
    fallback_old = old_video_css.split("width: 280px;")[0] + "width: 280px;"
    print("Could not find direct match. Will print search context.")

# 3. Add intro line CSS and HTML updates
intro_line_css = """
.video-intro-line {
  margin-bottom: 24px;
}
@media (min-width: 1024px) {
  .video-intro-line {
    white-space: nowrap;
    font-size: 19px;
  }
}
@media (max-width: 1023px) {
  .video-intro-line {
    white-space: normal;
  }
}
"""

# Let's append intro_line_css right before Hook Visual Panels CSS comment
hook_comment = "/* =========================================\n   HOOK VISUAL PANELS"
if hook_comment in content:
    content = content.replace(hook_comment, intro_line_css + "\n" + hook_comment)
    print("Added intro line CSS.")
else:
    hook_comment_norm = hook_comment.replace("\r\n", "\n")
    content_norm = content.replace("\r\n", "\n")
    if hook_comment_norm in content_norm:
        content_norm = content_norm.replace(hook_comment_norm, intro_line_css + "\n" + hook_comment_norm)
        content = content_norm
        print("Added intro line CSS (normalized newlines).")
    else:
        print("[WARNING] Could not find hook visual panels CSS comment to append intro line CSS.")

# Update HTML body
old_p = '<p class="article-p">One of our partners created this video, and it earns him hundreds in monthly commission. ?</p>'
new_p = '<p class="article-p video-intro-line">One of our partners created this video, and it earns him hundreds in monthly commission. ?</p>'

if old_p in content:
    content = content.replace(old_p, new_p)
    print("Updated intro paragraph HTML.")
else:
    old_p_norm = old_p.replace("\r\n", "\n")
    content_norm = content.replace("\r\n", "\n")
    if old_p_norm in content_norm:
        content_norm = content_norm.replace(old_p_norm, new_p)
        content = content_norm
        print("Updated intro paragraph HTML (normalized newlines).")
    else:
        print("[WARNING] Could not find intro paragraph HTML.")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Saved updates.")
