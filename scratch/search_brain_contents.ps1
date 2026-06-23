$brainDir = "C:\Users\khoadnd\.gemini\antigravity-ide\brain"
$files = Get-ChildItem -Path $brainDir -File -Recurse -ErrorAction SilentlyContinue

foreach ($file in $files) {
    if ($file.Length -gt 5000 -and $file.Name -notlike "*.log" -and $file.Name -notlike "*.jsonl" -and $file.Name -notlike "*.png" -and $file.Name -notlike "*.zip") {
        try {
            $content = Get-Content $file.FullName -Raw -ErrorAction SilentlyContinue
            if ($content -match "Stop Losing 30% Profit" -and $content -match "<!DOCTYPE html>") {
                Write-Host "Found full page in: $($file.FullName) (Size: $($file.Length))"
            }
        } catch {}
    }
}
