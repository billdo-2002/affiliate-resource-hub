import json, re

log_path = r"C:\Users\khoadnd\.gemini\antigravity-ide\brain\747a92e1-4dcd-4b09-9f10-5c7e7a83e756\.system_generated\logs\transcript.jsonl"

targets = ["track-profit-like-a-pro.html", "scale-safely-with-margins.html", "stop-losing-30-profit.html"]

with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
    for line_num, line in enumerate(f):
        try:
            data = json.loads(line)
        except Exception:
            continue
        
        # Check if this is a model step with tool calls
        tool_calls = data.get("tool_calls", [])
        for tc in tool_calls:
            name = tc.get("name")
            args = tc.get("args", {})
            target_file = args.get("TargetFile") or ""
            # If the target file matches one of our files, let's inspect
            if any(t in target_file for t in targets):
                print(f"Line {line_num}: Tool {name} targeted {target_file}")
                # Print keys inside args to see if CodeContent or ReplacementContent is there
                for key in ["CodeContent", "ReplacementContent"]:
                    if key in args:
                        val = args[key]
                        print(f"  Found {key} (length: {len(val)})")
                        # Write the extracted content to scratch/extracted_<filename>.txt
                        basename = target_file.split("/")[-1].split("\\")[-1]
                        out_path = f"scratch/extracted_{basename}_{line_num}.txt"
                        with open(out_path, "w", encoding="utf-8") as out:
                            out.write(val)
                        print(f"  Wrote content to {out_path}")
