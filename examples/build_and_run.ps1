# examples\build_and_run.ps1 - build and run ParseExample on Windows (PowerShell)
Set-StrictMode -Version Latest
$here = Split-Path -Parent $MyInvocation.MyCommand.Definition
Push-Location $here\..\

# Clean
if (Test-Path examples_bin) { Remove-Item -Recurse -Force examples_bin }
New-Item -ItemType Directory -Force -Path examples_bin | Out-Null

# Clean old class files in source tree to prevent conflicts
if (Test-Path org\fmgroup\mediator\plugins\generators\z3\Z3Generator.class) {
    Remove-Item org\fmgroup\mediator\plugins\generators\z3\Z3Generator.class
}

# Compile
# Include Z3Generator explicitly to ensure recompilation
javac -cp ".;org" examples\ParseExample.java org\fmgroup\mediator\plugins\generators\z3\Z3Generator.java -d examples_bin
if ($LASTEXITCODE -ne 0) { Pop-Location; exit $LASTEXITCODE }

# Run - prefer examples_bin
java -cp "examples_bin;.;org" ParseExample
$rc = $LASTEXITCODE
Pop-Location
exit $rc
