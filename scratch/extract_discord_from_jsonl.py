import os
import json

BASE = r"c:\Users\khoadnd\Desktop\onboarding hub"
restored_file = os.path.join(BASE, "scratch", "restored_pages", "discord-blueprint.html")

if not os.path.exists(restored_file):
    print("restored_file does not exist!")
    exit(1)

with open(restored_file, "r", encoding="utf-8", errors="ignore") as f:
    for idx, line in enumerate(f, 1):
        try:
            data = json.loads(line)
            # Check if this data has tool_calls or content
            step_idx = data.get("step_index", "unknown")
            source = data.get("source", "")
            type_val = data.get("type", "")
            
            # Print basic info
            # print(f"Line {idx} (Step {step_idx}): Source={source}, Type={type_val}")
            
            # Look for content or arguments matching our file
            content_str = data.get("content", "")
            if "discord-blueprint.html" in content_str and len(content_str) > 1000:
                print(f"-> Found long content with 'discord-blueprint.html' at Line {idx} (Step {step_idx}). Length: {len(content_str)}")
                # save to file
                out_fn = f"scratch/extracted_discord_content_step_{step_idx}.txt"
                with open(os.path.join(BASE, out_fn), "w", encoding="utf-8") as out_f:
                    out_f.write(content_str)
                print(f"   Saved to {out_fn}")
                
            tool_calls = data.get("tool_calls", [])
            for tc in tool_calls:
                args = tc.get("args", {})
                args_str = json.dumps(args)
                if "discord-blueprint.html" in args_str and len(args_str) > 1000:
                    print(f"-> Found long tool call argument with 'discord-blueprint.html' at Line {idx} (Step {step_idx}). Length: {len(args_str)}")
                    out_fn = f"scratch/extracted_discord_args_step_{step_idx}.txt"
                    with open(os.path.join(BASE, out_fn), "w", encoding="utf-8") as out_f:
                        out_f.write(args_str)
                    print(f"   Saved to {out_fn}")
        except Exception as e:
            # print(f"Error at line {idx}: {e}")
            pass
