import pygame
from bullet.Bullet import Bullet
from constant.constant import *

class Boss(pygame.sprite.Sprite):
    """Jefe del juego.
    """
    def __init__(self, position: tuple, images: tuple) -> None:
        super().__init__()
        self.images = images
        self.image = pygame.image.load(images[1])
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.topleft = position
        self.health = 250
        self.limit_left = -1
        self.limit_right = -1
        self.velocity = 5
        self.left = False
        self.right = True

    def update(self):
        self.move()
        self.difficulty()

    def move(self):
        """Actualiza los Sprite del enemigo en base a la velocidad.
        """
        if self.right and not self.left:
            self.image = pygame.image.load(self.images[1])
            self.rect.x += self.velocity
        elif self.left and not self.right:
            self.image = pygame.image.load(self.images[0])
            self.rect.x -= self.velocity

        if self.rect.x > WIDTH:
            self.right = False
            self.left = True
            self.rect.right = WIDTH
        if self.rect.x > self.limit_right:
            self.right = False
            self.left = True
            self.rect.right = self.limit_right
        
        if self.rect.x < self.limit_left:
            self.left = False
            self.right = True
            self.rect.x = self.limit_left
        if self.rect.left < 0:
            self.left = False
            self.right = True

            self.rect.left = 0
    
    def difficulty(self):
        """Varia la velocidad del jefe final en base a su vida
        """
        if 150 < self.health <= 250:
            self.velocity = 5
        elif 50 < self.health <= 150:
            self.velocity = 10
        elif 0 < self.health <= 50:
            self.velocity = 15

    def shoot(self):
        """Realiza un disparo.

        Returns
        -------
        bullet: Bullet
            Bala del disparo.
        """
        if 150 < self.health <= 250:
            return self.create_bullet()
        elif 50 < self.health <= 150:
            return self.create_bullet(15)
        elif 0 < self.health <= 50:
            return self.create_bullet(20)

    def create_bullet(self, velocity : int = 10):
        """Crea una bala.

        Parameters
        ----------
        velocity: int
            Velocidad de la bala, por defecto es 10
        
        Returns
        -------
        bullet: Bullet
            Bala del disparo
        """
        bullet = Bullet((self.rect.x+35, self.rect.y+19), 'resources/images/bullet/Bullet_b.png')
        bullet.velocity = velocity
        if self.right == True and self.left == False:
            bullet.set_direction('right')
        else:
            bullet.set_direction('left')
        return bullet