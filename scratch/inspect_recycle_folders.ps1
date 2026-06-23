$recyclePath = 'C:\$Recycle.Bin'
$dirs = Get-ChildItem -Path $recyclePath -Directory -Recurse -Force -ErrorAction SilentlyContinue
foreach ($dir in $dirs) {
    $files = Get-ChildItem -Path $dir.FullName -File -Force -ErrorAction SilentlyContinue
    if ($files.Length -gt 0) {
        Write-Output "Directory: $($dir.FullName) | Original Name: $($dir.Name)"
        foreach ($file in $files) {
            Write-Output "  File: $($file.Name) | Size: $($file.Length)"
        }
    }
}
