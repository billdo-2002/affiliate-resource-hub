import glob
import re

css_additions = """
@media (min-width: 1024px) {
  .header-inner {
    position: relative !important;
  }
  .nav-dropdown-wrapper {
    position: static !important;
  }
  .mega-menu {
    position: absolute !important;
    top: 100% !important; /* adjust if needed */
    left: 0 !important;
    right: 0 !important;
    width: auto !important;
    max-width: 100% !important;
    transform: none !important;
    box-sizing: border-box !important;
    overflow: hidden !important;
    display: flex !important;
    flex-direction: row !important;
    min-width: unset !important;
  }
  .mega-zone-1 {
    flex: 0 0 35% !important;
    box-sizing: border-box !important;
    overflow: hidden !important;
    min-width: 0 !important;
  }
  .mega-zone-2 {
    flex: 0 0 25% !important;
    box-sizing: border-box !important;
    overflow: hidden !important;
    min-width: 0 !important;
  }
  .mega-zone-3 {
    flex: 1 !important;
    box-sizing: border-box !important;
    overflow: hidden !important;
    min-width: 0 !important;
  }
  .mega-asset-card {
    width: 100% !important;
    box-sizing: border-box !important;
    word-wrap: break-word !important;
    overflow: hidden !important;
  }
  .mega-asset-desc {
    white-space: normal !important;
    word-wrap: break-word !important;
    overflow-wrap: break-word !important;
    max-width: 100% !important;
    display: block !important;
  }
}
"""

for f in glob.glob('**/*.html', recursive=True):
    try:
        with open(f, 'r', encoding='utf-8') as file:
            html = file.read()
    except FileNotFoundError:
        continue

    # Skip files that don't have .mega-menu
    if '.mega-menu' not in html:
        continue

    # Remove previous @media (min-width: 1024px) block
    html = re.sub(r'@media \(min-width: 1024px\) \{.*?\n\}\n?', '', html, flags=re.DOTALL)
    
    # Insert new CSS before </style>
    html = html.replace('</style>', css_additions + '\n</style>')

    # Write file
    with open(f, 'w', encoding='utf-8') as file:
        file.write(html)

print("Done")
