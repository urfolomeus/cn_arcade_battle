import pygame

from fighter import Fighter

pygame.init()

SCREEN_OPTS_WIDTH = 1000
SCREEN_OPTS_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_OPTS_WIDTH, SCREEN_OPTS_HEIGHT))
pygame.display.set_caption("Cartoon Network Arcade Battle")

# load bg image
bg_image = pygame.image.load("./assets/images/background/background.jpg").convert_alpha()


# function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_OPTS_WIDTH, SCREEN_OPTS_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


# create two instances of fighter
fighter_1 = Fighter(200, 310)
fighter_2 = Fighter(700, 310)

# game loop
run = True
while run:
    # draw background
    draw_bg()

    # draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display
    pygame.display.update()

# close out pygame once we exit our game
pygame.quit()
