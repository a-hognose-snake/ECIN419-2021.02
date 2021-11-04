import pygame
from platform.Platform import Platform
from character.Character import Character
from enemy.Enemy import Enemy

class Level:
    def __init__(self, character: Character, level: int) -> None:
        self.character = character
        self.maps = ['src/level/map_1.txt', 'src/level/map_2.txt']
        self.path_background = ['src/level/background_1.jpg', 'src/level/background_2.jpg', 'src/level/background_3.jpg', 'src/level/background_4.jpg']
        self.level = level
        self.platform = self.generate_platform_map()
        self.background = pygame.image.load(self.path_background[level])
        self.bullets = pygame.sprite.Group()   
        self.bullets_enemy = pygame.sprite.Group()
        self.enemy = Enemy((200, 200))
        self.cont = 0

    def generate_platform_map(self) -> pygame.sprite.Group:
        map = open(self.maps[self.level])
        self.platform_aux = pygame.sprite.Group()
        x = 0
        y = 0
        for row in map:
            for column in row:
                if column == 'L':
                    platform = Platform((x, y), 'L')
                    self.platform_aux.add(platform)
                elif column == 'M':
                    platform = Platform((x, y), 'M')
                    self.platform_aux.add(platform)
                elif column == 'R':
                    platform = Platform((x, y), 'R')
                    self.platform_aux.add(platform)
                x += 20
            x = 0
            y += 15
        return self.platform_aux

    def runnin_level(self) -> bool:
        self.cont+=1
        if self.cont == 50:
            self.cont = 0
            self.bullets_enemy.add(self.enemy.shoot())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_SPACE]:
                    self.bullets.add(self.character.shoot())

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.character.rect.y -= 5
        if pressed[pygame.K_DOWN]:
            self.character.rect.y += 5    
        if pressed[pygame.K_LEFT]:
            self.character.rect.x -= 5
        else:
            self.character.rect.x += 0
        if pressed[pygame.K_RIGHT]:
            self.character.rect.x += 5
        else:
            self.character.rect.x += 0
        return False

    def level_update(self, height: int):
        self.character.update(height)
        self.bullets.update()
        self.enemy.update()
        self.bullets_enemy.update()
        #self.platform.update()

    def level_draw(self, screen: pygame.Surface):
        screen.blit(self.background, (0,0))
        screen.blit(self.character.image, self.character.rect)
        screen.blit(self.enemy.image, self.enemy.rect)
        self.bullets.draw(screen)
        self.bullets_enemy.draw(screen)
        #self.platform.draw(screen)

    def collide_character_platform(self):
        platform: Platform = pygame.sprite.spritecollideany(self.character, self.platform)
        pressed = pygame.key.get_pressed()
        up = False
        if platform:
            if pressed[pygame.K_UP]:
                up = True
        if up:
            self.character.rect.y = platform.rect.y - self.character.rect.width 
            up = False

    def collide_bullet_with_character(self):
        bullet = pygame.sprite.spritecollideany(self.character, self.bullets_enemy)
        print(self.character.health)
        if bullet:
            self.character.health -= 10
            bullet.kill()