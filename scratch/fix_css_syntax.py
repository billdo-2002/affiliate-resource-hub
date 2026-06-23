import os
import glob
import re

base_dir = r'c:\Users\khoadnd\Desktop\onboarding hub'
files = glob.glob(os.path.join(base_dir, '**/*.html'), recursive=True)

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We need to find the dangling ".mega-asset-card:hover" and remove it.
    # It might look like ".mega-asset-card:hover \n\n.mega-asset-card {"
    # Let's use a regex that matches .mega-asset-card:hover followed by optional whitespace and then .mega-asset-card {
    pattern = r'\.mega-asset-card:hover\s*\n\s*\.mega-asset-card\s*\{'
    
    if re.search(pattern, content):
        content = re.sub(pattern, '.mega-asset-card {', content)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Fixed CSS syntax error in {f}")
