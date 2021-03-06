"""
        Turdle
This is a Word Guessing Game similar to Wordle.
    The Goal is to guess the word within 5 tries.
    Hints will be given after each guess until you run out of tries.

Author: Jacob Howard
Ver. 0.1
"""

#Python classes
import sys

sys.path.append('C:/Users/jacob/OneDrive/Desktop/Turtle/venv/Lib/site-packages/playsound.py')
import time
#from playsound import playsound #Plays music file at start of game


#from numpy import loadtxt

#My Modules
from randomWord import pickRandomWord
from continueGame import continueGame
from guessWord import guessCompair
from bank import clearBank
from bank import bank
from selectGameMode import selectMode
from selectGameMode import selectedGamemode
from wordBank import wordBank
from fullscreen import maximize_console
from sounds import music
from endGame import endGame
from art import textArt



"""
Global Variables
"""
filename = []
tries = 0 #sets current tries to 0

"""
------------------------------------------------------------------
----------------------Main Program Start--------------------------
------------------------------------------------------------------
"""

def main():

    music()
    maximize_console()
    #playsound('music.mp3', False)  # Plays music (commented out as was giving bugs)

    global tries
    textArt()
    print("\n--------------------------WELCOME TO TURDLE-------------------------\n"
          "The goal of the game is to guess the 5-letter word in 5 tries or less.\n"
          "----------------------------Good Luck!----------------------------\n\n")

    filename = wordBank()
    randWord = pickRandomWord(filename)
    #cheats(randWord)
    gamemode = selectMode()
    tries = selectedGamemode(gamemode, randWord)

    print("\nThe game has picked a random 5 letter word\n")
    return filename, randWord, tries, gamemode

#Main Structure if user wants to continue game
def mainCont(filename, tries, gamemode):
    tries = tries
    filename = filename

    randWord = pickRandomWord(filename)
    #cheats(randWord)

    print("\nThe game has picked a random 5 letter word\n")
    tries = selectedGamemode(gamemode, randWord)
    return filename, randWord, tries, gamemode

if __name__ == '__main__':

    startTime = time.time()  # starting time

    #main() #main program
    mainOut = main()
    cont = int(0)

    #Setting values that will be stored from users guesses
    incorrectBank = bank()[1]
    locationBankStorage = bank()[2]
    locationBank = bank()[3]
    guessedWords = bank()[0]

    guessCompair(mainOut[0], mainOut[1], mainOut[2],
                 incorrectBank, locationBankStorage, locationBank,
                 mainOut[3], guessedWords)

    cont = continueGame()

   #Loop if user wants to continue the game
    while cont == 1:
        mainContinue = mainCont(mainOut[0], mainOut[2], mainOut[3])

        #clears stored values that have been guessed
       #guessedWords = clearBank(cont)[0]
        incorrectBank = clearBank(cont)[1]
        locationBankStorage = clearBank(cont)[2]
        locationBank = clearBank(cont)[3]
        guessedWords = clearBank(cont)[0]

        guessCompair(mainContinue[0], mainContinue[1], mainContinue[2],
                     incorrectBank, locationBankStorage, locationBank,
                     mainContinue[3], guessedWords)
        cont = continueGame()

    endGame(startTime) #ends game
