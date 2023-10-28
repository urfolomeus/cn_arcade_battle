import pygame


class Audio:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("./assets/audio/music.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1, 0.0, 5000)

        self.sword_fx = pygame.mixer.Sound("./assets/audio/sword.wav")
        self.sword_fx.set_volume(0.5)

        self.magic_fx = pygame.mixer.Sound("./assets/audio/magic.wav")
        self.magic_fx.set_volume(0.75)
