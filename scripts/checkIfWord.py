#This will check if the users input is a word in the word list
import re

from wordArrays import createArray
from cheats import cheats
from quitGame import quitGame
from clearScreen import cls
from bank import bank

def listToString(list):
    string = " "

    return (string.join(list))


def checkWord(filename, usrInput, randWord):
    list = createArray(filename)
    words = listToString(list).lower()

    #Checks if the length of words match
    while len(usrInput) != len(randWord):
        print("You typed: ", usrInput)
        print("That is not a word in the Word-Bank! Please try again.")

        usrInput = input("Input:")
        cls()  # clears screen

    #If length matches, we check to make sure the word exists
    while usrInput.lower() not in words:
        if usrInput == "/quit":  #quits the game and clears score
            quitGame(randWord)
            break

        else:
            print("You typed: ", usrInput)
            print("That is not a word in the Word-Bank! Please try again.")

            usrInput = input("Input:")
            cls() #clears screen

    return usrInput
