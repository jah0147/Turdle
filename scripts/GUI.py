#imports
import pygame, sys
from scripts.sounds import music
mainClock = pygame.time.Clock()
from pygame.locals import *
from tkinter import *

#script inports
from guessWord import guessCompair

pygame.init()
pygame.display.set_caption('Turdle')
width = 800
height = 900
screen = pygame.display.set_mode((width, height),0,32)
#creating icon
icon = pygame.image.load('images/turtle.png')
pygame.display.set_icon(icon)

font = pygame.font.SysFont(None, 20)
##############################
#Global Variables
click = False
tries = 10
filename = "words.txt"
##############################

#Menue Images
def backgroundImage():
    turtle = pygame.image.load('images/turtle.png')
    text = pygame.image.load('images/title.png')

    turtlePos = (150, 500) #pos of turtle
    textPos = (250, 5) #pos of text

    # #Resize
    turtleSize = (512, 512)
    turtle = pygame.transform.scale(turtle, turtleSize)

    screen.blit(text, textPos)
    screen.blit(turtle, turtlePos) #draws turtle

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)



def main_menu():
    music() #plays music

    while True:

        screenBackgroundColor = (204, 220, 204)
        screen.fill(screenBackgroundColor) #background color
        textColor = (255, 183, 142)
        draw_text('by Jacob Howard', font, textColor, screen, 350, 150)

        backgroundImage() #calls menue images to be loaded

        mx, my = pygame.mouse.get_pos() #x and y of mouse

        button_1 = pygame.Rect(300, 265, 200, 50) #creating button
        button_2 = pygame.Rect(310, 365, 180, 40)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (100, 52, 8), button_1) #button color and shape
        pygame.draw.rect(screen, (68, 39, 1), button_2)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def game(): #game window
    ############################
    #variables
    #global tries
    usrInput = []
    running = True
    ############################
    #Game UI
    while running:
        #Background
        screenBackgroundColor = (204, 220, 204)
        screen.fill(screenBackgroundColor)

        draw_text('game', font, (255, 255, 255), screen, 20, 20)

        #Load reg boxes
        box1 = pygame.image.load('images/tiles/defaultBox.png')
        box2 = pygame.image.load('images/tiles/defaultBox.png')
        box3 = pygame.image.load('images/tiles/defaultBox.png')
        box4 = pygame.image.load('images/tiles/defaultBox.png')
        box5 = pygame.image.load('images/tiles/defaultBox.png')

        #reg boxes possition
        box1Pos = (130, 50)  # pos of box
        box2Pos = (240, 50)  # pos of box
        box3Pos = (350, 50)  # pos of box
        box4Pos = (460, 50)  # pos of box
        box5Pos = (570, 50)  # pos of box

        # #Resize reg boxes
        box1Size = (100, 100)
        box2Size = (100, 100)
        box3Size = (100, 100)
        box4Size = (100, 100)
        box5Size = (100, 100)
        box1 = pygame.transform.scale(box1, box1Size)
        box2 = pygame.transform.scale(box2, box2Size)
        box3 = pygame.transform.scale(box3, box3Size)
        box4 = pygame.transform.scale(box4, box4Size)
        box5 = pygame.transform.scale(box5, box5Size)

        #draw reg boxes
        screen.blit(box1, box1Pos)
        screen.blit(box2, box2Pos)
        screen.blit(box3, box3Pos)
        screen.blit(box4, box4Pos)
        screen.blit(box5, box5Pos)


        ############################
        #In-Game
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:

                #if user presses ESC
                if event.key == K_ESCAPE:
                    quitPopUp() #Popup to quit game
                    running = False

                if len(usrInput) < 5: #making sure user only inputs 5 letter words
                    #Checking letters pressed
                    if event.key == K_a or event.key == K_b or event.key == K_c or \
                            event.key == K_d or event.key == K_e or event.key == K_f or \
                            event.key == K_g or event.key == K_h or event.key == K_i or \
                            event.key == K_j or event.key == K_k or event.key == K_l or \
                            event.key == K_m or event.key == K_n or event.key == K_o or \
                            event.key == K_p or event.key == K_q or event.key == K_r or \
                            event.key == K_s or event.key == K_t or event.key == K_u or \
                            event.key == K_v or event.key == K_w or event.key == K_x or \
                            event.key == K_y or event.key == K_z:

                        print(pygame.key.name(event.key)) #prints key pressed for debug
                        letter = (pygame.key.name(event.key))
                        #print(len(usrInput))

                        usrInput.append(letter)
                        print(len(usrInput))
                        print(usrInput)

                #checks if user wants to delete letters
                if event.key == K_BACKSPACE: #if user deletes letters
                    if len(usrInput) > 0:
                        usrInput.pop() #deletes a letter

                #If user presses enter to guess the 5 letter word
                if len(usrInput) == 5:
                    if event.key == K_RETURN: #If enter is pressed
                        guessedWord = ''.join(usrInput) #creates list to string
                        print(str(guessedWord)) #for testing

                        #compair guessed word to word here
                        guessCompair(filename, guessedWord, tries)

                        tries -= tries #subtracts tries every guess

        pygame.display.update()
        mainClock.tick(60)

def quitPopUp():
    print("") #ask if user wants to quit here

def options():
    running = True
    global tries #The options menu can change the ammount of tries
    while running:
        screen.fill((0, 0, 0))

        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

if __name__ == '__main__':
    main_menu()
    game()