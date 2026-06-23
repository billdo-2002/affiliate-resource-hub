import os

prefix_map = {
    'index.html': '',
    'guides.html': '',
    'mcp-promotion.html': '',
    'resources/mcp/x-twitter-ready-to-post.html': '../../',
    'resources/mcp/reddit-ready-to-post.html': '../../',
    'resources/mcp/short-form-video-guidelines.html': '../../',
    'guides/tiktok-youtube-shorts.html': '../',
    'guides/general-guide.html': '../',
    'guides/discord-blueprint.html': '../',
    'guides/angles/track-profit-like-a-pro.html': '../../',
    'guides/angles/stop-losing-30-profit.html': '../../',
    'guides/angles/scale-safely-with-margins.html': '../../'
}

base_dir = r'c:\Users\khoadnd\Desktop\onboarding hub'

mega_menu_template = """<div class="mega-menu">
          <!-- Zone 1: Guides & Angles (White) -->
          <div class="mega-zone mega-zone-1">
            <a class="mega-pill-badge" href="{prefix}guides.html">
              <svg fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" style="margin-right: 4px;" viewbox="0 0 24 24" width="14"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
              GUIDES &rarr;
            </a>
            <div class="mega-links-grid">
              <a class="mega-link-item" href="{prefix}guides/general-guide.html">General Guide</a>
              <a class="mega-link-item" href="{prefix}guides/discord-blueprint.html">Discord Blueprint</a>
              <a class="mega-link-item" href="{prefix}guides/tiktok-youtube-shorts.html">TikTok &amp; YouTube Shorts</a>
            </div>
            <div class="mega-section-label" style="margin-top: 8px;">HIGH-CONVERTING ANGLES:</div>
            <div class="mega-gems-list">
              <a class="mega-gem-card" href="{prefix}guides/angles/track-profit-like-a-pro.html">
                <div class="mega-gem-img" style="background: #0B1D2E;">
                  <img src="{prefix}images/22.svg" alt="Track Profit Like A Pro">
                </div>
                <div class="mega-gem-text">Track Profit Like A Pro</div>
              </a>
              <a class="mega-gem-card" href="{prefix}guides/angles/scale-safely-with-margins.html">
                <div class="mega-gem-img" style="background: #62BBA2;">
                  <img src="{prefix}images/19.svg" alt="Scale Safely with Margins">
                </div>
                <div class="mega-gem-text">Scale Safely with Margins</div>
              </a>
              <a class="mega-gem-card" href="{prefix}guides/angles/stop-losing-30-profit.html">
                <div class="mega-gem-img" style="background: #FCE1DA;">
                  <img src="{prefix}images/21.svg" alt="Stop Losing 30% Profit">
                </div>
                <div class="mega-gem-text">Stop Losing 30% Profit</div>
              </a>
            </div>
          </div>
          <!-- Zone 2: MCP Promotion (Mint) -->
          <div class="mega-zone mega-zone-2">
            <a class="mega-pill-badge" href="{prefix}mcp-promotion.html" style="border-color: #1d9e75; color: #1d9e75; background: #e6fbf1;">
              <svg fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" style="margin-right: 4px;" viewbox="0 0 24 24" width="14"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
              MCP PROMOTION &rarr;
              <svg fill="currentColor" height="10" style="color: #f59e0b; margin-left: 6px; vertical-align: middle;" viewbox="0 0 24 24" width="10"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
            </a>
            <div class="mega-links-list" style="margin-top: 24px; gap: 24px;">
              <a class="mega-link-item" href="{prefix}mcp-promotion.html">MCP Promotion Hub</a>
              <a class="mega-link-item" href="{prefix}resources/mcp/x-twitter-ready-to-post.html">X/Twitter Ready-to-Post</a>
              <a class="mega-link-item" href="{prefix}resources/mcp/reddit-ready-to-post.html">Reddit Ready-to-Post</a>
              <a class="mega-link-item" href="{prefix}resources/mcp/short-form-video-guidelines.html">Short-Form Video Guidelines</a>
            </div>
          </div>
          <!-- Zone 3: Creative Assets (Navy) -->
          <div class="mega-zone mega-zone-3">
            <a class="mega-pill-badge mega-pill-badge-dark" href="#" style="margin-bottom: 24px;">
              <svg fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" style="margin-right: 4px;" viewbox="0 0 24 24" width="14"><rect height="7" width="7" x="3" y="3"></rect><rect height="7" width="7" x="14" y="3"></rect><rect height="7" width="7" x="14" y="14"></rect><rect height="7" width="7" x="3" y="14"></rect></svg>
              CREATIVE ASSETS &rarr;
            </a>

            <a class="mega-asset-card" href="https://trueprofit.notion.site/2e265f0648c680b68a14ec66c712323b?v=2e265f0648c681fb9db2000c532b98a0" target="_blank" rel="noopener noreferrer">
              <div class="mega-asset-content">
                <div class="mega-asset-name">Logo Kit</div>
                <div class="mega-asset-desc">Download official TrueProfit logos and brand marks for affiliate posts, landing pages, guides, and promotional content.</div>
              </div>
              <div class="mega-asset-visual-wrap">
                <div class="mega-asset-visual-bg">
                  <svg width="100" height="82" viewBox="0 0 100 82" fill="none">
                    <rect x="25" y="25" width="60" height="45" rx="6" fill="rgba(45,212,152,0.15)" stroke="#2dd498" stroke-width="1.5"/>
                    <rect x="15" y="12" width="60" height="45" rx="6" fill="rgba(45,212,152,0.05)" stroke="#2dd498" stroke-width="1.5" stroke-dasharray="4 4"/>
                  </svg>
                </div>
                <div class="mega-asset-visual-icon">
                  <svg fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="16"><path d="M12 2L2 7l10 5 10-5-10-5z"></path><path d="M2 17l10 5 10-5"></path><path d="M2 12l10 5 10-5"></path></svg>
                </div>
              </div>
            </a>

            <a class="mega-asset-card" href="https://trueprofit.notion.site/2e265f0648c680b68a14ec66c712323b?v=2e265f0648c681dbb776000cb2feef3f" target="_blank" rel="noopener noreferrer">
              <div class="mega-asset-content">
                <div class="mega-asset-name">Campaign Banners</div>
                <div class="mega-asset-desc">Ready-to-use banner creatives for social posts, resource pages, affiliate campaigns, and seasonal promotions.</div>
              </div>
              <div class="mega-asset-visual-wrap">
                <div class="mega-asset-visual-bg">
                  <svg width="100" height="82" viewBox="0 0 100 82" fill="none">
                    <rect x="10" y="20" width="80" height="42" rx="4" fill="rgba(45,212,152,0.1)" stroke="#2dd498" stroke-width="1.5"/>
                    <rect x="20" y="30" width="60" height="22" rx="3" fill="rgba(45,212,152,0.2)"/>
                  </svg>
                </div>
                <div class="mega-asset-visual-icon">
                  <svg fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="16"><rect height="18" rx="2" ry="2" width="18" x="3" y="3"></rect><line x1="3" x2="21" y1="9" y2="9"></line><line x1="9" x2="9" y1="21" y2="9"></line></svg>
                </div>
              </div>
            </a>

            <a class="mega-asset-card" href="https://trueprofit.notion.site/2e265f0648c680b68a14ec66c712323b?v=2e265f0648c681eb8be9000c647955f8" target="_blank" rel="noopener noreferrer" style="margin-bottom: 0;">
              <div class="mega-asset-content">
                <div class="mega-asset-name">App Footages</div>
                <div class="mega-asset-desc">Screen recordings and product visuals you can use for demos, tutorials, short-form videos, and content examples.</div>
              </div>
              <div class="mega-asset-visual-wrap">
                <div class="mega-asset-visual-bg">
                  <svg width="100" height="82" viewBox="0 0 100 82" fill="none">
                    <rect x="15" y="15" width="70" height="52" rx="6" fill="rgba(45,212,152,0.1)" stroke="#2dd498" stroke-width="1.5"/>
                    <polygon points="42,32 58,41 42,50" fill="rgba(45,212,152,0.3)" stroke="#2dd498" stroke-width="1.5" stroke-linejoin="round"/>
                  </svg>
                </div>
                <div class="mega-asset-visual-icon">
                  <svg fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="16"><polygon points="23 7 16 12 23 17 23 7"></polygon><rect height="14" rx="2" ry="2" width="15" x="1" y="5"></rect></svg>
                </div>
              </div>
            </a>
          </div>
        </div>"""

