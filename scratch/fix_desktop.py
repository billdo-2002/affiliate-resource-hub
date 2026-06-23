import glob

css_additions = """
@media (min-width: 1024px) {
  .mega-menu {
    min-width: 900px !important;
    width: max-content !important;
    max-width: 95vw !important;
  }
  .mega-zone-3 {
    min-width: 320px !important;
    flex-shrink: 0 !important;
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

for f in ['guides.html', 'index.html', 'mcp-promotion.html']:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            html = file.read()
    except FileNotFoundError:
        continue

    # Insert new CSS before </style>
    if "min-width: 900px !important;" not in html:
        html = html.replace('</style>', css_additions + '\n</style>')

        # Write file
        with open(f, 'w', encoding='utf-8') as file:
            file.write(html)

print("Done")
