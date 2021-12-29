import pygame
pygame.init()

FONT_SMALL = pygame.font.SysFont("comicsansms", 20)
WIDTH = 1080
HEIGHT = 720
FPS = 60
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
GRAVITY = 9

#imagenes de los enemigos
ENEMYS_IMAGES = \
    [['resources/images/enemy/enemy_1_a.png', 'resources/images/enemy/enemy_1_b.png'],
    ['resources/images/enemy/enemy_2_a.png', 'resources/images/enemy/enemy_2_b.png'],
    ['resources/images/enemy/enemy_3_a.png', 'resources/images/enemy/enemy_3_b.png'],
    ['resources/images/enemy/boss/boss_1.png', 'resources/images/enemy/boss/boss_2.png']]