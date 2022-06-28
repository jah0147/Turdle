#from numpy import loadtxt

words = []

def createArray(filename): #change filename to any other filename containing words of length=5
    #words = loadtxt(filename, dtype=str, comments="#", delimiter="\n", unpack=False)

    #hack to run program without numpy functions
    file = open(filename, 'r')
    for line in file:
        words.extend(line.splitlines())

    if len(words) > 0:
        return words
    else: #Error checking to make sure words are in the text file
        print("--------ERROR--------\n"
              "No Words found in text file.\n"
              "Please make sure there is a list of words in the text file in the correct format.\n"
              "The game is shutting down...")
        quit()

# def testClass(words): #This is just used for testing
#     #print specific word
#     print(words[100]) #change number to print specific word
#
#     #print in order
#     for i in range(10): #Prints words in order for a certain range
#        print(words[i])
