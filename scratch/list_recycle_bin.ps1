$sh = New-Object -ComObject Shell.Application
$rb = $sh.NameSpace(10) # 10 is the ShellSpecialFolderConstants for Recycle Bin
$items = $rb.Items()
foreach ($item in $items) {
    Write-Output "Name: $($item.Name) | Path: $($item.Path)"
}
