import pygame
#from pygame.locals import *
from pygame import mixer

def soundSettings(setting): #changing sound settings in text file
    if setting == 0:
        f = open('files/settings.txt')
        music = f.readlines()
        music[10] = 'OFF\n'
        with open('files/settings.txt', 'w') as f:
            f.writelines(music)
            f.close()
        f = open('files/settings.txt')
        soundFX = f.readlines()
        soundFX[13] = 'OFF\n'
        with open('files/settings.txt', 'w') as f:
            f.writelines(soundFX)
            f.close()
    elif setting == 1:
        f = open('files/settings.txt')
        music = f.readlines()
        music[10] = 'ON\n'
        with open('files/settings.txt', 'w') as f:
            f.writelines(music)
            f.close()
        f = open('files/settings.txt')
        soundFX = f.readlines()
        soundFX[13] = 'ON\n'
        with open('files/settings.txt', 'w') as f:
            f.writelines(soundFX)
            f.close()
    elif setting == 2:
        f = open('files/settings.txt')
        music = f.readlines()
        music[10] = 'OFF\n'
        with open('files/settings.txt', 'w') as f:
            f.writelines(music)
            f.close()
    elif setting == 3:
        f = open('files/settings.txt')
        music = f.readlines()
        music[10] = 'ON\n'
        with open('files/settings.txt', 'w') as f:
            f.writelines(music)
            f.close()
    elif setting == 4:
        f = open('files/settings.txt')
        soundFX = f.readlines()
        soundFX[13] = 'OFF\n'
        with open('files/settings.txt', 'w') as f:
            f.writelines(soundFX)
            f.close()
    elif setting == 5:
        f = open('files/settings.txt')
        soundFX = f.readlines()
        soundFX[13] = 'ON\n'
        with open('files/settings.txt', 'w') as f:
            f.writelines(soundFX)
            f.close()

def music():
    f = open('files/settings.txt')
    play = f.readlines()
    mixer.init()
    music = pygame.mixer.Sound('sounds/music.wav')
    if play[10] == "ON\n":
        music.set_volume(0.2)
        music.play(-1)
    elif play[10] == "OFF\n":
        mixer.stop()

def correctSound():
    f = open('files/settings.txt')
    soundFX = f.readlines()

    if soundFX[13] == 'ON\n':
        mixer.init()
        correct = pygame.mixer.Sound('sounds/correct.wav')
        correct.set_volume(0.7)
        correct.play()

def incorrectSound():
    f = open('files/settings.txt')
    soundFX = f.readlines()

    if soundFX[13] == 'ON\n':
        mixer.init()
        incorrect = pygame.mixer.Sound('sounds/incorrect.wav')
        incorrect.set_volume(0.7)
        incorrect.play()

def gameOvertSound():
    f = open('files/settings.txt')
    soundFX = f.readlines()

    if soundFX[13] == 'ON\n':
        mixer.init()
        incorrect = pygame.mixer.Sound('sounds/gameOver.wav')
        incorrect.set_volume(0.7)
        incorrect.play()
