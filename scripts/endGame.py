#ends the game
import time

from delay import delay

def endGame(startTime):
    f = open("keepScore.txt", "r")
    fileScore = int(f.read())
    f.close()
    print("You scored ", fileScore, "points!")

    f = open("keepScore.txt", "w")
    f.write(str(0))
    f.close()

    seconds = 5 #time in seconds for delay
    startTime = int(startTime) #changing to int for cleanliness
    #print("\nYou finished the game with a score of", score)
    print("\nYou completed the game in", int(time.time()) - startTime, "seconds.")
    print("\nThe game will close in", seconds,  "seconds...")
    delay(seconds) #delays for amount in seconds
    quit() #quits the game