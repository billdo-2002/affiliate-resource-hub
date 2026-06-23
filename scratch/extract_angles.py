import re

with open("TrueProfit Affiliate Playbook (2).md", "r", encoding="utf-8") as f:
    content = f.read()

# We want to extract content for:
# - Angle #1: Track Profit Like A Pro
# - Angle #2: Scale Safely With Margins
# - Angle #3: Stop Losing 30% Profit

angles = [
    (r"## Angle \\#1: Track Profit Like A Pro", r"## Angle \\#2: Scale Safely With Margins"),
    (r"## Angle \\#2: Scale Safely With Margins", r"## Angle \\#3: Stop Losing 30% Profit"),
    (r"## Angle \\#3: Stop Losing 30% Profit", r"## Promoting TrueProfit on Discord")
]

for pattern_start, pattern_end in angles:
    pattern = rf"({pattern_start}.*?)(?={pattern_end})"
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    if match:
        text = match.group(1).strip()
        # Clean title for filename
        title_clean = re.sub(r'[^a-zA-Z0-9_]', '', pattern_start.replace('##', '').strip().lower().replace(' ', '_'))
        filename = f"scratch/{title_clean}.txt"
        with open(filename, "w", encoding="utf-8") as out:
            out.write(text)
        print(f"Extracted {pattern_start} to {filename}")
    else:
        print(f"Failed to find {pattern_start}")
