@echo off
cd %~dp0
cd ../..
cd WatchMe/Files
git pull -q
git log --pretty="%%h - %%s" -1
