import pygame
from pygame.locals import *

pygame.init()

SCREEN_OPTS_WIDTH = 1000
SCREEN_OPTS_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_OPTS_WIDTH, SCREEN_OPTS_HEIGHT))
pygame.display.set_caption("Cartoon Network Arcade Battle")

# game loop
run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# close out pygame once we exit our game
pygame.quit()
