import pygame
from bullet.Bullet import Bullet
from character.Character import Character
from level.Level import Level

pygame.init()

FONT_SMALL = pygame.font.SysFont("comicsansms", 20)

def start_text(screen, background):
    """ Imprime el texto de inicio.

    Parameters
    ----------
    screen: Surface
        Pantalla del juego.
    background: Surface
        Fondo del juego.
    
    """
    screen.blit(background, (0,0))
    init_text = FONT_SMALL.render(
            "Press 'I' to START", True, (255, 255, 255))
    screen.blit(init_text, (600, 680))
    exit_text = FONT_SMALL.render(
            "Press 'E' to EXIT", True, (255, 255, 255))
    screen.blit(exit_text, (270, 680))

def main():
    """Función principal.
    """
    background = pygame.image.load("resources/images/level/init.jpg")
    width = 1080
    height = 720
    background = pygame.transform.scale(background, (width, height))
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))
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
                        continue_game = level.runnin_level(screen, height, width)
                    else:
                        continue_game = level.runnin_level(screen, height, width)

        start_text(screen, background)
        pygame.display.update()

        clock.tick(75)
    pygame.quit()


main()
exit()