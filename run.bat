set PATH=%PATH%;C:\Program Files\Git\bin

git init
git remote add origin https://github.com/jah0147/turdle
git fetch origin
git reset --hard origin/main

@echo off
for /f "tokens=*" %%s in (finishedUpdate.txt) do (
  echo %%s
)
pause

cd scripts
python turdle.py
