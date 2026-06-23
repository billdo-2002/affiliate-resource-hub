import os
import re

BASE = r"c:\Users\khoadnd\Desktop\onboarding hub"
TEMPLATE_PATH = os.path.join(BASE, "guides", "general-guide.html")
OUTPUT_DIR = os.path.join(BASE, "guides", "angles")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Read general-guide.html as template
with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
    template_html = f.read()

# Normalize newlines to Unix LF
template_html = template_html.replace("\r\n", "\n")

# Replace relative paths: since these pages live in guides/angles/, all ../ references become ../../
# We can do this on the template first to update headers, menus, style.css, logo, etc.
template_html = template_html.replace("../", "../../")

# Define additional CSS and JS to inject into each page
additional_head_code = """
  /* Styles for Copy Post Box and Buttons */
  .copy-post-box {
    background: #F8FAFC;
    border: 1px solid var(--border-light);
    border-radius: 20px;
    padding: 38px;
    position: relative;
    margin: 24px 0 40px;
    font-family: inherit;
    font-size: 19px;
    line-height: 1.8;
    color: #1e293b;
    text-align: justify;
    transition: border-color 0.25s ease, box-shadow 0.25s ease;
  }
  .copy-post-box:hover {
    border-color: #10b981;
    box-shadow: 0 10px 30px rgba(16, 185, 129, 0.05);
  }
  .copy-post-box p {
    margin-bottom: 16px;
  }
  .copy-post-box p:last-child {
    margin-bottom: 0;
  }
  .copy-post-btn-wrapper {
    display: flex;
    justify-content: flex-end;
    margin-bottom: -20px;
    position: relative;
    z-index: 10;
  }
  .copy-post-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #e6fbf1;
    border: 1px solid #10b981;
    color: #047857;
    font-size: 13px;
    font-weight: 700;
    padding: 8px 16px;
    border-radius: 100px;
    cursor: pointer;
    transition: all 0.2s ease;
  }
  .copy-post-btn:hover {
    background: #d1fae5;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(16, 185, 129, 0.15);
  }
  .copy-post-btn:active {
    transform: translateY(0);
  }
  .affiliate-link-code-pill {
    background: #e6fbf1;
    border: 1px solid #a7f3d0;
    color: #047857;
    font-family: monospace;
    font-size: 15px;
    padding: 2px 6px;
    border-radius: 6px;
    font-weight: 600;
  }
  
  /* Article image effects */
  .article-in-post-img {
    width: 100%;
    border: 3px solid #cbd5e1;
    border-radius: 12px;
    transition: transform 0.3s ease, border-color 0.3s ease;
    box-shadow: var(--shadow-md);
    cursor: zoom-in;
    max-width: 720px;
    display: block;
    margin: 40px auto;
  }
  .article-in-post-img:hover {
    transform: scale(1.02);
    border-color: #10b981;
  }
"""

clipboard_script = """
<script>
function copyPostText(btn, elementId) {
  const text = document.getElementById(elementId).innerText.trim();
  navigator.clipboard.writeText(text).then(() => {
    const originalText = btn.innerHTML;
    btn.innerHTML = 'Copied!';
    btn.style.background = '#047857';
    btn.style.color = '#fff';
    btn.style.borderColor = '#047857';
    setTimeout(() => {
      btn.innerHTML = originalText;
      btn.style.background = '#e6fbf1';
      btn.style.color = '#047857';
      btn.style.borderColor = '#10b981';
    }, 2000);
  }).catch(err => {
    console.error('Failed to copy: ', err);
  });
}
</script>
"""

