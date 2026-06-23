import re

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero Buttons
content = re.sub(
    r'<button class="btn-hero-outline" onclick="document\.getElementById\(\'section-playbook\'\)\.scrollIntoView\(\{behavior:\'smooth\'\}\)">\s*Jump to Playbook\s*</button>',
    '',
    content,
    flags=re.DOTALL
)

# 2. Nav Bar
nav_original = '''      <a href="#dashboard-setup">Dashboard Setup</a>
      <a href="#section-materials">Materials</a>
      <a href="#section-playbook">Playbook</a>'''
nav_replacement = '''      <a href="#dashboard-setup">Dashboard Setup</a>
      <div class="nav-dropdown-wrapper">
        <a href="#resources" class="nav-dropdown-trigger">Resources</a>
        <div class="mega-menu">
          <div class="mega-col">
            <div class="mega-subhead">GETTING STARTED</div>
            <a href="#" class="mega-main-link">A. General Guide</a>
          </div>
          <div class="mega-col">
            <div class="mega-subhead">AD ANGLES</div>
            <a href="#" class="mega-main-link">B. Ready-to-post</a>
            <div class="mega-sublinks">
              <a href="#">&bull; Angle 1: Profit Tracking</a>
              <a href="#">&bull; Angle 2: Scaling Margin</a>
              <a href="#">&bull; Angle 3: Hidden Fees</a>
            </div>
          </div>
          <div class="mega-col">
            <div class="mega-subhead">GROWTH CHANNELS</div>
            <a href="#" class="mega-main-link">C. Other Platforms</a>
            <div class="mega-sublinks">
              <a href="#">&bull; Discord Blueprint</a>
              <a href="#">&bull; TikTok &amp; Shorts Guide</a>
            </div>
          </div>
          <div class="mega-col mega-featured">
            <div class="mega-badge">MEDIA KIT</div>
            <div class="mega-featured-title">D. Creative Assets</div>
            <div class="mega-featured-text">Kho tài nguyên hình ảnh dashboard &amp; video b-roll.</div>
            <button class="mega-btn">Go to Drive <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg></button>
          </div>
        </div>
      </div>'''
content = content.replace(nav_original, nav_replacement)

# 3. Footer Links
footer_original = '''      <a href="#section-commission">Commission Structure</a>
      <a href="#section-materials">Materials Library</a>
      <a href="#section-playbook">Playbook</a>'''
footer_replacement = '''      <a href="#section-commission">Commission Structure</a>'''
content = content.replace(footer_original, footer_replacement)

# 4. Mega Menu CSS
mega_menu_css = '''
/* =========================================
   MEGA MENU STYLES
   ========================================= */
.nav-dropdown-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}
.mega-menu {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%) translateY(10px);
  width: 900px;
  background: var(--white);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.08);
  opacity: 0;
  visibility: hidden;
  transition: all 0.2s ease;
  z-index: 1001;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1.1fr;
  gap: 32px;
  padding: 32px;
}
.nav-dropdown-wrapper:hover .mega-menu {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
}
.mega-col {
  display: flex;
  flex-direction: column;
}
.mega-subhead {
  font-size: 11px;
  font-weight: 700;
  color: var(--text-light);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 12px;
}
.mega-main-link {
  font-size: 15px;
  font-weight: 700;
  color: var(--text-dark);
  margin-bottom: 12px;
  transition: color 0.2s ease;
}
.mega-main-link:hover {
  color: #002d33 !important;
}
.mega-sublinks {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.mega-sublinks a {
  font-size: 13px !important;
  color: var(--text-muted) !important;
  font-weight: 500 !important;
  padding: 0 !important;
  transition: color 0.2s ease !important;
}
.mega-sublinks a:hover {
  color: #002d33 !important;
}
.mega-featured {
  background: #002d33;
  border-radius: 12px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
.mega-badge {
  background: #fef08a;
  color: #854d0e;
  font-size: 10px;
  font-weight: 800;
  padding: 4px 8px;
  border-radius: 4px;
  margin-bottom: 12px;
}
.mega-featured-title {
  color: #fff;
  font-size: 16px;
  font-weight: 700;
  margin-bottom: 8px;
}
.mega-featured-text {
  color: rgba(255,255,255,0.7);
  font-size: 13px;
  line-height: 1.5;
  margin-bottom: 16px;
}
.mega-btn {
  background: #fff;
  color: #002d33;
  border: none;
  border-radius: 6px;
  padding: 8px 16px;
  font-size: 13px;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  margin-top: auto;
}
.mega-btn:hover {
  background: #f1f5f9;
  transform: translateY(-1px);
}

@media (max-width: 768px) {
  .nav-dropdown-wrapper {
    flex-direction: column;
    align-items: flex-start;
  }
  .mega-menu {
    position: static;
    transform: none;
    width: 100%;
    box-shadow: none;
    border: none;
    padding: 16px 0 0 12px;
    grid-template-columns: 1fr;
    gap: 24px;
    display: none;
    opacity: 1;
    visibility: visible;
  }
  .nav-dropdown-wrapper:hover .mega-menu {
    display: none;
  }
  .nav-dropdown-wrapper.active .mega-menu {
    display: grid;
  }
  .mega-featured {
    padding: 16px;
  }
}
</style>'''
content = content.replace('</style>', mega_menu_css, 1)

# 5. Remove Materials & Playbook sections
content = re.sub(
    r'<!-- ==============================\s*MATERIALS LIBRARY\s*============================== -->.*?<!-- ==============================\s*FINAL CTA\s*============================== -->',
    '<!-- ==============================\n     FINAL CTA\n     ============================== -->',
    content,
    flags=re.DOTALL
)

# 6. Replace Tabs and Filter JS
js_original = '''/* =========================================
   TABS
   ========================================= */
document.querySelectorAll('.tab-navbtn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.tab-navbtn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
    btn.classList.add('active');
    const target = document.getElementById(btn.getAttribute('data-tab'));
    if(target) target.classList.add('active');
  });
});


/* =========================================
   MATERIALS FILTER
   ========================================= */
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const filter = btn.getAttribute('data-filter');
    document.querySelectorAll('.asset-card').forEach(card => {
      card.style.display = (filter === 'all' || card.getAttribute('data-category') === filter) ? '' : 'none';
    });
  });
});'''

js_replacement = '''/* =========================================
   MOBILE MEGA MENU ACCORDION
   ========================================= */
document.querySelectorAll('.nav-dropdown-trigger').forEach(trigger => {
  trigger.addEventListener('click', (e) => {
    if (window.innerWidth <= 768) {
      e.preventDefault();
      const wrapper = trigger.closest('.nav-dropdown-wrapper');
      wrapper.classList.toggle('active');
    }
  });
});'''
content = content.replace(js_original, js_replacement)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates completed.")
