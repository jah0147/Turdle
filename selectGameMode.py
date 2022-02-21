import random
from bank import bank
from clearScreen import cls

#Select the game difficulty
def selectMode():
    gamemode = 0
    print("\nPLEASE SELECT YOUR GAMEMODE"
          "\n-----------------------------")
    print("EASY - TYPE 1\n"
          "MEDIUM - TYPE 2\n"
          "HARD - TYPE 3"
          "\n-----------------------------\n")

    usrInput = input("input:")
    gamemode = usrInput

    #Makse sure user enters a correct input
    while usrInput != str("1") and usrInput != str("2") and usrInput != str("3"):
        cls() #clears screen
        print("\n-----------------------------"
              "EASY - TYPE 1\n"
              "MEDIUM - TYPE 2\n"
              "HARD - TYPE 3"
              "\n-----------------------------\n")
        print("That is an invalid mode! Please enter 1, 2, or 3")
        usrInput = input("Input:")
        gamemode = usrInput

    if gamemode == "1" or gamemode == "2" or gamemode == "3":
        gamemode = int(usrInput)
        return int(gamemode)

freeLetter = [""]
def selectedGamemode(gamemode, randWord):
    if gamemode == 1:
        global freeLetter
        freeLetter.clear()
        freeLetter = bank()[2]
        length = len(randWord) - 1
        randNum1 = random.randint(0, 2)
        randNum2 = random.randint(3, length)
        tries = 10
        freeLetter[randNum1] = randWord[randNum1]
        freeLetter[randNum2] = randWord[randNum2]

        cls() #clears screen
        print("-----------------EASY MODE-----------------\n"
              "\nYou will be given a random letter in the word and", tries, "tries\n")
        print("\nYour free letters are\n",
              freeLetter)
        return tries

    elif gamemode == 2:
        tries = 8
        freeLetter.clear()
        freeLetter = bank()[2]
        randNum1 = random.randint(0, 4)

        freeLetter[randNum1] = randWord[randNum1]
        cls()  # clears screen
        print("-----------------Medium MODE-----------------\n"
              "\nYou will be given 1 random letter and", tries, "tries\n")
        print("\nYour free letter is\n",
                freeLetter)
        return tries
    elif gamemode == 3:
        tries = 6
        cls()  # clears screen
        print("-----------------HARD MODE-----------------\n"
              "\nYou will be given", tries, "tries and no letters\n")
        return tries