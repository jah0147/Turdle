#This module is the code for guessing the random word
import time

from randomWord import pickRandomWord
from compairLetters import compairCharAndLocation


def guessCompair(filename, word, tries):
    word = str(word)
    startTime = time.time()

    while tries != 0:
        usrInput = input("\nPlease input your guess: ")
        print("You guessed: ", usrInput)

        if len(usrInput) != 5:
            print("\nPlease enter a word that is 5 characters long!")
            guessCompair(filename, word, tries)

        tries = tries-1 #Every try, count goes down
        if tries <= 0:
            #If you run out of tries
            print("\nYou have ran out of tries!")
            print("The word was: ", word)
            gameCompleted()

        elif word.lower() == usrInput.lower():
            print("\nThat is Correct!")
            print("The word was: ", word)
            gameCompleted() #Goes to end screen

        else:
            print("\nThat answer is incorrect. Please try again!")
            print("You have", tries, "tries left\n")
            compairCharAndLocation(word, usrInput)
            guessCompair(filename, word, tries) #loops back to guessCompare



        return



def gameCompleted():
    print("\nYou have completed the game!")
    return
    #quit()