#This is console art for the game

def textArt():
    # Prints Text Art
    file = open("art.txt", "r")
    art = file.readlines()
    for line in art:
        print(line)
    file.close()