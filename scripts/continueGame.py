def continueGame():
    f = open("keepScore.txt", "r")
    fileScore = int(f.read())
    f.close()

    if fileScore > 0:
        print("Your current score is", fileScore)
        usrInput = input("\nWould you like to continue the game?\n"
                          "y or n:")
        if usrInput == "y":
            return int(1)
    else:
        usrInput = input("\nWould you like to play again?\n"
                         "Type y or n:")
        if usrInput == "y":
            return int(1)
        else:
            return int(0)
        return int(0) #making sure a value is retuned