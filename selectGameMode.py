import random

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
    if gamemode == "1" or gamemode == "2" or gamemode == "3":
        gamemode = int(usrInput)
        return gamemode
    else:
        print("That is an invalid mode")
        selectMode()

def selectedGamemode(gamemode, randWord):
    if gamemode == 1:
        freeLetter = ["_","_","_","_","_"]
        randNum = random.randint(0, 4)
        tries = 10
        freeLetter[randNum] = randWord[randNum]
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