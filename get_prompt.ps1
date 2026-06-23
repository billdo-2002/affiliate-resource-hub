$lines = Get-Content 'C:\Users\khoadnd\.gemini\antigravity-ide\brain\01fbcdd2-45d6-4791-83c6-3ed2d29fd68f\.system_generated\logs\transcript.jsonl' -Encoding UTF8 -Tail 1000
$lastInput = ""
foreach ($line in $lines) {
    if ($line -match '"type":"USER_INPUT"') {
        $lastInput = $line
    }
}
$json = $lastInput | ConvertFrom-Json
$json.content | Out-File -Encoding UTF8 'full_prompt.txt'
