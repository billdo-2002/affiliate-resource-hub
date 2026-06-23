import os
import re

BASE = r"c:\Users\khoadnd\Desktop\onboarding hub"
TEMPLATE_ANGLE = os.path.join(BASE, "guides", "angles", "track-profit-like-a-pro.html")
TEMPLATE_VIDEO = os.path.join(BASE, "guides", "tiktok-youtube-shorts.html")
OUTPUT_DIR = os.path.join(BASE, "resources", "mcp")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Shared clipboard script to be injected before </body>
# We will make sure there is only one copyPostText script by stripping existing ones first
clipboard_script = """
<script>
function copyPostText(btn, elementId) {
  const el = document.getElementById(elementId);
  let text = "";
  const paragraphs = el.querySelectorAll('p');
  if (paragraphs.length > 0) {
    text = Array.from(paragraphs).map(p => p.innerText.trim()).join('\\n\\n');
  } else {
    text = el.innerText.trim();
  }
  
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

def clean_html_template(html):
    # Remove duplicate/existing copyPostText scripts to avoid duplicates
    html = re.sub(r'<script>\s*function\s+copyPostText.*?</script>', '', html, flags=re.DOTALL)
    # Normalize newlines
    html = html.replace("\r\n", "\n")
    return html

# =========================================================================
# 1. BUILD X/TWITTER READY-TO-POST PAGE
# =========================================================================
print("Generating x-twitter-ready-to-post.html...")
with open(TEMPLATE_ANGLE, "r", encoding="utf-8") as f:
    xt_html = clean_html_template(f.read())

# Replace Title & Meta Description
xt_html = xt_html.replace(
    "<title>Track Profit Like A Pro — TrueProfit Affiliate Resource Hub</title>",
    "<title>X/Twitter Ready-to-Post — TrueProfit Affiliate Resource Hub</title>"
)
xt_html = xt_html.replace(
    '<meta name="description" content="Casually frame the profit automation workflow for dropshippers and ecommerce store owners.">',
    '<meta name="description" content="Two ready-to-use MCP promotion angles for short, punchy X/Twitter content.">'
)

# Replace Breadcrumb
breadcrumb_old = """      <div class="guide-breadcrumb">
        <a href="../../index.html">Home</a><span class="sep">›</span><a href="../../guides.html">Guides</a><span class="sep">›</span><span class="current">Track Profit Like A Pro</span>
      </div>"""
breadcrumb_new = """      <div class="guide-breadcrumb">
        <a href="../../index.html">Home</a><span class="sep">›</span><a href="../../guides.html">Resources</a><span class="sep">›</span><a href="../../mcp-promotion.html">MCP Promotion</a><span class="sep">›</span><span class="current">X/Twitter Ready-to-Post</span>
      </div>"""
xt_html = xt_html.replace(breadcrumb_old, breadcrumb_new)

# Replace Hero Title & Subtitle & Tags
xt_html = xt_html.replace(
    '<h1 class="guide-hero-title">Track Profit Like A Pro</h1>',
    '<h1 class="guide-hero-title">X/Twitter Ready-to-Post</h1>'
)
xt_html = xt_html.replace(
    '<p class="guide-hero-subtitle">Casually frame the profit automation workflow for dropshippers and ecommerce store owners.</p>',
    '<p class="guide-hero-subtitle">Two ready-to-use MCP promotion angles for short, punchy X/Twitter content.</p>'
)

tags_old = """      <div class="guide-tags">
        <span class="guide-tag">Content Angle</span><span class="guide-tag">Automated Tracking</span><span class="guide-tag">Email &amp; Blog Copy</span>
      </div>"""
tags_new = """      <div class="guide-tags">
        <span class="guide-tag">MCP Promotion</span>
        <span class="guide-tag">X/Twitter</span>
        <span class="guide-tag">Ready-to-Post</span>
        <span class="guide-tag">Short Copy</span>
      </div>"""
xt_html = xt_html.replace(tags_old, tags_new)

# Replace Hero Visual Image
xt_html = xt_html.replace(
    '<img src="../../images/22.svg" alt="Angle Hero" style="width: 100%; max-width: 500px; max-height: 400px; object-fit: contain; background: transparent; box-shadow: none; border: none; border-radius: 0;">',
    '<img src="../../images/26.svg" alt="X/Twitter Ready-to-Post" style="width: 100%; max-width: 500px; max-height: 400px; object-fit: contain; background: transparent; box-shadow: none; border: none; border-radius: 0;">'
)

# Update Sidebar
sidebar_progress_old = """      <div class="sidebar-progress">
        <div class="sidebar-progress-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        </div>
        <div class="sidebar-progress-text">
          Track Profit Like A Pro
          <span>3 sections &middot; ~4 min read</span>
        </div>
      </div>"""
sidebar_progress_new = """      <div class="sidebar-progress">
        <div class="sidebar-progress-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        </div>
        <div class="sidebar-progress-text">
          X/Twitter Ready-to-Post
          <span>2 hooks &middot; ~5 min read</span>
        </div>
      </div>"""
xt_html = xt_html.replace(sidebar_progress_old, sidebar_progress_new)

sidebar_toc_old = """        <ul class="sidebar-toc">
          <li><a href="#why-does-this-happen" class="active">Why does this happen?</a></li>
          <li><a href="#how-to-pitch">How to pitch TrueProfit</a></li>
          <li><a href="#example-content">Example Content</a></li>
        </ul>"""
sidebar_toc_new = """        <ul class="sidebar-toc">
          <li><a href="#hook-1" class="active">Hook #1</a></li>
          <li><a href="#hook-2">Hook #2</a></li>
          <li><a href="#materials">Materials</a></li>
        </ul>"""
xt_html = xt_html.replace(sidebar_toc_old, sidebar_toc_new)

sidebar_cta_old = """      <div class="sidebar-card" style="background: #e6fbf1; border-color: rgba(35,196,140,0.3);">
        <div class="sidebar-card-title" style="color: #047857;">Start Earning</div>
        <p class="sidebar-cta-text">Get your affiliate link and start promoting TrueProfit today.</p>
        <a href="../../index.html#dashboard-setup" class="sidebar-btn-primary">Get affiliate link</a>
        <a href="https://trueprofit.trackdesk.com/dashboard" target="_blank" class="sidebar-link">Affiliate Dashboard &rarr;</a>
      </div>"""
sidebar_cta_new = """      <div class="sidebar-card" style="background: #e6fbf1; border-color: rgba(35,196,140,0.3);">
        <div class="sidebar-card-title" style="color: #047857;">Start Earning</div>
        <p class="sidebar-cta-text">Pick one post, customize it for your audience, and add your affiliate link naturally.</p>
        <a href="../../index.html#dashboard-setup" class="sidebar-btn-primary">Get affiliate link</a>
        <a href="https://trueprofit.trackdesk.com/dashboard" target="_blank" class="sidebar-link">Affiliate Dashboard &rarr;</a>
      </div>"""
xt_html = xt_html.replace(sidebar_cta_old, sidebar_cta_new)

# Replace Left Column Content
art_start = xt_html.find('<div class="guide-content">') + len('<div class="guide-content">')
art_end = xt_html.find('<!-- Right Column: Sticky Sidebar -->')
if art_end == -1:
    art_end = xt_html.find('<div class="guide-sidebar">')

article_content_xt = """
      <article class="article-body" id="post-examples">
        <div class="article-top-label" style="display:flex;align-items:center;gap:6px;">
          X/Twitter Post Formats
        </div>

        <section class="article-section" id="hook-1">
          <h2 class="article-h2" style="margin-top: 0;">Hook #1: 2am, no app, still got my numbers.</h2>
          <div class="callout-box emerald">
            <div class="callout-title" style="color: #047857;">Angle:</div>
            <div class="callout-bullets">
              <div class="callout-row">
                <div class="callout-icon" style="border-color: #047857; color: #047857;">
                  <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                </div>
                <div class="callout-text">
                  Video shows the actual Claude conversation pulling store data. Text sets up the relatable moment first, video does the rest.
                </div>
              </div>
            </div>
          </div>
          
          <div class="copy-post-btn-wrapper">
            <button class="copy-post-btn" onclick="copyPostText(this, 'copy-text-1')">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 4px;"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
              Copy Post
            </button>
          </div>
          <div class="copy-post-box" id="copy-text-1">
            <p>Couldn't sleep, started spiraling about whether this week was actually profitable or just high-revenue`</p>
            <p>Typed into claude: "How's my store doing vs last week"</p>
            <p>It just answered. real margin, ad efficiency, everything and pulled straight from TrueProfit</p>
            <p>It took 30 seconds.</p>
            <p>If you did not try TrueProfit, grab it here <strong class="text-emerald">[your affiliate link]</strong>. Don’t let your store data just sit in an app doing nothing, connect it to your AI and actually use it.</p>
          </div>
        </section>

        <section class="article-section" id="hook-2">
          <h2 class="article-h2">Hook #2: Revenue looked fine. Something was still wrong.</h2>
          <div class="callout-box emerald">
            <div class="callout-title" style="color: #047857;">Angle:</div>
            <div class="callout-bullets">
              <div class="callout-row">
                <div class="callout-icon" style="border-color: #047857; color: #047857;">
                  <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                </div>
                <div class="callout-text">
                  Root cause. Hits the gap between revenue and real profit. Works as a standalone observation.
                </div>
              </div>
            </div>
          </div>
          
          <div class="copy-post-btn-wrapper">
            <button class="copy-post-btn" onclick="copyPostText(this, 'copy-text-2')">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 4px;"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
              Copy Post
            </button>
          </div>
          <div class="copy-post-box" id="copy-text-2">
            <p>January: best revenue month ever</p>
            <p>Also January: margin quietly dropped 8 points</p>
            <p>Also January: found out because I asked my AI, not because my dashboard told me</p>
            <p>Shipping cost miscalculation. ~$340 in avoidable losses. 30 seconds to find.</p>
            <p>So… Getting TrueProfit here <strong class="text-emerald">[your affiliate link]</strong> and putting it to work with your AI. Your store data shouldn't just live in an app!!</p>
          </div>
        </section>

        <section class="article-section" id="materials">
          <h3 class="article-h3">Materials</h3>
          <ul class="article-list">
            <li><strong>Video:</strong> [material video] (Show the Claude/ChatGPT conversation pulling real store data)</li>
          </ul>
          <div class="material-note" style="text-align: center; font-style: italic; color: #64748b; font-size: 15px; margin-top: 20px;">
            *(We’re rushing to update some videos that you can use along the content to get a better conversion - be sure to stay active)*
          </div>
        </section>
      </article>
