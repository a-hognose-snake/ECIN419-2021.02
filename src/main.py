import pygame
from bullet.Bullet import Bullet
from character.Character import Character
from level.Level import Level

pygame.init()

def main():
    width = 1080
    height = 720
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))
    character = Character((50, 50))
    salida = False
    level = Level(character, 0)
    while not salida:
        salida = level.runnin_level()
        level.level_update(height)
        level.level_draw(screen)
        level.collide_bullet_with_character()
        #level.collide_character_platform()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


main()
print("FIN")
exit()
