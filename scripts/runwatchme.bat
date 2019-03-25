@echo off
cd ..\..\
cd WatchMe/Program
start "" WatchMe.exe
cd %~dp0
start "" "C:\Program Files (x86)\AutoIt3\AutoIt3.exe" startup_watchme.au3
exit
