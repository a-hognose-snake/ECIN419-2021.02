import pygame
from platform.Platform import Platform
from character.Character import Character

class Level():
    def __init__(self, character: Character, level: int) -> None:
        self.character = character
        self.maps = ['src/level/map_1.txt', 'src/level/map_2.txt']
        self.path_background = ['src/level/background_1.jpg', 'src/level/background_2.jpg', 'src/level/background_3.jpg', 'src/level/background_4.jpg']
        self.level = level
        self.platform = self.generate_platform_map()
        self.background = pygame.image.load(self.path_background[level])
        self.bullets = pygame.sprite.Group()   

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bullets.add(self.character.shoot())
        return False

    def level_update(self, height: int):
        self.character.update(height)
        self.bullets.update()
        self.platform.update()

    def level_draw(self, screen: pygame.Surface):
        screen.blit(self.background, (0,0))
        screen.blit(self.character.image, self.character.rect)
        self.bullets.draw(screen)
        self.platform.draw(screen)

    def collide_character_platform(self):
        platform: Platform = pygame.sprite.spritecollideany(self.character, self.platform)
        pressed = pygame.key.get_pressed()
        up = False
        if platform:
            if pressed[pygame.K_UP]:
                up = True
        else:
            self.character.rect.y += 2

        if up:
            self.character.rect.y = platform.rect.y - self.character.rect.width 
            up = False