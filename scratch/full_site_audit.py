import os
import re
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

BASE_DIR = r"c:\Users\khoadnd\Desktop\onboarding hub"

HTML_FILES = [
    "index.html",
    "guides.html",
    "mcp-promotion.html",
    "guides/general-guide.html",
    "guides/discord-blueprint.html",
    "guides/tiktok-youtube-shorts.html",
    "guides/angles/track-profit-like-a-pro.html",
    "guides/angles/scale-safely-with-margins.html",
    "guides/angles/stop-losing-30-profit.html",
    "resources/mcp/x-twitter-ready-to-post.html",
    "resources/mcp/reddit-ready-to-post.html",
    "resources/mcp/short-form-video-guidelines.html"
]

class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.images = []
        self.css_links = []
        self.js_links = []
        self.copy_buttons = []
        self.toc_links = []
        self.accordion_headers = []
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        # ID check
        if "id" in attrs_dict:
            self.ids.append(attrs_dict["id"])
            
        # Links
        if tag == "a" and "href" in attrs_dict:
            self.links.append((attrs_dict["href"], self.getpos()))
            # TOC links
            if "class" in attrs_dict and "sidebar-toc" in attrs_dict.get("class", "") or tag == "a" and attrs_dict["href"].startswith("#"):
                # If it's a TOC link specifically
                self.toc_links.append(attrs_dict["href"])
                
        # Images / SVGs
        if tag == "img" and "src" in attrs_dict:
            self.images.append((attrs_dict["src"], self.getpos()))
            
        # CSS Link
        if tag == "link" and attrs_dict.get("rel") == "stylesheet" and "href" in attrs_dict:
            self.css_links.append((attrs_dict["href"], self.getpos()))
            
        # JS Link
        if tag == "script" and "src" in attrs_dict:
            self.js_links.append((attrs_dict["src"], self.getpos()))
            
        # Copy buttons
        if tag == "button" and "onclick" in attrs_dict:
            onclick = attrs_dict["onclick"]
            if "copyPostText" in onclick:
                self.copy_buttons.append((onclick, self.getpos()))
                
        # Accordion header
        if "class" in attrs_dict and ("faq-header" in attrs_dict["class"] or "accordion-header" in attrs_dict["class"]):
            self.accordion_headers.append(attrs_dict.get("id", "no-id"))

