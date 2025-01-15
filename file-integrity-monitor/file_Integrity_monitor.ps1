Write-Host "what would you like to do?"
Write-Host "A) Collect a new Baseline?"
Write-Host "B) Begin monitoring files with saved baseline?"

$response = Read-Host -Prompt "Please enter 'A' or 'B'"
Write-Host "User entered option: $($response)"
Write-Host ""

Function Calculate-File-Hash($filepath) {
    $filehash = Get-FileHash -Path $filepath -Algorithm SHA512
    return $filehash
}

Function Erase-Baseline-If-Already-Exists() {
    $baselinexists = Test-Path -Path .\baseline.txt # to check if file exists

    if ($baselinexists) {
        # Delete it
        Remove-Item -Path .\baseline.txt
    }
}

if ($response -eq "A".ToUpper()) {
    #Delete baseline if it already exists
    Erase-Baseline-If-Already-Exists

    # Calculate the hash of the files and store in the baseline
    Write-Host "Calculating Hashes...." -ForegroundColor Cyan
    Write-Host "May make new baseline.txt...." -ForegroundColor Cyan

    # Fetch all files from "target folder"
    $targetFiles = Get-ChildItem -Path target_Files

    # Calculate the hashes and write to baseline.txt
    foreach($file in $targetFiles) {
        $hash = Calculate-File-Hash $file.FullName
        # "$($hash.Path) | $($hash.Hash)" | Set-Content -Path .\baseline.txt   
        "$($hash.Path) | $($hash.Hash)" | Out-File -FilePath .\baseline.txt -Append 
    }

} elseif ($response -eq "B".ToUpper()) {
    # Begin monitoring files with saved Baseline
    Write-Host "Read exisiting baseline.txt , start monitoring files " -ForegroundColor Yellow
}