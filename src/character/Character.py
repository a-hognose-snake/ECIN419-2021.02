import pygame
from bullet.Bullet import Bullet


class Character(pygame.sprite.Sprite):
    def __init__(self, position: tuple) -> None:
        super().__init__()
        self.front = ["resources/images/character/2.png"]
        self.left_move = ["resources/images/character/3.png", "resources/images/character/4.png"]
        self.right_move = ["resources/images/character/1.png", "resources/images/character/0.png"]
        self.image = pygame.image.load(self.front[0])
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.topleft = position
        self.health = 100
        self.left = False
        self.right = False
        self.platform = None
        self.velocity = 5
        self.velocity_y = 0
        self.didJump = False
        self.countJumps = 10

        self.falling_timer = 0
        self.state_y = 'falling'
        self.jump_timer = 0

        self.bullets_shoot = 0 #contador de balas lanzadas
        self.bullets_hit = 0 #contador de balas acertadas

    """ def jump(self):
        pressed = pygame.key.get_pressed()
        if not self.didJump:
            if pressed[pygame.K_w]:
                self.state_y = 'jumping'
                self.didJump = True
                    
        else:
            if self.countJumps >= -10:
                neg = 1
                if self.countJumps < 0:
                    neg = -1
                self.rect.y -= (self.countJumps ** 2) * 0.5 * neg
                self.countJumps -= 2
            else:
                self.didJump = False
                #self.state_y == 'falling'
                self.countJumps = 10 """
    def jump(self):
        self.rect.y += self.velocity_y

    def update(self, height: int) -> None:
        #self.jump()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            if self.state_y == 'standing':
                print('a')
                self.state_y = 'jumping'
                print(self.state_y)
        else:
            if self.state_y == 'jumping':
                print('b')
                self.state_y = 'falling'
                print(self.state_y)
        if self.jump_timer <= 0:
            self.state_y = 'falling'

        """         if pressed[pygame.K_f] and self.rect.y > - 10:
            self.rect.y -= self.velocity_y """
        
        if pressed[pygame.K_s] and self.rect.y < 720 - 64 - self.velocity:
            self.rect.y += self.velocity

        if pressed[pygame.K_a] and self.rect.x > -21:
            self.left = True
            self.right = False
            self.move_sprite('left', pressed)
            
        elif pressed[pygame.K_d] and self.rect.x < 1080 - 43 - self.velocity:
            self.left = False
            self.right = True
            self.move_sprite('right', pressed)
        else:
            self.image = pygame.image.load(self.front[0])

    def move_sprite(self, pos, pressed):
        if pos == 'left':
            self.left = True
            self.rect.x -= self.velocity
            if not pressed[pygame.K_SPACE]:
                self.image = pygame.image.load(self.left_move[0])
            else:
                self.image = pygame.image.load(self.left_move[1])

        if pos == 'right':
            self.right = True
            self.rect.x += self.velocity
            if not pressed[pygame.K_SPACE]:
                self.image = pygame.image.load(self.right_move[0])
            else:
                self.image = pygame.image.load(self.right_move[1])
    
    def shoot(self):
        bullet = Bullet((self.rect.x, self.rect.y+12))
        if self.right:
            bullet.set_direction('right')
            return bullet
        if self.left:
            bullet.set_direction('left')
            return bullet

    def isAlive(self):
        return self.health > 0

    def kill_character(self) -> bool:
        if self.health == 0:
            self.kill()
            return True
        return False
        
    def collide(self, other):
        return self.rect.colliderect(other)

    def calculate_score(self) -> int:
        if self.bullets_shoot == 0:
            return 0
        else:
            return int((self.bullets_hit/self.bullets_shoot) * 100)