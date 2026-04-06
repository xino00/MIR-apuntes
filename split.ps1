$lines = Get-Content "C:\Users\arena\OneDrive\Documentos\MIR\manual.txt"

$chapters = @(
    @{ Name="Dolor"; Start=6105; End=7400 },
    @{ Name="IC"; Start=7401; End=8029 },
    @{ Name="Arritmias"; Start=8030; End=8839 },
    @{ Name="Isquemica"; Start=8840; End=10125 },
    @{ Name="Miocardiopatias"; Start=10126; End=10831 },
    @{ Name="Pericardio"; Start=10832; End=11736 },
    @{ Name="HP"; Start=11737; End=12500 }, # Estimated end for HP based on average size
    @{ Name="Endocarditis"; Start=39378; End=40000 } # Estimated end
)

foreach ($chap in $chapters) {
    if ($chap.End -ge $lines.Count) { $chap.End = $lines.Count - 1 }
    $chunk = $lines[$chap.Start..$chap.End]
    $chunk | Set-Content "C:\Users\arena\OneDrive\Documentos\MIR\chap_$($chap.Name).txt"
}

Write-Host "Split complete."
