import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract head styles
styles_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
styles = styles_match.group(0) if styles_match else ''

# Extract header
header_match = re.search(r'<header id=\"header\".*?</header>', html, re.DOTALL)
header = header_match.group(0) if header_match else ''

# Extract footer
footer_match = re.search(r'<footer>.*?</footer>', html, re.DOTALL)
footer = footer_match.group(0) if footer_match else ''

# Extract hamburger menu scripts
hamburger_script = '''
document.getElementById('hamburgerBtn').addEventListener('click', function() {
  document.getElementById('header').classList.toggle('nav-open');
  const spans = this.querySelectorAll('span');
  if (document.getElementById('header').classList.contains('nav-open')) {
    spans[0].style.transform = 'rotate(45deg) translate(5px,5px)';
    spans[1].style.opacity = '0';
    spans[2].style.transform = 'rotate(-45deg) translate(5px,-5px)';
  } else {
    spans[0].style.transform = '';
    spans[1].style.opacity = '';
    spans[2].style.transform = '';
  }
});

/* close nav on link click */
document.querySelectorAll('#headerNav a').forEach(a => {
  a.addEventListener('click', () => {
    document.getElementById('header').classList.remove('nav-open');
    const spans = document.getElementById('hamburgerBtn').querySelectorAll('span');
    if(spans.length >= 3){
      spans[0].style.transform = ''; spans[1].style.opacity = ''; spans[2].style.transform = '';
    }
  });
});

document.querySelectorAll('.nav-dropdown-trigger').forEach(trigger => {
  trigger.addEventListener('click', (e) => {
    if (window.innerWidth <= 768) {
      e.preventDefault();
      const wrapper = trigger.closest('.nav-dropdown-wrapper');
      wrapper.classList.toggle('active');
    }
  });
});
'''

# Base page template
page_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Promote TrueProfit MCP | Affiliate Resource Hub</title>
<meta name="description" content="Promote TrueProfit MCP. Earn while AI takes over Ecom.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400&display=swap" rel="stylesheet">
{styles}
<style>
/* OVERRIDES FOR MCP PAGE */
:root {{
  --primary-dark: #0D1F2D;
  --accent-teal: #00C896;
  --secondary-dark: #1A3A4A;
  --text-white: #FFFFFF;
  --text-muted: #8B9BAA;
  --bg-light: #F8FFFE;
}}
body {{
  font-family: 'Inter', sans-serif;
}}
/* Override background dots */
.bg-dots-mcp {{
  background-color: var(--primary-dark);
  background-image: radial-gradient(circle, rgba(255,255,255,0.06) 1px, transparent 1px);
  background-size: 24px 24px;
}}
/* Override animations */
.stagger-enter {{
  opacity: 0;
  animation: fadeInSlideUp 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}}
.scroll-animate {{
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}}
.scroll-animate.animated {{
  opacity: 1;
  transform: translateY(0);
}}
/* Pulse dot */
.pulse-dot {{
  width: 8px;
  height: 8px;
  background: var(--accent-teal);
  border-radius: 50%;
  display: inline-block;
  animation: ping 2s cubic-bezier(0, 0, 0.2, 1) infinite;
}}
/* Hover cards */
.hover-card {{
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.2s ease;
}}
.hover-card:hover {{
  transform: translateY(-4px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.15);
}}
.content-card:hover {{
  border-color: var(--accent-teal);
  box-shadow: 0 0 15px rgba(0, 200, 150, 0.2);
}}
.btn-teal {{
  background: var(--accent-teal);
  color: #fff;
  border: none;
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s ease;
  text-decoration: none;
}}
.btn-teal:hover {{
  transform: translateY(-2px);
  box-shadow: 0 0 15px rgba(0, 200, 150, 0.4);
}}
.btn-outline {{
  background: transparent;
  color: var(--text-white);
  border: 1px solid rgba(255,255,255,0.2);
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.2s ease, color 0.2s ease;
  text-decoration: none;
}}
.btn-outline:hover {{
  border-color: var(--accent-teal);
  color: var(--accent-teal);
  transform: translateY(-2px);
}}
</style>
</head>
<body style="background: var(--primary-dark); color: var(--text-white);">
{header}

