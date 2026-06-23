import os
import re

BASE = r"c:\Users\khoadnd\Desktop\onboarding hub"
TEMPLATE_PATH = os.path.join(BASE, "guides", "general-guide.html")

# Read general-guide.html as template
with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
    template_html = f.read()

# ----------------- DISCORD BLUEPRINT LAYOUT GENERATOR -----------------

# Extract head CSS style block to append Discord-specific classes
discord_styles = """
/* Discord Guide specific styles */
.grid-2-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: center;
}
@media (max-width: 900px) {
  .grid-2-col { grid-template-columns: 1fr; gap: 40px; }
}
.mockup-card {
  background: var(--white);
  border-radius: var(--radius-lg);
  padding: 24px;
  box-shadow: var(--shadow-lg);
  border: 1px solid var(--border-light);
}
.mockup-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
}
.mockup-avatar {
  width: 40px;
  height: 40px;
  background: var(--green-bright);
  border-radius: 50%;
  flex-shrink: 0;
}
.mockup-name { font-weight: 700; color: var(--navy); font-size: 15px; }
.mockup-time { font-size: 12px; color: var(--text-muted); }
.mockup-body {
  font-size: 15px;
  color: var(--text-body);
  line-height: 1.6;
  background: var(--light-alt);
  padding: 16px;
  border-radius: 8px;
  font-style: italic;
  margin-bottom: 16px;
}
.mockup-footer {
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--green);
  text-align: right;
}
"""

discord_title = "Discord &amp; Community Blueprint — TrueProfit Affiliate Resource Hub"
discord_desc = "Learn how to promote TrueProfit inside ecommerce communities in a way that feels natural, helpful, and easy to replicate."

discord_hero_content = """<!-- ==============================
     HERO SECTION
     ============================== -->
<section class="guide-hero">
  <div class="guide-hero-inner">
    <div class="guide-hero-left stagger-enter" style="animation-delay: 0.1s;">
      <!-- Breadcrumb -->
      <div class="guide-breadcrumb">
        <a href="../index.html">Home</a><span class="sep">›</span><a href="../guides.html">Guides</a><span class="sep">›</span><span class="current">Discord Blueprint</span>
      </div>
      <!-- Title -->
      <h1 class="guide-hero-title">Discord Blueprint</h1>
      <!-- Subtitle -->
      <p class="guide-hero-subtitle">Learn how to promote TrueProfit inside ecommerce communities in a way that feels natural, helpful, and easy to replicate.</p>
      <!-- Tags -->
      <div class="guide-tags">
        <span class="guide-tag">Community</span>
        <span class="guide-tag">Discord</span>
        <span class="guide-tag">Affiliate Basics</span>
        <span class="guide-tag">Examples</span>
      </div>
      <!-- CTA Button -->
      <div class="guide-hero-btns">
        <a class="hero-btn-angles" href="#section-5">View Discord examples <svg class="hero-btn-arrow" fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 24 24" width="16"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg></a>
      </div>
    </div>
    <!-- Hero Illustration -->
    <div class="guide-hero-visual stagger-enter" style="animation-delay: 0.2s;">
      <img src="../images/2.svg" alt="Discord Blueprint" style="max-width: 440px; height: auto; object-fit: contain; background: transparent; border: none; box-shadow: none;">
    </div>
  </div>
</section>"""

