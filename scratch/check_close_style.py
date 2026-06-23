import os
import re

filepath = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\general-guide.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

close_style_tags = list(re.finditer(r'</style>', content, re.IGNORECASE))
print(f"Total </style> tags: {len(close_style_tags)}")
for i, m in enumerate(close_style_tags):
    print(f"  </style> tag {i+1} at position {m.start()}")
