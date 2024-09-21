import pygame
import time
from pygame import display

pygame.init()

# Resolution for the display
X = 500
Y = 300

DISPLAY = display.set_mode((X,Y))
display.set_caption("MENU")

# Event Handler
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           False()
        
pygame.quit()