discord_article_content = """<div class="article-top-label">Playbook Guide</div>
      
      <!-- Section 1 -->
      <div id="section-1" class="article-section scroll-animate">
        <h2 class="article-h2" style="margin-top: 0;">1. Introduction</h2>
        <p class="article-p">If you already own a Discord server or you’re planning to start one, this playbook is for you.</p>
        <p class="article-p">You don’t need ads, funnels, or a big audience. Discord works because it’s where people actually talk, ask questions, and share real experiences about ecommerce and dropshipping.</p>
        <p class="article-p">This page shows how affiliates promote TrueProfit on Discord in a way that feels natural, helpful, and easy to replicate.</p>
      </div>

      <!-- Section 2 -->
      <div id="section-2" class="article-section scroll-animate">
        <h2 class="article-h2">2. How to Set Things Up (Simple & Flexible)</h2>
        <p class="article-p">You don’t need a complex setup.</p>
        <p class="article-p">If you already have a Discord server, use (or create) a place where topics like profit, analytics, tools, or performance naturally belong.</p>
        <p class="article-p">If you’re planning to start a new Discord, you can build it around:</p>
        <ul class="article-list">
          <li class="article-p">Ecommerce or dropshipping discussions</li>
          <li class="article-p">Sharing wins, metrics, or mistakes</li>
          <li class="article-p">Learning how to scale more profitably</li>
        </ul>
        <p class="article-p">Once people start talking about performance, profit tracking naturally becomes relevant.</p>
        <p class="article-p">In both cases, the goal is the same: create a space where talking about numbers feels normal. From there, introducing TrueProfit is easy.</p>
      </div>

      <!-- Section 3 -->
      <div id="section-3" class="article-section scroll-animate">
        <h2 class="article-h2">3. Why Discord Works for TrueProfit</h2>
        <p class="article-p">Most ecommerce and dropshipping Discords exist to solve problems.</p>
        <p class="article-p">People talk about ads, scaling, suppliers, and tools — but many still don’t know their real net profit. They look at Shopify revenue or ROAS and assume things are fine, until margins quietly disappear.</p>
        <p class="article-p">That’s why profit tracking resonates so well on Discord.</p>
        <p class="article-p">When you bring this topic up, it doesn’t feel like promotion. It feels like you’re pointing out a blind spot and then sharing the tool that helps fix it. This applies whether you already run an active server or you’re planning to build one focused on ecommerce discussions.</p>
      </div>

      <!-- Section 4 -->
      <div id="section-4" class="article-section scroll-animate">
        <h2 class="article-h2">4. How to Talk About TrueProfit</h2>
        <p class="article-p">Start with the problem, not the product.</p>
        <p class="article-p">Many merchants don’t realize they can scale ads and still lose money. They trust revenue numbers and don’t see the full picture. When you mention this, people usually relate immediately.</p>
        <p class="article-p">After that, you can introduce TrueProfit as the tool that helps track real net profit in one place. At this point, sharing your affiliate link feels natural, not forced.</p>
        <p class="article-p">Just talk the way you normally talk in your Discord. Friendly, honest, and based on real experience works best.</p>
      </div>

      <!-- Section 5 -->
      <div id="section-5" class="article-section scroll-animate">
        <h2 class="article-h2">5. Real Examples from Discord Servers</h2>
        <p class="article-p">Both examples below use the same setup: <strong>a dedicated channel</strong> for profit tracking or tools.</p>
        <p class="article-p">What changes is <strong>how you introduce TrueProfit</strong>, not where you post it.</p>
        
        <h3 class="article-h3">Example 1: Educational / Problem-First Post</h3>
        <p class="article-p">In this example, the affiliate creates a channel focused on profit tracking or tools, then posts an educational message.</p>
        <p class="article-p">The post explains why many merchants don’t actually know their real profit and why relying on surface-level metrics is risky. TrueProfit is introduced as the tool that solves this problem, followed by the affiliate link.</p>
        <p class="article-p">This style works well when:</p>
        <ul class="article-list">
          <li class="article-p">Your server already has active ecommerce discussions</li>
          <li class="article-p">Members are used to longer, more educational messages</li>
          <li class="article-p">You want the channel to feel like a long-term resource</li>
        </ul>
        <p class="article-p">The message can be pinned and referenced whenever profit or margins come up.</p>
        <img src="../images/discord 1.webp" alt="Example 1: Educational / Problem-First Post" style="width: 100%; max-width: 720px; height: auto; display: block; margin: 40px auto; border: 3px solid #cbd5e1; border-radius: 12px; box-shadow: var(--shadow-md);">
        
        <h3 class="article-h3">Example 2: Personal Experience / Result-First Post</h3>
        <p class="article-p">Here, the affiliate still posts inside a <strong>dedicated profit-tracking channel</strong>, but opens with a short personal story.</p>
        <p class="article-p">Instead of explaining the problem in detail, the post jumps straight into experience: money wasted, time lost, or confusion around profit — and how TrueProfit solved it.</p>
        <p class="article-p">The affiliate link is placed naturally at the end, for anyone who wants to try the tool.</p>
        <p class="article-p">This style works well when:</p>
        <ul class="article-list">
          <li class="article-p">You want a shorter, more emotional message</li>
          <li class="article-p">You’re introducing the channel for the first time</li>
          <li class="article-p">You want to grab attention quickly without heavy explanation</li>
        </ul>
        <p class="article-p">Both examples work because the <strong>context is clear</strong>. Members expect content about profit in this channel, so the message never feels out of place.</p>
        <p class="article-p">Affiliates can start with either style and even mix both over time as long as everything lives inside the same dedicated channel.</p>
        <img src="../images/disord 2.webp" alt="Example 2: Personal Experience / Result-First Post" style="width: 100%; max-width: 720px; height: auto; display: block; margin: 40px auto; border: 3px solid #cbd5e1; border-radius: 12px; box-shadow: var(--shadow-md);">
      </div>

      <!-- Section 6 -->
      <div id="section-6" class="article-section scroll-animate">
        <h2 class="article-h2">6. Final Notes</h2>
        <p class="article-p">You don’t need a big audience or a perfect setup.</p>
        <p class="article-p">If you already have a Discord server, you can start with a single post.</p>
        <p class="article-p">If you’re planning to build one, profit tracking is a strong topic to anchor discussions around.</p>
        <p class="article-p">Focus on helping people understand their numbers better, and let TrueProfit be the natural solution you point them to.</p>
      </div>"""

