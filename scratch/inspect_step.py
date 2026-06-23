import os
import json

log_file = r"C:\Users\khoadnd\.gemini\antigravity-ide\brain\b2844f29-72f5-4036-b247-e50bf3687ab6\.system_generated\logs\transcript.jsonl"

if not os.path.exists(log_file):
    print("Log file does not exist!")
    exit(1)

with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
    for idx, line in enumerate(f, 1):
        if idx == 753:
            try:
                data = json.loads(line)
                print(f"Step Index: {data.get('step_index')}")
                print(f"Type: {data.get('type')}")
                # Print tool calls
                tool_calls = data.get("tool_calls", [])
                for tc in tool_calls:
                    print(f"Tool: {tc.get('name')}")
                    args = tc.get("args", {})
                    for k, v in args.items():
                        print(f"  Arg {k}: {str(v)[:300]}...")
            except Exception as e:
                print(e)
            break
