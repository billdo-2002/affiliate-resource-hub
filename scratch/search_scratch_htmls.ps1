$brainDir = "C:\Users\khoadnd\.gemini\antigravity-ide\brain"
$subdirs = Get-ChildItem -Path $brainDir -Directory
foreach ($dir in $subdirs) {
    $scratchDir = Join-Path $dir.FullName "scratch"
    if (Test-Path $scratchDir) {
        $files = Get-ChildItem -Path $scratchDir -File -Filter "*.html"
        foreach ($file in $files) {
            Write-Output "$($file.FullName) | $($file.Length)"
        }
        $baks = Get-ChildItem -Path $scratchDir -File -Filter "*.bak"
        foreach ($file in $baks) {
            Write-Output "$($file.FullName) | $($file.Length)"
        }
    }
}
