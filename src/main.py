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
    background = pygame.image.load("resources/images/level/init.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    SCREEN.fill((255, 255, 255))
    character = Character((0,200))
    exit_game = False
    level = Level(character, 0)
    continue_game = False
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    exit_game = True
            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_e]:
                    exit_game = True
                if keys[pygame.K_i]:
                    if continue_game:
                        character = Character((0,200))
                        level = Level(character, 0)
                        continue_game = level.runnin_level()
                    else:
                        continue_game = level.runnin_level()

        start_text(background)
        pygame.display.update()

        clock.tick(FPS)
    pygame.quit()


main()
exit()