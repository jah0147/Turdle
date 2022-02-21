#Lets user select wordbank

def wordBank():
    # Text Files
    customWords = "customWords.txt"
    testFile = "testFile.txt"
    mainFile = "words.txt"
    wow = "worldOFwords.txt"
    explicit = "explicitWords.txt"
    four = "4LetterWords.txt"

    # Choose a word-bank
    fileInput = input("\n What word-bank would you like to use?\n"
                      "(leave this blank to use the main word-bank)\n"
                      "Input:")
    if fileInput.lower() == "custom":
        filename = customWords
    elif fileInput.lower() == "test":
        filename = testFile
    elif fileInput.lower() == "wow":
        filename = wow
    elif fileInput.lower() == "x":
        filename = explicit
    # elif fileInput.lower() == "4" or "four":
    #     filename = four
    elif fileInput.lower() == "" or "main":
        filename = mainFile
    else:
        filename = mainFile

    path = 'wordbank/' + filename

    print("You are using the", filename, "word list!\n")
    return path