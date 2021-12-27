import pygame
from platform.Platform import Platform
from character.Character import Character
from enemy.Enemy import Enemy

GRAVEDAD = 9
class Level:
    def __init__(self, character: Character, level: int) -> None:
        self.character = character
        self.maps = ['resources/images/level/map_1.txt', 'resources/images/level/map_2.txt']
        self.path_background = ['resources/images/level/background_1.jpg', 'resources/images/level/background_2.jpg', 'resources/images/level/background_3.jpg', 'resources/images/level/background_4.jpg']
        self.level = level
        self.screen = None
        self.platform = self.generate_platform_map()
        self.background = pygame.transform.scale(pygame.image.load(self.path_background[level]), (1080, 720))
        self.bullets = pygame.sprite.Group()   
        self.bullets_enemy = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()
        self.cont = 0
        self.cant_enemys = level + 1
        self.generate_enemys()
        self.game_over_c = False
        self.game_win_c = False

        #ESCRIBIR EN PANTALLA
        self.font = pygame.font.Font("resources/fonts/minimal/Minimal3x5.ttf", 25)
        self.font_game_over = pygame.font.Font("resources/fonts/minimal/Minimal3x5.ttf", 55)
        self.white_blue = (20, 171, 245)

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

    def generate_enemys(self):
        for i in range(self.cant_enemys):
            self.enemy = Enemy((100, 669))
            self.enemys.add(self.enemy)

    def runnin_level(self, screen: pygame.Surface, height: int, width: int) -> bool:

        clock = pygame.time.Clock()
        while not self.game_over_c or not self.game_win_c:
            self.cont+=1
            if self.cont == 50:
                for e in self.enemys:
                    self.bullets_enemy.add(e.shoot())
                self.cont = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                keys = pygame.key.get_pressed()
                if event.type == pygame.KEYDOWN:
                    if keys[pygame.K_SPACE]:
                        character_shoot = self.character.shoot()
                        if character_shoot:
                            self.character.bullets_shoot += 1
                            self.bullets.add(character_shoot)

            platform_aux = pygame.sprite.spritecollideany(self.character, self.platform)
            if platform_aux:
                self.collide_platform(platform_aux)
            else:
                self.character.state_y = 'falling'

            if self.character.state_y == 'falling':
                self.character.velocity_y = self.character.falling_timer * GRAVEDAD
                self.character.rect.y += self.character.velocity_y
                self.character.falling_timer += 0.15
            elif self.character.state_y == 'jumping':
                self.character.jump()
            elif self.character.state_y == 'standing':
                self.character.velocity_y = 0
                self.character.jump_timer = 40
                self.character.falling_timer = 0

            if self.character.rect.left < 0:
                self.character.rect.left = 0
            elif self.character.rect.right > 1080:
                self.character.rect.right = 1080
            if self.character.rect.top < 0:
                self.character.rect.top = 0
            elif self.character.rect.bottom > 720:
                self.character.rect.bottom = 720
                self.character.state_y = 'standing'


            self.level_update(height)
            self.level_draw(screen)
            self.collide_bullet_with_enemy()
            self.collide_character_with_enemy()
            self.collide_bullet_with_character()
            self.show_score()

            if self.character_win():
                self.game_win()
                self.game_win_c = True
                return self.game_win_c
            if not self.character.isAlive():
                self.game_over()
                self.game_over_c = True
                return self.game_over_c

            clock.tick(75)
            pygame.display.update()

    def level_update(self, height: int):
        self.character.update(height)
        self.bullets.update()
        self.enemys.update(height)
        self.bullets_enemy.update()
        self.platform.update()

    def level_draw(self, screen: pygame.Surface):
        self.screen = screen
        screen.blit(self.background, (0,0))
        screen.blit(self.character.image, self.character.rect)
        self.enemys.draw(screen)
        self.bullets.draw(screen)
        self.bullets_enemy.draw(screen)
        self.platform.draw(screen)
        
    #No esta terminado
    def collide_character_with_platform(self):
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
        if bullet:
            self.character.health -= 10
            bullet.kill()

    def collide_bullet_with_enemy(self):
        enemy = pygame.sprite.groupcollide(self.bullets, self.enemys, True, False)
        if enemy:
            for key, values in enemy.items():
                enemy_c = enemy[key][0]
                enemy_c.health -= 10
                if enemy_c.health == 0:
                    enemy_c.kill()
                    self.cant_enemys -= 1
            self.character.bullets_hit += 1
    
    def collide_character_with_enemy(self):
        if pygame.sprite.spritecollideany(self.character, self.enemys):
            self.character.health -= 10
            if self.character.right:
                self.character.rect.x -= 20
            if self.character.left:
                self.character.rect.x += 20

    def character_win(self) -> bool:
        return self.character.isAlive() and self.cant_enemys == 0

    def show_score(self):
        if self.screen is not None:
            text = self.font.render("SCORE: " + str(self.character.calculate_score()), True,(0,0,0))
            self.screen.blit(text, (975, 690))

    def game_over(self):
        exit_lost = False
        if self.cant_enemys > 0:
            for e in self.enemys:
                e.kill()
        while not exit_lost:
            text = self.font_game_over.render("You Lose!!  Score: " + str(self.character.calculate_score()), True, (0,0,0))
            self.screen.blit(text, ((1080/2)-210, (720/2)-90))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_lost = True
            pygame.display.update()

    def game_win(self):
        exit_game_win = False
        while not exit_game_win:
            text = self.font_game_over.render("Win!!  Score: " + str(self.character.calculate_score()), True, (0,0,0))
            self.screen.blit(text, ((1080/2)-210, (720/2)-90))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game_win = True
            pygame.display.update()

    def collide_platform(self, platform_aux: Platform):
        if self.character.state_y == 'falling':
            self.character.rect.bottom = platform_aux.rect.top+1
            self.character.state_y = 'standing'

        elif self.character.state_y == 'jumping':
            self.character.rect.bottom = platform_aux.rect.top+1