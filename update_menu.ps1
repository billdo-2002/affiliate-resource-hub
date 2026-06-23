$path = "c:\Users\khoadnd\Desktop\onboarding hub\index.html"
$content = Get-Content -Raw -Encoding UTF8 $path

$headerStart = '<header id="header">'
$heroStart = '<!-- ==============================
     HERO
     ============================== -->'

$split1 = $content.Split([string[]]@($headerStart), 2, [System.StringSplitOptions]::None)
if ($split1.Length -ne 2) { Write-Host "Failed 1"; exit 1 }

$split2 = $split1[1].Split([string[]]@($heroStart), 2, [System.StringSplitOptions]::None)
if ($split2.Length -ne 2) { Write-Host "Failed 2"; exit 1 }

$newHeader = Get-Content -Raw -Encoding UTF8 "c:\Users\khoadnd\Desktop\onboarding hub\new_header.txt"
$newHeader = $newHeader + "`r`n`r`n"

$newContent = $split1[0] + $newHeader + $heroStart + $split2[1]
Set-Content -Path $path -Value $newContent -Encoding UTF8
Write-Host "Success"