def build_angle_page(filename, title, description, hero_grid_cols, hero_img, breadcrumb_html, hero_title, hero_subtitle, tags_html, article_html, sidebar_progress_html, toc_html, related_html, cta_html):
    html = template_html
    
    # 1. Replace Title & Meta Description
    html = html.replace("<title>General Affiliate Guide — TrueProfit Affiliate Resource Hub</title>", f"<title>{title}</title>")
    html = html.replace('<meta name="description" content="Learn how to start promoting TrueProfit with the right audience, angle, and content approach.">', f'<meta name="description" content="{description}">')
    
    # 2. Inject Page Specific Head Style Overrides
    style_override = f"""{additional_head_code}
  .guide-hero-inner {{
    max-width: 1160px;
    margin: 0 auto;
    position: relative;
    z-index: 2;
    display: grid;
    grid-template-columns: {hero_grid_cols};
    gap: 32px;
    align-items: center;
    min-height: 340px;
  }}
"""
    style_end = html.find("</style>")
    if style_end != -1:
        html = html[:style_end] + style_override + html[style_end:]
    else:
        print("Error: Could not find </style> tag.")
        return
        
    # 3. Replace Hero Section
    # Find start and end of <section class="guide-hero">...</section>
    hero_start = html.find('<section class="guide-hero">')
    hero_end = html.find('</section>', hero_start) + len('</section>')
    
    new_hero_html = f"""<section class="guide-hero">
  <div class="guide-hero-inner">
    <div class="guide-hero-left stagger-enter" style="animation-delay: 0.1s;">
      <!-- Breadcrumb -->
      <div class="guide-breadcrumb">
        {breadcrumb_html}
      </div>
      <!-- Title -->
      <h1 class="guide-hero-title">{hero_title}</h1>
      <!-- Subtitle -->
      <p class="guide-hero-subtitle">{hero_subtitle}</p>
      <!-- Tags -->
      <div class="guide-tags">
        {tags_html}
      </div>
      <!-- CTA Button -->
      <div class="guide-hero-btns">
        <a class="hero-btn-angles" href="#why-does-this-happen">Read the angle below <svg class="hero-btn-arrow" fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 24 24" width="16"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg></a>
      </div>
    </div>
    <!-- Hero Illustration -->
    <div class="guide-hero-visual stagger-enter" style="animation-delay: 0.2s;">
      <img src="{hero_img}" alt="Angle Hero" style="width: 100%; max-width: 500px; max-height: 400px; object-fit: contain; background: transparent; box-shadow: none; border: none; border-radius: 0;">
    </div>
  </div>
</section>"""
    
    if hero_start != -1 and hero_end != -1:
        html = html[:hero_start] + new_hero_html + html[hero_end:]
    else:
        print("Error: Could not find guide-hero section.")
        return

    # 4. Replace Left Column Article Content
    art_start = html.find('<div class="guide-content">') + len('<div class="guide-content">')
    art_end = html.find('<!-- Right Column: Sticky Sidebar -->')
    if art_end == -1:
        art_end = html.find('<div class="guide-sidebar">')
        
    if art_start != -1 and art_end != -1:
        html = html[:art_start] + "\n      " + article_html + "\n\n    </div>\n\n    " + html[art_end:]
    else:
        print("Error: Could not find article content container.")
        return

    # 5. Replace Right Column Sidebar
    sidebar_start = html.find('<!-- Right Column: Sticky Sidebar -->')
    if sidebar_start == -1:
        sidebar_start = html.find('<div class="guide-sidebar">')
        
    match_str = "    </div>\n\n  </div>\n</section>"
    pos = html.find(match_str, sidebar_start)
    if pos == -1:
        match_str = "    </div>\n  </div>\n</section>"
        pos = html.find(match_str, sidebar_start)
        
    new_sidebar_html = f"""<!-- Right Column: Sticky Sidebar -->
    <div class="guide-sidebar">
      <!-- Progress Bar -->
      <div class="sidebar-progress">
        <div class="sidebar-progress-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        </div>
        {sidebar_progress_html}
      </div>

      <!-- TOC Menu -->
      <div class="sidebar-card">
        <div class="sidebar-card-title">On this page</div>
        <ul class="sidebar-toc">
          {toc_html}
        </ul>
      </div>

      <!-- CTA Card -->
      <div class="sidebar-card" style="background: #e6fbf1; border-color: rgba(35,196,140,0.3);">
        <div class="sidebar-card-title" style="color: #047857;">Start Earning</div>
        <p class="sidebar-cta-text">Get your affiliate link and start promoting TrueProfit today.</p>
        <a href="../../index.html#dashboard-setup" class="sidebar-btn-primary">Get affiliate link</a>
        <a href="https://trueprofit.trackdesk.com/dashboard" target="_blank" class="sidebar-link">Affiliate Dashboard &rarr;</a>
      </div>
    </div>"""

    if sidebar_start != -1 and pos != -1:
        html = html[:sidebar_start] + new_sidebar_html + "\n" + html[pos:]
    else:
        print("Error: Could not find sidebar end position.")
        return

    # 6. Replace Related Playbooks Section
    related_start = html.find('<section class="related-section">')
    related_end = html.find('</section>', related_start) + len('</section>')
    
    new_related_html = f"""<section class="related-section">
  <div class="related-inner">
    <div class="related-header">
      <div class="related-label">More Playbooks</div>
      <h2 class="related-title">Continue with another angle</h2>
    </div>
    <div class="related-grid">
      {related_html}
    </div>
  </div>
</section>"""

    if related_start != -1 and related_end != -1:
        html = html[:related_start] + new_related_html + html[related_end:]
    else:
        print("Error: Could not find related playbooks section.")
        return

    # 7. Replace Bottom CTA Section
    cta_start = html.find('<section class="guide-cta-section">')
    cta_end = html.find('</section>', cta_start) + len('</section>')
    
    new_cta_html = f"""<section class="guide-cta-section">
  <div class="guide-cta-inner">
    {cta_html}
  </div>
</section>"""

    if cta_start != -1 and cta_end != -1:
        html = html[:cta_start] + new_cta_html + html[cta_end:]
    else:
        print("Error: Could not find bottom CTA section.")
        return

    # 8. Inject Clipboard script right before </body> tag
    body_close = html.find("</body>")
    if body_close != -1:
        html = html[:body_close] + clipboard_script + "\n" + html[body_close:]
        
    # Write output file ensuring LF endings (\n)
    out_path = os.path.join(OUTPUT_DIR, filename)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f_out:
        f_out.write(html)
        
    print(f"Generated {filename} ({len(html)} bytes)")

