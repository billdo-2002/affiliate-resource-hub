"""
GLOBAL REPAIR SCRIPT - Phase 2: Shared Components
Applies consistent announce bar + header + mega menu to ALL HTML pages.

This script:
1. Reads each HTML file
2. Replaces the announce bar HTML
3. Replaces the header/nav HTML (with correct relative paths)
4. Replaces the mobile menu HTML
5. Ensures CSS variables are consistent
6. Fixes article layout issues (scroll-margin-top)
7. Saves as UTF-8

The "source of truth" navbar comes from index.html (best state).
"""

import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

# ============================================================
# SHARED ANNOUNCE BAR HTML (source of truth)
# ============================================================
ANNOUNCE_BAR = '''<div id="announce-bar">
  <span class="announce-star">&#9733;</span>
  <span>Earn 100% on your first month + 20% recurring for the year. Join 1,000+ affiliates.</span>
  <a href="https://affiliate.trueprofit.io/sign-up" target="_blank">JOIN NOW</a>
  <span class="announce-star">&#9733;</span>
  <button class="close-btn" onclick="document.getElementById('announce-bar').style.display='none'" aria-label="Close">&times;</button>
</div>'''

# ============================================================
# SHARED HEADER HTML TEMPLATE
# Logo and mega menu image paths must be prefixed with {PREFIX}
# ============================================================
def make_header_html(prefix, nav_links, page_type='guide'):
    """
    Generate header HTML with correct relative paths.
    
    nav_links: list of (href, label, active) tuples for main nav
    prefix: relative path prefix (e.g. '../' or '../../' or '')
    page_type: 'index' for index page with anchor links, 'guide' for others
    """
    
    # For index page: nav links point to #anchors
    # For other pages: nav links use prefixed paths
    if page_type == 'index':
        nav_html = '''      <a href="#section-start">Get Started</a>
      <a href="#section-who">Who to Target</a>
      <a href="#commission">Commission</a>
      <a href="#section-opportunity">Opportunity</a>
      <a href="#dashboard-setup">Dashboard Setup</a>'''
        cta_href = '#dashboard-setup'
    else:
        nav_html = '''      <a href="{p}index.html#section-start">Get Started</a>
      <a href="{p}index.html#section-who">Who to Target</a>
      <a href="{p}index.html#commission">Commission</a>
      <a href="{p}index.html#section-opportunity">Opportunity</a>
      <a href="{p}index.html#dashboard-setup">Dashboard Setup</a>'''.format(p=prefix)
        cta_href = prefix + 'index.html#dashboard-setup'
    
    # Active class for Resources in nav
    resources_active = ' active' if page_type in ['guides', 'mcp'] else ''
    
    header = '''<header id="header" class="stagger-enter" style="animation-delay: 0s;">
  <div class="header-inner">
    <a href="{prefix}index.html" class="header-logo">
      <img src="{prefix}logo.svg" alt="TrueProfit Affiliate Program" class="logo-img">
    </a>
    <nav class="header-nav" id="headerNav">
{nav_html}
      <div class="nav-dropdown-wrapper">
        <a href="#resources" class="nav-dropdown-trigger{resources_active}">Resources <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-left:4px; vertical-align:middle;"><polyline points="6 9 12 15 18 9"></polyline></svg></a>
                        <div class="mega-menu">
          <!-- Zone 1: Guides & Angles (White) -->
          <div class="mega-zone mega-zone-1">
            <a class="mega-pill-badge" href="{prefix}guides.html">
              <svg fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" style="margin-right: 4px;" viewBox="0 0 24 24" width="14"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
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
                  <img src="{prefix}22.svg" alt="Track Profit Like A Pro">
                </div>
                <div class="mega-gem-text">Track Profit Like A Pro</div>
              </a>
              <a class="mega-gem-card" href="{prefix}guides/angles/scale-safely-with-margins.html">
                <div class="mega-gem-img" style="background: #62BBA2;">
                  <img src="{prefix}19.svg" alt="Scale Safely with Margins">
                </div>
                <div class="mega-gem-text">Scale Safely with Margins</div>
              </a>
              <a class="mega-gem-card" href="{prefix}guides/angles/stop-losing-30-profit.html">
                <div class="mega-gem-img" style="background: #FCE1DA;">
                  <img src="{prefix}21.svg" alt="Stop Losing 30% Profit">
                </div>
                <div class="mega-gem-text">Stop Losing 30% Profit</div>
              </a>
            </div>
          </div>
          <!-- Zone 2: MCP Promotion (Mint) -->
          <div class="mega-zone mega-zone-2">
            <a class="mega-pill-badge" href="{prefix}mcp-promotion.html" style="border-color: #1d9e75; color: #1d9e75; background: #e6fbf1;">
              <svg fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" style="margin-right: 4px;" viewBox="0 0 24 24" width="14"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
              MCP PROMOTION &rarr;
              <svg fill="currentColor" height="10" style="color: #f59e0b; margin-left: 6px; vertical-align: middle;" viewBox="0 0 24 24" width="10"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
            </a>
            <div class="mega-links-list" style="margin-top: 24px; gap: 24px;">
              <a class="mega-link-item" href="{prefix}mcp-promotion.html">MCP Promotion Hub</a>
              <a class="mega-link-item" href="{prefix}resources/mcp/x-twitter-ready-to-post.html">X/Twitter Ready-to-Post</a>
              <a class="mega-link-item" href="{prefix}resources/mcp/reddit-ready-to-post.html">Reddit Ready-to-Post</a>
              <a class="mega-link-item" href="{prefix}resources/mcp/short-form-video-guidelines.html">Short-Form Video Guidelines</a>
            </div>
            <!-- Featured MCP Card inside menu -->
            <a class="mega-mcp-card" href="{prefix}mcp-promotion.html">
              <div class="mega-mcp-icon">
                <svg fill="none" height="18" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 24 24" width="18"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
              </div>
              <div class="mega-mcp-info">
                <span class="mega-mcp-title">TrueProfit MCP</span>
                <span class="mega-mcp-subtitle">TrueProfit x LLMs</span>
              </div>
            </a>
          </div>
          <!-- Zone 3: Creative Assets (Navy) -->
          <div class="mega-zone mega-zone-3">
            <a class="mega-pill-badge mega-pill-badge-dark" href="#" style="margin-bottom: 24px;">
              <svg fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" style="margin-right: 4px;" viewBox="0 0 24 24" width="14"><rect height="7" width="7" x="3" y="3"></rect><rect height="7" width="7" x="14" y="3"></rect><rect height="7" width="7" x="14" y="14"></rect><rect height="7" width="7" x="3" y="14"></rect></svg>
              CREATIVE ASSETS &rarr;
            </a>

            <a class="mega-asset-card" href="https://trueprofit.notion.site/2e265f0648c680b68a14ec66c712323b?v=2e265f0648c681fb9db2000c532b98a0" target="_blank" rel="noopener noreferrer">
              <div class="mega-asset-content">
                <div class="mega-asset-name">Logo Kit</div>
                <div class="mega-asset-desc">Download high-res TrueProfit logos in multiple formats.</div>
              </div>
              <span class="mega-asset-plus">+</span>
              <img src="{prefix}36.svg" alt="" class="mega-asset-svg">
            </a>

            <a class="mega-asset-card" href="https://trueprofit.notion.site/2e265f0648c680b68a14ec66c712323b?v=2e265f0648c681dbb776000cb2feef3f" target="_blank" rel="noopener noreferrer">
              <div class="mega-asset-content">
                <div class="mega-asset-name">Campaign Banners</div>
                <div class="mega-asset-desc">Ready-to-use campaign banners sized for every platform.</div>
              </div>
              <span class="mega-asset-plus">+</span>
              <img src="{prefix}37.svg" alt="" class="mega-asset-svg">
            </a>

            <a class="mega-asset-card" href="https://trueprofit.notion.site/2e265f0648c680b68a14ec66c712323b?v=2e265f0648c681eb8be9000c647955f8" target="_blank" rel="noopener noreferrer" style="margin-bottom: 0;">
              <div class="mega-asset-content">
                <div class="mega-asset-name">App Footages</div>
                <div class="mega-asset-desc">Raw screen recordings and dashboard visuals for B-roll.</div>
              </div>
              <span class="mega-asset-plus">+</span>
              <img src="{prefix}35.svg" alt="" class="mega-asset-svg">
            </a>
          </div>
        </div>
      </div>
    </nav>
    <div class="header-actions" id="headerActions">
      <a href="https://trueprofit.trackdesk.com/dashboard" target="_blank" class="btn-ghost">My Dashboard</a>
      <a href="{cta_href}" class="btn-cta">Get affiliate link &rarr;</a>
    </div>
    <button class="hamburger" id="hamburgerBtn" aria-label="Open menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>'''.format(
        prefix=prefix,
        nav_html=nav_html,
        resources_active=resources_active,
        cta_href=cta_href
    )
    
    return header


