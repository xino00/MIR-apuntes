param([string]$msg = "sync: $(Get-Date -Format 'yyyy-MM-dd HH:mm')")

Set-Location $PSScriptRoot
git add -A
git commit -m $msg
git push origin master:main