"""

xt_html = xt_html[:art_start] + article_content_xt + xt_html[art_end:]

# Replace Related section
related_old = """<section class="related-section">
  <div class="related-inner">
    <div class="related-header">
      <div class="related-label">More Playbooks</div>
      <h2 class="related-title">Continue with another angle</h2>
    </div>
    <div class="related-grid">
      <a class="related-card scroll-animate" href="scale-safely-with-margins.html" style="transition-delay: 0.1s;">
        <span class="related-card-tag">Content Angle</span>
        <h3 class="related-card-title">Scale Safely With Margins</h3>
        <p class="related-card-desc">Show scaling dropshippers why ROAS and revenue can hide silent margin killers.</p>
        <div class="related-card-footer">
          <div class="related-card-link">
            Read playbook
            <svg class="related-card-arrow" fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 24 24" width="14"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
          </div>
        </div>
      </a><a class="related-card scroll-animate" href="stop-losing-30-profit.html" style="transition-delay: 0.2s;">
        <span class="related-card-tag">Content Angle</span>
        <h3 class="related-card-title">Stop Losing 30% Profit</h3>
        <p class="related-card-desc">Help dropshippers identify and cut the hidden fees that eat up their real margins.</p>
        <div class="related-card-footer">
          <div class="related-card-link">
            Read playbook
            <svg class="related-card-arrow" fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 24 24" width="14"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
          </div>
        </div>
      </a>
    </div>
  </div>
