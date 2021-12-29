import pygame
from bullet.Bullet import Bullet
from character.Character import Character
from level.Level import Level
from constant.constant import *
from sql.Connection import Connection

def text_box(background) -> str:
    """"""
    clock = pygame.time.Clock()
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    input_rect = pygame.Rect(200, 200, 140, 32)
    color = pygame.Color('lightskyblue3')
    exit_game = False
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
                if event.key == pygame.K_RETURN:
                    exit_game = True
        SCREEN.blit(background, (0,0))                
        pygame.draw.rect(SCREEN, color, input_rect, 2)
        text_surface = base_font.render(user_text, True, (255,255,255))  
        SCREEN.blit(text_surface, input_rect)
        pygame.display.update()
        clock.tick(FPS)
    return user_text
    

def start_text(background):
    """ Imprime el texto de inicio.

    Parameters
    ----------
    background: Surface
        Fondo del juego.
    
    """
    SCREEN.blit(background, (0,0))
    init_text = FONT_SMALL.render(
            "Press 'I' to START", True, (255, 255, 255))
    SCREEN.blit(init_text, (600, 680))
    exit_text = FONT_SMALL.render(
            "Press 'E' to EXIT", True, (255, 255, 255))
    SCREEN.blit(exit_text, (270, 680))

def main():
    """Función principal.
    """
    con = Connection()

    pygame.mixer.music.load('resources/sounds/init.mp3')
    pygame.mixer.music.set_volume(.5)
    pygame.mixer.music.play()
    background = pygame.image.load("resources/images/level/init.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    SCREEN.fill((255, 255, 255))
    score_level = 0
    exit_game = False
    nickname = text_box(background) 
    if nickname != '' or nickname != ' ':
        con.insert_player(nickname)
    else:
        return
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    exit_game = True
            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_e]:
                    exit_game = True
                if keys[pygame.K_i]:
                    pygame.mixer.music.stop()
                    n_level = 4
                    character = Character((0,200))
                    while True:
                        level = Level(character, n_level)
                        level.runnin_level()
                        character = level.character
                        character.health = 100
                        score_level = character.calculate_score()
                        character.bullets_shoot = 0 #contador de balas lanzadas
                        character.bullets_hit = 0 #contador de balas acertadas
                        con.modify_score(nickname, n_level + 1, score_level)
                        if n_level == 4: 
                            break
                        if level.isGameWin():
                            n_level = level.level + 1
                        if level.isGameOver():
                            break     
                            

        start_text(background)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()


main()
exit()