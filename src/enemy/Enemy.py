import pygame
from bullet.Bullet import Bullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, position: tuple) -> None:
        super().__init__()
        self.image = pygame.image.load("resources/images/enemy/7.png")
        self.image.set_clip(pygame.Rect(0, 0, 64, 64))
        self.image = self.image.subsurface(self.image.get_clip())
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.topleft = position
        self.health = 100
        
        self.path = [200, 720]
        self.countSteps = 0
        self.velocity = 3
        self.left = False
        self.right = False

    def update(self, height: int):
        self.move()
        if self.countSteps + 1 >= (3 * 4):
            self.countSteps = 0
            
        if self.velocity > 0:
            # walkRight
            self.countSteps += 1
        else:
            # walkLeft 
            self.countSteps += 1


    def move(self):
        if self.velocity > 0:
            # if we are moving right
            if self.rect.x < self.path[1] + self.velocity:
                self.left = False
                self.right = True
                # if we are not at the end of the path, keep moving
                self.image = pygame.image.load("resources/images/enemy/7.png")
                self.rect.x += self.velocity
            else:
                self.left = True
                self.right = False
                # else, change direction and move back the other way
                self.image = pygame.image.load("resources/images/enemy/4.png")
                self.velocity = self.velocity * -1
                self.rect.x += self.velocity
                self.countSteps = 0
        else:
            # if we are moving left
            if self.rect.x > self.path[0] - self.velocity:
                self.left = True
                self.right = False
                self.image = pygame.image.load("resources/images/enemy/4.png")
                # if we are not at the end of the path, keep moving
                self.rect.x += self.velocity
            else:  # else, change direction
                self.left = False
                self.right = True
                self.image = pygame.image.load("resources/images/enemy/7.png")
                self.velocity = self.velocity * -1
                self.rect.x += self.velocity
                self.countSteps = 0
                

    def shoot(self):
        bullet = Bullet((self.rect.x+35, self.rect.y+19))
        if self.right == True and self.left == False:
            bullet.set_direction('right')
        else:
            bullet.set_direction('left')
        return bullet