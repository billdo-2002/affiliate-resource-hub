import glob
import re

css_additions = """
@media (min-width: 1024px) {
  .mega-menu {
    position: fixed !important;
    top: 70px !important; /* adjust to sit under navbar */
    left: 50% !important;
    transform: translateX(-50%) !important;
    width: 960px !important;
    max-width: calc(100vw - 32px) !important;
    overflow-x: auto !important;
    box-sizing: border-box !important;
    min-width: unset !important;
  }
  .mega-zone-1 {
    flex: 0 0 300px !important;
  }
  .mega-zone-2 {
    flex: 0 0 220px !important;
  }
  .mega-zone-3 {
    flex: 0 0 320px !important;
    overflow: visible !important;
  }
  .mega-asset-card {
    width: 100% !important;
    box-sizing: border-box !important;
    overflow: hidden !important;
    white-space: normal !important;
    word-wrap: break-word !important;
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
    if 'max-width: calc(100vw - 32px) !important;' not in html:
        html = html.replace('</style>', css_additions + '\n</style>')

        # Write file
        with open(f, 'w', encoding='utf-8') as file:
            file.write(html)

print("Done")
