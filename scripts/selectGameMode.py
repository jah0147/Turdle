import random
from bank import bank

freeLetter = [""]

def selectGamemode(gamemode):
    if gamemode == 1:
        f = open('files/settings.txt')
        gm = f.readlines()
        gm[4] = 'EASY\n'

        with open('files/settings.txt', 'w') as f:
            f.writelines(gm)
            f.close()
    elif gamemode == 2:
        f = open('files/settings.txt')
        gm = f.readlines()
        gm[4] = 'MEDIUM\n'
        with open('files/settings.txt', 'w') as f:
            f.writelines(gm)
            f.close()
    elif gamemode == 3:
        f = open('files/settings.txt')
        gm = f.readlines()
        gm[4] = 'HARD\n'
        with open('files/settings.txt', 'w') as f:
            f.writelines(gm)
            f.close()

def selectedGamemode(randWord):
    f = open('files/settings.txt')
    gm = f.readlines()

    if gm[4] == 'EASY\n':
        global freeLetter
        freeLetter.clear()
        freeLetter = bank()[2]
        length = len(randWord) - 1
        randNum1 = random.randint(0, 2)
        randNum2 = random.randint(3, length)
        tries = 10
        freeLetter[randNum1] = randWord[randNum1]
        freeLetter[randNum2] = randWord[randNum2]

        return tries, freeLetter

    elif gm[4] == "MEDIUM\n":
        tries = 8
        freeLetter.clear()
        freeLetter = bank()[2]
        randNum1 = random.randint(0, 4)

        freeLetter[randNum1] = randWord[randNum1]

        return tries, freeLetter

    elif gm[4] == "HARD\n":
        tries = 6
        return tries, freeLetter

# if __name__ == '__main__': #FOR TESTING
#     selectGamemode(2)
#     #selectedGamemode(randWord="hello")