</section>"""

related_new = """<section class="related-section">
  <div class="related-inner">
    <div class="related-header">
      <div class="related-label">MCP PROMOTION</div>
      <h2 class="related-title">Continue with another MCP resource</h2>
      <p style="font-size: 18px; color: var(--text-body); margin-top: 12px;">Choose another format to promote TrueProfit MCP naturally.</p>
    </div>
    <div class="related-grid">
      <a class="related-card scroll-animate" href="reddit-ready-to-post.html" style="transition-delay: 0.1s;">
        <span class="related-card-tag">Ready-to-Post</span>
        <h3 class="related-card-title">Reddit Ready-to-Post</h3>
        <p class="related-card-desc">Longer community-friendly MCP post angles for Reddit and ecommerce discussions.</p>
        <div class="related-card-footer">
          <div class="related-card-link">
            Read playbook
            <svg class="related-card-arrow" fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 24 24" width="14"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
          </div>
        </div>
      </a>
      <a class="related-card scroll-animate" href="short-form-video-guidelines.html" style="transition-delay: 0.2s;">
        <span class="related-card-tag">Guidelines</span>
        <h3 class="related-card-title">Short-Form Video Guidelines</h3>
        <p class="related-card-desc">Two video hook frameworks with script flow, what to show, and execution notes.</p>
        <div class="related-card-footer">
          <div class="related-card-link">
            Read playbook
            <svg class="related-card-arrow" fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 24 24" width="14"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
          </div>
        </div>
      </a>
    </div>
  </div>
</section>"""
xt_html = xt_html.replace(related_old, related_new)

# Replace Bottom CTA Section
cta_old = """<section class="guide-cta-section">
  <div class="guide-cta-inner">
    <h2 class="guide-cta-h2">Ready to use this angle in <span>your content?</span></h2>
    <p class="guide-cta-sub">Customize the example for your own audience, add your affiliate link naturally, and publish it where merchants already ask for help.</p>
    <div class="guide-cta-btns">
      <a href="https://affiliate.trueprofit.io/sign-up" target="_blank" class="btn-cta-white">Get affiliate link &rarr;</a>
      <a href="../../guides.html" class="btn-cta-ghost">Back to MCP Playbook</a>
    </div>
  </div>
</section>"""

cta_new = """<section class="guide-cta-section" style="background-image: linear-gradient(rgba(5, 29, 41, 0.6), rgba(5, 29, 41, 0.6)), url('../../images/10.svg');">
  <div class="guide-cta-inner">
    <h2 class="guide-cta-h2">Ready to post your first MCP angle?</h2>
    <p class="guide-cta-sub">Choose one hook, customize the copy, replace the affiliate link placeholder, and publish it on X/Twitter.</p>
    <div class="guide-cta-btns">
      <a href="https://affiliate.trueprofit.io/sign-up" target="_blank" class="btn-cta-white">Get affiliate link &rarr;</a>
      <a href="../../mcp-promotion.html" class="btn-cta-ghost">Back to MCP Playbook</a>
    </div>
  </div>
