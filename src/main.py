import pygame
from bullet.Bullet import Bullet
from weapon.Weapon import Weapon
from character.Character import Character

pygame.init()


class Game():
    def __init__(self):
        self.width = 1080
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.bulletsCharacter = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        # self.weapons = pygame.sprite.Group()
        # self.background = pygame.Surface((self.width, self.height))
        self.screen.fill((255, 255, 255))
        self.salida = False
        self.run()

    def run(self):
        self.prota1 = Character((50, 50))
        # self.weapon = Weapon((self.prota1.rect.x, self.prota1.rect.y+10))
        # self.weapon.character = self.prota1
        # self.prota1.weapon = self.weapon
        # self.bullets.add(weapon)
        bullet = None
        while not self.salida:
            pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.salida = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bullets.add(self.prota1.shoot())

                # if pressed[pygame.K_SPACE]:
            # collide = pygame.sprite.spritecollide(weaponE, self.bullets, False)
            #    if colision:
            #    weaponE.rect.x = 3000
            #    weaponE.rect.y = 3000
            #    weaponE.kill()
            #    print("Colision")

            self.screen.fill((255, 255, 255))

            self.prota1.update()
            # self.weapon.update()
            self.screen.blit(self.prota1.image, self.prota1.rect)
            # self.screen.blit(self.weapon.image, self.weapon.rect)

            # self.weapons.update()
            # self.weapons.draw(self.screen)
            self.bullets.update()
            self.bullets.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(75)

        pygame.quit()


def execute():
    game = Game()


execute()
print("FIN")
exit()