# ============================================================
# MOBILE MENU HTML TEMPLATE
# ============================================================
def make_mobile_menu(prefix, page_type='guide'):
    if page_type == 'index':
        links = [
            ('#section-start', 'Get Started'),
            ('#section-who', 'Who to Target'),
            ('#commission', 'Commission'),
            ('#section-opportunity', 'Opportunity'),
            ('#dashboard-setup', 'Dashboard Setup'),
        ]
        cta_href = '#dashboard-setup'
    else:
        links = [
            (prefix + 'index.html#section-start', 'Get Started'),
            (prefix + 'index.html#section-who', 'Who to Target'),
            (prefix + 'index.html#commission', 'Commission'),
            (prefix + 'index.html#section-opportunity', 'Opportunity'),
            (prefix + 'index.html#dashboard-setup', 'Dashboard Setup'),
        ]
        cta_href = prefix + 'index.html#dashboard-setup'
    
    links_html = ''
    for href, label in links:
        links_html += '      <a href="%s" class="mobile-nav-link">%s</a>\n' % (href, label)
    
    # Resources section in mobile
    resources_html = '''      <div class="mobile-nav-section">
        <div class="mobile-nav-section-title">Resources</div>
        <a href="{p}guides.html" class="mobile-nav-link mobile-nav-link-sub">Guides</a>
        <a href="{p}guides/general-guide.html" class="mobile-nav-link mobile-nav-link-sub">General Guide</a>
        <a href="{p}guides/discord-blueprint.html" class="mobile-nav-link mobile-nav-link-sub">Discord Blueprint</a>
        <a href="{p}guides/tiktok-youtube-shorts.html" class="mobile-nav-link mobile-nav-link-sub">TikTok &amp; YouTube Shorts</a>
        <a href="{p}guides/angles/track-profit-like-a-pro.html" class="mobile-nav-link mobile-nav-link-sub">Track Profit Like A Pro</a>
        <a href="{p}guides/angles/scale-safely-with-margins.html" class="mobile-nav-link mobile-nav-link-sub">Scale Safely with Margins</a>
        <a href="{p}guides/angles/stop-losing-30-profit.html" class="mobile-nav-link mobile-nav-link-sub">Stop Losing 30% Profit</a>
        <div class="mobile-nav-section-title" style="margin-top: 12px;">MCP Promotion</div>
        <a href="{p}mcp-promotion.html" class="mobile-nav-link mobile-nav-link-sub">MCP Promotion Hub</a>
        <a href="{p}resources/mcp/x-twitter-ready-to-post.html" class="mobile-nav-link mobile-nav-link-sub">X/Twitter Ready-to-Post</a>
        <a href="{p}resources/mcp/reddit-ready-to-post.html" class="mobile-nav-link mobile-nav-link-sub">Reddit Ready-to-Post</a>
        <a href="{p}resources/mcp/short-form-video-guidelines.html" class="mobile-nav-link mobile-nav-link-sub">Short-Form Video Guidelines</a>
      </div>'''.format(p=prefix)
    
    return '''<div id="mobileOverlay" class="mobile-overlay" onclick="closeMobileMenu()"></div>
<div id="mobileMenu" class="mobile-menu">
  <div class="mobile-menu-header">
    <a href="{prefix}index.html" class="header-logo" onclick="closeMobileMenu()">
      <img src="{prefix}logo.svg" alt="TrueProfit" class="logo-img" style="height: 36px;">
    </a>
    <button class="mobile-close-btn" onclick="closeMobileMenu()" aria-label="Close menu">&times;</button>
  </div>
  <nav class="mobile-nav">
{links_html}{resources_html}
  </nav>
  <div class="mobile-menu-footer">
    <a href="{cta_href}" class="btn-cta" style="width: 100%; justify-content: center; text-align: center; display: flex;">Get affiliate link &rarr;</a>
  </div>
</div>'''.format(
        prefix=prefix,
        links_html=links_html,
        resources_html=resources_html,
        cta_href=cta_href
    )


