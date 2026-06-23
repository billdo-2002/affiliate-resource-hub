$sh = New-Object -ComObject Shell.Application
$rb = $sh.NameSpace(10)
$items = $rb.Items()
foreach ($item in $items) {
    $deletedFrom = $item.ExtendedProperty('System.Recycle.DeletedFrom')
    $name = $item.Name
    $path = $item.Path
    Write-Output "Name: $name | Original Path: $deletedFrom | Temporary Path: $path"
}
