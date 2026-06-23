import os

path = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\tiktok-youtube-shorts.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Normalize lines to simplify replacement
content_norm = content.replace("\r\n", "\n")

# Replace callout color mappings for mistake
old_border = """.callout-box.warning,
.callout-box.mistake {
  border-left-color: #f97316;
}"""

new_border = """.callout-box.warning {
  border-left-color: #f97316;
}
.callout-box.mistake {
  border-left-color: #EF4444;
}"""

old_title = """.callout-box.warning .callout-title,
.callout-box.mistake .callout-title {
  color: #ea580c;
}"""

new_title = """.callout-box.warning .callout-title {
  color: #ea580c;
}
.callout-box.mistake .callout-title {
  color: #EF4444;
}"""

old_icon = """.callout-box.warning .callout-icon,
.callout-box.mistake .callout-icon {
  border-color: #f97316;
  color: #f97316;
}"""

new_icon = """.callout-box.warning .callout-icon {
  border-color: #f97316;
  color: #f97316;
}
.callout-box.mistake .callout-icon {
  border-color: #EF4444;
  color: #EF4444;
}"""

if old_border.replace("\r\n", "\n") in content_norm:
    content_norm = content_norm.replace(old_border.replace("\r\n", "\n"), new_border)
    print("Replaced border color rules.")
else:
    print("Could not find border color rules.")

if old_title.replace("\r\n", "\n") in content_norm:
    content_norm = content_norm.replace(old_title.replace("\r\n", "\n"), new_title)
    print("Replaced title color rules.")
else:
    print("Could not find title color rules.")

if old_icon.replace("\r\n", "\n") in content_norm:
    content_norm = content_norm.replace(old_icon.replace("\r\n", "\n"), new_icon)
    print("Replaced icon color rules.")
else:
    print("Could not find icon color rules.")

# Save file back with native newlines
with open(path, "w", encoding="utf-8") as f:
    f.write(content_norm.replace("\n", "\r\n"))
print("Saved update v2.")