for rel_path, prefix in prefix_map.items():
    abs_path = os.path.join(base_dir, rel_path.replace('/', os.sep))
    if not os.path.exists(abs_path):
        print(f"Warning: File {abs_path} does not exist.")
        continue

    print(f"Processing {rel_path}...")
    with open(abs_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the start of mega-menu
    start_tag = '<div class="mega-menu">'
    start_idx = html.find(start_tag)
    if start_idx == -1:
        print(f"Could not find {start_tag} in {rel_path}.")
        continue

    # Tag counting logic to find matching closing div
    depth = 0
    i = start_idx
    end_idx = -1
    while i < len(html):
        if html[i:i+4] == '<div':
            depth += 1
            i += 4
        elif html[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                end_idx = i + 6
                break
            i += 6
        else:
            i += 1

    if end_idx == -1:
        print(f"Could not find matching closing div for mega-menu in {rel_path}.")
        continue

    # Generate custom mega menu for this file
    custom_menu = mega_menu_template.replace('{prefix}', prefix)

    # Replace the block
    new_html = html[:start_idx] + custom_menu + html[end_idx:]

    # Clean up trailing stray >> or &gt;&gt; characters right after closing div
    # Check up to 10 characters after the replacement point
    post_idx = start_idx + len(custom_menu)
    next_chars = new_html[post_idx:post_idx+20]
    if next_chars.startswith('>>'):
        new_html = new_html[:post_idx] + new_html[post_idx+2:]
    elif next_chars.startswith('&gt;&gt;'):
        new_html = new_html[:post_idx] + new_html[post_idx+8:]

    # Write back to file
    with open(abs_path, 'w', encoding='utf-8') as f:
        f.write(new_html)

print("Global mega menu updates complete!")
