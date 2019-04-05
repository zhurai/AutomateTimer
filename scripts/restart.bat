@echo off
cd %~dp0
start "" "C:\Program Files (x86)\AutoIt3\AutoIt3.exe" startup_bot.show.au3
cd %~dp0
cd ..
timeout /T 3 /NOBREAK
py bot.py
