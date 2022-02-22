cd scripts
cd messages

pip install numpy
pip install pygame

winget install --id Git.Git -e --source winget

@echo off
for /f "tokens=*" %%s in (finishedInstallMessage.txt) do (
  echo %%s
)
pause