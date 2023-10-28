import pygame

BASE_DIR = "./assets/images/"
DEFAULT_THEME = {
    "background": "background/background.jpg",
    "fighter_1": "warrior/Sprites/warrior.png",
    "fighter_2": "wizard/Sprites/wizard.png",
    "victory": "icons/victory.png"
}


class Images():
    def __init__(self):
        self.theme = DEFAULT_THEME

    # load bg image
    def bg_image(self):
        return self.load_image(self.theme["background"])

    # load warrier sprite_sheet
    def warrior_sheet(self):
        return self.load_image(self.theme["fighter_1"])

    # load warrier sprite_sheet
    def wizard_sheet(self):
        return self.load_image(self.theme["fighter_2"])

    # load victory image
    def victory_image(self):
        return self.load_image(self.theme["victory"])

    def load_image(self, url):
        full_url = BASE_DIR + url
        return pygame.image.load(full_url).convert_alpha()
