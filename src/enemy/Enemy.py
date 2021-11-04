import pygame
from bullet.Bullet import Bullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, position: tuple) -> None:
        super().__init__()
        self.image = pygame.image.load(
            "src/enemy/sprite_enemy/7.png")
        self.image.set_clip(pygame.Rect(0, 0, 64, 64))
        self.image = self.image.subsurface(self.image.get_clip())
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.topleft = position

    def update(self) -> None:
        pass

    def shoot(self):
        bullet = Bullet((self.rect.x+35, self.rect.y+19))
        return bullet
