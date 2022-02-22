set PATH=%PATH%;C:\Program Files\Git\bin

git init
git remote origin https://github.com/jah0147/turdle
git reset --hard origin/main
git pull https://github.com/jah0147/turdle
pause

@echo off
for /f "tokens=*" %%s in (finishedUpdate.txt) do (
  echo %%s
)
pause

cd scripts
python turdle.py