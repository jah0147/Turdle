#imports
import pygame, sys
from scripts.sounds import music
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()

pygame.display.set_caption('Turdle')
width = 600
height = 600
screen = pygame.display.set_mode((width, height),0,32)

#creating icon
icon = pygame.image.load('images/turtle.png')
pygame.display.set_icon(icon)

font = pygame.font.SysFont(None, 20)

#Menue Images
def backgroundImage():
    turtle = pygame.image.load('images/turtle.png')
    text = pygame.image.load('images/title.png')

    turtlePos = (50, 250) #pos of turtle
    textPos = (150, 5) #pos of text

    # #Resize
    # turtleSize = (100, 100)
    # turtle = pygame.transform.scale(turtle, turtleSize)

    screen.blit(text, textPos)
    screen.blit(turtle, turtlePos) #draws turtle

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    music() #plays music

    while True:

        screenBackgroundColor = (204, 220, 204)
        screen.fill(screenBackgroundColor) #background color
        textColor = (255, 183, 142)
        draw_text('by Jacob Howard', font, textColor, screen, 250, 150)

        backgroundImage() #calls menue images to be loaded

        mx, my = pygame.mouse.get_pos() #x and y of mouse

        button_1 = pygame.Rect(200, 175, 200, 50) #creating button
        button_2 = pygame.Rect(210, 500, 180, 40)
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


def game():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def options():
    running = True
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