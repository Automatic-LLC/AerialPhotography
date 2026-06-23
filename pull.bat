@echo off
REM ============================================================
REM  pull.bat - Download the latest version from GitHub
REM  Double-click this to update this folder with whatever is
REM  on GitHub (the "main" branch).  This updates the WEBSITE.
REM ============================================================

cd /d "%~dp0"

echo ============================================================
echo   Pulling latest from GitHub  (origin/main)
echo   Folder: %cd%
echo ============================================================
echo.

git pull origin main

echo.
if %errorlevel%==0 (
    echo  Done - this folder is now up to date.
) else (
    echo  Something went wrong above. Read the message, or ask for help.
)
echo.
pause
