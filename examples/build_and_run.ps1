# examples\build_and_run.ps1 - build and run ParseExample on Windows (PowerShell)
Set-StrictMode -Version Latest
$here = Split-Path -Parent $MyInvocation.MyCommand.Definition
Push-Location $here\..\

# Compile
javac -cp .;org examples\ParseExample.java -d examples_bin
if ($LASTEXITCODE -ne 0) { Pop-Location; exit $LASTEXITCODE }

# Run
java -cp .;org;examples_bin ParseExample
$rc = $LASTEXITCODE
Pop-Location
exit $rc
