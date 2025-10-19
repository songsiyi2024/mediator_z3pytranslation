@echo off
REM Delegator: forward to tools\gradle\gradlew.bat
set SCRIPT_DIR=%~dp0
%SCRIPT_DIR%tools\gradle\gradlew.bat %*