# ==================== DATA FOR EACH PAGE ====================

# Common Breadcrumb elements
breadcrumb_pro = '<a href="../../index.html">Home</a><span class="sep">›</span><a href="../../guides.html">Guides</a><span class="sep">›</span><span class="current">Track Profit Like A Pro</span>'
breadcrumb_margins = '<a href="../../index.html">Home</a><span class="sep">›</span><a href="../../guides.html">Guides</a><span class="sep">›</span><span class="current">Scale Safely With Margins</span>'
breadcrumb_30 = '<a href="../../index.html">Home</a><span class="sep">›</span><a href="../../guides.html">Guides</a><span class="sep">›</span><span class="current">Stop Losing 30% Profit</span>'

# Related Cards templates
card_pro = """<a class="related-card scroll-animate" href="track-profit-like-a-pro.html" style="transition-delay: 0.1s;">
        <span class="related-card-tag">Content Angle</span>
        <h3 class="related-card-title">Track Profit Like A Pro</h3>
        <p class="related-card-desc">Casually frame the profit automation workflow for all types of merchants.</p>
        <div class="related-card-footer">
          <div class="related-card-link">
            Read playbook
            <svg class="related-card-arrow" fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 24 24" width="14"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
          </div>
        </div>
      </a>"""

card_margins = """<a class="related-card scroll-animate" href="scale-safely-with-margins.html" style="transition-delay: 0.1s;">
        <span class="related-card-tag">Content Angle</span>
        <h3 class="related-card-title">Scale Safely With Margins</h3>
        <p class="related-card-desc">Show scaling dropshippers why ROAS and revenue can hide silent margin killers.</p>
        <div class="related-card-footer">
          <div class="related-card-link">
            Read playbook
            <svg class="related-card-arrow" fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 24 24" width="14"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
          </div>
        </div>
      </a>"""

