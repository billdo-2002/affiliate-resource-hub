import os
from html.parser import HTMLParser

class NestingParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.sidebar_parent = None
        self.content_parent = None
        
    def handle_starttag(self, tag, attrs):
        if tag.lower() in ['img', 'meta', 'link', 'br', 'hr', 'input', 'source', 'embed', 'col', 'base', 'area', 'param', 'track', 'wbr']:
            return
        attrs_dict = dict(attrs)
        classes = attrs_dict.get('class', '').split()
        
        self.stack.append((tag, classes))
        
        if 'guide-sidebar' in classes:
            # Print the stack of parents
            self.sidebar_parent = list(self.stack)
        if 'guide-content' in classes:
            self.content_parent = list(self.stack)
            
    def handle_endtag(self, tag):
        if tag.lower() in ['img', 'meta', 'link', 'br', 'hr', 'input', 'source', 'embed', 'col', 'base', 'area', 'param', 'track', 'wbr']:
            return
        if self.stack:
            # Pop the matching tag from stack
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag:
                    self.stack.pop(i)
                    break

def check_file(filepath):
    print(f"Checking nesting in {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    parser = NestingParser()
    parser.feed(content)
    
    if parser.content_parent:
        print("  guide-content path:", [x[1] for x in parser.content_parent if x[1]])
    if parser.sidebar_parent:
        print("  guide-sidebar path:", [x[1] for x in parser.sidebar_parent if x[1]])
        # Check if guide-content is in the parent path of guide-sidebar
        is_nested = any('guide-content' in x[1] for x in parser.sidebar_parent)
        print("  Is guide-sidebar nested inside guide-content?", is_nested)

files = [
    "guides/general-guide.html",
    "guides/discord-blueprint.html",
    "guides/tiktok-youtube-shorts.html",
    "guides/angles/track-profit-like-a-pro.html",
    "guides/angles/scale-safely-with-margins.html",
    "guides/angles/stop-losing-30-profit.html",
    "resources/mcp/reddit-ready-to-post.html",
    "resources/mcp/x-twitter-ready-to-post.html",
    "resources/mcp/short-form-video-guidelines.html"
]

for f in files:
    full_path = os.path.join(r"c:\Users\khoadnd\Desktop\onboarding hub", f)
    if os.path.exists(full_path):
        check_file(full_path)
