import pygame
from bullet.Bullet import Bullet


pygame.init()
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
balas = pygame.sprite.Group()
background = pygame.Surface((1080, 720))
salida = False
while not salida:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salida = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            bala = Bullet((50, 50))
            balas.add(bala)

    screen.blit(background, (0, 0))
    balas.update()
    balas.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("FIN")
exit()
