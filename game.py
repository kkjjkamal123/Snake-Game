import pygame
import time
from time import sleep
from pygame import display

pygame.init()

# Resolution for the display
X = 500
Y = 300

DISPLAY = display.set_mode((X,Y))
display.set_caption("MENU")

while True:
    
    # Backgroud Color
    DISPLAY.fill((202, 228, 241))

    # Event Handler
    for event in pygame.event.get():
        # Game Quits
        if event.type == pygame.QUIT:
           False()
    display.update()
    
pygame.quit()
