import pygame

from config import (RED, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, YELLOW)


class Screen(object):
    def __init__(self, theme):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Cartoon Network Arcade Battle")

        # load images
        self.bg_img = pygame.image.load(theme["background"]).convert_alpha()
        self.victory_img = pygame.image.load(theme["victory"]).convert_alpha()

    # function for drawing text
    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    # function for drawing background
    def draw_bg(self):
        scaled_bg = pygame.transform.scale(
            self.bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.blit(scaled_bg, (0, 0))

    # function for drawing health bars
    def draw_health_bar(self, health, x, y):
        ratio = health / 100
        pygame.draw.rect(self.screen, WHITE, (x - 2, y - 2, 404, 34))
        pygame.draw.rect(self.screen, RED, (x, y, 400, 30))
        pygame.draw.rect(self.screen, YELLOW, (x, y, 400 * ratio, 30))

    # function for drawing victory screen
    def draw_victory(self, x, y):
        self.screen.blit(self.victory_img, (x, y))
