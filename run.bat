set PATH=%PATH%;C:\Program Files\Git\bin

git init
git remote add origin https://github.com/jah0147/turdle
git fetch origin
git reset --hard origin/v1

REM Finished updating the game!
REM If you see an error that git was not recognized, please run the install.bat file and install Git
REM If you still receive an error, please go to https://git-scm.com/downloads to download and install Git. Install git to C:\Program Files\Git\bin
pause

cd scripts
python turdle.py
