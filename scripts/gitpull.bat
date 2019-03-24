@echo off
cd %~dp0
cd ..
git pull -q
git log --pretty="%%h - %%s" -1
