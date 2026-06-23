import json

log_path = r"C:\Users\khoadnd\.gemini\antigravity-ide\brain\97797bfe-2863-4a57-adac-9191425d5dd1\.system_generated\logs\transcript.jsonl"

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            # Look for run_command or write_to_file or replace_file_content or multi_replace_file_content
            tool_calls = data.get("tool_calls", [])
            for tc in tool_calls:
                name = tc.get("name")
                args = tc.get("args", {})
                if name == "run_command":
                    cmd = args.get("CommandLine", "")
                    if "rm" in cmd or "del" in cmd or "mv" in cmd or "move" in cmd or "Remove-Item" in cmd or "Move-Item" in cmd or "Rename-Item" in cmd or "git" in cmd:
                        print(f"STEP {data.get('step_index')}: CMD: {cmd}")
                elif name == "write_to_file":
                    target = args.get("TargetFile", "")
                    if "scratch" not in target:
                        print(f"STEP {data.get('step_index')}: WRITE: {target}")
        except Exception as e:
            pass
