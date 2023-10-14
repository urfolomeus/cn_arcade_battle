import pygame

from config import (
    FPS,
    RED,
    ROUND_OVER_COOLDOWN,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    WARRIOR_ANIMATION_STEPS,
    WARRIOR_DATA,
    WHITE,
    WIZARD_ANIMATION_STEPS,
    WIZARD_DATA,
    YELLOW)
from fighter import Fighter
from game import Game

pygame.mixer.init()
pygame.init()

# define game variables
game = Game()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cartoon Network Arcade Battle")

# set framerate
clock = pygame.time.Clock()

# load music and sounds
pygame.mixer.music.load("./assets/audio/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)

sword_fx = pygame.mixer.Sound("./assets/audio/sword.wav")
sword_fx.set_volume(0.5)

magic_fx = pygame.mixer.Sound("./assets/audio/magic.wav")
magic_fx.set_volume(0.75)

# load bg image
bg_image = pygame.image.load("./assets/images/background/background.jpg").convert_alpha()

# load sprite sheets
warrior_sheet = pygame.image.load("./assets/images/warrior/Sprites/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("./assets/images/wizard/Sprites/wizard.png").convert_alpha()

# load victory image
victory_img = pygame.image.load("./assets/images/icons/victory.png").convert_alpha()

# define font
count_font = pygame.font.Font("./assets/fonts/turok.ttf", 80)
score_font = pygame.font.Font("./assets/fonts/turok.ttf", 30)


# function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


# function for drawing health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))


# create two instances of fighter
fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)

# game loop
run = True
while run:
    clock.tick(FPS)

    # draw background
    draw_bg()

    # show player stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)
    draw_text("P1: " + str(game.score[0]), score_font, RED, 20, 60)
    draw_text("P2: " + str(game.score[1]), score_font, RED, 580, 60)

    # update countdown
    if game.intro_count <= 0:
        # move fighters
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, game.round_over)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, game.round_over)
    else:
        # display count timer
        draw_text(
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
    fighter_1.draw(screen)
    fighter_2.draw(screen)

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
        screen.blit(victory_img, (360, 150))
        if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
            game.round_over = False
            game.intro_count = 3
            # reset fighters by just creating new ones
            fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
            fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display
    pygame.display.update()

# close out pygame once we exit our game
pygame.quit()