discord_sidebar = """<!-- Right Column: Sticky Sidebar -->
    <div class="guide-sidebar">
      <!-- Progress Bar -->
      <div class="sidebar-progress">
        <div class="sidebar-progress-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        </div>
        <div class="sidebar-progress-text">
          Discord Blueprint
          <span>6 sections &middot; ~10 min read</span>
        </div>
      </div>

      <!-- TOC Menu -->
      <div class="sidebar-card">
        <div class="sidebar-card-title">On this page</div>
        <ul class="sidebar-toc">
          <li><a href="#section-1" class="active">Introduction</a></li>
          <li><a href="#section-2">How to Set Things Up</a></li>
          <li><a href="#section-3">Why Discord Works</a></li>
          <li><a href="#section-4">How to Talk About It</a></li>
          <li><a href="#section-5">Real Examples</a></li>
          <li><a href="#section-6">Final Notes</a></li>
        </ul>
      </div>

      <!-- CTA Card -->
      <div class="sidebar-card" style="background: #e6fbf1; border-color: rgba(35,196,140,0.3);">
        <div class="sidebar-card-title" style="color: #047857;">Start Earning</div>
        <p class="sidebar-cta-text">Get your affiliate link and start promoting TrueProfit today.</p>
        <a href="https://affiliate.trueprofit.io/sign-up" target="_blank" class="sidebar-btn-primary">Get affiliate link</a>
        <a href="https://trueprofit.trackdesk.com/dashboard" target="_blank" class="sidebar-link">Affiliate Dashboard &rarr;</a>
      </div>
    </div>"""

discord_related = """<section class="related-section">
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
</section>"""

discord_cta = """<section class="guide-cta-section">
  <div class="guide-cta-inner">
    <h2 class="guide-cta-h2">Ready to promote TrueProfit on <span>Discord</span>?</h2>
    <p class="guide-cta-sub">Create a dedicated channel, start sharing your experience, and watch your commissions grow.</p>
    <div class="guide-cta-btns">
      <a href="https://affiliate.trueprofit.io/sign-up" target="_blank" class="btn-cta-white">Get affiliate link &rarr;</a>
      <a href="https://trueprofit.trackdesk.com/dashboard" target="_blank" class="btn-cta-ghost">Go to Dashboard</a>
    </div>
  </div>
</section>"""


# ----------------- TIKTOK & SHORTS GENERATOR -----------------

shorts_styles = """
/* Hook visual panels styling */
.hook-visual-panel {
  display: grid;
  grid-template-columns: 55% 45%;
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
.hook-panel-img-col img {
  width: 100%;
  height: auto;
  border-radius: 12px;
  object-fit: cover;
  display: block;
  max-height: 340px;
}
.hook-panel-text-col {
  display: flex;
  flex-direction: column;
  gap: 16px;
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
  font-weight: 700;
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
  margin-top: 8px;
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
@media (max-width: 768px) {
  .hook-visual-panel {
    grid-template-columns: 1fr;
    padding: 24px;
    gap: 24px;
  }
  .hook-panel-img-col img {
    max-height: 240px;
  }
}

/* Responsive and premium tables styling */
.article-table-wrapper {
  overflow-x: auto;
  border-radius: 16px;
  border: 1px solid #DDE4F0;
  margin: 24px 0 40px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.04);
  background: #ffffff;
  -webkit-overflow-scrolling: touch;
  width: 100%;
  max-width: 100%;
}
.article-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 16px;
  min-width: 900px;
}
.article-table thead tr {
  background: #E9EDF7 !important;
}
.article-table th {
  background: #E9EDF7 !important;
  color: #0f172a;
  font-weight: 700;
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  padding: 18px 22px;
  text-align: left;
  border-bottom: 2px solid #DDE4F0;
  white-space: nowrap;
}
.article-table td {
  padding: 18px 22px;
  border-bottom: 1px solid #f1f5f9;
  vertical-align: top;
  line-height: 1.65;
  color: #374151;
}
.article-table tr:last-child td { border-bottom: none; }
.article-table tbody tr:hover td { background: #f0fdf4; }
.article-table td:first-child, .article-table th:first-child {
  font-weight: 700;
  color: #0f172a;
}

/* Scrollbar styling */
.article-table-wrapper::-webkit-scrollbar {
  height: 6px;
}
.article-table-wrapper::-webkit-scrollbar-track {
  background: #f1f5f9;
}
.article-table-wrapper::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 3px;
}

/* TikTok Mockup iframe styling */
.tiktok-video-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 36px auto;
  max-width: 300px;
}
.tiktok-video-placeholder {
  display: block;
  position: relative;
  width: 300px;
  aspect-ratio: 9 / 16;
  border-radius: 24px;
  border: 1px solid rgba(16, 185, 129, 0.45);
  overflow: hidden;
  background: transparent;
  box-shadow: 0 18px 45px rgba(15, 23, 42, 0.14);
  transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
  cursor: pointer;
}
.tiktok-video-placeholder:hover {
  transform: scale(1.025);
  border-color: rgba(16, 185, 129, 0.65);
  box-shadow: 0 24px 50px rgba(15, 23, 42, 0.18);
}
.tiktok-video-img {
  display: block;
  width: 100%;
  height: 100%;
  border: none;
  outline: none;
  box-shadow: none;
  filter: none;
  border-radius: inherit;
  object-fit: cover;
  object-position: center;
  transform: scale(1.03);
}
.tiktok-play-icon {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 64px;
  height: 64px;
  background: rgba(16, 185, 129, 0.8);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  transition: transform 0.25s ease, background 0.25s ease;
}
.tiktok-video-placeholder:hover .tiktok-play-icon {
  transform: translate(-50%, -50%) scale(1.1);
  background: rgba(16, 185, 129, 0.95);
}
.tiktok-caption-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-top: 16px;
  color: var(--green);
  font-size: 16px;
  font-weight: 700;
  text-decoration: none;
  transition: gap 0.2s ease;
}
.tiktok-caption-link:hover {
  text-decoration: underline;
  gap: 10px;
}
.video-intro-line {
  margin-bottom: 24px;
}
@media (min-width: 1024px) {
  .video-intro-line {
    white-space: nowrap;
    font-size: 19px;
  }
}
@media (max-width: 1023px) {
  .video-intro-line {
    white-space: normal;
  }
}
"""

