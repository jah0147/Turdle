:: This will install Python
REM Now installing Python 3
REM Please check 'Add Python to PATH' when installing
REM
REM Press No if you already have Python 3 installed
pause
winget install -e --id Python.Python.3

:: This will use the pip command to install required packages
REM Installing required Python Libraries
pip install numpy
pip install pygame
REM Python Libraries installed!
REM
REM If you recieved an error that command pip was not found,
REM please reinstall Python3 and check to Include Python in PATH
 pause
REM Installing Git for updating game
REM If you have Git installed, please press No
 pause
winget install --id Git.Git -e --source winget
