# This module is the code for guessing the random word
import os

from randomWord import pickRandomWord
from compairLetters import compairCharAndLocation
from wordArrays import createArray
from bank import bank
from cheats import cheats
from quitGame import quitGame
from clearScreen import cls
from checkIfWord import checkWord
#sounds
from sounds import correctSound
from sounds import incorrectSound
from sounds import gameOvertSound
# guessedWords = [] #stores words the user has guessed
#guessedWords = bank()[0]
score = 0


def guessCompair(filename, word, tries,
                 incorrectBank, locationBankStorage, locationBank,
                 gamemode, guessedWords):
    global score
    word = str(word)
    allWords = []

    # clearScreen = lambda: print('\n' * 150) #This was a sopy way of clearning screen
    allWords = str(createArray(filename)).lower()

    print("please feel free to type '/quit' at any time to quit the game")

    while int(tries) > 0:
        usrInput = input("\nPlease input your guess: ")
        #will clear screen


        if usrInput == "/quit":  #quits the game and clears score
            quitGame(word)

        if usrInput == "/cheat":  # enabes cheat menu
            tries = cheats(word, tries)
            usrInput = input("\nPlease input your guess:")

        if gamemode != 1:
            usrInput = checkWord(filename, usrInput, word)

        cls()

        guessedWords.append(usrInput)
        guessedWords.sort()
        print("You guessed: ", guessedWords)

        tries = tries - 1  # Every try, count goes down

        if word.lower() == usrInput.lower():
            score += 1
            correctSound() #plays correct sound
            print("\nThat is Correct!")
            print("The word was: ", word)
            addScore(tries)
            gameCompleted()  # Goes to end screen
            break

        elif tries > 0 and word.lower() != usrInput.lower():
            incorrectSound() #plays inccorrect sound
            print("\nThat answer is incorrect. Please try again!")
            print("You have", tries, "tries left\n")
            compairCharAndLocation(word, usrInput,
                                   incorrectBank, locationBankStorage, locationBank)


        elif tries <= 0 and word.lower() != usrInput.lower():
            # If you run out of tries
            gameOvertSound() #plays game over sound

            print("\nYou have ran out of tries!")
            print("The word was: ", word)

            # clears score
            # f = open("keepScore.txt", "w")
            # f.write(str(0))
            # f.close()

            gameCompleted()
            break
    # return


def gameCompleted():
    print("\nYou have completed the game!")


def addScore(tries):
    score = tries + 1
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
