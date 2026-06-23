import os
import re

filepath = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\general-guide.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
style = style_match.group(1)

# Let's write the style block to a standalone CSS file and analyze it
css_path = r"c:\Users\khoadnd\Desktop\onboarding hub\scratch\test_style.css"
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(style)

print(f"Written style to {css_path}")

# Let's inspect the CSS text programmatically for common CSS syntax issues
# Check for unmatched braces, unclosed blocks, empty properties, invalid characters, etc.
# We will check each selector block to make sure it's valid.
depth = 0
for idx, char in enumerate(style):
    if char == '{':
        depth += 1
    elif char == '}':
        depth -= 1
        if depth < 0:
            print(f"Error: Negative brace depth at position {idx}")
            depth = 0

print("Brace nesting check complete.")