</section>"""
xt_html = xt_html.replace(cta_old, cta_new)

# Inject copy function before </body>
xt_html = xt_html.replace("</body>", clipboard_script + "\n</body>")

with open(os.path.join(OUTPUT_DIR, "x-twitter-ready-to-post.html"), "w", encoding="utf-8", newline="\n") as f:
    f.write(xt_html)
print("x-twitter-ready-to-post.html generated.")


# =========================================================================
# 2. BUILD REDDIT READY-TO-POST PAGE
# =========================================================================
print("Generating reddit-ready-to-post.html...")
with open(TEMPLATE_ANGLE, "r", encoding="utf-8") as f:
    rd_html = clean_html_template(f.read())

# Replace Title & Meta Description
rd_html = rd_html.replace(
    "<title>Track Profit Like A Pro — TrueProfit Affiliate Resource Hub</title>",
    "<title>Reddit Ready-to-Post — TrueProfit Affiliate Resource Hub</title>"
)
rd_html = rd_html.replace(
    '<meta name="description" content="Casually frame the profit automation workflow for dropshippers and ecommerce store owners.">',
    '<meta name="description" content="Longer community-friendly MCP post angles for Reddit and ecommerce discussions.">'
)

# Replace Breadcrumb
rd_html = rd_html.replace(breadcrumb_old, """      <div class="guide-breadcrumb">
        <a href="../../index.html">Home</a><span class="sep">›</span><a href="../../guides.html">Resources</a><span class="sep">›</span><a href="../../mcp-promotion.html">MCP Promotion</a><span class="sep">›</span><span class="current">Reddit Ready-to-Post</span>
      </div>""")

# Replace Hero Title & Subtitle & Tags
rd_html = rd_html.replace(
    '<h1 class="guide-hero-title">Track Profit Like A Pro</h1>',
    '<h1 class="guide-hero-title">Reddit Ready-to-Post</h1>'
)
rd_html = rd_html.replace(
    '<p class="guide-hero-subtitle">Casually frame the profit automation workflow for dropshippers and ecommerce store owners.</p>',
    '<p class="guide-hero-subtitle">Longer community-friendly MCP post angles for Reddit and ecommerce discussions.</p>'
)
rd_html = rd_html.replace(tags_old, """      <div class="guide-tags">
        <span class="guide-tag">MCP Promotion</span>
        <span class="guide-tag">Reddit</span>
        <span class="guide-tag">Ready-to-Post</span>
        <span class="guide-tag">Long Copy</span>
      </div>""")

# Replace Hero Visual Image
rd_html = rd_html.replace(
    '<img src="../../images/22.svg" alt="Angle Hero" style="width: 100%; max-width: 500px; max-height: 400px; object-fit: contain; background: transparent; box-shadow: none; border: none; border-radius: 0;">',
    '<img src="../../images/27.svg" alt="Reddit Ready-to-Post" style="width: 100%; max-width: 600px; max-height: 400px; object-fit: contain; background: transparent; box-shadow: none; border: none; border-radius: 0;">'
)

# Update Sidebar
rd_html = rd_html.replace(sidebar_progress_old, """      <div class="sidebar-progress">
        <div class="sidebar-progress-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        </div>
        <div class="sidebar-progress-text">
          Reddit Ready-to-Post
          <span>2 hooks &middot; ~6 min read</span>
        </div>
      </div>""")

rd_html = rd_html.replace(sidebar_toc_old, """        <ul class="sidebar-toc">
          <li><a href="#hook-1" class="active">Hook #1</a></li>
          <li><a href="#hook-2">Hook #2</a></li>
        </ul>""")

rd_html = rd_html.replace(sidebar_cta_old, sidebar_cta_new)

# Replace Left Column Content
article_content_rd = """
      <article class="article-body" id="post-examples">
        <div class="article-top-label" style="display:flex;align-items:center;gap:6px;">
          Reddit Post Formats
        </div>

        <section class="article-section" id="hook-1">
          <h2 class="article-h2" style="margin-top: 0;">Hook #1: Lost $340 in margin. I didn't have to lose and here's how I finally caught it.</h2>
          <div class="callout-box emerald">
            <div class="callout-title" style="color: #047857;">Angle:</div>
            <div class="callout-bullets">
              <div class="callout-row">
                <div class="callout-icon" style="border-color: #047857; color: #047857;">
                  <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                </div>
                <div class="callout-text">
                  Root cause, storytelling. (r/dropship, r/ecommerce). Numbers make it real with the $340 and the 8-point margin drop are the hook. Keep the TrueProfit mention casual, not the focus.
                </div>
              </div>
            </div>
          </div>
          
          <div class="copy-post-btn-wrapper">
            <button class="copy-post-btn" onclick="copyPostText(this, 'copy-text-1')">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 4px;"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2 2v1"></path></svg>
              Copy Post
            </button>
          </div>
          <div class="copy-post-box" id="copy-text-1">
            <p>January was my best revenue month since I started: around $28k in sales, ~380 orders. Should've been great. But when I looked at my actual bank at the end of the month, the number didn't make sense. Revenue was up maybe 18% vs December but profit had barely moved.</p>
            <p>Spent a couple evenings going through everything manually. ROAS looked fine. The refund rate was normal. Ad spend was actually down slightly. I couldn't find it.</p>
            <p>Eventually I just asked my AI directly: "why is my profit lower than last month despite higher revenue?", it cross-referenced my product-level COGS, shipping costs, and ad spend by SKU and flagged something I'd completely missed. One of my top sellers had a shipping cost that I'd set up wrong back in November and the real cost was $6.80 per order, I had $4.50 in the system. Across 180 orders that month, that's roughly $340 in margin I was never going to recover.</p>
            <p>Embarrassing that it took me that long to find, but also kind of insane that the AI found it in like 20 seconds by just looking across all the data at once.</p>
            <p>The feature is called MCP: basically connects TrueProfit directly to Claude or ChatGPT so it can pull your live store data without you having to feed it anything manually. If you're already on TrueProfit, it's worth setting up. I didn't know it existed until someone mentioned it in a thread here. Otherwise, just feel free to install the app <strong class="text-emerald">[your affiliate link]</strong> and get it connected with your AI now!</p>
          </div>
        </section>

        <section class="article-section" id="hook-2">
          <h2 class="article-h2">Hook #2: Stopped copy-pasting my store data into ChatGPT every time and there's a better way</h2>
          <div class="callout-box emerald">
            <div class="callout-title" style="color: #047857;">Angle:</div>
            <div class="callout-bullets">
              <div class="callout-row">
                <div class="callout-icon" style="border-color: #047857; color: #047857;">
                  <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                </div>
                <div class="callout-text">
                  Context-aware, workflow improvement. (r/entrepreneur, r/SideProject). The frustration of manual AI workflows is the hook and frame TrueProfit MCP as the fix you stumbled onto, not the point of the post.
                </div>
              </div>
            </div>
          </div>
          
          <div class="copy-post-btn-wrapper">
            <button class="copy-post-btn" onclick="copyPostText(this, 'copy-text-2')">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 4px;"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2 2v1"></path></svg>
              Copy Post
            </button>
          </div>
          <div class="copy-post-box" id="copy-text-2">
            <p>For the past few months I've been using ChatGPT and Claude to help me think through store performance like comparing weeks, figuring out which products to push, that kind of thing. It actually works pretty well but the workflow was painful.</p>
            <p>Every single conversation I had to start by pasting in a table of numbers, explaining what each column meant, walking it through my cost structure. One time I counted that I spent 11 minutes setting up context before I could even ask my actual question. For a 4-minute answer.</p>
            <p>A few weeks ago I found out TrueProfit has an MCP integration. You connect your account once and after that the AI has your live profit data automatically loaded every conversation. Revenue, real profit, COGS, ad spend by product and all of it, without you touching anything.</p>
            <p>The difference is pretty significant in practice. I went from "okay let me pull my numbers and format this properly" to just opening Claude and typing "how did last week compare to my monthly average" and getting a proper answer in 10 seconds.</p>
            <p>I do maybe 3–4 of these check-ins per week. Saving probably 30–40 minutes a week just on setup alone.</p>
            <p>Not a huge thing but if you're already on TrueProfit and you use AI for any kind of analysis, it's worth the 5 minutes to connect it. Otherwise, just feel free to download it <strong class="text-emerald">[your affiliate link]</strong> and connect with your AI!</p>
          </div>
        </section>
      </article>
