import glob
import re

new_css = """
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
    content: "☰";
  }

  /* Hide "Get affiliate link" button in navbar on mobile */
  .get-affiliate-btn, .btn-cta, .btn-ghost {
    display: none !important;
  }
}

/* Mobile Dropdown styles (outside media query so JS can toggle it safely, or inside media query) */
.mobile-menu-dropdown {
  display: none;
  position: fixed;
  top: 64px; /* Adjust based on new header height 12px*2 + 40px = 64px */
  left: 0;
  width: 100%;
  z-index: 9999;
  background: #0D1F2D;
  border-top: 1px solid rgba(255,255,255,0.1);
  box-sizing: border-box;
}
.mobile-menu-dropdown.active {
  display: block;
}
.mobile-menu-dropdown a {
  display: block;
  padding: 14px 20px;
  color: white;
  border-bottom: 1px solid rgba(255,255,255,0.06);
  text-decoration: none;
  font-family: 'Inter', sans-serif;
  transition: background 0.2s;
}
.mobile-menu-dropdown a:hover {
  background: rgba(255,255,255,0.05);
}
.mobile-menu-dropdown a.mobile-btn-cta {
  background: #00C896;
  color: #0D1F2D;
  text-align: center;
  font-weight: 600;
  border-radius: 8px;
  margin: 16px 20px;
  padding: 14px 20px;
  border-bottom: none;
}
.mobile-menu-dropdown a.mobile-btn-cta:hover {
  background: #00B085;
}
"""

new_html = """
    <div class="mobile-menu-dropdown" id="mobileMenuDropdown">
      <a href="guides.html">Guides</a>
      <a href="mcp-promotion.html">MCP Promotion</a>
      <a href="#commission">Commission</a>
      <a href="#resources">Resources</a>
      <a href="https://trueprofit.trackdesk.com/dashboard" target="_blank">My Dashboard</a>
      <a href="https://trueprofit.trackdesk.com" target="_blank" class="mobile-btn-cta">Get Affiliate Link</a>
    </div>
"""

for f in ['guides.html', 'index.html', 'mcp-promotion.html']:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            html = file.read()
    except FileNotFoundError:
        continue

    # Remove previous @media (max-width: 1023px) block
    html = re.sub(r'@media \(max-width: 1023px\) \{.*?\n\}\n?', '', html, flags=re.DOTALL)
    
    # Remove previous .mobile-menu-dropdown HTML
    html = re.sub(r'\s*<div class="mobile-menu-dropdown" id="mobileMenuDropdown">.*?</div>\s*', '\n', html, flags=re.DOTALL)

    # Insert new CSS before </style>
    html = html.replace('</style>', new_css + '\n</style>')

    # Insert new HTML before </header>
    html = html.replace('</header>', new_html + '\n</header>')

    # Write file
    with open(f, 'w', encoding='utf-8') as file:
        file.write(html)

print("Done")
