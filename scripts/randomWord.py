from wordArrays import createArray
import random

#This module generates a radom word from the Array

def pickRandomWord(filename):

    words = createArray(filename)
    arrayLength = len(words) #creates an int length of the array for boundaries

    # generates a random number within array boundaries
    randomNumber = random.randint(0, arrayLength-1)  #Arrays go from 0 to n-1

    randomWord = words[randomNumber] #generates a random word
    return randomWord