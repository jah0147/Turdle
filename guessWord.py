# This module is the code for guessing the random word
import os

from randomWord import pickRandomWord
from compairLetters import compairCharAndLocation
from wordArrays import createArray
from bank import bank
from cheats import cheats
from quitGame import quitGame
from clearScreen import cls

# guessedWords = [] #stores words the user has guessed
guessedWords = bank()[0]
score = 0


def guessCompair(filename, word, tries,
                 incorrectBank, locationBankStorage, locationBank):
    global score
    word = str(word)
    allWords = []

    # clearScreen = lambda: print('\n' * 150) #This was a sopy way of clearning screen
    allWords = str(createArray(filename)).lower()

    print("please feel free to type '/quit' at any time to quit the game")

    while int(tries) > 0:
        usrInput = input("\nPlease input your guess: ")
        #will clear screen
        cls()

        if usrInput == "/quit":  #quits the game and clears score
            quitGame()

        if usrInput == "/cheats":  # enabes cheat menu
            tries = cheats(word, tries)

        # Make sure the user only inputs a 5 letter word
        while len(usrInput) != 5:
            print("\nPlease enter a word that is 5 characters long!")
            usrInput = input("\nPlease input your guess: ")
            # guessCompair(filename, word, tries)


        else:
            guessedWords.append(usrInput)
            guessedWords.sort()
            print("You guessed: ", guessedWords)

        tries = tries - 1  # Every try, count goes down

        if word.lower() == usrInput.lower():
            score += 1
            print("\nThat is Correct!")
            print("The word was: ", word)
            addScore()
            gameCompleted()  # Goes to end screen
            break

        elif tries > 0 and word.lower() != usrInput.lower():
            print("\nThat answer is incorrect. Please try again!")
            print("You have", tries, "tries left\n")
            compairCharAndLocation(word, usrInput,
                                   incorrectBank, locationBankStorage, locationBank)


        elif tries <= 0 and word.lower() != usrInput.lower():
            # If you run out of tries
            print("\nYou have ran out of tries!")
            print("The word was: ", word)

            # clears score
            f = open("keepScore.txt", "w")
            f.write(str(0))
            f.close()

            gameCompleted()
            break
    # return


def gameCompleted():
    print("\nYou have completed the game!")


def addScore():
    score = 1
    f = open("keepScore.txt", "r")
    fileScore = int(f.read())
    score += fileScore
    f.close()

    f = open("keepScore.txt", "w")
    f.write(str(score))
    f.close()

    f = open("keepScore.txt", "r")
    print("Your score is", f.read())
    f.close()
