#This will be used as storange for users guessed wornds, correct, and incorrect letters

guessWords = []
incorrectBank = []
locationBankStorage = ["_","_","_","_","_"]
locationBank = ["_","_","_","_","_"] #stores correct positioned letters

def clearBank(continueGame):
    if continueGame == 1:
        guessWords.clear()
        incorrectBank.clear()
        locationBankStorage = ["_","_","_","_","_"]
        locationBank = ["_","_","_","_","_"] #stores correct positioned letters
        return guessWords, incorrectBank, locationBankStorage, locationBank

#global bank of words guessed and letters guessed
def bank():
    global guessWords
    global incorrectBank
    global locationBankStorage
    global locationBank

    guessWords = []
    incorrectBank = []
    locationBankStorage = ["_", "_", "_", "_", "_"]
    locationBank = ["_", "_", "_", "_", "_"]  # stores correct positioned letters

    return guessWords, incorrectBank, locationBankStorage, locationBank



