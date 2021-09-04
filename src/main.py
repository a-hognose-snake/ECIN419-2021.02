import pygame
from bullet.Bullet import Bullet


pygame.init()


class Game():
    def __init__(self):
        self.width = 1080
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.bullets = pygame.sprite.Group()
        self.background = pygame.Surface((self.width, self.height))
        self.salida = False
        self.run()

    def run(self):
        while not self.salida:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.salida = True
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_SPACE]:
                    bullet = Bullet((50, 50))
                    self.bullets.add(bullet)

            self.screen.blit(self.background, (0, 0))
            self.bullets.update()
            self.bullets.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


def execute():
    game = Game()


execute()
print("FIN")
exit()
