Write-Host "what would you like to do?"
Write-Host "A) Collect a new Baseline?"
Write-Host "B) Begin monitoring files with saved baseline?"

$response = Read-Host -Prompt "Please enter 'A' or 'B'"
Write-Host "User entered option: $($response)"
Write-Host ""

if ($response -eq "A".ToUpper()) {
    # Calculate the hash of the files and store in the baseline
    Write-Host "Calculating Hashes, make new baseline.txt" -ForegroundColor Cyan     

} elseif ($response -eq "B".ToUpper()) {
    # Begin monitoring files with saved Baseline
    Write-Host "Read exisiting baseline.txt , start monitoring files " -ForegroundColor Yellow
}