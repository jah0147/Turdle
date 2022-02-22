#Quits the game at users request
from delay import delay

def quitGame(word):
    #clears score
    randomWord = word

    f = open("keepScore.txt", "w")
    f.write(str(0))
    f.close()
    print("You chose to quit the game.\n"
          "The word was", randomWord,
          "\nThe game will exit in 5 seconds..."
          "\n\n----------GOODBYE----------")
    delay(5)
    quit()  # quits the game