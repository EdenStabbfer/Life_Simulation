import pygame as pg
from settings import Settings


class Cell(pg.sprite.Sprite):
    def __init__(self, settings, display):
        super().__init__()
        self.disp = display
        self.settings = settings
        self.rect = pg.rect.Rect(0, 0, Settings().cell_radius*2, Settings().cell_radius*2)
        self.x, self.y = self.disp.get_rect().center

    def draw_me(self):
        pg.draw.circle(self.disp, self.settings.cell_color, (self.x, self.y), self.settings.cell_radius)
