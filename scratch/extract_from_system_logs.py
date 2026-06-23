import os
import json

appdata_dir = r"C:\Users\khoadnd\.gemini\antigravity-ide\brain"
out_dir = r"c:\Users\khoadnd\Desktop\onboarding hub\scratch"

for folder in os.listdir(appdata_dir):
    log_file = os.path.join(appdata_dir, folder, ".system_generated", "logs", "transcript.jsonl")
    if not os.path.exists(log_file):
        continue
    
    print(f"Reading log file for folder {folder}...")
    with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
        for idx, line in enumerate(f, 1):
            try:
                data = json.loads(line)
                
                # Check tool calls
                tool_calls = data.get("tool_calls", [])
                for tc in tool_calls:
                    name = tc.get("name", "")
                    if name in ["write_to_file", "replace_file_content"]:
                        args = tc.get("args", {})
                        target = args.get("TargetFile", "") or args.get("AbsolutePath", "") or args.get("Target", "")
                        if "discord-blueprint" in target:
                            content = args.get("CodeContent", "") or args.get("ReplacementContent", "")
                            if content and len(content) > 5000:
                                out_fn = os.path.join(out_dir, f"recovered_discord_{folder}_line_{idx}.html")
                                with open(out_fn, "w", encoding="utf-8") as out_f:
                                    out_f.write(content)
                                print(f"  - Found tool call write to discord-blueprint ({len(content)} bytes) at line {idx}. Saved to scratch/{os.path.basename(out_fn)}")
                        if "tiktok-youtube-shorts" in target:
                            content = args.get("CodeContent", "") or args.get("ReplacementContent", "")
                            if content and len(content) > 5000:
                                out_fn = os.path.join(out_dir, f"recovered_tiktok_{folder}_line_{idx}.html")
                                with open(out_fn, "w", encoding="utf-8") as out_f:
                                    out_f.write(content)
                                print(f"  - Found tool call write to tiktok-youtube-shorts ({len(content)} bytes) at line {idx}. Saved to scratch/{os.path.basename(out_fn)}")
                                
                # Check user inputs or other content step values
                content_str = data.get("content", "")
                if "discord-blueprint.html" in content_str and "CodeContent" in content_str and len(content_str) > 10000:
                    out_fn = os.path.join(out_dir, f"raw_content_discord_{folder}_line_{idx}.txt")
                    with open(out_fn, "w", encoding="utf-8") as out_f:
                        out_f.write(content_str)
                    print(f"  - Found raw content with discord-blueprint.html ({len(content_str)} bytes) at line {idx}. Saved to scratch/{os.path.basename(out_fn)}")
                if "tiktok-youtube-shorts.html" in content_str and "CodeContent" in content_str and len(content_str) > 10000:
                    out_fn = os.path.join(out_dir, f"raw_content_tiktok_{folder}_line_{idx}.txt")
                    with open(out_fn, "w", encoding="utf-8") as out_f:
                        out_f.write(content_str)
                    print(f"  - Found raw content with tiktok-youtube-shorts.html ({len(content_str)} bytes) at line {idx}. Saved to scratch/{os.path.basename(out_fn)}")

            except Exception as e:
                pass
print("Done!")
