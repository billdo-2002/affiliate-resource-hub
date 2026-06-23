"""
Add article-example-block and copy-content CSS to x-twitter and reddit pages.
Also verify article layout CSS.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

ARTICLE_EXAMPLE_CSS = '''
/* =========================================
   ARTICLE EXAMPLE / COPY BLOCKS
   ========================================= */
.article-example-block {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  padding: 28px 32px;
  position: relative;
  margin: 16px 0 8px;
}
.article-example-block .copy-post-btn {
  position: absolute;
  top: 16px;
  right: 16px;
}
.copy-content {
  padding-right: 120px;
}
.copy-content p,
.copy-content .article-p {
  margin-bottom: 12px;
  line-height: 1.7;
  color: #1e293b;
  font-size: 15px;
}
.copy-content p:last-child,
.copy-content .article-p:last-child {
  margin-bottom: 0;
}
.aff-link-code {
  font-family: 'Courier New', monospace;
  background: #d1fae5;
  color: #065f46;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 0.9em;
}
'''

TARGET_FILES = [
    'resources/mcp/x-twitter-ready-to-post.html',
    'resources/mcp/reddit-ready-to-post.html',
]

for rel_path in TARGET_FILES:
    path = os.path.join(BASE, rel_path.replace('/', os.sep))
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    original = text
    
    # Add CSS before the last </style> in head section
    # Find </style></head> or just the last </style> before line ~2200
    lines = text.split('\n')
    
    # Find the </style> that ends the CSS (should be around line 2000-2200)
    # We want the one right before </head>
    head_pos = text.find('</head>')
    if head_pos > 0:
        style_end = text.rfind('</style>', 0, head_pos + 100)
    else:
        style_end = text.rfind('</style>')
    
    if style_end != -1 and '.article-example-block' not in text:
        text = text[:style_end] + ARTICLE_EXAMPLE_CSS + text[style_end:]
        
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(text)
        print("Added article-example-block CSS to: %s" % rel_path)
    elif '.article-example-block' in text:
        print("Already has article-example-block CSS: %s" % rel_path)
    else:
        print("WARNING: Could not find </style> in: %s" % rel_path)

print("\nDone!")
