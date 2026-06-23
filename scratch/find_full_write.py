import os
import json

appdata_dir = r"C:\Users\khoadnd\.gemini\antigravity-ide\brain"
out_dir = r"c:\Users\khoadnd\Desktop\onboarding hub\scratch"

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
                        # print keys to debug
                        target = ""
                        for k, v in args.items():
                            if k.lower() in ["targetfile", "absolutepath", "target"]:
                                target = v
                                break
                        if target and ("discord-blueprint" in target.lower() or "tiktok-youtube-shorts" in target.lower()):
                            # Find code content key
                            code = ""
                            for k, v in args.items():
                                if k.lower() in ["codecontent", "replacementcontent"]:
                                    code = v
                                    break
                            print(f"Match: {target} in folder {folder} at line {idx}, code length: {len(code)}")
                            if len(code) > 10000:
                                name_prefix = "discord" if "discord" in target.lower() else "tiktok"
                                out_fn = os.path.join(out_dir, f"found_{name_prefix}_{folder}_line_{idx}.html")
                                with open(out_fn, "w", encoding="utf-8") as out_f:
                                    out_f.write(code)
                                print(f"  --> Saved {len(code)} bytes to {out_fn}")
            except Exception as e:
                pass
print("Done!")
