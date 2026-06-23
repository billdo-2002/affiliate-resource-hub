import os
import json
import re

brain_dir = r"C:\Users\khoadnd\.gemini\antigravity-ide\brain"
html_files = set()

# Normalize path to relative path under onboarding hub
def normalize(p):
    p = p.replace('\\\\', '/').replace('\\', '/').lower()
    idx = p.find("onboarding hub/")
    if idx != -1:
        return p[idx + len("onboarding hub/"):]
    return None

for root, dirs, files in os.walk(brain_dir):
    for f in files:
        if f == "transcript.jsonl":
            path = os.path.join(root, f)
            try:
                with open(path, "r", encoding="utf-8") as file:
                    for line in file:
                        if not line.strip():
                            continue
                        try:
                            data = json.loads(line)
                            if "tool_calls" in data:
                                for tc in data["tool_calls"]:
                                    if tc.get("name") in ["write_to_file", "replace_file_content"]:
                                        tf = tc.get("args", {}).get("TargetFile")
                                        if tf and tf.endswith(".html"):
                                            norm = normalize(tf)
                                            if norm:
                                                html_files.add(norm)
                        except Exception:
                            # regex fallback if json fails
                            matches = re.findall(r'"TargetFile"\s*:\s*"([^"]+)"', line)
                            for tf in matches:
                                if tf.endswith(".html"):
                                    norm = normalize(tf)
                                    if norm:
                                        html_files.add(norm)
            except Exception as e:
                pass

print("ALL FOUND HTML FILES:")
for h in sorted(html_files):
    print(f"- {h}")
