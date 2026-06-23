$dir = "C:\Users\khoadnd\.gemini\antigravity-ide\brain\85e38ad5-d4a2-42e0-b309-1bfb5d012e12"
if (Test-Path $dir) {
    Get-ChildItem -Path $dir -Recurse | Select-Object FullName, Length
} else {
    Write-Host "Directory not found"
}
