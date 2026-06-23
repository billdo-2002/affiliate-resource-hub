import os, json, re

base_brain = r"C:\Users\khoadnd\.gemini\antigravity-ide\brain"
subdirs = [
    "01fbcdd2-45d6-4791-83c6-3ed2d29fd68f",
    "1099c483-a3bf-4ee8-80cc-d70a619acf29",
    "157c16aa-accf-48f2-9bb7-55484f828977",
    "23a5b8c2-2d6f-432f-b017-974393dbdc5d",
    "30051294-e7c2-453d-a7af-1b2b09edc619",
    "32d9fc63-fd78-449e-ae52-e9732d519b62",
    "3abac1ac-04c3-4cf6-9acc-0e1f847094f1",
    "418f6f8b-4632-4fc3-8eab-77f0b6630095",
    "5970fea6-795a-46ae-93dd-b5eb561c1e09",
    "69f3d7c8-23a2-4dd9-a345-0ae2b1f44b6d",
    "747a92e1-4dcd-4b09-9f10-5c7e7a83e756",
    "7aa3ac27-55d6-4ed8-9355-a0f57acf21f6",
    "7bda0415-0802-46dc-bbe6-2b902584c2a6",
    "85c15c65-5339-4f06-8bc3-2d0dcfbb188c",
    "85e38ad5-d4a2-42e0-b309-1bfb5d012e12",
    "8fbb87a4-ae66-479b-b3c8-5c34ffdd809f",
    "97797bfe-2863-4a57-adac-9191425d5dd1",
    "9a89bd99-6216-47f0-ab5c-bc9b77f08e80",
    "9ace5b7d-c16d-4a88-9392-24a65034710f",
    "ae62d0f7-8a15-41ad-8b63-0212cf8af250",
    "af750129-5680-4be5-86a9-e7e9985dc873",
    "b14c5b82-2b16-4411-bff4-388d5f39f172",
    "b2844f29-72f5-4036-b247-e50bf3687ab6",
    "ba269ce2-8a06-45f9-ace8-dbade8e7539c",
    "be22a2d3-01ed-4d2c-a9ec-f93837c35ac5",
    "be53428a-7140-4d2f-9754-3565392336fe",
    "c0895a64-3d85-4572-952e-4aab60baad3a",
    "c3cfbbcf-29b7-40e0-b1da-21f766c75814",
    "c591acad-ac02-4937-90f4-a4fa3ffa8178",
    "c64c0e42-5f77-4d3b-babe-a86c4e543aba",
    "c7d14a8a-4549-4e17-9cfb-c2ec83a7178e",
    "ca9e0b9e-a40e-4400-88c1-7468f0dc096c",
    "d2d26d45-43a4-4ab6-a94d-acc1d017295c",
    "dd4bdc35-fed5-40db-bbdc-50f5834f28d4",
    "de853200-f4a1-41d1-8e50-72fa867364df",
    "e1436e3d-402f-4e4e-9be9-ac1fc7a7c561",
    "f343f9e6-7ad3-4d3f-af64-d6a1438e8ffe",
    "fa71a2a9-c0c1-4047-ba07-1f660674bc66"
]

targets = ["track-profit-like-a-pro.html", "scale-safely-with-margins.html", "stop-losing-30-profit.html"]

for subdir in subdirs:
    log_path = os.path.join(base_brain, subdir, ".system_generated", "logs", "transcript.jsonl")
    if os.path.exists(log_path):
        print(f"Scanning log: {log_path}")
        with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
            for line_num, line in enumerate(f):
                try:
                    data = json.loads(line)
                except Exception:
                    continue
                
                tool_calls = data.get("tool_calls", [])
                for tc in tool_calls:
                    name = tc.get("name")
                    args = tc.get("args", {})
                    target_file = args.get("TargetFile") or ""
                    if any(t in target_file for t in targets):
                        print(f"  [{subdir}] Line {line_num}: Tool {name} targeted {target_file}")
                        for key in ["CodeContent", "ReplacementContent"]:
                            if key in args:
                                val = args[key]
                                print(f"    Found {key} (length: {len(val)})")
                                basename_raw = target_file.split("/")[-1].split("\\")[-1]
                                basename = re.sub(r'[^a-zA-Z0-9_.-]', '', basename_raw)
                                out_path = f"scratch/extracted_{subdir[:8]}_{basename}_{line_num}.txt"
                                with open(out_path, "w", encoding="utf-8") as out:
                                    out.write(val)
                                print(f"    Wrote content to {out_path}")
