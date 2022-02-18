"""
        Turdle
This is a Word Guessing Game similar to Wordle.
    The Goal is to guess the word within 5 tries.
    Hints will be given after each guess until you run out of tries.

Author: Jacob Howard
Ver. 0.1
"""

#Python classes
import csv
import time

from numpy import loadtxt

#My Modules
from wordArrays import createArray
from randomWord import pickRandomWord
import guessWord
from guessWord import guessCompair


def testFileAndArray(filename): #testing Array Creation from textfile
    filename = filename

    words = createArray(filename)
    print("Array Length: ", len(words))
    print("\nCustom Word: ", words[5]) #change value to print a single word at that location
    print("\n-----------------------------------------"
          "Words in Array-----------------------------------------\n")
    print(words)

def testRandomWord(filename):
    randWord = pickRandomWord(filename)
    print("\n The random word chosen is:", randWord) #for testing
    return randWord

def testGuessCompair(filename, randWord, tries):
    word = randWord
    guessCompair(filename, word, tries)

def scoreCount(score):
    score +=1
    return score

def continueGame(score):
    print("Your current score is", score)
    usrInput = input("Would you like to continue the game?\n"
                     "y or n:")
    if usrInput == "y":
        main(score)
    else:
        return


def endGame(startTime):
    startTime = int(startTime) #changing to int for cleanliness
    #print("\nYou finished the game with a score of", score)
    print("\nYou completed the game in", int(time.time()) - startTime, "seconds.")

    quit() #quits the game



"""
------------------------------------------------------------------
----------------------Main Program Start--------------------------
------------------------------------------------------------------              
"""


def main():

    # Text Files
    customWords = "customWords.txt"
    testFile = "testFile.txt"
    mainFile = "words.txt"

    filename = testFile  # change the text file to change words
    print("You are using the", "'", filename, "'", "word list!\n")

    # Set varaibles -
    # These variables are called here so that they are consistent throughout the program.
    tries = 5
    randWord = pickRandomWord(filename)

    usrInput = input("Would you like to enable cheats?\n"
                     "y or n: ")
    if usrInput.lower() == "y":
        cheatcode = input("Please type in the cheat code: ")
        if cheatcode == "seethru":
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

    print("\nWELCOME TO TURDLE\n"
          "The goal of the game is to guess the 5-letter word in 5 tries or less.\n"
          "Good Luck!\n\n")

    guessCompair(filename, randWord, tries)
    return
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    startTime = time.time()  # starting time

    main()
    endGame(startTime)
