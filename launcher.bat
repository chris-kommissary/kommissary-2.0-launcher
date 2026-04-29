@echo off
REM Kommissary 2.0 - Utility Launcher (Windows)
REM Double-click this file to open the launcher.
cd /d "%~dp0"
python launcher.py
if %ERRORLEVEL% neq 0 (
  echo.
  echo Could not start launcher. Make sure Python 3 is installed and on PATH.
  echo Download from: https://www.python.org/downloads/
  pause
)
