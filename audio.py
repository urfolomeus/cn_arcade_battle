import pygame


class Audio:
    def setup(theme):
        pygame.mixer.init()
        pygame.mixer.music.load(theme["music"]["url"])
        pygame.mixer.music.set_volume(theme["music"]["volume"])
        pygame.mixer.music.play(-1, 0.0, 5000)

    def set_sound_effects(url, volume):
        sound_fx = pygame.mixer.Sound(url)
        sound_fx.set_volume(volume)
        return sound_fx
