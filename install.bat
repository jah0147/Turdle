cd scripts
cd install

pip install numpy
pip install pygame

@echo off
for /f "tokens=*" %%s in (finishedInstallMessage.txt) do (
  echo %%s
)
pause