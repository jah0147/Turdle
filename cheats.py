#If the user woould like cheats

def cheats(randWord):
    # usrInput = input("Would you like to enable cheats?\n"
    #                  "y or n: ")
    # if usrInput.lower() == "y":
        cheatcode = input("Please type in the cheat code: ")

        if cheatcode == "word":
            print("\nCHEATS ENABLED\n")
            print("The random word is: ", randWord, "\n")  # For testing, prints the randomly generated word

        elif cheatcode == "debug":

            print("\nDEBUG ENABLED\n")
            inputTries = input("Input the amount of tries you would like: ")
            while not inputTries.strip().isdigit():
                inputTries = input("Please input a number: ")

            tries = int(inputTries)  # tries set to two for debugging
            print("\nYou input", inputTries, "tries.")
            print("The random word is: ", randWord, "\n")

            return tries

        else:
            print("\nThat code is invalid!\n"
                  "Please enjoy the game with cheats disabled!\n")