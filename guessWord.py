#This module is the code for guessing the random word
import os

from randomWord import pickRandomWord
from compairLetters import compairCharAndLocation
from wordArrays import createArray

guessedWords = [] #stores words the user has guessed
score = 0

def guessCompair(filename, word, tries):
    global score
    word = str(word)
    allWords = []
    clearScreen = lambda: print('\n' * 150)
    allWords = str(createArray(filename)).lower()
    #allWords = str(allWords)
    #allWords = allWords.lower()

    while tries > 0:
        usrInput = input("\nPlease input your guess: ")
        clearScreen() #Clears up console somewhat

        # Make sure the user only inputs a 5 letter word
        if len(usrInput) != 5:
            print("\nPlease enter a word that is 5 characters long!")
            guessCompair(filename, word, tries)

        #Checks if the user typed a word in the word-set
        #This is only working with the words.txt file right now for some reason, so it will be commented out
        # if usrInput.lower() not in allWords:
        #     print("That is not a word in this word-set.\n"
        #           "Please try another word!")
        #     guessCompair(filename, word, tries)

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
            gameCompleted() #Goes to end screen
            break

        elif tries > 0 and word.lower() != usrInput.lower():
            print("\nThat answer is incorrect. Please try again!")
            print("You have", tries, "tries left\n")
            compairCharAndLocation(word, usrInput)


        elif tries <= 0 and word.lower() != usrInput.lower():
            #If you run out of tries
            print("\nYou have ran out of tries!")
            print("The word was: ", word)

            #clears score
            f = open("keepScore.txt", "w")
            f.write(str(0))
            f.close()

            gameCompleted()
            break
    #return

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