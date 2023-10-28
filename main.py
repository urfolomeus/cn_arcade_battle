import pygame

from config import (
    FPS,
    RED,
    ROUND_OVER_COOLDOWN,
    SCREEN_WIDTH,
    SCREEN_HEIGHT)
from themes import DEFAULT_THEME
from audio import Audio
from fighter import Fighter
from game import Game
from screen import Screen

pygame.init()

# define game variables
game = Game()

# set framerate
clock = pygame.time.Clock()

# set theme
theme = DEFAULT_THEME

# set up the screen
screen = Screen(theme)

# load music and sounds
audio = Audio.setup(theme)


# define font
count_font = pygame.font.Font("./assets/fonts/turok.ttf", 80)
score_font = pygame.font.Font("./assets/fonts/turok.ttf", 30)


# create two instances of fighter
fighter_1 = Fighter(1, 200, 310, theme["fighter_1"])
fighter_2 = Fighter(2, 700, 310, theme["fighter_2"])

# game loop
run = True
while run:
    clock.tick(FPS)

    # draw background
    screen.draw_bg()

    # show player stats
    screen.draw_health_bar(fighter_1.health, 20, 20)
    screen.draw_health_bar(fighter_2.health, 580, 20)
    screen.draw_text("P1: " + str(game.score[0]), score_font, RED, 20, 60)
    screen.draw_text("P2: " + str(game.score[1]), score_font, RED, 580, 60)

    # update countdown
    if game.intro_count <= 0:
        # move fighters
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_2, game.round_over)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_1, game.round_over)
    else:
        # display count timer
        screen.draw_text(
            str(game.intro_count),
            count_font,
            RED,
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 3
        )

        # update count timer
        if (pygame.time.get_ticks() - game.last_count_update) >= 1000:
            game.intro_count -= 1
            game.last_count_update = pygame.time.get_ticks()

    # update fighters
    fighter_1.update()
    fighter_2.update()

    # draw fighters
    fighter_1.draw(screen.screen)
    fighter_2.draw(screen.screen)

    # check for player defeat
    if not game.round_over:
        if not fighter_1.alive:
            game.score[1] += 1
            game.round_over = True
            round_over_time = pygame.time.get_ticks()
        elif not fighter_2.alive:
            game.score[0] += 1
            game.round_over = True
            round_over_time = pygame.time.get_ticks()
    else:
        screen.draw_victory(360, 150)
        if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
            game.round_over = False
            game.intro_count = 3
            fighter_1.reset()
            fighter_2.reset()

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display
    pygame.display.update()

# close out pygame once we exit our game
pygame.quit()
