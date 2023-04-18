# Create a shell script that Automatic screen lock .


$timeout = 300  # Set timeout value in seconds (e.g. 300 seconds = 5 minutes)

while ($true) {
    $idleTime = (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
    if ((New-TimeSpan -Start $idleTime).TotalSeconds -ge $timeout) {
        rundll32.exe user32.dll,LockWorkStation  # Lock the workstation
        break
    }
    Start-Sleep -Seconds 60  # Wait for 1 minute before checking again
}