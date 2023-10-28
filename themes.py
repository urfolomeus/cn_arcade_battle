import pygame

DEFAULT_THEME = {
    "background": "./assets/images/background/background.jpg",
    "victory": "./assets/images/icons/victory.png",
    "music": {
        "url": "./assets/audio/music.mp3",
        "volume": 0.5
    },
    "fighter_1": {
        "sprite_sheet": "./assets/images/warrior/Sprites/warrior.png",
        "sound": {
            "fx": "./assets/audio/sword.wav",
            "volume": 0.5
        },
        "size": 162,
        "scale": 4,
        "offset": [72, 56],
        "animation_steps": [10, 8, 1, 7, 7, 3, 7],
        "keys": {
            "left": pygame.K_a,
            "right": pygame.K_d,
            "jump": pygame.K_w,
            "attack_1": pygame.K_r,
            "attack_2": pygame.K_t
        }
    },
    "fighter_2": {
        "sprite_sheet": "./assets/images/wizard/Sprites/wizard.png",
        "sound": {
            "fx": "./assets/audio/magic.wav",
            "volume": 0.75
        },
        "size": 250,
        "scale": 3,
        "offset": [112, 107],
        "animation_steps": [8, 8, 1, 8, 8, 3, 7],
        "keys": {
            "left": pygame.K_LEFT,
            "right": pygame.K_RIGHT,
            "jump": pygame.K_UP,
            "attack_1": pygame.K_n,
            "attack_2": pygame.K_m
        }
    }
}
