import random
from clearScreen import cls

#Select the game difficulty
def selectMode():
    gamemode = 0
    print("\n-----------------------------"
          "\nPLEASE SELECT YOUR GAMEMODE\n")
    print("EASY - TYPE 1\n"
          "MEDIUM - TYPE 2\n"
          "HARD - TYPE 3"
          "\n-----------------------------\n")

    usrInput = input("input:")
    gamemode = usrInput

    #Makse sure user enters a correct input
    while usrInput != str("1") and usrInput != str("2") and usrInput != str("3"):
        cls() #clears screen
        print("EASY - TYPE 1\n"
              "MEDIUM - TYPE 2\n"
              "HARD - TYPE 3"
              "\n-----------------------------\n")
        print("That is an invalid mode! Please enter 1, 2, or 3")
        usrInput = input("Input:")
        gamemode = usrInput

    if gamemode == "1" or gamemode == "2" or gamemode == "3":
        gamemode = int(usrInput)
        return int(gamemode)

def selectedGamemode(gamemode, randWord):
    if gamemode == 1:
        freeLetter = ["_","_","_","_","_"]
        randNum = random.randint(0, 4)
        tries = 10
        freeLetter[randNum] = randWord[randNum]

        cls() #clears screen
        print("-----------------EASY MODE-----------------\n"
              "You will be given a random letter in the word and 10 tries\n"
              , freeLetter)
        return tries

    elif gamemode == 2:
        tries = 8
        print("-----------------Medium MODE-----------------\n"
              "You will be given 8 tries\n")
        return tries
    elif gamemode == 3:
        tries = 5
        print("-----------------HARD MODE-----------------\n"
              "You will be given 5 tries\n")
        return tries