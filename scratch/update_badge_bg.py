import os

source_file = r'c:\Users\khoadnd\Desktop\onboarding hub\mcp-promotion.html'
with open(source_file, 'r', encoding='utf-8') as f:
    html = f.read()

old_block = """<div class="stagger-enter hero-badge" style="display: inline-flex; align-items: center; justify-content: center; background: transparent; border-width: 1px 0; border-style: solid; border-image: linear-gradient(to right, transparent 0%, rgba(255,255,255,0.3) 50%, transparent 100%) 1; padding: 14px 40px; font-size: 15px; color: #f8fafc; margin-bottom: 24px; animation-delay: 0.1s; box-shadow: none; text-transform: uppercase; letter-spacing: 0.08em; text-shadow: 0 0 12px rgba(255,255,255,0.2);">
      <span class="badge-label" style="font-style: normal; font-weight: 500;">TrueProfit MCP</span>
      <span class="badge-divider" style="font-style: normal; font-weight: 500; white-space: pre;"> : </span>
      <span class="badge-sub" style="font-style: normal; font-weight: 500;">TrueProfit x LLMs</span>
    </div>"""

new_block = """<div class="stagger-enter hero-badge" style="display: inline-flex; align-items: center; justify-content: center; background: linear-gradient(90deg, transparent 0%, rgba(255,255,255,0.05) 50%, transparent 100%); border-width: 1px 0; border-style: solid; border-image: linear-gradient(to right, transparent 0%, rgba(255,255,255,0.3) 50%, transparent 100%) 1; padding: 14px 40px; font-size: 15px; color: #f8fafc; margin-bottom: 24px; animation-delay: 0.1s; box-shadow: none; text-transform: uppercase; letter-spacing: 0.08em; text-shadow: 0 0 12px rgba(255,255,255,0.2);">
      <span class="badge-label" style="font-style: normal; font-weight: 500;">TrueProfit MCP:</span>
      <span class="badge-sub" style="font-style: normal; font-weight: 500; margin-left: 8px;">TrueProfit x LLMs</span>
    </div>"""

if old_block in html:
    html = html.replace(old_block, new_block)
    with open(source_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replaced successfully")
else:
    print("Old block not found!")