<!-- SECTION 1: HERO -->
<section id="hero-mcp" class="bg-dots-mcp" style="position: relative; overflow: hidden; padding: 100px 24px 80px; text-align: center;">
  <svg width="100%" height="100%" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" style="position: absolute; top: 0; left: 0; pointer-events: none; z-index: 0;" fill="none" class="hero-bg-svg">
    <defs>
      <linearGradient id="ribbonGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#00C896" />
        <stop offset="65%" stop-color="#0A5540" />
        <stop offset="100%" stop-color="#031F17" />
      </linearGradient>
    </defs>
    <path d="M -200 0 C 300 150, 400 150, 800 300 L 820 400 C 420 250, 320 250, -200 -100 Z" fill="url(#ribbonGrad1)" opacity="0.22" />
  </svg>
  
  <div style="position: relative; z-index: 2; max-width: 800px; margin: 0 auto;">
    <div class="stagger-enter" style="display: inline-flex; align-items: center; gap: 8px; background: rgba(0,200,150,0.1); border: 1px solid rgba(0,200,150,0.2); border-radius: 100px; padding: 6px 16px; font-size: 13px; font-weight: 600; color: var(--accent-teal); margin-bottom: 24px; animation-delay: 0.1s;">
      <span class="pulse-dot"></span>
      ⚡ NEW FEATURE
    </div>
    
    <h1 class="stagger-enter" style="font-size: clamp(40px, 6vw, 64px); font-weight: 800; line-height: 1.1; margin-bottom: 24px; animation-delay: 0.2s;">
      Promote TrueProfit <span style="color: var(--accent-teal);">MCP</span>.<br>
      Earn While <span style="color: var(--accent-teal);">AI</span> Takes Over Ecom.
    </h1>
    
    <p class="stagger-enter" style="font-size: 18px; color: var(--text-muted); line-height: 1.6; margin-bottom: 40px; animation-delay: 0.3s;">
      TrueProfit just launched MCP — a feature that connects live profit data directly to Claude and ChatGPT. It's new, it's hot, and most affiliates haven't touched it yet. That's your advantage.
    </p>
    
    <div class="stagger-enter" style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; margin-bottom: 60px; animation-delay: 0.4s;">
      <button class="btn-teal" onclick="document.getElementById('toolkit-section').scrollIntoView({{behavior: 'smooth'}})">See Promotion Toolkit ↓</button>
      <a href="https://trueprofit.io/solutions/mcp" target="_blank" class="btn-outline">Learn About MCP →</a>
    </div>
    
    <div class="stagger-enter" style="margin: 0 auto; width: 100%; max-width: 600px; height: 320px; background: var(--secondary-dark); border: 1px solid rgba(0,200,150,0.2); border-radius: 20px; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 40px rgba(0,200,150,0.1); animation-delay: 0.5s;">
      <span style="color: var(--text-muted); font-size: 14px;">[ Illustration coming soon ]</span>
    </div>
  </div>
</section>