"""

rd_html = rd_html[:art_start] + article_content_rd + rd_html[art_end:]

# Replace Related section and Bottom CTA
rd_html = rd_html.replace(related_old, related_new)

cta_rd_new = """<section class="guide-cta-section" style="background-image: linear-gradient(rgba(5, 29, 41, 0.6), rgba(5, 29, 41, 0.6)), url('../../images/10.svg');">
  <div class="guide-cta-inner">
    <h2 class="guide-cta-h2">Ready to post your first Reddit thread?</h2>
    <p class="guide-cta-sub">Choose one hook, customize the copy, replace the affiliate link placeholder, and publish it on Reddit.</p>
    <div class="guide-cta-btns">
      <a href="https://affiliate.trueprofit.io/sign-up" target="_blank" class="btn-cta-white">Get affiliate link &rarr;</a>
      <a href="../../mcp-promotion.html" class="btn-cta-ghost">Back to MCP Playbook</a>
    </div>
  </div>
</section>"""
rd_html = rd_html.replace(cta_old, cta_rd_new)

# Inject copy function before </body>
rd_html = rd_html.replace("</body>", clipboard_script + "\n</body>")

with open(os.path.join(OUTPUT_DIR, "reddit-ready-to-post.html"), "w", encoding="utf-8", newline="\n") as f:
    f.write(rd_html)
print("reddit-ready-to-post.html generated.")


# =========================================================================
# 3. BUILD SHORT-FORM VIDEO GUIDELINES PAGE
# =========================================================================
print("Generating short-form-video-guidelines.html...")
with open(TEMPLATE_VIDEO, "r", encoding="utf-8") as f:
    vid_html = clean_html_template(f.read())

# Replace relative paths: change "../" to "../../"
vid_html = vid_html.replace("../", "../../")

# Replace Title & Meta Description
vid_html = vid_html.replace(
    "<title>TikTok &amp; YouTube Shorts Strategy — TrueProfit Affiliate Resource Hub</title>",
    "<title>Short-Form Video Guidelines — TrueProfit Affiliate Resource Hub</title>"
)
vid_html = vid_html.replace(
    '<meta name="description" content="Create short-form content that drives views, builds trust, and converts without sounding promotional.">',
    '<meta name="description" content="Two ready-to-use short-form video hooks, visual scripts, and execution guidelines for promoting TrueProfit MCP.">'
)

# Replace Breadcrumb
breadcrumb_vid_old = """      <div class="guide-breadcrumb">
        <a href="../../index.html">Home</a><span class="sep">›</span><a href="../../guides.html">Guides</a><span class="sep">›</span><span class="current">TikTok &amp; YouTube Shorts</span>
      </div>"""
breadcrumb_vid_new = """      <div class="guide-breadcrumb">
        <a href="../../index.html">Home</a><span class="sep">›</span><a href="../../guides.html">Resources</a><span class="sep">›</span><a href="../../mcp-promotion.html">MCP Promotion</a><span class="sep">›</span><span class="current">Short-Form Video Guidelines</span>
      </div>"""
vid_html = vid_html.replace(breadcrumb_vid_old, breadcrumb_vid_new)

# Replace Hero Title & Subtitle & Tags
vid_html = vid_html.replace(
    '<h1 class="guide-hero-title">TikTok &amp; YouTube Shorts</h1>',
    '<h1 class="guide-hero-title">Short-Form Video Guidelines</h1>'
)
vid_html = vid_html.replace(
    '<p class="guide-hero-subtitle">Create short-form content that drives views, builds trust, and converts without sounding promotional.</p>',
    '<p class="guide-hero-subtitle">Two ready-to-use short-form video hooks, visual scripts, and execution guidelines for promoting TrueProfit MCP.</p>'
)

tags_vid_old = """      <div class="guide-tags">
        <span class="guide-tag">Video</span>
        <span class="guide-tag">Short-Form</span>
        <span class="guide-tag">Content Angles</span>
        <span class="guide-tag">Creator Workflow</span>
      </div>"""
tags_vid_new = """      <div class="guide-tags">
        <span class="guide-tag">MCP Promotion</span>
        <span class="guide-tag">Short-Form Video</span>
        <span class="guide-tag">TikTok &amp; Shorts</span>
        <span class="guide-tag">Video Scripts</span>
      </div>"""
vid_html = vid_html.replace(tags_vid_old, tags_vid_new)

# Replace Hero Visual Image
vid_html = vid_html.replace(
    '<img src="../../images/3.svg" alt="TikTok &amp; YouTube Shorts" style="max-width: 440px; height: auto; object-fit: contain; background: transparent; border: none; box-shadow: none;">',
    '<img src="../../images/28.svg" alt="Short-Form Video Guidelines" style="width: 100%; max-width: 550px; max-height: 400px; object-fit: contain; background: transparent; box-shadow: none; border: none; border-radius: 0; filter: drop-shadow(0px 10px 20px rgba(0,0,0,0.1));">'
)

# Update Sidebar
sidebar_progress_vid_old = """      <div class="sidebar-progress">
        <div class="sidebar-progress-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        </div>
        <div class="sidebar-progress-text">
          TikTok &amp; YouTube Shorts
          <span>4 sections &middot; ~10 min read</span>
        </div>
      </div>"""
sidebar_progress_vid_new = """      <div class="sidebar-progress">
        <div class="sidebar-progress-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        </div>
        <div class="sidebar-progress-text">
          Short-Form Video
          <span>2 scripts &middot; ~6 min read</span>
        </div>
      </div>"""
vid_html = vid_html.replace(sidebar_progress_vid_old, sidebar_progress_vid_new)

sidebar_toc_vid_old = """      <div class="sidebar-card">
        <div class="sidebar-card-title">On this page</div>
        <ul class="sidebar-toc">
          <li><a href="#section-1" class="active">Example</a></li>
          <li><a href="#section-2">Why Short-Form Works</a></li>
          <li><a href="#section-3">Content Angles</a></li>
          <li><a href="#section-4">Creator Approaches</a></li>
        </ul>
      </div>"""
sidebar_toc_vid_new = """      <div class="sidebar-card">
        <div class="sidebar-card-title">On this page</div>
        <ul class="sidebar-toc">
          <li><a href="#why-it-works" class="active">Why it works</a></li>
          <li><a href="#hook-1">Hook #1 Script</a></li>
          <li><a href="#hook-2">Hook #2 Script</a></li>
          <li><a href="#creator-approaches">Creator Approaches</a></li>
        </ul>
      </div>"""
vid_html = vid_html.replace(sidebar_toc_vid_old, sidebar_toc_vid_new)

sidebar_cta_vid_old = """      <div class="sidebar-card" style="background: #e6fbf1; border-color: rgba(35,196,140,0.3);">
        <div class="sidebar-card-title" style="color: #047857;">Start Earning</div>
        <p class="sidebar-cta-text">Get your affiliate link and start promoting TrueProfit today.</p>
        <a href="https://affiliate.trueprofit.io/sign-up" target="_blank" class="sidebar-btn-primary">Get affiliate link</a>
        <a href="https://trueprofit.trackdesk.com/dashboard" target="_blank" class="sidebar-link">Affiliate Dashboard &rarr;</a>
      </div>"""
sidebar_cta_vid_new = """      <div class="sidebar-card" style="background: #e6fbf1; border-color: rgba(35,196,140,0.3);">
        <div class="sidebar-card-title" style="color: #047857;">Start Earning</div>
        <p class="sidebar-cta-text">Choose a script hook, record your video, connect with your AI, and place your affiliate link in your bio.</p>
        <a href="https://affiliate.trueprofit.io/sign-up" target="_blank" class="sidebar-btn-primary">Get affiliate link</a>
        <a href="https://trueprofit.trackdesk.com/dashboard" target="_blank" class="sidebar-link">Affiliate Dashboard &rarr;</a>
      </div>"""
vid_html = vid_html.replace(sidebar_cta_vid_old, sidebar_cta_vid_new)

# Replace Left Column Content
vid_art_start = vid_html.find('<div class="guide-content">') + len('<div class="guide-content">')
vid_art_end = vid_html.find('<!-- Right Column: Sticky Sidebar -->')
if vid_art_end == -1:
    vid_art_end = vid_html.find('<div class="guide-sidebar">')

article_content_vid = """
      <article class="article-body">
        <div class="article-top-label">
          Short-Form Video Strategy
        </div>

        <section class="article-section" id="why-it-works">
          <h2 class="article-h2" style="margin-top: 0;">Why Short-Form Works for TrueProfit MCP</h2>
          <p class="article-p">MCP is a feature most merchants haven't heard of. "AI connected to your profit data" sounds abstract until someone sees it in action. Short-form video closes that gap in 30–40 seconds by showing a real use case, not explaining a concept.</p>
          
          <div class="hook-visual-panel">
            <div class="hook-panel-text-col">
              <div class="hook-panel-eyebrow">Visual Demonstration</div>
              <div class="hook-panel-title">AI connected to your profit data</div>
              <div class="hook-panel-body">
                Showing a real Claude conversation pulling store data makes the abstract value concrete in seconds.
              </div>
              <div class="hook-panel-tags">
                <span class="hook-panel-tag">Show Outcome</span>
                <span class="hook-panel-tag">AI Chat View</span>
              </div>
            </div>
            <div class="hook-panel-img-col">
              <div class="tiktok-video-wrapper" style="margin: 0;">
                <div class="tiktok-video-placeholder" style="width: 200px; height: 355px; border-radius: 16px;">
                  <img src="../../images/revenue_vs_profit.png" alt="Claude Chat Preview" class="tiktok-video-img">
                  <div class="tiktok-play-icon" style="width: 48px; height: 48px;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <p class="article-p">The hook isn't "here's a new feature." The hook is a problem merchants already feel: checking profit is slow, dashboards don't explain why numbers change, AI tools need manual data every time. Once they see the problem framed clearly, the solution sells itself.</p>
        </section>

        <section class="article-section" id="hook-1">
          <h2 class="article-h2">Hook #1: "I Asked AI How My Store Was Doing. It Actually Knew."</h2>
          <p class="article-p" style="font-size: 17px; color: var(--text-muted); margin-bottom: 24px;">This angle reframes store performance tracking around the surprising moment where AI already understands the store’s data with no setup or copy paste needed. It taps into the relatable late night "how is my store actually doing?" anxiety.</p>
          
          <div class="article-table-wrapper">
            <table class="article-table">
              <thead>
                <tr>
                  <th>Section</th>
                  <th>What to Say (Script Guide)</th>
                  <th>What to Show</th>
                  <th>Execution Notes</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Hook (0–3s)</strong></td>
                  <td>"I asked Claude how my store was doing this week and it actually knew."</td>
                  <td>Face-on. No caption needed.</td>
                  <td>Slight pause after "actually knew." Let curiosity land before moving on.</td>
                </tr>
                <tr>
                  <td><strong>Problem (3–12s)</strong></td>
                  <td>"Usually I'd open TrueProfit, check revenue, cross-reference ad spend, do the math myself. Every. Single. Time."</td>
                  <td>Quick cuts: Shopify tab &rarr; ads dashboard &rarr; spreadsheet</td>
                  <td>Keep energy slightly frustrated. Relatable, not dramatic.</td>
                </tr>
                <tr>
                  <td><strong>Insight (12–25s)</strong></td>
                  <td>"TrueProfit has an MCP integration now. Connect once, and your AI already has your live profit data loaded: every conversation, automatically."</td>
                  <td>Screen recording: Claude chat open, typing the question, answer appearing</td>
                  <td>Show the actual AI response. Blur store name/revenue if needed. This is the proof moment, slow down slightly.</td>
                </tr>
                <tr>
                  <td><strong>Mention TrueProfit MCP (25–35s)</strong></td>
                  <td>Primary: "I've been using TrueProfit for profit tracking, this just made it way more useful."<br><br>Softer: "Didn't even know this was possible until I set it up."</td>
                  <td>3–5s dashboard clip. Blur specific numbers.</td>
                  <td>Don't zoom in on pricing or features. Just enough to show it's real.</td>
                </tr>
                <tr>
                  <td><strong>CTA (35–40s)</strong></td>
                  <td>"Install it from the Shopify App Store and the link's in the description, and connect it to whatever AI you're already using."</td>
                  <td>Caption: <em>Link below</em></td>
                  <td>Neutral tone. No urgency, no pressure.</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <section class="article-section" id="hook-2">
          <h2 class="article-h2">Hook #2: "My Revenue Was Up. My Profit Wasn't. Here's How I Found Out Why."</h2>
          <p class="article-p" style="font-size: 17px; color: var(--text-muted); margin-bottom: 24px;">This angle targets the specific pain of revenue-profit mismatch, one of the most common and frustrating ecom moments. The AI enters as the tool that found the root cause fast.</p>
          
          <div class="article-table-wrapper">
            <table class="article-table">
              <thead>
                <tr>
                  <th>Section</th>
                  <th>What to Say</th>
                  <th>What to Show</th>
                  <th>Execution Notes</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Hook (0–3s)</strong></td>
                  <td>"Last month my revenue was up 18%. My actual profit was down $600. And I had no idea why."</td>
                  <td>Face-on. Bold caption: <strong>Revenue &ne; Profit</strong></td>
                  <td>Say it matter-of-fact. The numbers do the work, don't over-emote.</td>
                </tr>
                <tr>
                  <td><strong>Problem (3–15s)</strong></td>
                  <td>"ROAS looked fine. Refunds were normal. Ad spend was actually lower. I went through everything manually and still couldn't find it."</td>
                  <td>Text overlays: ROAS &check; Refunds &check; Ad spend &check; &rarr; then a question mark</td>
                  <td>Faster pace. Keep the energy of someone genuinely confused, not panicking.</td>
                </tr>
                <tr>
                  <td><strong>Insight (15–28s)</strong></td>
                  <td>"I opened Claude, asked it why my margin dropped last month, it pulled my TrueProfit data and cross-referenced everything. Flagged a shipping cost I'd had wrong for weeks. $340 in avoidable losses."</td>
                  <td>Screen recording: the actual AI response with root cause visible</td>
                  <td>This is the <em>aha</em> moment. Slow down. Let the number ($340) land before moving on.</td>
                </tr>
                <tr>
                  <td><strong>Mention TrueProfit MCP (28–38s)</strong></td>
                  <td>Primary: "TrueProfit connects to Claude or ChatGPT directly before I touch the ad budget, I ask it first."<br><br>Softer: "It's like having someone who already knows all your numbers."</td>
                  <td>Product-level profit view. Show one SKU breakdown.</td>
                  <td>Position as your standard operating practice, not a recommendation.</td>
                </tr>
                <tr>
                  <td><strong>CTA (38–45s)</strong></td>
                  <td>"It's on the Shopify App Store, grab it and connect it to your AI. Link in the description."</td>
                  <td>Caption: <em>Link in description</em></td>
                  <td>Confident, not pushy. One sentence, no elaboration needed.</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <section class="article-section">
          <div class="callout-box warning" style="border-left-color: #EF4444;">
            <div class="callout-title" style="color: #EF4444;">Universal Mention Rules (Common Mistakes to Avoid)</div>
            <div class="callout-bullets">
              <div class="callout-row">
                <div class="callout-icon" style="border-color: #EF4444; color: #EF4444;">
                  <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                </div>
                <div class="callout-text">Tool mention must be &le; 5–8 seconds. Keep it short.</div>
              </div>
              <div class="callout-row">
                <div class="callout-icon" style="border-color: #EF4444; color: #EF4444;">
                  <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                </div>
                <div class="callout-text">Always tie it to <strong>your workflow</strong>, not as a direct recommendation. Frame it as: "This is how I operate."</div>
              </div>
              <div class="callout-row">
                <div class="callout-icon" style="border-color: #EF4444; color: #EF4444;">
                  <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                </div>
                <div class="callout-text">Never say: "This is the best app" or "Let me show you an app." Focus on demonstrating clarity, not listing features.</div>
              </div>
            </div>
          </div>
        </section>

        <section class="article-section" id="creator-approaches">
          <h2 class="article-h2">Creator Approaches</h2>
          
          <h3 class="article-h3">If you already have a channel</h3>
          <ul class="article-list">
            <li>Keep your existing format — tutorials, ad breakdowns, ecommerce insights.</li>
            <li>Integrate TrueProfit naturally into your workflow instead of creating a standalone app review.</li>
            <li>If you use screen recordings, show how you analyze real profit.</li>
            <li>Show your face when possible — personal authority builds trust and improves conversion.</li>
          </ul>

          <h3 class="article-h3">If you're building a channel from scratch</h3>
          <ul class="article-list">
            <li>Stay niche: Shopify, dropshipping, ecommerce metrics.</li>
            <li>Focus on short, insight-driven content.</li>
            <li>Start faceless if you're not comfortable on camera.</li>
            <li>Prioritize clarity over production quality.</li>
          </ul>

          <h3 class="article-h3">Using AI to support production</h3>
          <p class="article-p">AI can speed up content creation without replacing your expertise. You can use:</p>
          <ul class="article-list">
            <li>AI avatar tools (like HeyGen) if you don't want to film yourself.</li>
            <li>AI voiceover tools for faceless videos.</li>
            <li>CapCut AI features or Descript for editing.</li>
            <li>Auto-caption tools to improve retention.</li>
            <li>AI assistance for drafting scripts before recording.</li>
          </ul>
          <p class="article-p" style="font-style: italic; color: var(--text-muted);">AI should optimize your workflow, not replace your thinking.</p>
        </section>
      </article>