card_30 = """<a class="related-card scroll-animate" href="stop-losing-30-profit.html" style="transition-delay: 0.2s;">
        <span class="related-card-tag">Content Angle</span>
        <h3 class="related-card-title">Stop Losing 30% Profit</h3>
        <p class="related-card-desc">Help dropshippers identify and cut the hidden fees that eat up their real margins.</p>
        <div class="related-card-footer">
          <div class="related-card-link">
            Read playbook
            <svg class="related-card-arrow" fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 24 24" width="14"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
          </div>
        </div>
      </a>"""

# Common Bottom CTA content
bottom_cta_pro = """<h2 class="guide-cta-h2">Ready to use this angle in <span>your content?</span></h2>
    <p class="guide-cta-sub">Customize the example for your own audience, add your affiliate link naturally, and publish it where merchants already ask for help.</p>
    <div class="guide-cta-btns">
      <a href="https://affiliate.trueprofit.io/sign-up" target="_blank" class="btn-cta-white">Get affiliate link &rarr;</a>
      <a href="../../guides.html" class="btn-cta-ghost">Back to Guides</a>
    </div>"""

bottom_cta_margins = """<h2 class="guide-cta-h2">Ready to explain margins to <span>your audience?</span></h2>
    <p class="guide-cta-sub">Educate scaling merchants on net profit margin tracking, add your affiliate link, and share it on your blog or newsletter.</p>
    <div class="guide-cta-btns">
      <a href="https://affiliate.trueprofit.io/sign-up" target="_blank" class="btn-cta-white">Get affiliate link &rarr;</a>
      <a href="../../guides.html" class="btn-cta-ghost">Back to Guides</a>
    </div>"""

bottom_cta_30 = """<h2 class="guide-cta-h2">Ready to expose <span>hidden fees?</span></h2>
    <p class="guide-cta-sub">Share this raw, relatable merchant story on Reddit or Discord, and show how TrueProfit cuts down assumptions.</p>
    <div class="guide-cta-btns">
      <a href="https://affiliate.trueprofit.io/sign-up" target="_blank" class="btn-cta-white">Get affiliate link &rarr;</a>
      <a href="../../guides.html" class="btn-cta-ghost">Back to Guides</a>
    </div>"""

