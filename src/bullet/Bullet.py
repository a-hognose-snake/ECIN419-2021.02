import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position: tuple) -> None:
        super().__init__()

        # self.sheet = pygame.image.load("src/bullet/Bullet.png")
        # self.sheet.set_clip(pygame.Rect(0, 0, 80, 67))
        # self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image = pygame.transform.scale(pygame.image.load(
            "src/bullet/Bullet.png").convert(), (10, 10))
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self) -> None:
        self.rect.x += 20
        if self.rect.x == 1080:
            self.kill()