shorts_title = "TikTok &amp; YouTube Shorts Strategy — TrueProfit Affiliate Resource Hub"
shorts_desc = "Learn how to create short-form content that drives views, builds trust, and converts without sounding promotional."

shorts_hero_content = """<!-- ==============================
     HERO SECTION
     ============================== -->
<section class="guide-hero">
  <div class="guide-hero-inner">
    <div class="guide-hero-left stagger-enter" style="animation-delay: 0.1s;">
      <!-- Breadcrumb -->
      <div class="guide-breadcrumb">
        <a href="../index.html">Home</a><span class="sep">›</span><a href="../guides.html">Guides</a><span class="sep">›</span><span class="current">TikTok &amp; YouTube Shorts</span>
      </div>
      <!-- Title -->
      <h1 class="guide-hero-title">TikTok &amp; YouTube Shorts</h1>
      <!-- Subtitle -->
      <p class="guide-hero-subtitle">Create short-form content that drives views, builds trust, and converts without sounding promotional.</p>
      <!-- Tags -->
      <div class="guide-tags">
        <span class="guide-tag">Video</span>
        <span class="guide-tag">Short-Form</span>
        <span class="guide-tag">Content Angles</span>
        <span class="guide-tag">Creator Workflow</span>
      </div>
      <!-- CTA Button -->
      <div class="guide-hero-btns">
        <a class="hero-btn-angles" href="#section-3">View content angles <svg class="hero-btn-arrow" fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 24 24" width="16"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg></a>
      </div>
    </div>
    <!-- Hero Illustration -->
    <div class="guide-hero-visual stagger-enter" style="animation-delay: 0.2s;">
      <img src="../images/3.svg" alt="TikTok &amp; YouTube Shorts" style="max-width: 440px; height: auto; object-fit: contain; background: transparent; border: none; box-shadow: none;">
    </div>
  </div>
</section>"""