<!-- SECTION 2: WHAT IS MCP -->
<section style="background: var(--bg-light); padding: 100px 24px; color: #000;">
  <div style="max-width: 1000px; margin: 0 auto;">
    <div class="scroll-animate" style="font-size: 12px; font-weight: 700; color: var(--accent-teal); text-transform: uppercase; margin-bottom: 12px; letter-spacing: 0.1em;">UNDERSTAND THE FEATURE</div>
    <h2 class="scroll-animate" style="font-size: clamp(32px, 4vw, 42px); font-weight: 800; color: var(--primary-dark); margin-bottom: 16px; line-height: 1.2; transition-delay: 0.1s;">Your store's profit data, inside the AI you already use</h2>
    <p class="scroll-animate" style="font-size: 16px; color: #475569; line-height: 1.6; max-width: 700px; margin-bottom: 24px; transition-delay: 0.2s;">
      MCP (Model Context Protocol) connects TrueProfit directly to Claude or ChatGPT. Merchants ask questions in plain language and get real answers — no dashboards, no copy-pasting numbers, no manual setup per conversation.
    </p>
    
    <div class="scroll-animate" style="display: flex; gap: 24px; margin-bottom: 60px; transition-delay: 0.3s;">
      <a href="https://trueprofit.io/solutions/mcp" target="_blank" style="color: var(--accent-teal); font-weight: 600; display: inline-flex; align-items: center; gap: 4px; text-decoration: none; position: relative;">Full feature details →<span style="position:absolute; bottom:-2px; left:0; width:0; height:1px; background:currentColor; transition: width 0.2s;"></span></a>
      <a href="https://helpdesk.trueprofit.io/en/articles/14086381-trueprofit-mcp-connect-trueprofit-to-chatgpt-claude-and-openclaw-clawdbot" target="_blank" style="color: var(--accent-teal); font-weight: 600; display: inline-flex; align-items: center; gap: 4px; text-decoration: none; position: relative;">Setup guide →<span style="position:absolute; bottom:-2px; left:0; width:0; height:1px; background:currentColor; transition: width 0.2s;"></span></a>
    </div>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px;">
      <div class="scroll-animate hover-card" style="background: #fff; border: 1px solid #E0F5EE; border-radius: 12px; padding: 24px; transition-delay: 0.1s;">
        <h3 style="font-size: 18px; font-weight: 700; color: var(--primary-dark); margin-bottom: 12px;">Instant Answers</h3>
        <p style="color: #475569; font-size: 14px; line-height: 1.6;">Ask about profit, costs, or performance anytime — no need to open the app or pull reports manually.</p>
      </div>
      <div class="scroll-animate hover-card" style="background: #fff; border: 1px solid #E0F5EE; border-radius: 12px; padding: 24px; transition-delay: 0.2s;">
        <h3 style="font-size: 18px; font-weight: 700; color: var(--primary-dark); margin-bottom: 12px;">Always Knows Your Numbers</h3>
        <p style="color: #475569; font-size: 14px; line-height: 1.6;">Connect once. After that, the AI already has your live store data loaded every time — no re-explaining needed.</p>
      </div>
      <div class="scroll-animate hover-card" style="background: #fff; border: 1px solid #E0F5EE; border-radius: 12px; padding: 24px; transition-delay: 0.3s;">
        <h3 style="font-size: 18px; font-weight: 700; color: var(--primary-dark); margin-bottom: 12px;">Finds the Root Cause</h3>
        <p style="color: #475569; font-size: 14px; line-height: 1.6;">Goes beyond 'what changed' to explain why — cross-referencing COGS, ad spend, fees, and refunds all at once.</p>
      </div>
      <div class="scroll-animate hover-card" style="background: #fff; border: 1px solid #E0F5EE; border-radius: 12px; padding: 24px; transition-delay: 0.4s;">
        <h3 style="font-size: 18px; font-weight: 700; color: var(--primary-dark); margin-bottom: 12px;">Works with Claude & ChatGPT</h3>
        <p style="color: #475569; font-size: 14px; line-height: 1.6;">Not locked to one AI tool. Merchants use whichever assistant they're already on.</p>
      </div>
    </div>
  </div>
</section>

