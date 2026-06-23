"""
Add comprehensive CSS fixes for hook panels and tables in short-form-video-guidelines.html
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

HOOK_AND_TABLE_CSS = '''
/* =========================================
   HOOK VISUAL PANELS
   ========================================= */
.hook-visual-panel {
  display: grid;
  grid-template-columns: 55% 45%;
  gap: 32px;
  background: #f0fdf4;
  border-radius: 24px;
  border: 1px solid rgba(15, 23, 42, 0.08);
  padding: 32px;
  margin: 32px 0;
  overflow: hidden;
  align-items: center;
}
.hook-panel-img-col {
  border-radius: 16px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}
.hook-panel-img-col img {
  width: 100%;
  height: auto;
  border-radius: 12px;
  object-fit: cover;
  display: block;
  max-height: 340px;
}
.hook-panel-text-col {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.hook-panel-eyebrow {
  font-size: 11px;
  font-weight: 700;
  color: #1d9e75;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}
.hook-panel-title {
  font-size: 22px;
  font-weight: 700;
  color: #0f172a;
  line-height: 1.3;
  letter-spacing: -0.02em;
}
.hook-panel-body {
  font-size: 15px;
  color: #475569;
  line-height: 1.7;
}
.hook-panel-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 8px;
}
.hook-panel-tag {
  background: #fff;
  border: 1px solid #d1fae5;
  color: #065f46;
  font-size: 12px;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: 100px;
}

@media (max-width: 768px) {
  .hook-visual-panel {
    grid-template-columns: 1fr;
    padding: 24px;
    gap: 24px;
  }
  .hook-panel-img-col img {
    max-height: 240px;
  }
}

/* =========================================
   SCRIPT TABLES (article-table)
   ========================================= */
.article-table-wrapper {
  overflow-x: auto;
  border-radius: 16px;
  border: 1px solid #e2e8f0;
  margin: 24px 0 40px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.04);
}
.article-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
  min-width: 680px;
}
.article-table thead tr {
  background: #f1f5f9 !important;
}
.article-table th {
  background: #f1f5f9 !important;
  color: #0f172a;
  font-weight: 700;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  padding: 16px 20px;
  text-align: left;
  border-bottom: 2px solid #e2e8f0;
  white-space: nowrap;
}
.article-table td {
  padding: 16px 20px;
  border-bottom: 1px solid #f1f5f9;
  vertical-align: top;
  line-height: 1.65;
  color: #374151;
}
.article-table tr:last-child td { border-bottom: none; }
.article-table tbody tr:hover td { background: #f0fdf4; }
'''

path = os.path.join(BASE, 'resources', 'mcp', 'short-form-video-guidelines.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

original = text

# Add CSS before the last </style>
# Find the last </style> before any </head>
head_end = text.find('</head>')
if head_end == -1:
    head_end = len(text)

last_style_end = text.rfind('</style>', 0, head_end + 200)
if last_style_end == -1:
    # Try without head constraint
    last_style_end = text.find('</style>')

if last_style_end != -1:
    text = text[:last_style_end] + HOOK_AND_TABLE_CSS + text[last_style_end:]
    print("Added hook and table CSS")
else:
    print("WARNING: Could not find </style> to insert CSS")

if text != original:
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(text)
    print("Saved short-form-video-guidelines.html")
else:
    print("No changes made")
