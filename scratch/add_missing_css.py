"""
Add missing CSS for hook panels and common-mistake blocks
to tiktok-youtube-shorts.html and short-form-video-guidelines.html.
Also check all other files for any usage of these classes.
"""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

HOOK_PANEL_CSS = '''
/* =========================================
   HOOK VISUAL PANELS
   ========================================= */
.hook-visual-panel {
  display: grid;
  grid-template-columns: 1fr 1fr;
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
.hook-panel-img-col img,
img.hook-panel-img {
  width: 100%;
  height: auto;
  border-radius: 12px;
  object-fit: cover;
  display: block;
  max-height: 320px;
}
.hook-panel-text-col {
  display: flex;
  flex-direction: column;
  gap: 14px;
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
  font-weight: 800;
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
  margin-top: 4px;
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

/* =========================================
   COMMON MISTAKE CALLOUT
   ========================================= */
.common-mistake {
  background: #fff8f0;
  border: 1px solid #fed7aa;
  border-left: 4px solid #f97316;
  border-radius: 10px;
  padding: 18px 22px;
  font-size: 15px;
  color: #7c2d12;
  line-height: 1.65;
  margin: 24px 0 32px;
}
.common-mistake strong {
  font-weight: 700;
  color: #ea580c;
}

@media (max-width: 768px) {
  .hook-visual-panel {
    grid-template-columns: 1fr;
    padding: 24px;
    gap: 20px;
  }
}
'''

COMMON_MISTAKE_ONLY_CSS = '''
/* =========================================
   COMMON MISTAKE CALLOUT
   ========================================= */
.common-mistake {
  background: #fff8f0;
  border: 1px solid #fed7aa;
  border-left: 4px solid #f97316;
  border-radius: 10px;
  padding: 18px 22px;
  font-size: 15px;
  color: #7c2d12;
  line-height: 1.65;
  margin: 24px 0 32px;
}
.common-mistake strong {
  font-weight: 700;
  color: #ea580c;
}
'''

FILES = [
    'index.html',
    'guides.html',
    'mcp-promotion.html',
    'guides/discord-blueprint.html',
    'guides/general-guide.html',
    'guides/tiktok-youtube-shorts.html',
    'guides/angles/scale-safely-with-margins.html',
    'guides/angles/stop-losing-30-profit.html',
    'guides/angles/track-profit-like-a-pro.html',
    'resources/mcp/reddit-ready-to-post.html',
    'resources/mcp/short-form-video-guidelines.html',
    'resources/mcp/x-twitter-ready-to-post.html',
]

print('=' * 60)
print('ADDING MISSING CSS')
print('=' * 60)

for rel_path in FILES:
    path = os.path.join(BASE, rel_path.replace('/', os.sep))
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    original = text
    changes = []
    
    has_hook = '.hook-visual-panel' in text
    has_common_mistake = '.common-mistake' in text
    uses_hook_html = 'hook-visual-panel' in text and '<div' in text
    uses_mistake_html = 'common-mistake' in text and '<div' in text
    
    # Add hook panel CSS if page uses it but has no CSS for it
    if uses_hook_html and not has_hook:
        # Find last </style> before </head>
        head_end = text.find('</head>')
        style_end = text.rfind('</style>', 0, head_end + 200) if head_end > 0 else text.rfind('</style>')
        if style_end != -1:
            text = text[:style_end] + HOOK_PANEL_CSS + text[style_end:]
            changes.append('Added hook-visual-panel + common-mistake CSS')
            has_common_mistake = True  # CSS includes it now
    
    # Add only common-mistake CSS if needed
    if uses_mistake_html and not has_common_mistake:
        head_end = text.find('</head>')
        style_end = text.rfind('</style>', 0, head_end + 200) if head_end > 0 else text.rfind('</style>')
        if style_end != -1:
            text = text[:style_end] + COMMON_MISTAKE_ONLY_CSS + text[style_end:]
            changes.append('Added common-mistake CSS')
    
    if text != original:
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(text)
        print('[FIXED] %s' % rel_path)
        for c in changes:
            print('  + %s' % c)
    else:
        if uses_hook_html or uses_mistake_html:
            print('[OK]    %s  (hook=%s mistake=%s)' % (rel_path, has_hook, has_common_mistake))
        else:
            print('[SKIP]  %s  (no hook/mistake HTML)' % rel_path)

print('\nDone!')
