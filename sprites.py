import pygame as pg
from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.vx = 0
        self.vy = 0
        self.acc = 0

    def update(self):
        self.acc = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc = PLAYER_ACC

        self.acc += self.vx * PLAYER_FRICTION
        self.vx += self.acc
        self.rect.x += int(self.vx + 0.5 * self.acc)
        self.rect.y += self.vy

        if self.rect.x > WIDTH:
            self.rect.x = 0
        if self.rect.right < 0:
            self.rect.right = WIDTH