shorts_article_content = """<div class="article-top-label">Playbook Guide</div>
      
      <!-- Section 1 -->
      <div id="section-1" class="article-section scroll-animate">
        <h2 class="article-h2" style="margin-top: 0;">1. Example</h2>
        <p class="article-p">Short-form video is one of the most powerful free channels for affiliate promotion — if you know how to structure it. The goal is not to promote TrueProfit directly. The goal is to surface a blind spot your audience already has and introduce TrueProfit as the tool that fixes it.</p>
        
        <p class="article-p video-intro-line">One of our partners created this video, and it earns him hundreds in monthly commission. &rarr;</p>
        
        <!-- TikTok-style vertical video placeholder -->
        <div class="tiktok-video-wrapper">
          <a class="tiktok-video-placeholder" href="https://www.tiktok.com/@whatifhoot/video/7601991913104755999" rel="noopener noreferrer" target="_blank">
            <img alt="TikTok thumbnail" class="tiktok-video-img" src="../images/15.svg"/>
            <div class="tiktok-play-icon">
              <svg fill="currentColor" height="22" viewBox="0 0 24 24" width="22">
                <polygon points="5 3 19 12 5 21 5 3"></polygon>
              </svg>
            </div>
          </a>
          <a class="tiktok-caption-link" href="https://www.tiktok.com/@whatifhoot/video/7601991913104755999" rel="noopener noreferrer" target="_blank">
            Watch original TikTok <span class="arrow">&rarr;</span>
          </a>
        </div>

        <p class="article-p">Notice what he does: he opens with a problem statement, not a product pitch. He explains why the problem matters in concrete terms (revenue vs. actual profit). Then he shows TrueProfit as the tool he personally uses to fix it — and the affiliate link is in the bio, mentioned naturally at the end.</p>
        <p class="article-p">This structure is repeatable. You don't need a viral video. You need a clear hook, a real problem, and a genuine recommendation.</p>
      </div>

      <!-- Section 2 -->
      <div id="section-2" class="article-section scroll-animate">
        <h2 class="article-h2">2. Why Short-Form Works for TrueProfit</h2>
        <p class="article-p">Short-form video surfaces problems fast. You have 3 seconds to hook someone — which forces you to lead with the exact pain your audience feels. For TrueProfit, that pain is clear: most Shopify merchants don't know their real net profit.</p>
        <p class="article-p">Revenue looks good. Ads are running. Orders are coming in. But after COGS, shipping, fees, refunds, and ad spend — the actual margin is a fraction of what people assume. This disconnect is exactly what TrueProfit solves, and it's the kind of insight that stops someone mid-scroll.</p>
        
        <!-- Callout box Quick Tip -->
        <div class="callout-box emerald">
          <div class="callout-title">Quick Tip:</div>
          <div class="callout-bullets">
            <div class="callout-row">
              <div class="callout-icon">
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              </div>
              <div class="callout-text">
                <strong>You don't need</strong> thousands of followers. A well-structured 30–45 second video with a strong hook and clear problem can reach thousands of ecommerce viewers organically — even on a new account — because the algorithm rewards watch time, not follower count.
              </div>
            </div>
          </div>
        </div>
        
        <p class="article-p">The other reason short-form works: the tool mention is brief. You're not doing a product review. You're solving a problem in the video itself, and TrueProfit is the natural next step for anyone who wants to go further. That positioning converts much better than a direct promotion.</p>
      </div>

      <!-- Section 3 -->
      <div id="section-3" class="article-section scroll-animate">
        <h2 class="article-h2">3. Content Angles You Could Use</h2>
        <p class="article-p">These are three proven hook structures that work well for promoting TrueProfit on TikTok and YouTube Shorts. Each one targets a slightly different viewer mindset. Start with whichever matches your style — you can rotate through all three over time.</p>
        
        <!-- Hook 1 -->
        <div class="hook-visual-panel">
          <div class="hook-panel-img-col">
            <img alt="Revenue Looks Good. Profit Doesn't." class="hook-panel-img" src="../images/hook_1_revenue_profit (1).svg"/>
          </div>
          <div class="hook-panel-text-col">
            <div class="hook-panel-eyebrow">Hook 1</div>
            <div class="hook-panel-title">Surface metric vs real profit</div>
            <div class="hook-panel-body">This hook works because it challenges the revenue number most merchants trust, then reframes net profit as the number that actually matters.</div>
            <div class="hook-panel-tags">
              <span class="hook-panel-tag">Beginners</span>
              <span class="hook-panel-tag">30–40s</span>
              <span class="hook-panel-tag">Calm but corrective</span>
            </div>
          </div>
        </div>

        <div class="article-table-wrapper">
          <table class="article-table">
            <thead>
              <tr>
                <th>Section</th>
                <th>What to Say / Script Guide</th>
                <th>What to Show</th>
                <th>Execution Notes</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Hook (0–3s)</td>
                <td>"Your Shopify store can be doing $30k a month and still barely make money."</td>
                <td>Face-on. Bold caption: <em>Revenue &ne; Profit</em></td>
                <td>Say it confidently. Pause half a second after.</td>
              </tr>
              <tr>
                <td>Problem (3–12s)</td>
                <td>"Most people only look at revenue and ROAS. But they forget fees, refunds, shipping, product costs, app subscriptions…"</td>
                <td>Text overlays listing hidden costs</td>
                <td>Quick cuts. Keep energy slightly rising.</td>
              </tr>
              <tr>
                <td>Insight (12–25s)</td>
                <td>"So when you scale, you might just be scaling thin margins without realizing it."</td>
                <td>Simple visual: Revenue &uarr; / Profit &darr;</td>
                <td>This is the “realization” moment. Slow down slightly.</td>
              </tr>
              <tr>
                <td>Mention TrueProfit (25–35s)</td>
                <td>Primary: "That’s why I don’t rely on Shopify’s dashboard. I track my real net profit inside TrueProfit."<br><br>Softer: "I use TrueProfit to see what’s actually left after everything."</td>
                <td>3–5 sec dashboard screen recording (blur numbers)</td>
                <td>Do NOT zoom into pricing. No feature tour. Just clarity visuals.</td>
              </tr>
              <tr>
                <td>CTA (35–40s)</td>
                <td>"If you want to see your real numbers clearly, link’s in the description."</td>
                <td>Minimal caption: <em>Link below</em></td>
                <td>Neutral tone. No hype.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Callout box Mistake 1 -->
        <div class="callout-box mistake">
          <div class="callout-title">Common Mistake:</div>
          <div class="callout-bullets">
            <div class="callout-row">
              <div class="callout-icon">
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              </div>
              <div class="callout-text">
                <strong>Saying "TrueProfit is the best profit tracking tool"</strong> — this sounds promotional and kills trust. Instead, describe what it shows you: real net profit after every cost. Let the result do the selling.
              </div>
            </div>
          </div>
        </div>

        <!-- Hook 2 -->
        <div class="hook-visual-panel">
          <div class="hook-panel-img-col">
            <img alt="Scaling Doesn't Always Mean More Profit" class="hook-panel-img" src="../images/hook_2_ad_spend_margin.svg"/>
          </div>
          <div class="hook-panel-text-col">
            <div class="hook-panel-eyebrow">Hook 2</div>
            <div class="hook-panel-title">Scaling can hide margin problems</div>
            <div class="hook-panel-body">This hook works for merchants running ads because it connects growth with cost pressure and makes profit tracking feel like an operator habit.</div>
            <div class="hook-panel-tags">
              <span class="hook-panel-tag">Paid ads operators</span>
              <span class="hook-panel-tag">35–45s</span>
              <span class="hook-panel-tag">Analytical</span>
            </div>
          </div>
        </div>

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
                <td>Hook</td>
                <td>"Scaling ads doesn’t automatically mean you’re making more money."</td>
                <td>Direct eye contact</td>
                <td>Deliver like a correction.</td>
              </tr>
              <tr>
                <td>Problem</td>
                <td>"When ad spend increases, your hidden costs increase too: CPM swings, refunds, transaction fees."</td>
                <td>Text overlays appearing quickly</td>
                <td>Keep pacing slightly faster here.</td>
              </tr>
              <tr>
                <td>Insight</td>
                <td>"If you’re not tracking net profit properly, you could be celebrating revenue while losing margin."</td>
                <td>Margin example breakdown</td>
                <td>Make it feel like operator logic.</td>
              </tr>
              <tr>
                <td>Mention TrueProfit</td>
                <td>Primary: "Before I increase the budget, I check my net profit in one place - I use TrueProfit."<br><br>Softer: "It pulls everything into one dashboard so I can make smarter decisions."</td>
                <td>Product-level profit view</td>
                <td>Show decision-making context, not homepage.</td>
              </tr>
              <tr>
                <td>CTA</td>
                <td>"If you’re running ads, you should be tracking this too."</td>
                <td>Caption: <em>Link in bio</em></td>
                <td>Position as best practice, not recommendation.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Callout box Mistake 2 -->
        <div class="callout-box mistake">
          <div class="callout-title">Common Mistake:</div>
          <div class="callout-bullets">
            <div class="callout-row">
              <div class="callout-icon">
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              </div>
              <div class="callout-text">
                <strong>Leading with "Let me show you an app"</strong> — this immediately frames the video as an ad. Lead with the insight (scaling ads doesn't automatically mean more profit) and let TrueProfit appear as evidence, not the subject.
              </div>
            </div>
          </div>
        </div>

        <!-- Hook 3 -->
        <div class="hook-visual-panel">
          <div class="hook-panel-img-col">
            <img alt="Before I Scale, I Check This One Number." class="hook-panel-img" src="../images/hook_3_net_profit.svg"/>
          </div>
          <div class="hook-panel-text-col">
            <div class="hook-panel-eyebrow">Hook 3</div>
            <div class="hook-panel-title">Check the number before scaling</div>
            <div class="hook-panel-body">This hook positions TrueProfit as part of a smarter decision-making workflow, not as a random app recommendation.</div>
            <div class="hook-panel-tags">
              <span class="hook-panel-tag">Experienced operators</span>
              <span class="hook-panel-tag">30–35s</span>
              <span class="hook-panel-tag">Instructional</span>
            </div>
          </div>
        </div>

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
                <td>Hook</td>
                <td>"Before I scale any product, I check this one number."</td>
                <td>Pause. Caption: <em>Not ROAS.</em></td>
                <td>Let curiosity build.</td>
              </tr>
              <tr>
                <td>Problem</td>
                <td>"Most people scale based on ROAS. That’s incomplete."</td>
                <td>Screenshot of ROAS metric</td>
                <td>Slightly shake head or subtle emphasis.</td>
              </tr>
              <tr>
                <td>Insight</td>
                <td>"The only number that matters is net profit after all costs."</td>
                <td>Highlight text: <em>Net Profit</em></td>
                <td>This is the authority moment.</td>
              </tr>
              <tr>
                <td>Mention TrueProfit</td>
                <td>Primary: "I track that inside TrueProfit so I don’t have to guess from spreadsheets."<br><br>Softer: "It consolidates all my costs into one view."</td>
                <td>Spreadsheet &rarr; cut &rarr; clean dashboard</td>
                <td>Show contrast. Keep it under 5 seconds.</td>
              </tr>
              <tr>
                <td>CTA</td>
                <td>"Link’s in bio if you want to check it out."</td>
                <td>Clean minimal caption</td>
                <td>No pressure tone.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Callout box Mistake 3 -->
        <div class="callout-box mistake">
          <div class="callout-title">Common Mistake:</div>
          <div class="callout-bullets">
            <div class="callout-row">
              <div class="callout-icon">
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              </div>
              <div class="callout-text">
                <strong>Spending more than 5–8 seconds</strong> talking about TrueProfit's features. The tool mention should feel like a natural part of your workflow — not a feature overview. Show clarity, not capabilities.
              </div>
            </div>
          </div>
        </div>

        <!-- Callout box Universal Rule -->
        <div class="callout-box warning">
          <div class="callout-title">Universal Rule:</div>
          <div class="callout-bullets">
            <div class="callout-row">
              <div class="callout-icon">
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              </div>
              <div class="callout-text">
                <strong>Tool mention = 5–8 seconds.</strong> Always tie it to YOUR workflow. Show clarity, not features. Never say "This is the best app." Never lead with "Let me show you an app."
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Section 4 -->
      <div id="section-4" class="article-section scroll-animate">
        <h2 class="article-h2">4. Creator Approaches</h2>
        
        <h3 class="article-h3">Already have a channel</h3>
        <p class="article-p">Keep your existing format. Don't change your style to accommodate TrueProfit — instead, find the natural moment where profit tracking fits your existing content. If you already talk about Shopify, scaling, or ecommerce tools, you can introduce one of the hooks above as a standalone video or weave it into a broader "tools I use" type of content.</p>
        <p class="article-p">The key is to show how you actually use TrueProfit to analyze real profit — not just name the tool. Showing your dashboard, even briefly, adds far more credibility than describing it.</p>
        
        <h3 class="article-h3">Building from scratch</h3>
        <p class="article-p">Stay niche: focus on Shopify and dropshipping. This audience is large, active, and constantly looking for practical insights. You don't need to be an expert — you need to be one step ahead of your viewer on a specific problem they're dealing with right now.</p>
        <p class="article-p">Start with short insight-driven content: one problem, one insight, one solution per video. If you're not comfortable on camera, start faceless — screen recordings with a voiceover work just as well for this type of content, and sometimes better because the focus stays on the data.</p>
        
        <!-- Callout box Quick Tip -->
        <div class="callout-box emerald">
          <div class="callout-title">Quick Tip:</div>
          <div class="callout-bullets">
            <div class="callout-row">
              <div class="callout-icon">
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              </div>
              <div class="callout-text">
                <strong>Post consistently</strong> for at least 30–60 days before evaluating results. Short-form video compounds slowly at first, then accelerates. One video earning steady commissions is worth more than 10 videos that spike once and fade.
              </div>
            </div>
          </div>
        </div>
      </div>"""