"""

vid_html = vid_html[:vid_art_start] + article_content_vid + vid_html[vid_art_end:]

# Replace Related section
related_vid_old = """<section class="related-section">
  <div class="related-inner">
    <div class="related-header">
      <div class="related-label">More Playbooks</div>
      <h2 class="related-title">Continue with another guide</h2>
    </div>
    <div class="related-grid">
      <a class="related-card scroll-animate" href="general-guide.html" style="transition-delay: 0.1s;">
        <span class="related-card-tag">Core Path</span>
        <h3 class="related-card-title">General Affiliate Guide</h3>
        <p class="related-card-desc">The foundational playbook. Learn the core product value, who to target, and how to start making your first commissions.</p>
        <div class="related-card-footer">
          <div class="related-card-link">
            Read playbook
            <svg class="related-card-arrow" fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 24 24" width="14"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
          </div>
        </div>
      </a>
      <a class="related-card scroll-animate" href="discord-blueprint.html" style="transition-delay: 0.2s;">
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
    </div>
  </div>
</section>"""

related_vid_new = """<section class="related-section">
  <div class="related-inner">
    <div class="related-header">
      <div class="related-label">MCP PROMOTION</div>
      <h2 class="related-title">Continue with another MCP resource</h2>
      <p style="font-size: 18px; color: var(--text-body); margin-top: 12px;">Choose another format to promote TrueProfit MCP naturally.</p>
    </div>
    <div class="related-grid">
      <a class="related-card scroll-animate" href="x-twitter-ready-to-post.html" style="transition-delay: 0.1s;">
        <span class="related-card-tag">Ready-to-Post</span>
        <h3 class="related-card-title">X/Twitter Ready-to-Post</h3>
        <p class="related-card-desc">Two ready-to-use MCP promotion angles for short, punchy X/Twitter content.</p>
        <div class="related-card-footer">
          <div class="related-card-link">
            Read playbook
            <svg class="related-card-arrow" fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 24 24" width="14"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
          </div>
        </div>
      </a>
      <a class="related-card scroll-animate" href="reddit-ready-to-post.html" style="transition-delay: 0.2s;">
        <span class="related-card-tag">Ready-to-Post</span>
        <h3 class="related-card-title">Reddit Ready-to-Post</h3>
        <p class="related-card-desc">Longer community-friendly MCP post angles for Reddit and ecommerce discussions.</p>
        <div class="related-card-footer">
          <div class="related-card-link">
            Read playbook
            <svg class="related-card-arrow" fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 24 24" width="14"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
          </div>
        </div>
      </a>
    </div>
  </div>
