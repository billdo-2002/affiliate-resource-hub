import os
import re

filepath = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\discord-blueprint.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

body_start = content.find('<!-- Left Column: Article Content -->')
if body_start != -1:
    print("Discord HTML around content:")
    print(content[body_start-200:body_start+400])
else:
    print("Left Column: Article Content not found")
