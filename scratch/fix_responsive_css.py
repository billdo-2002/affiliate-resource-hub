"""
Fix the unclosed @media (max-width: 1024px) block in all pages that have it.
Also clean up the mobile nav CSS to use proper selectors for the hamburger.
"""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

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

# The broken pattern (first @media 1024px is UNCLOSED, 1100px nested inside):
BAD_PATTERN = '''\
@media (max-width: 1024px) {
  .guide-hero-inner { grid-template-columns: 1fr; gap: 48px; }
@media (max-width: 1100px) {
  .header-nav { display: none; }
  .header-actions { display: none; }
  .hamburger { display: flex; }
  #header.nav-open .header-nav {
    display: flex; flex-direction: column; position: fixed;
    top: 64px; left: 0; right: 0; bottom: 0;
    background: rgba(255,255,255,0.98);
    padding: 32px 28px; gap: 8px; backdrop-filter: blur(12px);
    z-index: 999; overflow-y: auto;
  }
  #header.nav-open .header-actions {
    display: flex; flex-direction: column; padding: 0 28px 28px;
    position: fixed; bottom: 0; left: 0; right: 0;
    background: rgba(255,255,255,0.98); border-top: 1px solid var(--border-light);
    padding-top: 16px; z-index: 1000;
  }
}
@media (max-width: 1024px) {
  .guide-hero-inner { grid-template-columns: 1fr; gap: 48px; }
  .guide-hero-visual { max-width: 500px; }
  .guide-body-inner { grid-template-columns: 1fr; }
  .guide-sidebar { position: static; top: auto; }
  .audience-block { grid-template-columns: 1fr; }
  .audience-visual { order: -1; }
  .info-cards { grid-template-columns: 1fr; }
}'''

# The corrected pattern:
GOOD_PATTERN = '''\
@media (max-width: 1100px) {
  .header-nav { display: none; }
  .header-actions { display: none; }
  .hamburger { display: flex; }
  #header.nav-open .header-nav {
    display: flex; flex-direction: column; position: fixed;
    top: 64px; left: 0; right: 0; bottom: 0;
    background: rgba(255,255,255,0.98);
    padding: 32px 28px; gap: 8px; backdrop-filter: blur(12px);
    z-index: 999; overflow-y: auto;
  }
  #header.nav-open .header-actions {
    display: flex; flex-direction: column; padding: 0 28px 28px;
    position: fixed; bottom: 0; left: 0; right: 0;
    background: rgba(255,255,255,0.98); border-top: 1px solid var(--border-light);
    padding-top: 16px; z-index: 1000;
  }
}
@media (max-width: 1024px) {
  .guide-hero-inner { grid-template-columns: 1fr; gap: 48px; }
  .guide-hero-visual { max-width: 500px; }
  .guide-body-inner { grid-template-columns: 1fr; }
  .guide-sidebar { position: static; top: auto; }
  .audience-block { grid-template-columns: 1fr; }
  .audience-visual { order: -1; }
  .info-cards { grid-template-columns: 1fr; }
}'''

# Also fix the mobile 1023px block:
# The current block hides header-nav and btn-cta with display:none!important
# But it also sets weird background on hamburger (rgba(255,255,255,0.08) = near-transparent white)
# And sets color:white on hamburger which is wrong on white background
# Let's replace the whole block with a clean version
OLD_MOBILE_1023 = '''\
@media (max-width: 1023px) {
  /* Hide all nav links and buttons in navbar */
  nav .nav-links,
  nav .nav-items,
  nav ul,
  nav a:not(.logo-link),
  nav button:not(.hamburger-btn):not(.get-affiliate-btn),
  .navbar-menu,
  .nav-center,
  [class*="nav-link"],
  [class*="menu-item"],
  .header-nav,
  .header-actions {
    display: none !important;
  }

  /* Navbar layout */
  nav, header, .navbar, .header-inner {
    display: flex !important;
    flex-direction: row !important;
    justify-content: space-between !important;
    align-items: center !important;
    padding: 12px 16px !important;
    overflow: hidden !important;
    flex-wrap: nowrap !important;
  }

  /* Keep only logo visible on left */
  .logo, .navbar-logo, [class*="logo"], .header-logo {
    display: flex !important;
    flex-shrink: 0 !important;
  }

  /* Hamburger button — show on right */
  .hamburger-btn, .hamburger {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 40px !important;
    height: 40px !important;
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 8px !important;
    color: white !important;
    font-size: 18px !important;
    cursor: pointer !important;
    flex-shrink: 0 !important;
  }
  .hamburger span {
    display: none;
  }
  .hamburger::before {
    content: "\\2630";
  }

  /* Hide "Get affiliate link" button in navbar on mobile */
  .get-affiliate-btn, .btn-cta, .btn-ghost {
    display: none !important;
  }
}'''

NEW_MOBILE_1023 = '''\
@media (max-width: 1023px) {
  .header-nav,
  .header-actions {
    display: none !important;
  }
  .hamburger {
    display: flex !important;
  }
  .hamburger span {
    display: block;
  }
}'''

print('=' * 70)
print('RESPONSIVE CSS FIX')
print('=' * 70)

for rel_path in FILES:
    path = os.path.join(BASE, rel_path.replace('/', os.sep))
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    original = text
    changes = []
    
    # Fix 1: unclosed @media 1024px block
    if BAD_PATTERN in text:
        text = text.replace(BAD_PATTERN, GOOD_PATTERN)
        changes.append('Fixed unclosed @media 1024px block')
    
    # Fix 2: Replace the bloated mobile 1023px block with clean version
    # Only if it matches our old pattern exactly
    if OLD_MOBILE_1023 in text:
        text = text.replace(OLD_MOBILE_1023, NEW_MOBILE_1023)
        changes.append('Replaced bloated @media 1023px block with clean version')
    
    if text != original:
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(text)
        print('\n[FIXED] %s' % rel_path)
        for c in changes:
            print('  + %s' % c)
    else:
        print('[OK]    %s' % rel_path)

print('\n' + '=' * 70)
print('Done!')
