import pygame
from bullet.Bullet import Bullet
from character.Character import Character
from level.Level import Level

pygame.init()

def main():
    font_mid = pygame.font.SysFont("comicsansms", 50)
    font_small = pygame.font.SysFont("comicsansms", 20)
    font_v_small = pygame.font.SysFont("comicsansms", 14)
    width = 1080
    height = 720
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

        screen.fill((0, 55, 79))
        initmessage = font_mid.render("Fukushū", True, (254, 254, 254))
        centerInitMessage = initmessage.get_rect(center=(width / 2, height / 2))
        screen.blit(initmessage, centerInitMessage)
        init_text = font_small.render(
            "Press I to start", True, (255, 255, 255))
        screen.blit(init_text, (460, 400))
        """
        instruction1 = font_v_small.render(
            "Press P to pause", True, (0,0,0))
        screen.blit(instruction1, (10, 470))
        """
        exit_text = font_v_small.render(
            "Press E to exit", True, (255, 255, 255))
        screen.blit(exit_text, (475, 440))
        pygame.display.update()
        #level.collide_character_platform()

        clock.tick(75)
    pygame.quit()


main()
print("FIN")
exit()