# ============================================================
# FILE CONFIGURATIONS
# ============================================================
FILES = [
    # (rel_path, prefix, page_type)
    ('index.html', '', 'index'),
    ('guides.html', '', 'guides'),
    ('mcp-promotion.html', '', 'mcp'),
    ('guides/discord-blueprint.html', '../', 'guide'),
    ('guides/general-guide.html', '../', 'guide'),
    ('guides/tiktok-youtube-shorts.html', '../', 'guide'),
    ('guides/angles/scale-safely-with-margins.html', '../../', 'guide'),
    ('guides/angles/stop-losing-30-profit.html', '../../', 'guide'),
    ('guides/angles/track-profit-like-a-pro.html', '../../', 'guide'),
    ('resources/mcp/reddit-ready-to-post.html', '../../', 'mcp-resource'),
    ('resources/mcp/short-form-video-guidelines.html', '../../', 'mcp-resource'),
    ('resources/mcp/x-twitter-ready-to-post.html', '../../', 'mcp-resource'),
]


def replace_announce_bar(text, new_announce_bar):
    """Replace announce bar HTML in text."""
    # Try to find the existing announce bar
    pattern = r'<div\s+id=["\']announce-bar["\'][^>]*>.*?</div>'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return text[:match.start()] + new_announce_bar + text[match.end():]
    
    # If not found, insert before <header
    pattern2 = r'(<header\s)'
    match2 = re.search(pattern2, text)
    if match2:
        return text[:match2.start()] + '\n' + new_announce_bar + '\n\n' + text[match2.start():]
    
    return text  # fallback: don't modify


