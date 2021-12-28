import pygame
from platform.Platform import Platform
from character.Character import Character
from enemy.Enemy import Enemy
from constant.constant import *
from random import randint

class Level:
    def __init__(self, character: Character, level: int) -> None:
        self.character = character
        self.maps = ['resources/images/level/map_1.txt', 
                    'resources/images/level/map_2.txt',
                    'resources/images/level/map_3.txt',
                    'resources/images/level/map_4.txt',
                    'resources/images/level/map_5.txt']
        self.path_background = ['resources/images/level/l_1.jpg', 
                                'resources/images/level/l_2.jpg', 
                                'resources/images/level/l_3.jpg', 
                                'resources/images/level/l_4.jpg', 
                                'resources/images/level/l_5.jpg']
        self.level = level
        self.enemys = pygame.sprite.Group()
        self.platform = self.generate_platform_map()
        self.background = pygame.transform.scale(pygame.image.load(self.path_background[level]), (1080, 720))
        self.bullets = pygame.sprite.Group()   
        self.bullets_enemy = pygame.sprite.Group()
        self.cont = 0
        self.cant_enemys = self.enemys.__len__()
        self.game_over = False
        self.game_win = False
        self.finished = False

        #ESCRIBIR EN PANTALLA
        self.font = pygame.font.Font("resources/fonts/minimal/Minimal3x5.ttf", 25)
        self.font_game_over = pygame.font.Font("resources/fonts/minimal/Minimal3x5.ttf", 55)
        self.white_blue = (20, 171, 245)

    def generate_platform_map(self) -> pygame.sprite.Group:
        """Genera las plataformas que se mostrarán en el nivel.

        Returns
        -------
        Group
            Plataformas del nivel.
        """
        map = open(self.maps[self.level])
        self.platform_aux = pygame.sprite.Group()
        x = 0
        y = 0
        coord_x_l = 0
        coord_x_r = 0
        for row in map:
            for column in row:
                if column == '1':
                    self.create_enemy(coord_x_r, coord_x_l, y)
                if column == 'l':
                    coord_x_l = x
                if column == 'r':
                    coord_x_r = x
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

    def create_enemy(self, coord_x_r, coord_x_l, y):
        """Crea enemigos en una posicion indicada.
        
        Parameters
        ----------
        coord_x_r: int
            Limite derecho en el cual se puede mover el enemigo
        coord_x_l: int
            Limite izquierdo en el cual se puede mover el enemigo.
        y: int
            Posición y del enemigo.
        """
        enemy = Enemy((((coord_x_r + coord_x_l)/2), y), ENEMYS_IMAGES[randint(0, len(ENEMYS_IMAGES)-1)])
        enemy.limit_left = coord_x_l
        enemy.limit_right = coord_x_r
        self.enemys.add(enemy)

    def runnin_level(self) -> bool:
        """Ejecuta el nivel que esté jugando el jugador.

        Returns
        -------
        Bool
            
        """
        clock = pygame.time.Clock()
        while not self.finished:
            self.cont+=1
            if self.cont == 50:
                for e in self.enemys:
                    self.bullets_enemy.add(e.shoot())
                self.cont = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.finished
                keys = pygame.key.get_pressed()
                if event.type == pygame.KEYDOWN:
                    if keys[pygame.K_SPACE]:
                        character_shoot = self.character.shoot()
                        if character_shoot:
                            self.character.bullets_shoot += 1
                            self.bullets.add(character_shoot)

            platform_aux = pygame.sprite.spritecollideany(self.character, self.platform)
            if platform_aux:
                self.update_coordinates(platform_aux)
            else:
                self.character.state_y = 'falling'
                
            self.update_status_character()
            self.update_position_character()
            self.level_update()
            self.level_draw()
            self.collide_bullet_with_enemy()
            self.collide_character_with_enemy()
            self.collide_bullet_with_character()
            self.show_score()

            enemy = pygame.sprite.groupcollide(self.platform, self.enemys, False, False)
            if enemy:
                for platform, values in enemy.items():
                    enemy_c = enemy[platform][0]
                    enemy_c.rect.bottom = platform.rect.top+1

            if self.character_win():
                self.win_game()
                self.game_over = False
                self.game_win = True
                self.finished = True
            if not self.character.isAlive():
                self.lost_game()
                self.game_win = False
                self.game_over = True
                self.finished = True

            clock.tick(FPS)
            pygame.display.update()

        return self.finished

    def isGameWin(self):
        return self.game_win

    def isGameOver(self):
        return self.game_over

    def update_status_character(self):
        """Actualiza a todos los estados del jugador.
        """
        if self.character.state_y == 'falling':
            self.character.velocity_y = self.character.falling_timer * GRAVITY
            self.character.rect.y += self.character.velocity_y
            self.character.falling_timer += 0.15
        elif self.character.state_y == 'jumping':
            self.character.jump()
        elif self.character.state_y == 'standing':
            self.character.velocity_y = 0
            self.character.jump_timer = 40
            self.character.falling_timer = 0

    def update_position_character(self):
        """Actualiza la posicion del jugador en base a los bordes de la pantalla.
        """
        if self.character.rect.left < 0:
            self.character.rect.left = 0
        elif self.character.rect.right > WIDTH:
            self.character.rect.right = WIDTH
        if self.character.rect.top < 0:
            self.character.rect.top = 0
        elif self.character.rect.bottom > HEIGHT:
            self.character.rect.bottom = HEIGHT
            self.character.state_y = 'standing'

    def level_update(self):
        """Actualiza a todos los elementos del juego.
        """
        self.character.update()
        self.bullets.update()
        self.enemys.update()
        self.bullets_enemy.update()
        self.platform.update()

    def level_draw(self):
        """Actualiza la vida del jugador en caso de que colisione una bala lanzada por un enemigo.
        """
        SCREEN.blit(self.background, (0,0))
        SCREEN.blit(self.character.image, self.character.rect)
        self.enemys.draw(SCREEN)
        self.bullets.draw(SCREEN)
        self.bullets_enemy.draw(SCREEN)
        self.platform.draw(SCREEN)
        
    def collide_bullet_with_character(self):
        """Actualiza la vida del jugador en caso de que colisione una bala lanzada por un enemigo.
        """
        bullet = pygame.sprite.spritecollideany(self.character, self.bullets_enemy)
        if bullet:
            self.character.health -= 10
            bullet.kill()

    def collide_bullet_with_enemy(self):
        """Actualiza la vida del enemigo en caso de que colisione con una bala lanzada por un jugador.
        """
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
        """Actualiza la vida del jugador en caso de que colisione con un enemigo.
        """
        if pygame.sprite.spritecollideany(self.character, self.enemys):
            self.character.health -= 10
            if self.character.right:
                self.character.rect.x -= 20
            if self.character.left:
                self.character.rect.x += 20

    def character_win(self) -> bool:
        """Verifica si el jugador gana o pierde.
        Returns
        -------
        True
            Si el jugador esta vivo y no hay enemigos.
        False
            Si el jugador no esta vivo.
        """
        return self.character.isAlive() and self.cant_enemys == 0

    def show_score(self):
        """Muestra el puntaje obtenido por el jugador.
        """
        if SCREEN is not None:
            text = self.font.render("SCORE: " + str(self.character.calculate_score()), True,(0,0,0))
            SCREEN.blit(text, (975, 690))

    def lost_game(self):
        """Se verifica si el jugador ha perdido la partida.
        """
        exit_lost = False
        if self.cant_enemys > 0:
            for e in self.enemys:
                e.kill()
        while not exit_lost:
            text = self.font_game_over.render("You Lose!!  Score: " + str(self.character.calculate_score()), True, (0,0,0))
            SCREEN.blit(text, ((WIDTH/2)-210, (HEIGHT/2)-90))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_lost = True
            pygame.display.update()

    def win_game(self):
        exit_game_win = False
        while not exit_game_win:
            text = self.font_game_over.render("Win!!  Score: " + str(self.character.calculate_score()), True, (0,0,0))
            SCREEN.blit(text, ((WIDTH/2)-210, (HEIGHT/2)-90))

            text_continue = self.font.render("Press 'ENTER' to continue...", True, (0,0,0))
            SCREEN.blit(text_continue, ((WIDTH/2)-190,(HEIGHT/2)- 20))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game_win = True
                keys = pygame.key.get_pressed()
                if event.type == pygame.KEYDOWN:
                    if keys[pygame.K_RETURN]:
                        exit_game_win = True

            pygame.display.update()

    def update_coordinates(self, platform_aux: Platform):
        """Actualiza la ubicacion del jugador en base a una plataforma.

        Parameters
        ----------
        platform_aux: Platform
            Plataforma con la cual esta colisionando el jugador.
            
        """
        if self.character.state_y == 'falling':
            self.character.rect.bottom = platform_aux.rect.top+1
            self.character.state_y = 'standing'

        elif self.character.state_y == 'jumping':
            self.character.rect.bottom = platform_aux.rect.top+1