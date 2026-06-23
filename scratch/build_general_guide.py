import os
import re

BASE = r"c:\Users\khoadnd\Desktop\onboarding hub"
head_path = os.path.join(BASE, "scratch", "general_guide_head.txt")

# 1. Read CSS and head sections from general_guide_head.txt
with open(head_path, "r", encoding="utf-8") as f:
    text = f.read()

# Locate the end of styling section
style_end_idx = text.find("</style>")
if style_end_idx == -1:
    raise ValueError("Could not find </style> in general_guide_head.txt")

head_content = text[:style_end_idx]

# Define new callout-box CSS
new_css = """/* Unified Callout / Note Boxes in "Quick Recap" Style */
.callout-box {
  border-left: 4px solid var(--green, #10b981);
  padding-left: 32px;
  margin: 36px 0;
  background: transparent !important;
  border-radius: 0 !important;
  box-shadow: none !important;
}
.callout-box.emerald {
  border-left-color: var(--green, #10b981);
}
.callout-box.warning,
.callout-box.mistake {
  border-left-color: #f97316;
}
.callout-title {
  font-size: 20px;
  font-weight: 700;
  color: var(--green, #10b981);
  margin-bottom: 18px;
  font-family: var(--font-family, inherit);
}
.callout-box.warning .callout-title,
.callout-box.mistake .callout-title {
  color: #ea580c;
}
.callout-bullets {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.callout-row {
  display: flex;
  align-items: flex-start;
  gap: 16px;
}
.callout-icon {
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  border: 1.5px dashed var(--green, #10b981);
  color: var(--green, #10b981);
  margin-top: 2px;
  box-sizing: border-box;
}
.callout-box.warning .callout-icon,
.callout-box.mistake .callout-icon {
  border-color: #f97316;
  color: #f97316;
}
.callout-icon svg {
  width: 14px;
  height: 14px;
  fill: currentColor;
}
.callout-text {
  font-size: 18px;
  line-height: 1.8;
  color: var(--text-color, #334155);
}
@media (max-width: 768px) {
  .callout-box {
    padding-left: 24px;
  }
  .callout-title {
    font-size: 18px;
  }
  .callout-text {
    font-size: 16px;
    line-height: 1.7;
  }
  .callout-bullets {
    gap: 16px;
  }
}

/* Fix content hidden under sticky header */
.article-section, [id] { scroll-margin-top: 120px; }
"""

# Replace old note styling in head_content
css_pattern = re.compile(
    r'\/\*\s*Insight\s*&\s*Info\s*Note\s*Blocks\s*\*\/.*?'
    r'\.article-note\s*\{.*?'
    r'\.article-note\.info\s*\{[^\}]*\}',
    re.DOTALL
)

if css_pattern.search(head_content):
    head_content = css_pattern.sub(new_css, head_content)
else:
    # Fallback to general replace
    fallback_pattern = re.compile(
        r'\.article-note\s*\{.*?'
        r'\.article-note\.info\s*\{[^\}]*\}',
        re.DOTALL
    )
    if fallback_pattern.search(head_content):
        head_content = fallback_pattern.sub(new_css, head_content)
    else:
        # Just append new_css before </style> in the string
        head_content += "\n" + new_css