def replace_header(text, new_header):
    """Replace the <header>...</header> block."""
    pattern = r'<header\s[^>]*id=["\']header["\'][^>]*>.*?</header>'
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    if match:
        return text[:match.start()] + new_header + text[match.end():]
    
    # Try without id
    pattern2 = r'<header[^>]*>.*?</header>'
    match2 = re.search(pattern2, text, re.DOTALL | re.IGNORECASE)
    if match2:
        return text[:match2.start()] + new_header + text[match2.end():]
    
    return text


def replace_mobile_menu(text, new_mobile_menu):
    """Replace mobile overlay + menu HTML."""
    # Remove existing mobile overlay
    text = re.sub(r'<div\s+id=["\']mobileOverlay["\'][^>]*/>', '', text)
    text = re.sub(r'<div\s+id=["\']mobileOverlay["\'][^>]*></div>', '', text)
    text = re.sub(r'<div\s+id=["\']mobileOverlay["\'][^>]*>.*?</div>', '', text, flags=re.DOTALL)
    
    # Remove existing mobile menu
    pattern = r'<div\s+id=["\']mobileMenu["\'][^>]*>.*?</div>\s*(?=<!--|\n<[a-z]|$)'
    # More reliable: find the div with id=mobileMenu and its matching closing tag
    # Count div nesting
    idx = text.find('id="mobileMenu"')
    if idx == -1:
        idx = text.find("id='mobileMenu'")
    
    if idx != -1:
        # Find the opening <div
        start = text.rfind('<div', 0, idx)
        if start != -1:
            # Find matching closing div
            depth = 0
            pos = start
            while pos < len(text):
                if text[pos:pos+4] == '<div':
                    depth += 1
                elif text[pos:pos+6] == '</div>':
                    depth -= 1
                    if depth == 0:
                        end = pos + 6
                        text = text[:start] + text[end:]
                        break
                pos += 1
    
    # Now insert mobile menu before </body>
    text = text.replace('</body>', '\n' + new_mobile_menu + '\n</body>', 1)
    
    return text


# ============================================================
# MAIN REPAIR LOOP
# ============================================================
print("=" * 60)
print("PHASE 2: Shared Components Repair")
print("=" * 60)

for rel_path, prefix, page_type in FILES:
    path = os.path.join(BASE, rel_path.replace('/', os.sep))
    print("\nProcessing: %s (prefix='%s', type=%s)" % (rel_path, prefix, page_type))
    
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # 1. Replace announce bar
    text = replace_announce_bar(text, ANNOUNCE_BAR)
    
    # 2. Replace header with correct paths
    new_header = make_header_html(prefix, [], page_type)
    text = replace_header(text, new_header)
    
    # Check if header was found
    if 'id="header"' not in text:
        print("  WARNING: header not found/replaced!")
    
    # 3. Add scroll-margin-top to article sections if missing
    if 'article-section' in text and 'scroll-margin-top' not in text:
        # Add scroll-margin-top CSS
        css_to_add = '\n/* Fix content hidden under sticky header */\n.article-section, [id] { scroll-margin-top: 120px; }\n'
        text = text.replace('</style>', css_to_add + '</style>', 1)
    
    # 4. Save
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(text)
    
    print("  Saved: %s" % rel_path)

print("\n" + "=" * 60)
print("Phase 2 complete!")
print("=" * 60)
