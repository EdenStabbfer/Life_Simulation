import pygame as pg
from game_functions import id_gen
import numpy as np
import pygame.gfxdraw


# Просто клетка (без подвида)
class Ball(pg.sprite.Sprite):
    def __init__(self, screen, rect, velocity):
        super().__init__()
        self.screen = screen
        self.rect = rect
        self.x, self.y = rect.centerx, rect.centery
        self.radius = rect.width//2
        self.velocity = velocity
        self.id = id_gen()

    def update(self):
        dir_x, dir_y = pg.mouse.get_pos()
        dist = ((dir_x - self.x)**2 + (dir_y - self.y)**2) ** 0.5

        if dist <= self.velocity:
            self.x, self.y = dir_x, dir_y
        else:
            dx = dir_x - self.x
            dy = dir_y - self.y
            norm = np.linalg.norm((dx, dy)).item()
            dx, dy = dx / norm, dy / norm
            self.x += dx * self.velocity
            self.y += dy * self.velocity

    def draw_me(self):
        pg.gfxdraw.aacircle(self.screen, int(self.x), int(self.y), self.radius, (0, 200, 0))
        pg.gfxdraw.filled_circle(self.screen, int(self.x), int(self.y), self.radius, (0, 200, 0))
