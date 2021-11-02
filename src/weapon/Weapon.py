import pygame
from bullet.Bullet import Bullet


class Weapon(pygame.sprite.Sprite):
    def __init__(self, position: tuple) -> None:
        super().__init__()
        self.sheet = pygame.image.load("src/weapon/WeaponR1.png")
        self.sheet.set_clip(pygame.Rect(0, 0, 64, 64))
        self.image = pygame.transform.scale(
            self.sheet.subsurface(self.sheet.get_clip()), (20, 20))
        self.rect = self.image.get_rect()
        self.rect.topleft = (position[0]+10, position[1]+10)
        self.frame = 0
        self.shooting = {0: (0, 0, 64, 64), 1: (64, 0, 64, 64), 2: (
            0, 64, 64, 64), 3: (64, 64, 64, 64), 4: (0, 128, 64, 64)}
        self.character = None
        self.balas_disparada = 0

    def update(self) -> None:
        if self.character is not None:
            self.update_pos(self.character.rect.x, self.character.rect.y)

    def update_pos(self, coord_x: int, coord_y: int) -> None:
        self.rect.x = coord_x+25
        self.rect.y = coord_y+20

    def get_frame(self, frame_set):
        self.frame += 1
        print(f"B {self.frame}")
        if self.frame > (len(frame_set) - 1):
            print(self.frame)
            self.frame = 0
        print(f"{frame_set[self.frame]}")
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            print("A")
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        return clipped_rect

    def shoot(self) -> Bullet:
        self.balas_disparada +=1
        for i in range(len(self.shooting)):
            self.clip(self.shooting)
            self.image = pygame.transform.scale(
                self.sheet.subsurface(self.sheet.get_clip()), (20, 20))
        bullet = Bullet((self.rect.x, self.rect.y+1))
        return bullet
