import os

import pygame
import sys
from pygame import mixer


def music():
    mixer.init()
    if getattr(sys, 'frozen', False): #This is adding path for .exe conversion
        music = pygame.mixer.Sound(file=os.path.join(sys._MEIPASS, "sounds/music.wav"))
    else:
        music = pygame.mixer.Sound(file='sounds/music.wav')
    #mixer.music.load()
    music.set_volume(0.2)
    music.play(-1)
    #mixer.music.play(-1)

def correctSound():
    mixer.init()
    correct = pygame.mixer.Sound('sounds/correct.wav')
    correct.set_volume(0.7)
    correct.play()

def incorrectSound():
    mixer.init()
    incorrect = pygame.mixer.Sound('sounds/incorrect.wav')
    incorrect.set_volume(0.7)
    incorrect.play()

def gameOvertSound():
    mixer.init()
    incorrect = pygame.mixer.Sound('sounds/gameOver.wav')
    incorrect.set_volume(0.7)
    incorrect.play()