<!-- SECTION 3: WHY PROMOTE NOW -->
<section style="background: var(--primary-dark); padding: 100px 24px;">
  <div style="max-width: 1000px; margin: 0 auto;">
    <div class="scroll-animate" style="font-size: 12px; font-weight: 700; color: var(--accent-teal); text-transform: uppercase; margin-bottom: 12px; letter-spacing: 0.1em;">AFFILIATE OPPORTUNITY</div>
    <h2 class="scroll-animate" style="font-size: clamp(32px, 4vw, 42px); font-weight: 800; color: #fff; margin-bottom: 40px; line-height: 1.2; transition-delay: 0.1s;">Early Feature. Early Mover. More Commission.</h2>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-bottom: 40px;">
      <div class="scroll-animate hover-card" style="background: var(--secondary-dark); border-left: 3px solid var(--accent-teal); border-radius: 12px; padding: 24px; transition-delay: 0.1s;">
        <h3 style="font-size: 18px; font-weight: 700; color: #fff; margin-bottom: 12px;">Brand New Feature</h3>
        <p style="color: var(--text-muted); font-size: 14px; line-height: 1.6;">Most affiliates haven't promoted it yet — you can own this angle</p>
      </div>
      <div class="scroll-animate hover-card" style="background: var(--secondary-dark); border-left: 3px solid var(--accent-teal); border-radius: 12px; padding: 24px; transition-delay: 0.2s;">
        <h3 style="font-size: 18px; font-weight: 700; color: #fff; margin-bottom: 12px;">Same <span class="countup-metric" data-countup="20" data-suffix="%">20%</span> Recurring</h3>
        <p style="color: var(--text-muted); font-size: 14px; line-height: 1.6;">Every merchant you refer keeps earning you commission month after month</p>
      </div>
      <div class="scroll-animate hover-card" style="background: var(--secondary-dark); border-left: 3px solid var(--accent-teal); border-radius: 12px; padding: 24px; transition-delay: 0.3s;">
        <h3 style="font-size: 18px; font-weight: 700; color: #fff; margin-bottom: 12px;">High Curiosity Right Now</h3>
        <p style="color: var(--text-muted); font-size: 14px; line-height: 1.6;">AI + profit tracking is a hot topic. MCP content gets organic reach</p>
      </div>
    </div>
    
    <p class="scroll-animate" style="font-size: 16px; color: var(--text-muted); line-height: 1.6; max-width: 800px; transition-delay: 0.4s;">
      MCP is the kind of feature people share because it surprises them. 'I asked Claude how my store was doing and it actually knew' is a hook that writes itself.
    </p>
  </div>
</section>

