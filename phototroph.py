import pygame as pg
import numpy as np
from cell import Cell
from settings import Settings


class Сhemotroph(Cell):
    def __init__(self, settings, display, rect, velosity):
        super().__init__(settings, display, rect)
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
