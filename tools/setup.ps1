param(
    [string]$PythonExe
)

$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot
$venvPython = Join-Path $repoRoot '.venv\Scripts\python.exe'

if (-not (Test-Path -LiteralPath $venvPython)) {
    if ($PythonExe) {
        & $PythonExe -m venv --without-pip (Join-Path $repoRoot '.venv')
    } elseif (Get-Command py -ErrorAction SilentlyContinue) {
        & py -3 -m venv --without-pip (Join-Path $repoRoot '.venv')
    } elseif (Get-Command python -ErrorAction SilentlyContinue) {
        & python -m venv --without-pip (Join-Path $repoRoot '.venv')
    } else {
        throw 'Python 3.9 or newer is required. Install Python, then rerun tools/setup.ps1.'
    }
}

& $venvPython -m unittest discover -s (Join-Path $repoRoot 'tools') -p 'test_*.py'
Write-Host "Python environment is ready: $venvPython"
