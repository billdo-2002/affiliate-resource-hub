import glob
import re

css_additions = """
@media (max-width: 1023px) {
  .mega-menu,
  .nav-dropdown-wrapper,
  [class*="mega-menu"] {
    display: none !important;
  }
  .header-nav {
    display: none !important;
  }
  .btn-ghost {
    display: none !important;
  }
  .header-inner {
    flex-wrap: wrap;
  }
  .hamburger {
    display: flex !important;
    order: 3;
    background: transparent;
    border: none;
    color: var(--text-dark);
    font-size: 24px;
    cursor: pointer;
  }
  .header-actions {
    margin-left: auto;
    margin-right: 16px;
    order: 2;
  }
  .mobile-menu-dropdown {
    display: none;
    width: 100%;
    background: #0D1F2D;
    padding: 16px;
    margin-top: 16px;
    order: 4;
    border-radius: 8px;
  }
  .mobile-menu-dropdown.active {
    display: block;
  }
  .mobile-menu-dropdown a {
    display: block;
    padding: 12px 16px;
    color: white;
    border-bottom: 1px solid rgba(255,255,255,0.08);
    text-decoration: none;
    font-weight: 500;
  }
  .mobile-menu-dropdown a:last-child {
    border-bottom: none;
  }
}
"""

mobile_html = """
    <div class="mobile-menu-dropdown" id="mobileMenuDropdown">
      <a href="#section-start">Get Started</a>
      <a href="guides.html">Resources</a>
      <a href="#section-commission">Commission</a>
      <a href="https://trueprofit.trackdesk.com/dashboard" target="_blank">My Dashboard</a>
      <a href="https://trueprofit.io/partner" target="_blank">Get Affiliate Link</a>
    </div>
"""

js_logic = """
<script>
  document.addEventListener('DOMContentLoaded', function() {
    var hamburgerBtn = document.getElementById('hamburgerBtn');
    var mobileMenuDropdown = document.getElementById('mobileMenuDropdown');
    if (hamburgerBtn && mobileMenuDropdown) {
      hamburgerBtn.addEventListener('click', function() {
        mobileMenuDropdown.classList.toggle('active');
      });
    }
  });
</script>
"""

for f in ['guides.html', 'index.html', 'mcp-promotion.html']:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            html = file.read()
    except FileNotFoundError:
        continue

    # Revert CSS
    html = html.replace('width: 100%;\n  min-width: unset;', 'width: 1280px;')
    html = re.sub(
        r'(?s)(\.mega-menu\s*\{[^\}]*?)\bdisplay:\s*flex;',
        r'\1display: grid;\n  grid-template-columns: 35% 25% 40%;',
        html
    )
    html = html.replace('overflow-x: auto;', 'overflow: hidden;')
    
    html = html.replace('  flex: 0 0 32%;\n  min-width: 280px;\n', '')
    html = html.replace('  flex: 0 0 26%;\n  min-width: 220px;\n', '')
    html = html.replace('  flex: 0 0 auto;\n  flex: 1;\n  min-width: 300px;\n', '')
    html = re.sub(r'(\.mega-asset-card\s*\{.*?)\s*overflow:\s*hidden;\n', r'\1', html, flags=re.DOTALL)
    html = re.sub(r'(\.mega-asset-desc\s*\{.*?)\s*white-space:\s*normal;\n\s*word-wrap:\s*break-word;\n', r'\1', html, flags=re.DOTALL)
    
    # Remove previous media queries
    html = re.sub(r'@media \(max-width: 1200px\).*?@media \(max-width: 1024px\) \{.*?\n\}\n', '', html, flags=re.DOTALL)
    
    # Add new CSS
    if '@media (max-width: 1023px)' not in html:
        html = html.replace('</style>', css_additions + '</style>')
    
    # Add new HTML
    if 'id="mobileMenuDropdown"' not in html:
        html = html.replace('</header>', mobile_html + '</header>')
        
    # Add JS logic
    if 'mobileMenuDropdown.classList.toggle' not in html:
        html = html.replace('</body>', js_logic + '\n</body>')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(html)

print('Done!')