# ----------------- PAGE 1: track-profit-like-a-pro.html -----------------
article_pro = """<div class="article-top-label">Content Angle</div>
      
      <!-- ======== SECTION 1 ======== -->
      <div id="why-does-this-happen" class="article-section scroll-animate">
        <h2 class="article-h2" style="margin-top: 0;">1. Why does this happen? (The Pain Point)</h2>
        <p class="article-p">This angle can work for all types of merchants—especially those who haven’t heard of TrueProfit yet, or those who have but still need a strong reason to use it.</p>
        <p class="article-p">When it comes to net profit tracking, the day-to-day pain point isn’t “whether they know they should track net profit”—don’t misunderstand this. As an ecom expert, profit is the first thing merchants think about. The real problem is <em>how</em> they’re tracking it.</p>
        <p class="article-p">Right now, many merchants still rely on spreadsheets or simple calculations to estimate net profit and net margin. The upside is control, but the tradeoff often isn’t worth it: Shopify data changes every day (sometimes every hour), and spreadsheets don’t always reflect those changes. This leads to bigger issues:</p>
        
        <div class="callout-box warning">
          <div class="callout-title">The Spreadsheet Trap:</div>
          <div class="callout-bullets">
            <div class="callout-row">
              <div class="callout-icon">
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              </div>
              <div class="callout-text">
                <strong>Inaccurate numbers:</strong> Mis-tracked data that produces inaccurate net profit and net profit margin numbers.
              </div>
            </div>
            <div class="callout-row">
              <div class="callout-icon">
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              </div>
              <div class="callout-text">
                <strong>Time sink:</strong> To keep the sheet accurate, merchants have to spend a huge amount of time updating every cost column manually.
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ======== SECTION 2 ======== -->
      <div id="how-to-pitch" class="article-section scroll-animate">
        <h2 class="article-h2">2. How to pitch TrueProfit (The Solution)</h2>
        <p class="article-p">TrueProfit is built to solve the problems above, so mention it naturally as an effective solution for merchants tackling net profit tracking.</p>
        <p class="article-p">You can use the following hook to make your content more persuasive:</p>
        <div class="article-pullquote">
          "Running an ecom business is serious, and there are higher-value tasks merchants should spend time on - like strategy, planning, and ads - not sitting all day trying to keep a spreadsheet accurate. So isn't it a good thing if there's an app like TrueProfit that automates the entire tracking flow, so merchants can focus on what actually brings in the money?"
        </div>
      </div>

      <!-- ======== SECTION 3 ======== -->
      <div id="example-content" class="article-section scroll-animate">
        <h2 class="article-h2">3. Example Content</h2>
        <p class="article-p">Hey guys, just wanted to share something I recently discovered while desperately searching for a solution for my dropshipping store.</p>
        
        <div class="copy-post-btn-wrapper">
          <button class="copy-post-btn" onclick="copyPostText(this, 'copy-text-pro')">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right:4px;"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
            Copy post
          </button>
        </div>
        <div class="copy-post-box" id="copy-text-pro">
          <p>I started my store a few months back selling pet food. After some testing and trial and error, I managed to get it running smoothly with stable traffic and daily orders. But then I ran into another problem—figuring out exactly how much money my store was actually making.</p>
          <p>At first, I tried keeping it simple by checking Shopify reports for revenue and looking at my bills for costs, then calculating it in my head. But the numbers weren't matching up. So I created a spreadsheet with formulas to calculate profit. It worked, though it was still 10–15% off from what showed in my bank account. Acceptable, I guess. The real issue was the time it took—I can't sit there all day doing spreadsheets. I need to focus on strategy, planning, and ads—the stuff that actually keeps my store making money, you know?</p>
          <p>So I started looking for apps that could do the job for me. From all the search results, TrueProfit and TripleWhale came up the most. I tried TripleWhale but it wasn't for me, so I switched to TrueProfit—and so far it's been exactly what I needed. Revenue and orders are auto-synced, and there are features to set up COGS and shipping with custom rules (I sell globally, so shipping costs vary a lot). What's great is that I use AutoDS and Facebook Ads, and TrueProfit integrates with both platforms. Everything syncs in real-time between platforms—I just had to connect my accounts once. Can't believe I spent weeks doing everything manually in Google Sheets when apps like this exist.</p>
          <p>Got a link here <span class="affiliate-link-code-pill">[place your affiliate link here]</span> if anyone's having the same issue. Really great app, honestly.</p>
        </div>
      </div>"""

sidebar_prog_pro = """<div class="sidebar-progress-text">
          Track Profit Like A Pro
          <span>3 sections &middot; ~4 min read</span>
        </div>"""

toc_pro = """<li><a href="#why-does-this-happen" class="active">Why does this happen?</a></li>
          <li><a href="#how-to-pitch">How to pitch TrueProfit</a></li>
          <li><a href="#example-content">Example Content</a></li>"""

related_pro = card_margins + card_30

build_angle_page(
    "track-profit-like-a-pro.html",
    "Track Profit Like A Pro — TrueProfit Affiliate Resource Hub",
    "Learn how to casually frame the profit automation workflow for dropshippers and ecommerce store owners.",
    "1fr 500px",
    "../../images/22.svg",
    breadcrumb_pro,
    "Track Profit Like A Pro",
    "Casually frame the profit automation workflow for dropshippers and ecommerce store owners.",
    '<span class="guide-tag">Content Angle</span><span class="guide-tag">Automated Tracking</span><span class="guide-tag">Email &amp; Blog Copy</span>',
    article_pro,
    sidebar_prog_pro,
    toc_pro,
    related_pro,
    bottom_cta_pro
)

