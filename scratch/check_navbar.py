import os, re

base = r'c:\Users\khoadnd\Desktop\onboarding hub'

files_to_check = [
    'index.html',
    'guides/general-guide.html',
    'resources/mcp/short-form-video-guidelines.html',
    'resources/mcp/x-twitter-ready-to-post.html',
]

for rel_path in files_to_check:
    path = os.path.join(base, rel_path.replace('/', os.sep))
    with open(path, 'rb') as f:
        raw = f.read()
    text = raw.decode('cp1252', errors='replace')
    lines = text.split('\n')
    
    # Find announce-bar, header, and mega menu regions
    print(f"\n{'='*60}")
    print(f"FILE: {rel_path}")
    print(f"{'='*60}")
    
    # Find announce-bar HTML
    in_bar = False
    for i, line in enumerate(lines, 1):
        if 'announce' in line.lower() or 'id="header"' in line or 'header-inner' in line:
            if not in_bar:
                print(f"\n--- Found at line {i} ---")
                in_bar = True
            print(f"{i:5d}: {line.rstrip()}")
        elif in_bar and line.strip() == '':
            in_bar = False
    
    # Find mega menu
    in_menu = False
    menu_lines = 0
    for i, line in enumerate(lines, 1):
        if 'mega-menu' in line.lower() or 'resources-menu' in line.lower() or 'dropdown' in line.lower():
            if not in_menu:
                print(f"\n--- Mega menu at line {i} ---")
                in_menu = True
                menu_lines = 0
            print(f"{i:5d}: {line.rstrip()}")
            menu_lines += 1
            if menu_lines > 60:
                print("  ... (truncated)")
                in_menu = False
        elif in_menu:
            print(f"{i:5d}: {line.rstrip()}")
            menu_lines += 1
            if '</nav>' in line or menu_lines > 80:
                in_menu = False