shorts_sidebar = """<!-- Right Column: Sticky Sidebar -->
    <div class="guide-sidebar">
      <!-- Progress Bar -->
      <div class="sidebar-progress">
        <div class="sidebar-progress-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        </div>
        <div class="sidebar-progress-text">
          TikTok &amp; YouTube Shorts
          <span>4 sections &middot; ~10 min read</span>
        </div>
      </div>

      <!-- TOC Menu -->
      <div class="sidebar-card">
        <div class="sidebar-card-title">On this page</div>
        <ul class="sidebar-toc">
          <li><a href="#section-1" class="active">Example</a></li>
          <li><a href="#section-2">Why Short-Form Works</a></li>
          <li><a href="#section-3">Content Angles</a></li>
          <li><a href="#section-4">Creator Approaches</a></li>
        </ul>
      </div>

      <!-- CTA Card -->
      <div class="sidebar-card" style="background: #e6fbf1; border-color: rgba(35,196,140,0.3);">
        <div class="sidebar-card-title" style="color: #047857;">Start Earning</div>
        <p class="sidebar-cta-text">Get your affiliate link and start promoting TrueProfit today.</p>
        <a href="https://affiliate.trueprofit.io/sign-up" target="_blank" class="sidebar-btn-primary">Get affiliate link</a>
        <a href="https://trueprofit.trackdesk.com/dashboard" target="_blank" class="sidebar-link">Affiliate Dashboard &rarr;</a>
      </div>
    </div>"""