# ----------------- PAGE 2: scale-safely-with-margins.html -----------------
article_margins = """<div class="article-top-label">Content Angle</div>
      
      <!-- ======== SECTION 1 ======== -->
      <div id="why-does-this-happen" class="article-section scroll-animate">
        <h2 class="article-h2" style="margin-top: 0;">1. Why does this happen? (The Pain Point)</h2>
        <p class="article-p">This angle works especially well for merchants who are scaling and aren't aware of the importance of tracking accurate net profit.</p>
        <p class="article-p">Since we're talking about scaling merchants, these aren't newcomers to Shopify or dropshipping. They already have stores that are making money. Their issue is that they do track net profit, but not in the most efficient way (maybe they're still using spreadsheets). This isn't because they don't know TrueProfit is a better option—it's mainly because they don't have a strong enough reason to switch.</p>
      </div>

      <!-- ======== SECTION 2 ======== -->
      <div id="how-to-pitch" class="article-section scroll-animate">
        <h2 class="article-h2">2. How to pitch TrueProfit (The Solution)</h2>
        <p class="article-p">With this angle, it's better if you act like an expert and explain why it's critical for merchants to track their net profit accurately, especially when they're scaling. Here's a reference for educational content that can be shared on personal ecom blogs, sites, or newsletters.</p>
        
        <div class="callout-box warning">
          <div class="callout-title">The Scaling Trap:</div>
          <div class="callout-bullets">
            <div class="callout-row">
              <div class="callout-icon">
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              </div>
              <div class="callout-text">
                Acknowledge that a few chargebacks won’t kill a good store. But remind them that in a bad month, spikes in these fees will skew margins.
              </div>
            </div>
            <div class="callout-row">
              <div class="callout-icon">
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              </div>
              <div class="callout-text">
                If they don’t know <strong>why</strong> the margin dropped (because a spreadsheet doesn’t show hidden fees), they will make decisions based on blind assumptions.
              </div>
            </div>
            <div class="callout-row">
              <div class="callout-icon">
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              </div>
              <div class="callout-text">
                And chargebacks are only one type of cost. Add up untracked shipping variables, transaction fees, and refunds, and the total loss is massive.
              </div>
            </div>
          </div>
        </div>

        <p class="article-p">Tell them TrueProfit is among the best solutions to eliminate such assumptions. It automatically pulls every hidden fee so they know exactly what’s happening and can make data-driven decisions. Then, drop your affiliate link.</p>
      </div>

      <!-- ======== SECTION 3 ======== -->
      <div id="example-content" class="article-section scroll-animate">
        <h2 class="article-h2">3. Example Content</h2>
        <p class="article-p">Did you know that 99% of dropshippers can't scale if they have less than 5% net profit margin?</p>
        
        <div class="copy-post-btn-wrapper">
          <button class="copy-post-btn" onclick="copyPostText(this, 'copy-text-margins')">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right:4px;"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
            Copy post
          </button>
        </div>
        <div class="copy-post-box" id="copy-text-margins">
          <p>There's no need to explain the difference between a $10M revenue store and a $10K one—scaling matters to any business. But I've worked with many merchants and found that although they can be extremely talented at finding winning products or designing ad strategies, their mindset around scaling is often too simple.</p>
          <p>Many merchants I've worked with said that as long as they see a good signal on their ROAS, they'll start investing more to scale up. Others said they'll look for ways to scale once they have steady traffic and orders for 2–3 months or more. Both approaches have fair points, but they're far from enough.</p>
          <p>The main issue is that ROAS, orders, or even revenue are never good benchmarks to decide whether it's time to scale up an ecom store. These metrics only tell you how effective your ads are or how much money you're generating (without factoring in costs). They don't reflect your store's financial health. Knowing your store's financial health is the key to scaling tactics, and the only way to know how healthy your store is is to track your net profit and net profit margin.</p>
          <p>Net profit tells you exactly how profitable your business is. And profit margin gives you a basic benchmark to know whether it's time to scale up or reevaluate your numbers. Now back to the earlier question—why isn't 5% enough to scale? Because 5% is a very low profit margin compared to the 10–15% market benchmark. When your margin is too low, hidden costs can eat into your profit without you knowing. As a result, you keep scaling and keep losing money. That's why tracking net profit is so important.</p>
          <p>You can set up a spreadsheet system to calculate net profit or use apps to auto-track this in real time. If you go with apps, TrueProfit <span class="affiliate-link-code-pill">[place your affiliate link here]</span> is my recommendation. It's very easy to get used to (they have a great onboarding flow) and the data is usually more accurate (compared to Google Sheets).</p>
        </div>
      </div>"""