<!-- SECTION 4: PROMOTION TOOLKIT -->
<section id="toolkit-section" style="background: var(--bg-light); padding: 100px 24px; color: #000;">
  <div style="max-width: 1000px; margin: 0 auto;">
    <div class="scroll-animate" style="font-size: 12px; font-weight: 700; color: var(--accent-teal); text-transform: uppercase; margin-bottom: 12px; letter-spacing: 0.1em;">READY-TO-USE CONTENT</div>
    <h2 class="scroll-animate" style="font-size: clamp(32px, 4vw, 42px); font-weight: 800; color: var(--primary-dark); margin-bottom: 16px; line-height: 1.2; transition-delay: 0.1s;">Pick Your Channel. Start Posting.</h2>
    <p class="scroll-animate" style="font-size: 16px; color: #475569; line-height: 1.6; margin-bottom: 40px; transition-delay: 0.2s;">Each guide includes ready-to-post content and a short-form video script you can use immediately.</p>
    
    <div style="display: flex; flex-direction: column; gap: 24px;">
      <!-- Card 1 -->
      <div class="scroll-animate hover-card content-card" style="background: #fff; border: 1px solid #E0F5EE; border-radius: 16px; padding: 32px; display: flex; flex-wrap: wrap; gap: 32px; justify-content: space-between; align-items: center; transition-delay: 0.1s;">
        <div style="flex: 1; min-width: 280px;">
          <div style="display: inline-block; background: var(--primary-dark); color: #fff; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 100px; margin-bottom: 16px; letter-spacing: 0.05em;">X / TWITTER</div>
          <h3 style="font-size: 24px; font-weight: 700; color: var(--primary-dark); margin-bottom: 12px;">X/Twitter Ready-to-Post</h3>
          <p style="color: #475569; font-size: 15px; line-height: 1.6; margin-bottom: 20px;">2 ready-to-post content pieces crafted for X/Twitter. Copy, swap your link, post.</p>
          <div style="display: flex; gap: 8px; margin-bottom: 24px;">
            <span style="background: #F1F5F9; color: #475569; font-size: 12px; font-weight: 600; padding: 4px 10px; border-radius: 100px;">2 posts ready</span>
            <span style="background: #F1F5F9; color: #475569; font-size: 12px; font-weight: 600; padding: 4px 10px; border-radius: 100px;">Copy-paste</span>
          </div>
          <a href="resources/mcp/x-twitter-ready-to-post.html" class="btn-teal" style="padding: 10px 20px; font-size: 14px;">Open X/Twitter Guide →</a>
        </div>
        <div style="width: 200px; height: 140px; border-radius: 12px; background: linear-gradient(135deg, #1a1a2e, #16213e); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
          <span style="color: rgba(255,255,255,0.4); font-size: 13px;">[ Thumbnail ]</span>
        </div>
      </div>
      
      <!-- Card 2 -->
      <div class="scroll-animate hover-card content-card" style="background: #fff; border: 1px solid #E0F5EE; border-radius: 16px; padding: 32px; display: flex; flex-wrap: wrap; gap: 32px; justify-content: space-between; align-items: center; transition-delay: 0.2s;">
        <div style="flex: 1; min-width: 280px;">
          <div style="display: inline-block; background: var(--primary-dark); color: #fff; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 100px; margin-bottom: 16px; letter-spacing: 0.05em;">REDDIT</div>
          <h3 style="font-size: 24px; font-weight: 700; color: var(--primary-dark); margin-bottom: 12px;">Reddit Ready-to-Post</h3>
          <p style="color: #475569; font-size: 15px; line-height: 1.6; margin-bottom: 20px;">2 Reddit posts written in native community style. Drop into r/dropship, r/shopify, or similar subreddits.</p>
          <div style="display: flex; gap: 8px; margin-bottom: 24px;">
            <span style="background: #F1F5F9; color: #475569; font-size: 12px; font-weight: 600; padding: 4px 10px; border-radius: 100px;">2 posts ready</span>
            <span style="background: #F1F5F9; color: #475569; font-size: 12px; font-weight: 600; padding: 4px 10px; border-radius: 100px;">Community style</span>
          </div>
          <a href="resources/mcp/reddit-ready-to-post.html" class="btn-teal" style="padding: 10px 20px; font-size: 14px;">Open Reddit Guide →</a>
        </div>
        <div style="width: 200px; height: 140px; border-radius: 12px; background: linear-gradient(135deg, #1a0a0a, #2e1010); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
          <span style="color: rgba(255,255,255,0.4); font-size: 13px;">[ Thumbnail ]</span>
        </div>
      </div>
      
      <!-- Card 3 -->
      <div class="scroll-animate hover-card content-card" style="background: #fff; border: 1px solid #E0F5EE; border-radius: 16px; padding: 32px; display: flex; flex-wrap: wrap; gap: 32px; justify-content: space-between; align-items: center; transition-delay: 0.3s;">
        <div style="flex: 1; min-width: 280px;">
          <div style="display: inline-block; background: var(--primary-dark); color: #fff; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 100px; margin-bottom: 16px; letter-spacing: 0.05em;">TIKTOK / YOUTUBE SHORTS</div>
          <h3 style="font-size: 24px; font-weight: 700; color: var(--primary-dark); margin-bottom: 12px;">Short-Form Video Guidelines</h3>
          <p style="color: #475569; font-size: 15px; line-height: 1.6; margin-bottom: 20px;">2 complete hook-to-CTA video scripts with shot directions and execution notes. Works faceless or on-camera.</p>
          <div style="display: flex; gap: 8px; margin-bottom: 24px;">
            <span style="background: #F1F5F9; color: #475569; font-size: 12px; font-weight: 600; padding: 4px 10px; border-radius: 100px;">2 video scripts</span>
            <span style="background: #F1F5F9; color: #475569; font-size: 12px; font-weight: 600; padding: 4px 10px; border-radius: 100px;">Hook included</span>
          </div>
          <a href="resources/mcp/short-form-video-guidelines.html" class="btn-teal" style="padding: 10px 20px; font-size: 14px;">Open Video Guide →</a>
        </div>
        <div style="width: 200px; height: 140px; border-radius: 12px; background: linear-gradient(135deg, #0a0a1a, #101030); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
          <span style="color: rgba(255,255,255,0.4); font-size: 13px;">[ Thumbnail ]</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- SECTION 5: HOW TO TALK ABOUT MCP -->
