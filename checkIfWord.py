#This will check if the users input is a word in the word list
from wordArrays import createArray
from cheats import cheats
from quitGame import quitGame
from clearScreen import cls

def checkWord(filename, usrInput):
    words = str(createArray(filename))

    while usrInput.lower() not in words.lower():
        if usrInput == "/quit":  #quits the game and clears score
            quitGame()
            break

        else:
            print("You typed: ", usrInput)
            print("That is not a word in the Word-Bank! Please try again.")
            usrInput = input("Input:")
            cls() #clears screen

    return usrInput