sidebar_prog_margins = """<div class="sidebar-progress-text">
          Scale Safely with Margins
          <span>3 sections &middot; ~4 min read</span>
        </div>"""

toc_margins = """<li><a href="#why-does-this-happen" class="active">Why does this happen?</a></li>
          <li><a href="#how-to-pitch">How to pitch TrueProfit</a></li>
          <li><a href="#example-content">Example Content</a></li>"""

related_margins = card_pro + card_30

build_angle_page(
    "scale-safely-with-margins.html",
    "Scale Safely with Margins — TrueProfit Affiliate Resource Hub",
    "Learn how to explain the importance of tracking accurate net profit to scaling ecommerce merchants.",
    "1fr 500px",
    "../../images/23.svg",
    breadcrumb_margins,
    "Scale Safely with Margins",
    "Deep-dive educational approach for paid ad operators who want to protect their margins while scaling.",
    '<span class="guide-tag">Content Angle</span><span class="guide-tag">Scale Strategy</span><span class="guide-tag">Paid Ads</span>',
    article_margins,
    sidebar_prog_margins,
    toc_margins,
    related_margins,
    bottom_cta_margins
)

# ----------------- PAGE 3: stop-losing-30-profit.html -----------------
article_30 = """<div class="article-top-label">Content Angle</div>
      
      <!-- ======== SECTION 1 ======== -->
      <div id="why-does-this-happen" class="article-section scroll-animate">
        <h2 class="article-h2" style="margin-top: 0;">1. Why does this happen? (The Pain Point)</h2>
        <p class="article-p">Everyone thinks profit is just <code>Revenue - Ads - COGS</code>. That’s BS. Most dropshippers miss the silent profit killers.</p>
        <p class="article-p">Look at the screenshot below. A merchant gets a fraud order, cancels it, and still eats a $55 processing fee. Then the scammer files a chargeback, and Shopify hits the merchant with <em>another</em> $15 fee while keeping the $55.</p>
        <p class="article-p"><strong>End result? Out $70 for an order they didn't even ship.</strong> Good luck tracking that in a simple Google Sheet. If merchants aren’t tracking these sneaky, overlapping fees, they’re faking their profit numbers.</p>
        
        <img src="../../images/20.png" class="article-in-post-img" alt="Hidden fees screenshot">
      </div>

      <!-- ======== SECTION 2 ======== -->
      <div id="how-to-pitch" class="article-section scroll-animate">
        <h2 class="article-h2">2. How to pitch TrueProfit (The Solution)</h2>
        <p class="article-p">Keep it casual but logical. Acknowledge that a few chargebacks won’t kill a good store. But remind them that in a bad month, spikes in these fees will skew margins. If they don’t know <em>why</em> the margin dropped (because a spreadsheet doesn’t show hidden fees), they will make decisions based on blind assumptions. And chargebacks are only one type of cost. Add up untracked shipping variables, transaction fees, and refunds, and the total loss is massive.</p>
        <p class="article-p">Tell them TrueProfit is among the best solutions to eliminate such assumptions. It automatically pulls every hidden fee so they know exactly what’s happening and can make data-driven decisions. Then, drop your affiliate link.</p>
      </div>

      <!-- ======== SECTION 3 ======== -->
      <div id="example-content" class="article-section scroll-animate">
        <h2 class="article-h2">3. Example Content</h2>
        <p class="article-p">This template sounds exactly like a real merchant venting on Reddit (r/dropship) or in a Discord server. It's raw, relatable, and logically bridges the problem to the app.</p>
        
        <div class="copy-post-btn-wrapper">
          <button class="copy-post-btn" onclick="copyPostText(this, 'copy-text-stop')">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right:4px;"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
            Copy post
          </button>
        </div>
        <div class="copy-post-box" id="copy-text-stop">
          <p><strong>Lost $70 on an order I didn’t even ship. Your Google Sheet profit is probably a lie 🤦‍♂️</strong></p>
          <p>I thought I was having a killer month until I checked my actual bank account. Let me tell you about Shopify's BS fees on fraud orders so you don’t bleed cash like I did.</p>
          <p>I got a $1,500 order. Shopify flagged it as fraud. Cool. I did the right thing, canceled it, and refunded it right away. But Shopify still kept a $55 processing fee. Annoying, but whatever.</p>
          <p>Then the scammer hit me with a chargeback. The chargeback canceled out my refund, and Shopify slapped me with ANOTHER $15 fee. And they still kept the original $55. So I’m down $70 for an order I caught as fraud and literally refused to ship.</p>
          <p>Look, I get it. If your store is running perfectly and chargebacks are low, these fees might not seem like a big deal. But what happens when you have a rough month and chargeback rates spike? Your profit margin tanks, and because your basic spreadsheet doesn’t show these hidden fees, you have no idea why. You start making wild guesses to fix it, maybe you cut ads, maybe you switch products, all based on blind assumptions. That’s the fastest way to kill your business.</p>
          <p>And remember, chargebacks are just ONE piece of the puzzle. Factor in fluctuating shipping rates, gateway transaction fees, and currency conversions. If you aren’t tracking every one of these tightly, the total amount of "hidden costs" will give you a heart attack at the end of the month.</p>
          <p>If you’re using a basic spreadsheet to track your profits (Revenue - Ads - COGS), you’re screwing yourself because spreadsheets can’t catch this stuff. You’re probably overestimating your take-home profit by 20-30%.</p>
          <p>I got sick of guessing and moved to a profit tracker that actually syncs directly with Shopify. It pulls every hidden fee automatically, so you know exactly what you’re making down to the penny, with no assumptions.</p>
          <p>If you want to stop scaling based on fake numbers, check out TrueProfit here: <span class="affiliate-link-code-pill">[Insert Your Affiliate Link]</span>. Ditch the spreadsheets before you scale a store that’s actually losing money.</p>
        </div>
      </div>"""

sidebar_prog_30 = """<div class="sidebar-progress-text">
          Stop Losing 30% Profit
          <span>3 sections &middot; ~4 min read</span>
        </div>"""

toc_30 = """<li><a href="#why-does-this-happen" class="active">Why does this happen?</a></li>
          <li><a href="#how-to-pitch">How to pitch TrueProfit</a></li>
          <li><a href="#example-content">Example Content</a></li>"""

related_30 = card_pro + card_margins

build_angle_page(
    "stop-losing-30-profit.html",
    "Stop Losing 30% Profit — TrueProfit Affiliate Resource Hub",
    "Learn how to show merchants how Shopify hidden fees can eat up 30% of their net margins.",
    "1fr 480px",
    "../../images/21.svg",
    breadcrumb_30,
    "Stop Losing 30% Profit",
    "Real merchant style venting about Shopify processing fees and hidden dropshipping costs.",
    '<span class="guide-tag">Content Angle</span><span class="guide-tag">Hidden Costs</span><span class="guide-tag">Reddit Copy</span>',
    article_30,
    sidebar_prog_30,
    toc_30,
    related_30,
    bottom_cta_30
)
