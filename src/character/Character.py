import pygame
from bullet.Bullet import Bullet


class Character(pygame.sprite.Sprite):
    def __init__(self, position: tuple) -> None:
        super().__init__()
        self.image = pygame.image.load(
            "src/character/sprite_character/gato_2.png")
        self.image.set_clip(pygame.Rect(0, 0, 64, 64))
        self.image = self.image.subsurface(self.image.get_clip())
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.topleft = position
        self.health = 100
        self.salto = 10

    def update(self, height: int) -> None:
        """
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.rect.y -= self.salto
        else:
            self.rect.y += 0
            #self.rect.y = self.rect.y + self.salto
        if pressed[pygame.K_DOWN]:
            self.rect.y += 2
        else:
            self.rect.y += 0
        if pressed[pygame.K_LEFT]:
            self.rect.x -= 2
        else:
            self.rect.x += 0
        if pressed[pygame.K_RIGHT]:
            self.rect.x += 2
        else:
            self.rect.x += 0
        """

        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y + self.rect.height >= height:
            self.rect.y = height - self.rect.height

    def shoot(self):
        bullet = Bullet((self.rect.x, self.rect.y+1))
        return bullet
