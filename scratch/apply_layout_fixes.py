import os

BASE = r"c:\Users\khoadnd\Desktop\onboarding hub"
files_to_fix = [
    os.path.join(BASE, "guides", "general-guide.html"),
    os.path.join(BASE, "guides", "discord-blueprint.html"),
    os.path.join(BASE, "guides", "tiktok-youtube-shorts.html"),
    os.path.join(BASE, "guides", "angles", "track-profit-like-a-pro.html"),
    os.path.join(BASE, "guides", "angles", "scale-safely-with-margins.html"),
    os.path.join(BASE, "guides", "angles", "stop-losing-30-profit.html")
]

# We will perform string replacements for the unclosed media query and the layout styles.
# Unclosed block:
# @media (max-width: 1024px) {
#   .guide-hero-inner { grid-template-columns: 1fr; gap: 48px; }
# @media (max-width: 1100px) {

unclosed_old = """@media (max-width: 1024px) {
  .guide-hero-inner { grid-template-columns: 1fr; gap: 48px; }
@media (max-width: 1100px) {"""

unclosed_new = """@media (max-width: 1100px) {"""

# If there are variations in spaces/newlines, we'll use a regex search and replace for robustness.
# Let's define the replacements for layout values:
# 1. Container max-width to 1200px (from 1280px)
# 2. grid-template-columns to minmax(0, 820px) 320px (from 1fr 320px)
# 3. gap to 60px (remains 60px, but let's make sure it is set)
# 4. article max-width to 820px (from 900px)
# 5. sticky top to 120px (from 110px)

body_inner_old = """.guide-body-inner {
  max-width: 1280px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 320px;
  gap: 60px;
  align-items: start;
}"""

body_inner_new = """.guide-body-inner {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: minmax(0, 820px) 320px;
  gap: 60px;
  align-items: start;
}"""

content_old = """.guide-content {
  max-width: 900px;"""

content_new = """.guide-content {
  max-width: 820px;"""

sidebar_old = """.guide-sidebar {
  position: sticky;
  top: 110px;
}"""

sidebar_new = """.guide-sidebar {
  position: sticky;
  top: 120px;
}"""

for filepath in files_to_fix:
    if os.path.exists(filepath):
        print(f"Fixing file: {filepath}")
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Normalize newlines
        original_newlines = "\r\n" if "\r\n" in content else "\n"
        content_norm = content.replace("\r\n", "\n")
        
        # 1. Remove the unclosed media query
        if unclosed_old in content_norm:
            content_norm = content_norm.replace(unclosed_old, unclosed_new)
            print("  Removed unclosed media query block.")
        else:
            # Fallback regex search and replace
            import re
            pattern = re.compile(r'@media\s*\(max-width:\s*1024px\)\s*\{\s*\.guide-hero-inner\s*\{\s*grid-template-columns:\s*1fr;\s*gap:\s*48px;\s*\}\s*@media\s*\(max-width:\s*1100px\)\s*\{', re.DOTALL)
            content_norm, count = pattern.subn('@media (max-width: 1100px) {', content_norm)
            print(f"  Removed unclosed media query block (regex): {count} replacement(s)")
            
        # 2. Update .guide-body-inner rules
        if body_inner_old in content_norm:
            content_norm = content_norm.replace(body_inner_old, body_inner_new)
            print("  Updated .guide-body-inner rules.")
        else:
            print("  [Warning] .guide-body-inner rules not matched exactly.")
            
        # 3. Update .guide-content max-width
        if content_old in content_norm:
            content_norm = content_norm.replace(content_old, content_new)
            print("  Updated .guide-content max-width.")
        else:
            print("  [Warning] .guide-content rules not matched exactly.")
            
        # 4. Update .guide-sidebar sticky top
        if sidebar_old in content_norm:
            content_norm = content_norm.replace(sidebar_old, sidebar_new)
            print("  Updated .guide-sidebar sticky top.")
        else:
            print("  [Warning] .guide-sidebar rules not matched exactly.")
            
        # Save back the file with Unix LF endings
        with open(filepath, "w", encoding="utf-8", newline="\n") as f:
            f.write(content_norm)
        print("  File saved successfully.")
        print("-" * 50)