<section style="background: var(--primary-dark); padding: 100px 24px;">
  <div style="max-width: 1000px; margin: 0 auto;">
    <div class="scroll-animate" style="font-size: 12px; font-weight: 700; color: var(--accent-teal); text-transform: uppercase; margin-bottom: 12px; letter-spacing: 0.1em;">MESSAGING GUIDE</div>
    <h2 class="scroll-animate" style="font-size: clamp(32px, 4vw, 42px); font-weight: 800; color: #fff; margin-bottom: 40px; line-height: 1.2; transition-delay: 0.1s;">The Angle That Works</h2>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 32px; margin-bottom: 40px;">
      <!-- DO -->
      <div class="scroll-animate" style="background: var(--secondary-dark); border-radius: 16px; padding: 32px; transition-delay: 0.2s;">
        <h3 style="font-size: 20px; font-weight: 700; color: #fff; margin-bottom: 24px;">Start with the problem</h3>
        <ul style="list-style: none; padding: 0; margin: 0;">
          <li style="display: flex; gap: 12px; margin-bottom: 16px;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--accent-teal)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-top: 2px;"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span style="color: var(--text-muted); font-size: 15px; line-height: 1.5;">Most merchants check revenue and think they're doing fine</span>
          </li>
          <li style="display: flex; gap: 12px; margin-bottom: 16px;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--accent-teal)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-top: 2px;"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span style="color: var(--text-muted); font-size: 15px; line-height: 1.5;">They don't see the real net profit until it's too late</span>
          </li>
          <li style="display: flex; gap: 12px; margin-bottom: 16px;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--accent-teal)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-top: 2px;"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span style="color: var(--text-muted); font-size: 15px; line-height: 1.5;">MCP makes that visible in seconds — just by asking</span>
          </li>
          <li style="display: flex; gap: 12px;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--accent-teal)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-top: 2px;"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span style="color: var(--text-muted); font-size: 15px; line-height: 1.5;">Position it as a blind spot fix, not a product pitch</span>
          </li>
        </ul>
      </div>
      
      <!-- DON'T -->
      <div class="scroll-animate" style="background: var(--secondary-dark); border-radius: 16px; padding: 32px; transition-delay: 0.3s;">
        <h3 style="font-size: 20px; font-weight: 700; color: #fff; margin-bottom: 24px;">Avoid these</h3>
        <ul style="list-style: none; padding: 0; margin: 0;">
          <li style="display: flex; gap: 12px; margin-bottom: 16px;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#EF4444" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-top: 2px;"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            <span style="color: var(--text-muted); font-size: 15px; line-height: 1.5;">Don't lead with 'Let me show you an app'</span>
          </li>
          <li style="display: flex; gap: 12px; margin-bottom: 16px;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#EF4444" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-top: 2px;"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            <span style="color: var(--text-muted); font-size: 15px; line-height: 1.5;">Don't say 'This is the best Shopify app'</span>
          </li>
          <li style="display: flex; gap: 12px; margin-bottom: 16px;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#EF4444" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-top: 2px;"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            <span style="color: var(--text-muted); font-size: 15px; line-height: 1.5;">Don't explain MCP technically — show the outcome</span>
          </li>
          <li style="display: flex; gap: 12px;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#EF4444" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-top: 2px;"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            <span style="color: var(--text-muted); font-size: 15px; line-height: 1.5;">Don't spend more than 5–8 seconds on the tool mention</span>
          </li>
        </ul>
      </div>
    </div>
    
    <div class="scroll-animate" style="background: rgba(255,255,255,0.03); border-left: 4px solid var(--accent-teal); border-radius: 8px; padding: 24px; transition-delay: 0.4s;">
      <p style="color: #E2E8F0; font-size: 15px; line-height: 1.6; margin: 0;">
        The hook isn't 'here's a new feature.' The hook is a problem merchants already feel: checking profit is slow, dashboards don't explain why numbers change, AI tools need manual data every time. Once they see the problem framed clearly, the solution sells itself.
      </p>
    </div>
  </div>
