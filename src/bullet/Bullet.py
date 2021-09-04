import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position: tuple) -> None:
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(
            "src/bullet/Bullet.png").convert(), (10, 10))
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self) -> None:
        self.rect.x += 20
        if self.rect.x == 1080:
            self.kill()
