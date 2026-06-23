$recyclePath = 'C:\$Recycle.Bin'
$destDir = "c:\Users\khoadnd\Desktop\onboarding hub\scratch\recovered_htmls"

if (!(Test-Path $destDir)) {
    New-Item -ItemType Directory -Path $destDir -Force | Out-Null
}

$files = Get-ChildItem -Path $recyclePath -Filter "*.html" -Recurse -Force -ErrorAction SilentlyContinue
foreach ($file in $files) {
    # Copy to dest directory with a safe name based on its Recycle Bin name
    $destFile = Join-Path $destDir $file.Name
    Copy-Item $file.FullName $destFile -Force
    Write-Host "Copied: $($file.FullName) -> $destFile"
}
