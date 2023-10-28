import pygame

from audio import Audio


class Fighter():
    def __init__(self, player, x, y, theme):
        self.player = player
        self.x = x
        self.y = y

        self.keys = theme["keys"]
        self.image_scale = theme["scale"]
        self.offset = theme["offset"]

        self.animation_list = self.load_images(theme)
        self.attack_sound = Audio.set_sound_effects(
            theme["sound"]["fx"], theme["sound"]["volume"])

        self.reset()

    def reset(self):
        self.rect = pygame.Rect((self.x, self.y, 80, 180))
        self.flip = self.player == 2
        # 0:idle 1:run 2:jump 3:attack1 4:attack2 5:hit 6:death
        self.action = 0
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.vel_y = 0
        self.running = False
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.attack_cooldown = 0
        self.hit = False
        self.health = 100
        self.alive = True

    def load_images(self, theme):
        # extract images from sprite sheet
        sprite_sheet = pygame.image.load(theme["sprite_sheet"]).convert_alpha()
        animation_list = []
        size = theme["size"]

        for y, animation in enumerate(theme["animation_steps"]):
            temp_img_list = []

            for x in range(animation):
                temp_img = sprite_sheet.subsurface(
                    x * size, y * size, size, size)
                scaled_img = pygame.transform.scale(
                    temp_img,
                    (size * self.image_scale, size * self.image_scale)
                )
                temp_img_list.append(scaled_img)

            animation_list.append(temp_img_list)

        return animation_list

    def move(self, screen_width, screen_height, target, round_over):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0

        self.running = False
        self.attack_type = 0

        # get keypresses
        key = pygame.key.get_pressed()

        if not self.attacking and self.alive and not round_over:
            # movement
            if key[self.keys["left"]]:
                dx = -SPEED
                self.running = True
            if key[self.keys["right"]]:
                dx = SPEED
                self.running = True

            # jump
            if key[self.keys["jump"]] and not self.jump:
                self.vel_y = -30
                self.jump = True

            # attack
            if key[self.keys["attack_1"]]:
                self.attack(target)
                self.attack_type = 1
            if key[self.keys["attack_2"]]:
                self.attack(target)
                self.attack_type = 2

        # apply gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        # ensure player stays on screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 110 - self.rect.bottom

        # ensure players face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        # apply cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        # update player position
        self.rect.x += dx
        self.rect.y += dy

    def update(self):
        # order is important here
        # I think because some actions block others
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_action(6)
        elif self.hit:
            self.update_action(5)
        elif self.attacking:
            # attack_type_1 == 3 and acttack_type_2 = 4
            if self.attack_type == 1:
                self.update_action(3)
            elif self.attack_type == 2:
                self.update_action(4)
        elif self.jump:
            self.update_action(2)
        elif self.running:
            self.update_action(1)
        else:
            self.update_action(0)

        animation_cooldown = 50
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animation_list[self.action]):
            if not self.alive:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
                if self.action == 3 or self.action == 4:
                    self.attacking = False
                    self.attack_cooldown = 20
                if self.action == 5:
                    self.hit = False
                    # if the player was in the middle of an attack
                    # then the attack is stopped
                    self.attacking = False
                    self.attack_cooldown = 20

    def attack(self, target):
        if self.attack_cooldown == 0:
            self.attacking = True
            self.attack_sound.play()

            attacking_rect = pygame.Rect(
                self.rect.centerx - (2 * self.rect.width * self.flip),
                self.rect.y,
                2 * self.rect.width,
                self.rect.height)

            if attacking_rect.colliderect(target.rect):
                target.health -= 10
                target.hit = True

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        coords = (
            self.rect.x - (self.offset[0] * self.image_scale),
            self.rect.y - (self.offset[1] * self.image_scale)
        )
        surface.blit(img, coords)
