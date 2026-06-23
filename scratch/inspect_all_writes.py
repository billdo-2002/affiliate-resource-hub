import os
import json

appdata_dir = r"C:\Users\khoadnd\.gemini\antigravity-ide\brain"

write_logs = []

for folder in os.listdir(appdata_dir):
    log_file = os.path.join(appdata_dir, folder, ".system_generated", "logs", "transcript.jsonl")
    if not os.path.exists(log_file):
        continue
    
    with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
        for idx, line in enumerate(f, 1):
            try:
                data = json.loads(line)
                tool_calls = data.get("tool_calls", [])
                for tc in tool_calls:
                    name = tc.get("name", "")
                    if name in ["write_to_file", "replace_file_content"]:
                        args = tc.get("args", {})
                        target = args.get("TargetFile", "") or args.get("AbsolutePath", "") or args.get("Target", "")
                        if target:
                            write_logs.append({
                                "folder": folder,
                                "line": idx,
                                "tool": name,
                                "target": target,
                                "size": len(args.get("CodeContent", "") or args.get("ReplacementContent", ""))
                            })
            except:
                pass

print(f"Total write calls found: {len(write_logs)}")
# Sort by size descending
write_logs.sort(key=lambda x: x["size"], reverse=True)
for item in write_logs[:50]:
    print(f"Size: {item['size']:6d} | Tool: {item['tool']:18s} | Folder: {item['folder']} | File: {item['target']}")
