import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position: tuple) -> None:
        super().__init__()
        self.image = pygame.image.load(
            "resources/images/bullet/Bullet.png")
        self.image.set_clip(pygame.Rect(0, 0, 10, 10))
        self.image = self.image.subsurface(self.image.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.direction = ''

    def update(self) -> None:
        if self.direction == 'left':
            self.rect.x -= 10
            if self.rect.x == 0:
                self.kill()
        elif self.direction == 'right':
            self.rect.x += 10
            if self.rect.x ==1080:
                self.kill()

    def set_direction(self, direction):
        self.direction = direction