shorts_related = """<section class="related-section">
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

shorts_cta = """<section class="guide-cta-section">
  <div class="guide-cta-inner">
    <h2 class="guide-cta-h2">Ready to create your first <span>short-form</span> affiliate content?</h2>
    <p class="guide-cta-sub">Start with one clear problem, turn it into a simple hook, and introduce TrueProfit naturally.</p>
    <div class="guide-cta-btns">
      <a href="https://affiliate.trueprofit.io/sign-up" target="_blank" class="btn-cta-white">Get affiliate link &rarr;</a>
      <a href="https://trueprofit.trackdesk.com/dashboard" target="_blank" class="btn-cta-ghost">Go to Dashboard</a>
    </div>
  </div>
</section>"""


# ----------------- REPLACEMENT ENGINE -----------------

def build_page(output_filename, title, desc, extra_styles, hero_html, article_html, sidebar_html, related_html, cta_html):
    html = template_html
    
    # 1. Replace Title & Description
    html = html.replace("<title>General Affiliate Guide — TrueProfit Affiliate Resource Hub</title>", f"<title>{title}</title>")
    html = html.replace('<meta name="description" content="Learn how to start promoting TrueProfit with the right audience, angle, and content approach.">', f'<meta name="description" content="{desc}">')
    
    # 2. Inject extra CSS inside the </style> tag
    style_end = html.find("</style>")
    if style_end != -1:
        html = html[:style_end] + extra_styles + html[style_end:]
    else:
        print("Error: Could not find </style> tag in template.")
        return
        
    # 3. Replace Hero Section
    # Find start and end of <section class="guide-hero">...</section>
    hero_start = html.find('<section class="guide-hero">')
    hero_end = html.find('</section>', hero_start) + len('</section>')
    if hero_start != -1 and hero_end != -1:
        html = html[:hero_start] + hero_html + html[hero_end:]
    else:
        print("Error: Could not find guide-hero section in template.")
        return
        
    # 4. Replace Left Column Article Content
    # Start: <div class="guide-content">
    # End: <!-- Right Column: Sticky Sidebar --> or <div class="guide-sidebar">
    art_start = html.find('<div class="guide-content">') + len('<div class="guide-content">')
    art_end = html.find('<!-- Right Column: Sticky Sidebar -->')
    if art_end == -1:
        art_end = html.find('<div class="guide-sidebar">')
        
    if art_start != -1 and art_end != -1:
        html = html[:art_start] + "\n      " + article_html + "\n\n    </div>\n\n    " + html[art_end:]
    else:
        print("Error: Could not find article content container in template.")
        return

    # 5. Replace Right Column Sidebar
    # Start: <!-- Right Column: Sticky Sidebar --> ... <div class="guide-sidebar">...
    # End: </div>\n\n  </div>\n</section> (before RELATED PLAYBOOKS section)
    sidebar_start = html.find('<!-- Right Column: Sticky Sidebar -->')
    if sidebar_start == -1:
        sidebar_start = html.find('<div class="guide-sidebar">')
        
    # Find the next </section> after sidebar_start
    section_end = html.find('</section>', sidebar_start)
    # The sidebar ends before the two closing divs of guide-body-inner and guide-body, followed by the </section>
    # So we'll look for the end of the sidebar wrapper. 
    # To be extremely safe, we can match:
    # </div>\n\n  </div>\n</section> or similar. Let's find the closing tag for the sidebar.
    # In general-guide.html:
    #     </div>\n  </div>\n</section>\n\n<!-- ==============================\n     RELATED PLAYBOOKS
    # Let's search for: </div>\n  </div>\n</section>
    tag_pattern = "  </div>\\n</section>"
    # Let's find the first occurrence of </div>\n  </div>\n</section> after sidebar_start
    # Note that there is:
    #   </div> <!-- end of sidebar -->
    #  </div> <!-- end of guide-body-inner -->
    # </section> <!-- end of guide-body -->
    # In template:
    #     </div>\n\n  </div>\n</section> (on line 2320-2323)
    # Let's search using simple string locate
    match_str = "    </div>\n\n  </div>\n</section>"
    pos = html.find(match_str, sidebar_start)
    if pos == -1:
        # Fallback to single newlines
        match_str = "    </div>\n  </div>\n</section>"
        pos = html.find(match_str, sidebar_start)
        
    if sidebar_start != -1 and pos != -1:
        html = html[:sidebar_start] + sidebar_html + "\n" + html[pos:]
    else:
        print("Error: Could not find sidebar end position in template.")
        return

    # 6. Replace Related Playbooks Section
    related_start = html.find('<!-- ==============================\n     RELATED PLAYBOOKS')
    if related_start == -1:
        related_start = html.find('<section class="related-section">')
        
    related_end = html.find('</section>', related_start) + len('</section>')
    if related_start != -1 and related_end != -1:
        html = html[:related_start] + related_html + html[related_end:]
    else:
        print("Error: Could not find related playbooks section.")
        return

    # 7. Replace Bottom CTA Section
    cta_start = html.find('<!-- ==============================\n     BOTTOM CTA')
    if cta_start == -1:
        cta_start = html.find('<section class="guide-cta-section">')
        
    cta_end = html.find('</section>', cta_start) + len('</section>')
    if cta_start != -1 and cta_end != -1:
        html = html[:cta_start] + cta_html + html[cta_end:]
    else:
        print("Error: Could not find bottom CTA section.")
        return

    # 8. Normalize newlines to match project files (using LF \n for consistency, no \r\n, no trailing mojibake)
    html = html.replace("\r\n", "\n")
    
    # Save the file
    out_path = os.path.join(BASE, "guides", output_filename)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
        
    print(f"Successfully generated {output_filename} ({len(html)} bytes)")


# Build Discord Blueprint
build_page(
    "discord-blueprint.html",
    discord_title,
    discord_desc,
    discord_styles,
    discord_hero_content,
    discord_article_content,
    discord_sidebar,
    discord_related,
    discord_cta
)

# Build TikTok & YouTube Shorts
build_page(
    "tiktok-youtube-shorts.html",
    shorts_title,
    shorts_desc,
    shorts_styles,
    shorts_hero_content,
    shorts_article_content,
    shorts_sidebar,
    shorts_related,
    shorts_cta
)
