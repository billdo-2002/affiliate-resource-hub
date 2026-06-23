$logFile = "C:\Users\khoadnd\.gemini\antigravity-ide\brain\7aa3ac27-55d6-4ed8-9355-a0f57acf21f6\.system_generated\logs\transcript.jsonl"

# Read all content as raw text, find the step 2861 area
$allText = [System.IO.File]::ReadAllText($logFile)

# Find step_index 2861
$idx = $allText.IndexOf('"step_index":2861')
if ($idx -ge 0) {
    # Get 200 chars around it to see structure
    $snippet = $allText.Substring([Math]::Max(0, $idx), [Math]::Min(5000, $allText.Length - $idx))
    Write-Output "RAW around step 2861:"
    Write-Output $snippet.Substring(0, 1000)
} else {
    Write-Output "step 2861 not found as inline text"
}
