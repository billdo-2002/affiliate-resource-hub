import os, json

base_brain = r"C:\Users\khoadnd\.gemini\antigravity-ide\brain"
subdirs = os.listdir(base_brain)

targets = ["track-profit-like-a-pro.html", "scale-safely-with-margins.html", "stop-losing-30-profit.html"]

for subdir in subdirs:
    log_path = os.path.join(base_brain, subdir, ".system_generated", "logs", "transcript.jsonl")
    if os.path.exists(log_path):
        with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
            for line_num, line in enumerate(f):
                try:
                    data = json.loads(line)
                except Exception:
                    continue
                
                # Check all fields for targets
                text_repr = json.dumps(data)
                if any(t in text_repr for t in targets):
                    tool_calls = data.get("tool_calls", [])
                    content = data.get("content") or ""
                    # If this line has tool calls
                    if tool_calls:
                        for tc in tool_calls:
                            tc_name = tc.get("name")
                            tc_args = tc.get("args") or {}
                            arg_str = json.dumps(tc_args)
                            if any(t in arg_str for t in targets):
                                print(f"[{subdir[:8]}] Line {line_num}: Tool {tc_name}")
                                if tc_name == 'run_command':
                                    print(f"  Cmd: {tc_args.get('CommandLine')}")
                                elif tc_name == 'write_to_file':
                                    print(f"  Write: {tc_args.get('TargetFile')} (len={len(tc_args.get('CodeContent', ''))})")
                    # If it's a command output (SYSTEM/CONVERSATION_HISTORY etc)
                    elif data.get("type") == "RUN_COMMAND" or "CommandLine" in text_repr:
                        print(f"[{subdir[:8]}] Line {line_num}: {data.get('type')}")
                        if "output" in data:
                            out = data["output"]
                            if isinstance(out, str) and len(out) < 500:
                                print(f"  Output: {out.strip()}")