</section>"""
vid_html = vid_html.replace(related_vid_old, related_vid_new)

# Replace Bottom CTA
cta_vid_old = """<section class="guide-cta-section">
  <div class="guide-cta-inner">
    <h2 class="guide-cta-h2">Ready to create your first <span>short-form</span> affiliate content?</h2>
    <p class="guide-cta-sub">Start with one clear problem, turn it into a simple hook, and introduce TrueProfit naturally.</p>
    <div class="guide-cta-btns">
      <a href="https://affiliate.trueprofit.io/sign-up" target="_blank" class="btn-cta-white">Get affiliate link &rarr;</a>
      <a href="https://trueprofit.trackdesk.com/dashboard" target="_blank" class="btn-cta-ghost">Go to Dashboard</a>
    </div>
  </div>
</section>"""

cta_vid_new = """<section class="guide-cta-section" style="background-image: linear-gradient(rgba(5, 29, 41, 0.6), rgba(5, 29, 41, 0.6)), url('../../images/16.svg');">
  <div class="guide-cta-inner">
    <h2 class="guide-cta-h2">Ready to create your first short-form video?</h2>
    <p class="guide-cta-sub">Choose a script hook, record your video, connect with your AI, and place your affiliate link in your bio.</p>
    <div class="guide-cta-btns">
      <a href="https://affiliate.trueprofit.io/sign-up" target="_blank" class="btn-cta-white">Get affiliate link &rarr;</a>
      <a href="../../mcp-promotion.html" class="btn-cta-ghost">Back to MCP Playbook</a>
    </div>
  </div>
</section>"""
vid_html = vid_html.replace(cta_vid_old, cta_vid_new)

with open(os.path.join(OUTPUT_DIR, "short-form-video-guidelines.html"), "w", encoding="utf-8", newline="\n") as f:
    f.write(vid_html)
print("short-form-video-guidelines.html generated.")

print("Batch 3 rebuild complete!")
