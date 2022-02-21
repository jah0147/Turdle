#Quits the game at users request

def quitGame():
    #clears score
    f = open("keepScore.txt", "w")
    f.write(str(0))
    f.close()
    print("You chose to quit the game.\n"
          "----------GOODBYE----------")

    quit()  # quits the game