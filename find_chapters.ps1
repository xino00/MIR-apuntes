$lines = Get-Content "C:\Users\arena\OneDrive\Documentos\MIR\manual.txt"
$count = $lines.Count

$cardio_chapters = @()

for ($i = 0; $i -lt $count; $i++) {
    $line = $lines[$i].Trim()
    if ($line -match "^AUTORES:$" -or $line -match "^AUTORAS:$") {
        # Check the next few lines for Cardiolog
        $is_cardio = $false
        for ($j = 1; $j -le 5; $j++) {
            if (($i+$j) -lt $count -and $lines[$i+$j] -match "Cardiolog") {
                $is_cardio = $true
                break
            }
        }
        
        if ($is_cardio) {
            $pathology = ""
            if ($i -gt 0) {
                $pathology = $lines[$i-1].Trim()
                # If pathology is a number, it might be the chapter number, but usually the pathology is line $i-1
            }
            $cardio_chapters += [PSCustomObject]@{
                Line = $i
                Name = $pathology
            }
        }
    }
}

foreach ($chap in $cardio_chapters) {
    Write-Host "$($chap.Line): $($chap.Name)"
}
