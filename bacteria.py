import pygame as pg
import numpy as np
from pygame.sprite import Sprite
from settings import Settings


class Cell(Sprite):
    def __init__(self, settings, display, velosity):
        super().__init__()
        self.disp = display
        self.settings = settings
        self.x, self.y = self.disp.get_rect().center
        self.v = velosity

    def update(self):
        cur = pg.mouse.get_pos()
        dist = ((cur[0] - self.x)**2 + (cur[1] - self.y)**2) ** 0.5

        if dist <= self.v:
            self.x, self.y = cur
        else:
            dir = cur[0] - self.x, cur[1] - self.y
            norm = np.linalg.norm(dir).item()
            dir = dir[0] / norm, dir[1] / norm
            self.x, self.y = self.x + dir[0] * self.v, self.y + dir[1] * self.v

    def draw_me(self):
        pg.draw.circle(self.disp, (0, 255, 0), (self.x, self.y), self.settings.cell_radius)
