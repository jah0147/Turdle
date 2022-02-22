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

    print("\033[A                             \033[A")  # clears 1 line in terminal
    #Checks if the length of words match
    while len(usrInput) != len(randWord):
        print("You typed: ", usrInput)
        print("That is not a word in the Word-Bank! Please try again.")

        usrInput = input("Input:")

        #Clears 3 lines of terminal and places cursor in correct location
        print ("\033[A                             \033[A")
        print("\033[A                             \033[A")
        print("\033[A                             \033[A")
        #cls()  # clears screen

        exp1 = usrInput.lower() not in words
        exp2 = len(usrInput) != len(randWord)
    #If length matches, we check to make sure the word exists and legth still matches
    while usrInput.lower() not in words \
            or len(usrInput) != len(randWord):
        if usrInput == "/quit":  #quits the game and clears score
            quitGame(randWord)
            break

        else:
            print("You typed: ", usrInput)
            print("That is not a word in the Word-Bank! Please try again.")

            usrInput = input("Input:")

            # Clears 3 lines of terminal and places cursor in correct location
            print("\033[A                             \033[A")
            print("\033[A                             \033[A")
            print("\033[A                             \033[A")
            #cls() #clears screen

    return usrInput