# Construct body content
body_html = """
</style>
</head>
<body>

<!-- ==============================
     ANNOUNCEMENT BAR
     ============================== -->
<div id="announce-bar">
  <span class="announce-star">&#9733;</span>
  <span>Earn 100% on your first month + 20% recurring for the year. Join 1,000+ affiliates.</span>
  <a href="https://affiliate.trueprofit.io/sign-up" target="_blank">JOIN NOW</a>
  <span class="announce-star">&#9733;</span>
  <button class="close-btn" onclick="document.getElementById('announce-bar').style.display='none'" aria-label="Close">&times;</button>
</div>

<!-- ==============================
     HEADER (with prefix ../)
     ============================== -->
<header id="header" class="stagger-enter" style="animation-delay: 0s;">
  <div class="header-inner">
    <a href="../index.html" class="header-logo">
      <img src="../logo.svg" alt="TrueProfit Affiliate Program" class="logo-img">
    </a>
    <nav class="header-nav" id="headerNav">
      <a href="../index.html#section-start">Get Started</a>
      <a href="../index.html#section-who">Who to Target</a>
      <a href="../index.html#commission">Commission</a>
      <a href="../index.html#section-opportunity">Opportunity</a>
      <a href="../index.html#dashboard-setup">Dashboard Setup</a>
      <div class="nav-dropdown-wrapper">
        <a href="#resources" class="nav-dropdown-trigger active">Resources <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-left:4px; vertical-align:middle;"><polyline points="6 9 12 15 18 9"></polyline></svg></a>
        <div class="mega-menu">
          <!-- Zone 1: Guides & Angles (White) -->
          <div class="mega-zone mega-zone-1">
            <a class="mega-pill-badge" href="../guides.html">
              <svg fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" style="margin-right: 4px;" viewBox="0 0 24 24" width="14"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
              GUIDES &rarr;
            </a>
            <div class="mega-links-grid">
              <a class="mega-link-item" href="../guides/general-guide.html">General Guide</a>
              <a class="mega-link-item" href="../guides/discord-blueprint.html">Discord Blueprint</a>
              <a class="mega-link-item" href="../guides/tiktok-youtube-shorts.html">TikTok &amp; YouTube Shorts</a>
            </div>
            <div class="mega-section-label" style="margin-top: 8px;">HIGH-CONVERTING ANGLES:</div>
            <div class="mega-gems-list">
              <a class="mega-gem-card" href="../guides/angles/track-profit-like-a-pro.html">
                <div class="mega-gem-img" style="background: #0B1D2E;">
                  <img src="../images/22.svg" alt="Track Profit Like A Pro">
                </div>
                <div class="mega-gem-text">Track Profit Like A Pro</div>
              </a>
              <a class="mega-gem-card" href="../guides/angles/scale-safely-with-margins.html">
                <div class="mega-gem-img" style="background: #62BBA2;">
                  <img src="../images/19.svg" alt="Scale Safely with Margins">
                </div>
                <div class="mega-gem-text">Scale Safely with Margins</div>
              </a>
              <a class="mega-gem-card" href="../guides/angles/stop-losing-30-profit.html">
                <div class="mega-gem-img" style="background: #FCE1DA;">
                  <img src="../images/21.svg" alt="Stop Losing 30% Profit">
                </div>
                <div class="mega-gem-text">Stop Losing 30% Profit</div>
              </a>
            </div>
          </div>
          <!-- Zone 2: MCP Promotion (Mint) -->
          <div class="mega-zone mega-zone-2">
            <a class="mega-pill-badge" href="../mcp-promotion.html" style="border-color: #1d9e75; color: #1d9e75; background: #e6fbf1;">
              <svg fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" style="margin-right: 4px;" viewBox="0 0 24 24" width="14"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
              MCP PROMOTION &rarr;
              <svg fill="currentColor" height="10" style="color: #f59e0b; margin-left: 6px; vertical-align: middle;" viewBox="0 0 24 24" width="10"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
            </a>
            <div class="mega-links-list" style="margin-top: 24px; gap: 24px;">
              <a class="mega-link-item" href="../mcp-promotion.html">MCP Promotion Hub</a>
              <a class="mega-link-item" href="../resources/mcp/x-twitter-ready-to-post.html">X/Twitter Ready-to-Post</a>
              <a class="mega-link-item" href="../resources/mcp/reddit-ready-to-post.html">Reddit Ready-to-Post</a>
              <a class="mega-link-item" href="../resources/mcp/short-form-video-guidelines.html">Short-Form Video Guidelines</a>
            </div>
            <!-- Featured MCP Card inside menu -->
            <a class="mega-mcp-card" href="../mcp-promotion.html">
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
              <img src="../images/36.svg" alt="" class="mega-asset-svg">
            </a>

            <a class="mega-asset-card" href="https://trueprofit.notion.site/2e265f0648c680b68a14ec66c712323b?v=2e265f0648c681dbb776000cb2feef3f" target="_blank" rel="noopener noreferrer">
              <div class="mega-asset-content">
                <div class="mega-asset-name">Campaign Banners</div>
                <div class="mega-asset-desc">Ready-to-use campaign banners sized for every platform.</div>
              </div>
              <span class="mega-asset-plus">+</span>
              <img src="../images/37.svg" alt="" class="mega-asset-svg">
            </a>

            <a class="mega-asset-card" href="https://trueprofit.notion.site/2e265f0648c680b68a14ec66c712323b?v=2e265f0648c681eb8be9000c647955f8" target="_blank" rel="noopener noreferrer" style="margin-bottom: 0;">
              <div class="mega-asset-content">
                <div class="mega-asset-name">App Footages</div>
                <div class="mega-asset-desc">Raw screen recordings and dashboard visuals for B-roll.</div>
              </div>
              <span class="mega-asset-plus">+</span>
              <img src="../images/35.svg" alt="" class="mega-asset-svg">
            </a>
          </div>
        </div>
      </div>
    </nav>
    <div class="header-actions" id="headerActions">
      <a href="https://trueprofit.trackdesk.com/dashboard" target="_blank" class="btn-ghost">My Dashboard</a>
      <a href="../index.html#dashboard-setup" class="btn-cta">Get affiliate link &rarr;</a>
    </div>
    <button class="hamburger" id="hamburgerBtn" aria-label="Open menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<!-- ==============================
     HERO SECTION
     ============================== -->
<section class="guide-hero">
  <div class="guide-hero-inner">
    <div class="guide-hero-left stagger-enter" style="animation-delay: 0.1s;">
      <!-- Breadcrumb -->
      <div class="guide-breadcrumb">
        <a href="../index.html">Home</a><span class="sep">›</span><a href="../guides.html">Guides</a><span class="sep">›</span><span class="current">General Affiliate Guide</span>
      </div>
      <!-- Title -->
      <h1 class="guide-hero-title">General Affiliate Guide</h1>
      <!-- Subtitle -->
      <p class="guide-hero-subtitle">The foundational playbook. Learn the core product value, who to target, and how to start making your first commissions.</p>
      <!-- Tags -->
      <div class="guide-tags">
        <span class="guide-tag">Core Path</span>
        <span class="guide-tag">General Guide</span>
        <span class="guide-tag">Playbook</span>
      </div>
      <!-- CTA Button -->
      <div class="guide-hero-btns">
        <a class="hero-btn-angles" href="#section-1">View guide content <svg class="hero-btn-arrow" fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 24 24" width="16"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg></a>
      </div>
    </div>
    <!-- Hero Illustration -->
    <div class="guide-hero-visual stagger-enter" style="animation-delay: 0.2s;">
      <img src="../images/1.svg" alt="General Affiliate Guide" style="max-width: 440px; height: auto; object-fit: contain; background: transparent; border: none; box-shadow: none;">
    </div>
  </div>
</section>

<!-- ==============================
     GUIDE BODY LAYOUT — 2 COLUMN
     ============================== -->
<section class="guide-body">
  <div class="guide-body-inner">
    
    <!-- Left Column: Article Content -->
    <div class="guide-content">
      <div class="article-top-label">Playbook Guide</div>
      
      <!-- Section 1 -->
      <div id="section-1" class="article-section scroll-animate">
        <h2 class="article-h2" style="margin-top: 0;">1. Before Sharing Your 1st Content</h2>
        <p class="article-p">Once you have your affiliate link, you can start sharing your first piece of content. But before doing so, please keep these in mind:</p>
        
        <!-- Callout box Remember -->
        <div class="callout-box emerald">
          <div class="callout-title">Remember:</div>
          <div class="callout-bullets">
            <div class="callout-row">
              <div class="callout-icon">
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              </div>
              <div class="callout-text">
                <strong>90%</strong> of our customers are dropshippers who use Shopify to run their ecommerce stores. They often engage in communities on Reddit, Discord, and courses, or search for related content using specific keywords.
              </div>
            </div>
          </div>
        </div>

        <ul class="article-list">
          <li class="article-p"><strong>Communities where they hang out:</strong> <code>r/dropship</code>, <code>r/shopify</code>, <code>r/dropshipping</code>, <code>r/ecommerce</code> (Reddit), or dropshipping Discord servers</li>
          <li class="article-p"><strong>Keywords they search:</strong> "how to start dropshipping 2026," "ads strategy for dropshipper," "how to track profit/manage PnL for Shopify store",...</li>
        </ul>
        
        <p class="article-p">So let's ask a simple question:</p>
        <div class="article-pullquote">
          "Why would they join those communities or watch that content?"
        </div>
        <p class="article-p">The answer is because they want to gather knowledge that could help them run their business better.</p>
      </div>

      <!-- Section 2 -->
      <div id="section-2" class="article-section scroll-animate">
        <h2 class="article-h2">2. Content Angles That Convert</h2>
        <p class="article-p">First, a quick warning:</p>

        <!-- Callout box Quick Warning -->
        <div class="callout-box warning">
          <div class="callout-title">Quick Warning:</div>
          <div class="callout-bullets">
            <div class="callout-row">
              <div class="callout-icon">
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              </div>
              <div class="callout-text">
                <strong>Spammy or vague content</strong> like <em>"Hey, if you want to succeed/make more money, use TrueProfit—here's the link"</em> will never work for our app.
              </div>
            </div>
          </div>
        </div>

        <p class="article-p"><strong>People only explore an app or tool when they see specific value that solves a current problem.</strong> So, start your content by calling out an issue or challenge they may have. This will capture their attention more effectively, for example:</p>

        <!-- Article Link Rows -->
        <div class="article-links">
          <a href="angles/track-profit-like-a-pro.html" class="article-link-row">
            <div class="article-link-text">
              <strong>Track Profit Like A Pro</strong>
              <span> — Casually frame the profit automation workflow</span>
            </div>
            <div class="article-link-arrow-wrapper">
              <svg class="article-link-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
            </div>
          </a>
          <a href="angles/scale-safely-with-margins.html" class="article-link-row">
            <div class="article-link-text">
              <strong>Scale Safely with Margins</strong>
              <span> — Deep-dive educational approach for paid ad operators</span>
            </div>
            <div class="article-link-arrow-wrapper">
              <svg class="article-link-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
            </div>
          </a>
          <a href="angles/stop-losing-30-profit.html" class="article-link-row">
            <div class="article-link-text">
              <strong>Stop Losing 30% Profit</strong>
              <span> — Real merchant style venting about Shopify processing fees</span>
            </div>
            <div class="article-link-arrow-wrapper">
              <svg class="article-link-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
            </div>
          </a>
        </div>

        <!-- Callout box Reference Note -->
        <div class="callout-box emerald">
          <div class="callout-title">Reference Note:</div>
          <div class="callout-bullets">
            <div class="callout-row">
              <div class="callout-icon">
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              </div>
              <div class="callout-text">
                <strong>These references</strong> are completely usable, but it's best to treat them as raw inspiration for how to approach our audience, then develop your own content based on what works best for your specific channels and audiences.
              </div>
            </div>
          </div>
        </div>

        <p class="article-p"><strong>Your next step?</strong> → Check out each Angle page for detailed content guidance.</p>
      </div>

      <!-- Section 3 -->
      <div id="section-3" class="article-section scroll-animate">
        <h2 class="article-h2">3. Build Your Audience</h2>
        <p class="article-p">Posting 1–2 pieces of content is a good start, and it might get you from a few hundred bucks here and there. But if you're aiming for a consistent <strong>$500–$1,000 monthly passive income</strong>, one-off content won't be enough.</p>
        <p class="article-p">You'll need to build active audiences or communities that actually care about what you post and say.</p>
        <p class="article-p">Once you have a loyal, engaged audience, there are many passive ways to promote. You can share valuable content and naturally include your affiliate link once or twice—and the traffic (and conversions) will come organically over time.</p>
      </div>
      
    </div>

    <!-- Right Column: Sticky Sidebar -->
    <div class="guide-sidebar">
      <!-- Progress Bar -->
      <div class="sidebar-progress">
        <div class="sidebar-progress-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        </div>
        <div class="sidebar-progress-text">
          Your progress
          <span>0 / 3 guides completed</span>
        </div>
      </div>

      <!-- TOC Menu -->
      <div class="sidebar-card">
        <div class="sidebar-card-title">On this page</div>
        <ul class="sidebar-toc">
          <li><a href="#section-1" class="active">Before Sharing Content</a></li>
          <li><a href="#section-2">Content Angles</a></li>
          <li><a href="#section-3">Build Your Audience</a></li>
        </ul>
      </div>

      <!-- CTA Card -->
      <div class="sidebar-card" style="background: #e6fbf1; border-color: rgba(35,196,140,0.3);">
        <div class="sidebar-card-title" style="color: #047857;">Start Earning</div>
        <p class="sidebar-cta-text">Get your affiliate link and start promoting TrueProfit today.</p>
        <a href="../index.html#dashboard-setup" class="sidebar-btn-primary">Get affiliate link</a>
        <a href="https://trueprofit.trackdesk.com/dashboard" target="_blank" class="sidebar-link">Affiliate Dashboard &rarr;</a>
      </div>
    </div>

  </div>
</section>

<!-- ==============================
     RELATED PLAYBOOKS
     ============================= -->
<section class="related-section">
  <div class="related-inner">
    <div class="related-header">
      <div class="related-label">More Playbooks</div>
      <h2 class="related-title">Continue with another guide</h2>
    </div>
    <div class="related-grid">
      <a class="related-card scroll-animate" href="discord-blueprint.html" style="transition-delay: 0.1s;">
        <span class="related-card-tag">Community</span>
        <h3 class="related-card-title">Discord &amp; Community Blueprint</h3>
        <p class="related-card-desc">Monetize Discord servers, Facebook groups, or ecommerce communities with natural mentions and AMAs.</p>
        <div class="related-card-footer">
          <div class="related-card-link">
            Read playbook
            <svg class="related-card-arrow" fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 24 24" width="14"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
          </div>
        </div>
      </a>
      <a class="related-card scroll-animate" href="tiktok-youtube-shorts.html" style="transition-delay: 0.2s;">
        <span class="related-card-tag">Video</span>
        <h3 class="related-card-title">TikTok &amp; YouTube Shorts</h3>
        <p class="related-card-desc">Hook frameworks, timelines, and creator strategies to drive traffic through vertical short-form video.</p>
        <div class="related-card-footer">
          <div class="related-card-link">
            Read playbook
            <svg class="related-card-arrow" fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 24 24" width="14"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
          </div>
        </div>
      </a>
    </div>
  </div>
</section>

<!-- ==============================
     BOTTOM CTA
     ============================= -->
<section class="guide-cta-section">
  <div class="guide-cta-inner">
    <h2 class="guide-cta-h2">Ready to <span>start promoting</span> TrueProfit?</h2>
    <p class="guide-cta-sub">Sign up for our affiliate program, grab your link, and start earning today.</p>
    <div class="guide-cta-btns">
      <a href="https://affiliate.trueprofit.io/sign-up" target="_blank" class="btn-cta-white">Sign Up Now &rarr;</a>
      <a href="https://trueprofit.trackdesk.com/dashboard" target="_blank" class="btn-cta-ghost">Go to Dashboard</a>
    </div>
  </div>
</section>

<!-- ==============================
     FOOTER
     ============================= -->
<footer>
  <div class="footer-inner">
    <div>
      <img src="../images/white_horizontal.svg" alt="TrueProfit Logo" style="height: 38px; width: auto; margin-bottom: 16px; display: block;">
      <div class="footer-tagline">Affiliate Resource Hub — everything you need to earn with TrueProfit.</div>
    </div>
    <div class="footer-links">
      <h5>Resources</h5>
      <a href="../guides.html">Guides</a>
      <a href="#">Creative Assets</a>
      <a href="../index.html#commission">Commission Calculator</a>
      <a href="https://trueprofit.trackdesk.com/dashboard" target="_blank">Affiliate Dashboard</a>
    </div>
    <div class="footer-links">
      <h5>TrueProfit</h5>
      <a href="https://trueprofit.io" target="_blank">Homepage</a>
      <a href="https://trueprofit.io/blog" target="_blank">Blog</a>
      <a href="https://trueprofit.io/partner/affiliate-program" target="_blank">Affiliate Program</a>
      <a href="mailto:partners@trueprofit.io">Contact</a>
    </div>
  </div>
  <div class="footer-bottom">
    <span>© 2026 TrueProfit. All rights reserved.</span>
    <span>Affiliate Resource Hub</span>
  </div>
</footer>

<script>
/* =========================================
   SCROLL INTERSECTION OBSERVER
   ========================================= */
document.addEventListener('DOMContentLoaded', () => {
  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animated');
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -10% 0px' });

  const scrollTargets = document.querySelectorAll('.scroll-animate');
  scrollTargets.forEach(el => observer.observe(el));
  
  /* =========================================
     STICKY TOC LINK HIGHLIGHTING
     ========================================= */
  const sections = document.querySelectorAll('.article-section');
  const tocLinks = document.querySelectorAll('.sidebar-toc a');
  
  function highlightTOC() {
    let scrollPos = window.scrollY || document.documentElement.scrollTop;
    
    // Add offset for sticky header
    scrollPos += 150;
    
    sections.forEach(sec => {
      const top = sec.offsetTop;
      const height = sec.offsetHeight;
      const id = sec.getAttribute('id');
      
      if (scrollPos >= top && scrollPos < top + height) {
        tocLinks.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === '#' + id) {
            link.classList.add('active');
          }
        });
      }
    });
  }
  
  window.addEventListener('scroll', highlightTOC);
  highlightTOC();
});
</script>

</body>
</html>
"""

# Combine head and body
full_html = head_content + body_html

# Ensure parent directory guides/ exists
os.makedirs(os.path.join(BASE, "guides"), exist_ok=True)

# Write output file
out_path = os.path.join(BASE, "guides", "general-guide.html")
with open(out_path, "w", encoding="utf-8") as f_out:
    f_out.write(full_html)

print(f"Assembled successfully and written to: {out_path}")
print(f"File size: {os.path.getsize(out_path)} bytes")
