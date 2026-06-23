$lastInput = Get-Content 'C:\Users\khoadnd\.gemini\antigravity-ide\brain\01fbcdd2-45d6-4791-83c6-3ed2d29fd68f\.system_generated\logs\transcript.jsonl' -Encoding UTF8 -Tail 1000 | Where-Object { $_ -match '"type":"USER_INPUT"' } | Select-Object -Last 1
$json = $lastInput | ConvertFrom-Json
[System.IO.File]::WriteAllText("c:\Users\khoadnd\Desktop\onboarding hub\full_prompt_raw.txt", $json.content)
