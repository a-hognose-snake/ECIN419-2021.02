import pygame
from bullet.Bullet import Bullet
from character.Character import Character
from level.Level import Level
from constant.constant import *

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
    pygame.mixer.music.load('resources/sounds/init.mp3')
    pygame.mixer.music.set_volume(.5)
    pygame.mixer.music.play()
    background = pygame.image.load("resources/images/level/init.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    SCREEN.fill((255, 255, 255))
    character_point = 0
    exit_game = False
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
                    n_level = 0
                    character = Character((0,200))
                    while True:
                        print('while')
                        level = Level(character, n_level)
                        print(f'el nivel es: {level.level + 1}')
                        finish_level = level.runnin_level()
                        if finish_level:
                            if level.isGameWin():
                                character = level.character
                                character.health = 100
                                character_point += character.calculate_score()
                                n_level = level.level + 1
                            if level.isGameOver():
                                break      
                        else:
                            break  
        start_text(background)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()

    print(f'El puntaje total obtenido fue de:{character_point}')


main()
exit()