import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position: tuple) -> None:
        super().__init__()
        self.image = pygame.image.load(
            "src/bullet/Bullet.png")
        self.image.set_clip(pygame.Rect(0, 0, 10, 10))
        self.image = self.image.subsurface(self.image.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self) -> None:
        self.rect.x += 20
        if self.rect.x == 1080:
            self.kill()