def run_audit():
    report = {
        "broken_links": [],
        "missing_assets": [],
        "duplicate_ids": {},
        "missing_css_js": [],
        "copy_button_issues": [],
        "toc_issues": [],
        "accordion_issues": []
    }
    
    # Pre-parse all files to map their IDs
    file_ids = {}
    for rel_path in HTML_FILES:
        abs_path = os.path.join(BASE_DIR, rel_path.replace("/", os.sep))
        if not os.path.exists(abs_path):
            continue
        with open(abs_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        parser = AuditParser()
        parser.feed(html_content)
        file_ids[rel_path] = set(parser.ids)
        
    for rel_path in HTML_FILES:
        abs_path = os.path.join(BASE_DIR, rel_path.replace("/", os.sep))
        if not os.path.exists(abs_path):
            report["broken_links"].append({
                "file": rel_path,
                "error": "File does not exist in workspace."
            })
            continue
            
        with open(abs_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            
        parser = AuditParser()
        parser.feed(html_content)
        
        # 1. Duplicate ID check
        seen_ids = set()
        dups = []
        for id_val in parser.ids:
            if id_val in seen_ids:
                dups.append(id_val)
            seen_ids.add(id_val)
        if dups:
            report["duplicate_ids"][rel_path] = list(set(dups))
            
        # 2. CSS / JS references check
        # Check inline styles background-image: url(...)
        inline_bg_urls = re.findall(r"url\(['\"]?(.*?)['\"]?\)", html_content)
        for bg_url in inline_bg_urls:
            if not bg_url.startswith("http") and not bg_url.startswith("data:"):
                # resolve path relative to file
                file_dir = os.path.dirname(abs_path)
                asset_abs = os.path.normpath(os.path.join(file_dir, unquote(bg_url)))
                if not os.path.exists(asset_abs):
                    report["missing_assets"].append({
                        "file": rel_path,
                        "asset": bg_url,
                        "type": "Inline CSS Background Image"
                    })
                    
        for href, pos in parser.css_links:
            if not href.startswith("http"):
                file_dir = os.path.dirname(abs_path)
                css_abs = os.path.normpath(os.path.join(file_dir, unquote(href)))
                if not os.path.exists(css_abs):
                    report["missing_css_js"].append({
                        "file": rel_path,
                        "reference": href,
                        "type": "CSS Stylesheet",
                        "line": pos[0]
                    })
                    
        for src, pos in parser.js_links:
            if not src.startswith("http"):
                file_dir = os.path.dirname(abs_path)
                js_abs = os.path.normpath(os.path.join(file_dir, unquote(src)))
                if not os.path.exists(js_abs):
                    report["missing_css_js"].append({
                        "file": rel_path,
                        "reference": src,
                        "type": "JS Script",
                        "line": pos[0]
                    })
                    
        # 3. Images check
        for src, pos in parser.images:
            if not src.startswith("http") and not src.startswith("data:"):
                file_dir = os.path.dirname(abs_path)
                img_abs = os.path.normpath(os.path.join(file_dir, unquote(src)))
                if not os.path.exists(img_abs):
                    report["missing_assets"].append({
                        "file": rel_path,
                        "asset": src,
                        "type": "Image tag",
                        "line": pos[0]
                    })
                    
        # 4. Links check (including fragments)
        for href, pos in parser.links:
            if href.startswith("#"):
                # Internal fragment in same file
                target_id = href[1:]
                if target_id and target_id not in file_ids.get(rel_path, set()):
                    report["broken_links"].append({
                        "file": rel_path,
                        "link": href,
                        "error": f"Anchor ID '{target_id}' not found in the same file.",
                        "line": pos[0]
                    })
            elif not href.startswith("http") and not href.startswith("mailto:") and not href.startswith("tel:") and href != "#":
                # Relative link
                parsed_url = urlparse(href)
                path = parsed_url.path
                fragment = parsed_url.fragment
                
                file_dir = os.path.dirname(rel_path)
                target_rel = os.path.normpath(os.path.join(file_dir, unquote(path))).replace("\\", "/")
                
                # Check file existence
                target_abs = os.path.normpath(os.path.join(BASE_DIR, target_rel.replace("/", os.sep)))
                if not os.path.exists(target_abs):
                    report["broken_links"].append({
                        "file": rel_path,
                        "link": href,
                        "error": f"Target file '{target_rel}' does not exist.",
                        "line": pos[0]
                    })
                else:
                    # Check fragment if specified
                    if fragment:
                        if fragment not in file_ids.get(target_rel, set()):
                            report["broken_links"].append({
                                "file": rel_path,
                                "link": href,
                                "error": f"Anchor ID '{fragment}' not found in target file '{target_rel}'.",
                                "line": pos[0]
                            })
                            
        # 5. Copy button check
        has_copy_script = "function copyPostText" in html_content
        for onclick, pos in parser.copy_buttons:
            if not has_copy_script:
                report["copy_button_issues"].append({
                    "file": rel_path,
                    "error": "Copy button present but copyPostText JS function is missing from the file.",
                    "line": pos[0]
                })
            else:
                # extract target ID from copyPostText(this, 'target')
                match = re.search(r"copyPostText\(\s*this\s*,\s*['\"](.*?)['\"]\s*\)", onclick)
                if match:
                    target_id = match.group(1)
                    if target_id not in file_ids.get(rel_path, set()):
                        report["copy_button_issues"].append({
                            "file": rel_path,
                            "error": f"Copy button references target ID '{target_id}' which does not exist in the HTML.",
                            "line": pos[0]
                        })
                else:
                    report["copy_button_issues"].append({
                        "file": rel_path,
                        "error": f"Could not parse target ID from onclick handler: {onclick}",
                        "line": pos[0]
                    })
                    
        # 6. Sidebar TOC check
        # TOC links must point to existing section IDs on the page
        sidebar_sections = []
        if "sidebar-toc" in html_content:
            toc_hrefs = re.findall(r"<a[^>]*href=\"(#.*?)\"[^>]*>", html_content)
            for href in toc_hrefs:
                target_id = href[1:]
                if target_id and target_id not in file_ids.get(rel_path, set()):
                    report["toc_issues"].append({
                        "file": rel_path,
                        "error": f"Sidebar TOC link '{href}' points to a non-existent element ID on this page."
                    })
                    
        # 7. FAQ accordion check
        # Check index.html and mcp-promotion.html for accordions and make sure they have JS to toggle
        if "faq-header" in html_content or "accordion-header" in html_content:
            has_accordion_js = "classList.toggle('active')" in html_content or "classList.toggle" in html_content or "slideToggle" in html_content or "jQuery" in html_content
            # Let's check for standard event listener on headers
            if not has_accordion_js:
                report["accordion_issues"].append({
                    "file": rel_path,
                    "error": "FAQ accordion headers are present but JS toggle script is missing."
                })
                
    return report

if __name__ == "__main__":
    report = run_audit()
    
    # Write report in Markdown format
    qa_path = os.path.join(r"C:\Users\khoadnd\.gemini\antigravity-ide\brain\747a92e1-4dcd-4b09-9f10-5c7e7a83e756", "RECOVERY_QA_REPORT.md")
    
    with open(qa_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("# QA AUDIT REPORT — TrueProfit Affiliate Onboarding Hub\n\n")
        f.write("This report summarizes the full site audit checking links, assets, IDs, and interactivity across all onboarding hub HTML files.\n\n")
        
        f.write("## 1. Broken Internal Links\n")
        if report["broken_links"]:
            f.write("| File | Broken Link | Error | Line |\n")
            f.write("| --- | --- | --- | --- |\n")
            for bl in report["broken_links"]:
                f.write(f"| {bl['file']} | `{bl['link']}` | {bl['error']} | {bl.get('line', 'N/A')} |\n")
        else:
            f.write("✓ No broken internal links found.\n")
        f.write("\n")
        
        f.write("## 2. Missing Images / SVGs\n")
        if report["missing_assets"]:
            for ma in report["missing_assets"]:
                f.write(f"- **{ma['file']}**: Missing {ma['type']} reference `{ma['asset']}` (Line: {ma.get('line', 'N/A')})\n")
        else:
            f.write("✓ All referenced image and SVG assets exist on disk.\n")
        f.write("\n")
        
        f.write("## 3. Duplicate IDs\n")
        if report["duplicate_ids"]:
            for fn, ids in report["duplicate_ids"].items():
                f.write(f"- **{fn}**: Duplicate IDs found: " + ", ".join(f"`{i}`" for i in ids) + "\n")
        else:
            f.write("✓ No duplicate IDs found in any single file.\n")
        f.write("\n")
        
        f.write("## 4. Missing CSS & JS References\n")
        if report["missing_css_js"]:
            for mc in report["missing_css_js"]:
                f.write(f"- **{mc['file']}**: Missing external {mc['type']} file: `{mc['reference']}` (Line: {mc['line']})\n")
        else:
            f.write("✓ All external stylesheet and script references exist on disk.\n")
        f.write("\n")
        
        f.write("## 5. Copy Button Functionality\n")
        if report["copy_button_issues"]:
            for cb in report["copy_button_issues"]:
                f.write(f"- **{cb['file']}**: {cb['error']} (Line: {cb['line']})\n")
        else:
            f.write("✓ All copy buttons have matching target elements and JS copy functions.\n")
        f.write("\n")
        
        f.write("## 6. Sidebar TOC Functionality\n")
        if report["toc_issues"]:
            for ti in report["toc_issues"]:
                f.write(f"- **{ti['file']}**: {ti['error']}\n")
        else:
            f.write("✓ All sidebar TOC links resolve correctly to element IDs on their respective pages.\n")
        f.write("\n")
        
        f.write("## 7. FAQ Accordion Functionality\n")
        if report["accordion_issues"]:
            for ai in report["accordion_issues"]:
                f.write(f"- **{ai['file']}**: {ai['error']}\n")
        else:
            f.write("✓ All FAQ pages have functioning toggle scripts.\n")
        f.write("\n")
        
    print("RECOVERY_QA_REPORT.md generated successfully!")
