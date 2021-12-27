import pygame


class Platform(pygame.sprite.Sprite):
    """Plataformas disponibles en un nivel.
    """
    def __init__(self, position: tuple, ex: str) -> None:
        super().__init__()
        if ex == 'L':
            self.get_left_platform(position)
        elif ex == 'M':
            self.get_middle_platform(position)
        elif ex == 'R':
            self.get_right_platform(position)

    def get_left_platform(self, position: tuple) -> None:
        """Crea la plataforma correspondiente al lado izquierdo.

        Parameters
        ----------
        position: tuple
            Posición en donde se va a posicionar la plataforma.
        """
        self.image = pygame.image.load('resources/images/platform/left.png')
        self.image.set_clip(pygame.Rect(0, 0, 20, 15))
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def get_right_platform(self, position: tuple) -> None:
        """Crea la plataforma correspondiente al lado derecho.

        Parameters
        ----------
        position: tuple
            Posición en donde se va a posicionar la plataforma.
        """
        self.image = pygame.image.load('resources/images/platform/right.png')
        self.image.set_clip(pygame.Rect(0, 0, 20, 15))
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def get_middle_platform(self, position: tuple) -> None:
        """Crea la plataforma correspondiente al centro.

        Parameters
        ----------
        position: tuple
            Posición en donde se va a posicionar la plataforma.
        """
        self.image = pygame.image.load('resources/images/platform/middle.png')
        self.image.set_clip(pygame.Rect(0, 0, 20, 15))
        self.rect = self.image.get_rect()
        self.rect.topleft = position
