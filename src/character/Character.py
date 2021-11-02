import pygame
from weapon.Weapon import Weapon


class Character(pygame.sprite.Sprite):
    def __init__(self, position: tuple) -> None:
        super().__init__()
        self.image = pygame.image.load(
            "src/character/Character.png")
        self.image.set_clip(pygame.Rect(0, 0, 60, 60))
        self.image = self.image.subsurface(self.image.get_clip())
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.topleft = position
        self.weapon = Weapon((self.rect.x, self.rect.y+10))
        self.weapon.character = self
        self.salto = 10

    def update(self) -> None:
        self.weapon.update()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.rect.y -= 4
        elif pressed[pygame.K_DOWN]:
            self.rect.y += 4
        else:
            self.rect.y += 0
        if pressed[pygame.K_LEFT]:
            self.rect.x -= 4
        elif pressed[pygame.K_RIGHT]:
            self.rect.x += 4
        else:
            self.rect.x += 0

    def shoot(self):
        if self.weapon is not None:
            return self.weapon.shoot()

    def jump(self) -> None:
        pressed = pygame.key.get_pressed()
        isJump = False
        if pressed[pygame.K_UP]:
            isJump = True
        if isJump:
            if self.salto >= -10:
                self.rect.y -= (self.salto * abs(self.salto)) * 0.5
                self.salto -= 1
            else:
                self.salto = 10
                isJump = False
