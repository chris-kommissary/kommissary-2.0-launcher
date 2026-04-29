# Kommissary 2.0 Launcher — bootstrap (first-time install)
#
# Customers can run this in one line:
#   iex (irm https://raw.githubusercontent.com/chris-kommissary/kommissary-2.0-launcher/main/bootstrap.ps1)
#
# The script:
#   1. Installs Python 3 (via winget) if missing — UAC prompt
#   2. Installs Git (via winget) if missing — UAC prompt
#   3. Clones the launcher repo to %USERPROFILE%\Desktop\kommissary-2.0-launcher
#      (or `git pull`s if it\u0027s already there)
#   4. Runs launcher.py
$ErrorActionPreference = "Stop"
Write-Host ""
Write-Host "Kommissary 2.0 Launcher - bootstrap" -ForegroundColor Cyan
Write-Host "------------------------------------"

function Has-Cmd($name) { return [bool](Get-Command $name -ErrorAction SilentlyContinue) }

if (-not (Has-Cmd "python")) {
    Write-Host "Installing Python 3 via winget..." -ForegroundColor Yellow
    winget install --id Python.Python.3.12 --accept-source-agreements --accept-package-agreements --silent
    # winget install adds to PATH for new shells; refresh env in this session
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
} else {
    Write-Host "Python found: $((& python --version) 2>&1)"
}

if (-not (Has-Cmd "git")) {
    Write-Host "Installing Git via winget..." -ForegroundColor Yellow
    winget install --id Git.Git --accept-source-agreements --accept-package-agreements --silent
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
} else {
    Write-Host "Git found:    $((& git --version) 2>&1)"
}

$dest = Join-Path $env:USERPROFILE "Desktop\kommissary-2.0-launcher"
$repoUrl = "https://github.com/chris-kommissary/kommissary-2.0-launcher.git"

if (Test-Path $dest) {
    Write-Host ""
    Write-Host "Updating existing install at $dest..." -ForegroundColor Yellow
    git -C $dest pull --quiet
} else {
    Write-Host ""
    Write-Host "Cloning launcher to $dest..." -ForegroundColor Yellow
    git clone --quiet $repoUrl $dest
}

Write-Host ""
Write-Host "Starting launcher..." -ForegroundColor Green
Start-Process -FilePath "python" -ArgumentList "$dest\launcher.py" -WorkingDirectory $dest
Write-Host "Done. The launcher window should be visible now."
