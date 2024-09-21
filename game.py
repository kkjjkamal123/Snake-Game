import pygame
import time

pygame.init()

# Resolution for the display
X = 1000
Y = 760

display = pygame.display.set_mode((X,Y))

# Event Handler
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           False()
        
pygame.quit()