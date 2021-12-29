import pygame


class Bullet(pygame.sprite.Sprite):
    """Bala disparada por el jugador/enemigo.
    """
    def __init__(self, position: tuple, image: str) -> None:
        super().__init__()
        self.image = pygame.image.load(image)
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
