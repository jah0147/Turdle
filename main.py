"""
        Turdle
This is a Word Guessing Game similar to Wordle.
    The Goal is to guess the word within 5 tries.
    Hints will be given after each guess until you run out of tries.

Author: Jacob Howard
Ver. 0.1
"""

#Python classes
#import csv
import random
import time

#from numpy import loadtxt

#My Modules
from wordArrays import createArray
from randomWord import pickRandomWord
from continueGame import continueGame
from guessWord import guessCompair

tries = 0

#Select the game difficulty
def selectMode():
    gamemode = 0
    print("PLEASE SELECT YOUR GAMEMODE\n")
    print("EASY - TYPE 1\n"
          "MEDIUM - TYPE 2\n"
          "HARD - TYPE 3")
    usrInput = input()
    gamemode = int(usrInput)
    if gamemode == 1 or gamemode == 2 or gamemode == 3:
        #gamemode = usrInput
        return gamemode
    else:
        print("That is an invalid mode")
        selectMode()

def selectedGamemode(gamemode, randWord):
    if gamemode == 1:
        freeLetter = ["_","_","_","_","_"]
        randNum = random.randint(0, 4)
        tries = 10
        freeLetter[randNum] = randWord[randNum]
        print("-----------------EASY MODE-----------------\n"
              "You will be given a random letter in the word and 10 tries\n"
              , freeLetter)
        return tries

    elif gamemode == 2:
        tries = 8
        print("-----------------Medium MODE-----------------\n"
              "You will be given 8 tries\n")
        return tries
    elif gamemode == 3:
        tries = 5
        print("-----------------HARD MODE-----------------\n"
              "You will be given 5 tries\n")
        return tries

def wordBank():
    # Text Files
    customWords = "customWords.txt"
    testFile = "testFile.txt"
    mainFile = "words.txt"
    wow = "worldOFwords.txt"

    # Choose a word-bank
    fileInput = input("\nWhat word-bank would you like to use:")
    if fileInput.lower() == "custom":
        filename = testFile
    elif fileInput.lower() == "test":
        filename = testFile
    elif fileInput.lower() == "wow":
        filename = wow
    elif fileInput.lower() == "" or "main":
        filename = mainFile
    else:
        filename = mainFile
    # filename = testFile  # change the text file to change words
    print("You are using the", filename, "word list!\n")
    return filename

def endGame(startTime):
    f = open("keepScore.txt", "r")
    fileScore = int(f.read())
    f.close()
    print("You scored ", fileScore, "points!")

    f = open("keepScore.txt", "w")
    f.write(str(0))
    f.close()

    startTime = int(startTime) #changing to int for cleanliness
    #print("\nYou finished the game with a score of", score)
    print("\nYou completed the game in", int(time.time()) - startTime, "seconds.")

    quit() #quits the game

def cheats(randWord):
    usrInput = input("Would you like to enable cheats?\n"
                     "y or n: ")
    if usrInput.lower() == "y":
        cheatcode = input("Please type in the cheat code: ")
        if cheatcode == "word":
            print("\nCHEATS ENABLED\n")
            print("The random word is: ", randWord, "\n")  # For testing, prints the randomly generated word

        elif cheatcode == "debug":

            print("\nDEBUG ENABLED\n")
            inputTries = input("Input the amount of tries you would like: ")
            while not inputTries.strip().isdigit():
                inputTries = input("Please input a number: ")

            tries = int(inputTries)  # tries set to two for debugging
            print("\nYou input", inputTries, "tries.")
            print("The random word is: ", randWord, "\n")

        else:
            print("\nThat code is invalid!\n"
                  "Please enjoy the game with cheats disabled!\n")

"""
Global Variables
"""
filename = []


"""
------------------------------------------------------------------
----------------------Main Program Start--------------------------
------------------------------------------------------------------              
"""

def main():
    global tries
    print("\nWELCOME TO TURDLE\n"
          "The goal of the game is to guess the 5-letter word in 5 tries or less.\n"
          "Good Luck!\n\n")

    filename = wordBank()
    randWord = pickRandomWord(filename)
    cheats(randWord)
    gamemode = selectMode()
    tries = selectedGamemode(gamemode, randWord)

    print("\nThe game has picked a random 5 letter word\n")
    return filename, randWord, tries

#Main Structure if user wants to continue game
def mainCont(filename, tries):
    tries = tries
    filename = filename

    randWord = pickRandomWord(filename)
    cheats(randWord)
    print("\nThe game has picked a random 5 letter word\n")
    return filename, randWord, tries

if __name__ == '__main__':
    startTime = time.time()  # starting time

    #main() #main program
    mainOut = main()
    guessCompair(mainOut[0], mainOut[1], mainOut[2])
    cont = continueGame()

   #Loop if user wants to continue the game
    while cont == 1:
        mainContinue = mainCont(mainOut[0], mainOut[2])
        guessCompair(mainContinue[0], mainContinue[1], mainContinue[2])
        cont = continueGame()

    endGame(startTime) #ends game