</section>

<!-- SECTION 6: CTA BLOCK -->
<section style="background: var(--primary-dark) url('trueprofit_affiliate_background.svg') no-repeat center/cover; padding: 100px 24px; text-align: center;">
  <div style="max-width: 800px; margin: 0 auto;">
    <h2 class="scroll-animate" style="font-size: clamp(32px, 4vw, 52px); font-weight: 900; color: #fff; margin-bottom: 16px; line-height: 1.1; letter-spacing: -0.04em;">
      Ready to promote TrueProfit <span style="color: var(--accent-teal);">MCP?</span>
    </h2>
    <p class="scroll-animate" style="font-size: 16px; color: rgba(255,255,255,0.5); line-height: 1.6; margin-bottom: 40px; transition-delay: 0.1s;">
      You have the toolkit. Now go create content that converts.
    </p>
    
    <div class="scroll-animate" style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; transition-delay: 0.2s;">
      <a href="guides.html" style="display: inline-flex; align-items: center; gap: 8px; background: #fff; color: var(--primary-dark); font-weight: 700; font-size: 14px; padding: 12px 26px; border-radius: 8px; text-decoration: none; transition: transform 0.2s ease, background 0.2s ease;">
        Open the Playbook →
      </a>
      <a href="https://trueprofit.trackdesk.com/dashboard" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: transparent; border: 1.5px solid rgba(255,255,255,0.2); color: #fff; font-weight: 600; font-size: 14px; padding: 12px 26px; border-radius: 8px; text-decoration: none; transition: transform 0.2s ease, border-color 0.2s ease;">
        Get My Affiliate Link →
      </a>
    </div>
  </div>
</section>

{footer}

<script>
{hamburger_script}

/* Scroll Animations */
document.addEventListener('DOMContentLoaded', () => {{
  const observer = new IntersectionObserver((entries, obs) => {{
    entries.forEach(entry => {{
      if (entry.isIntersecting) {{
        entry.target.classList.add('animated');
        obs.unobserve(entry.target);
        if (entry.target.hasAttribute('data-countup') || entry.target.classList.contains('countup-metric')) {{
          startCountUp(entry.target);
        }}
      }}
    }});
  }}, {{ threshold: 0.1, rootMargin: '0px 0px -10% 0px' }});

  document.querySelectorAll('.scroll-animate').forEach(el => {{
    observer.observe(el);
  }});
  
  function easeOutCubic(t) {{ return 1 - Math.pow(1 - t, 3); }}
  
  function startCountUp(el) {{
    if (el.dataset.countingUp === 'true') return;
    el.dataset.countingUp = 'true';
    
    const endValStr = el.getAttribute('data-countup') || el.textContent.replace(/[^0-9]/g, '');
    const endVal = parseInt(endValStr, 10);
    if (isNaN(endVal)) {{
      el.dataset.countingUp = 'false';
      return;
    }}
    
    const prefix = el.getAttribute('data-prefix') || (el.textContent.includes('$') ? '$' : '');
    const suffix = el.getAttribute('data-suffix') || (el.textContent.includes('%') ? '%' : '');
    const duration = 1500;
    const startTime = performance.now();
    
    function update(currentTime) {{
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const currentVal = Math.floor(endVal * easeOutCubic(progress));
      el.textContent = prefix + currentVal.toLocaleString() + suffix;
      
      if (progress < 1) {{
        requestAnimationFrame(update);
      }} else {{
        el.textContent = prefix + endVal.toLocaleString() + suffix;
        el.dataset.countingUp = 'false';
      }}
    }}
    requestAnimationFrame(update);
  }}
}});
</script>
</body>
</html>
'''

with open('mcp-promotion.html', 'w', encoding='utf-8') as f:
    f.write(page_template)
