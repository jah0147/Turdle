"""This portion will compare the users input string to the randomly generated word
    and let the user know what letters are in the correct position.
    This will give the user hints to how close they are to guessing the word.
"""
#Importing this to guessWord

incorrectBank = [] #Stores incorrect
locationBankStorage = ["_","_","_","_","_"]

#Compairs exact location of letters
def compairCharAndLocation(word, usrInput):
    rndWord = word #This is the random word that was generated
    size = min(len(usrInput), len(rndWord)) #Finds min length
    countLocation = 0
    countChar = 0

    #For console view
    locationBank = ["_","_","_","_","_"] #stores correct positioned letters
    charBank = []  # keeps similar letters that are out of order

    countCharBank = 0 #counter for charBank


    for i in range(size):
        if usrInput[i].lower() in rndWord.lower():
            if usrInput[i].lower() == rndWord[i].lower():
                locationBank[i] = usrInput[i] #For visuals in console
                locationBankStorage[i] = locationBank[i]
                countLocation +=1  # Updating the counter when characters are same at an index
            else:
                if usrInput[i] in charBank: #This is to check if a letter is already stored in this array
                    countChar += 1
                else: #If the letter needs to be stored and is not already stored in character bank
                    charBank.append(usrInput[i])
                    #charBank[countCharBank] = usrInput[i]
                    #countCharBank += 1
                    #countChar += 1

              #Stores incorrect words guessed
        else:
            if usrInput[i].lower() not in incorrectBank:
                incorrectBank.append(usrInput[i].lower())




    #Information that will be printed every time
    print("\nLetters in the correct Location")
    #print("['{}'{}'{}'{}'{}']".format(*locationBank))
    print("['{}'{}'{}'{}'{}']".format(*locationBankStorage))

    print("\nCorrect letters you have put in the wrong location")
    charBank.sort()
    #print("[{}{}{}{}]".format(*charBank))
    print(charBank)

    print("\nIncorrect Letters you have guessed")
    #charBank = str(charBank)

    incorrectBank.sort() #alphabetically sorts array
    print(incorrectBank)

    # print("\n\nThere is/are", countLocation, "letter(s) in the correct spot\n"
    # "and there is/are", countChar,"total similar letter(s)!")
    return