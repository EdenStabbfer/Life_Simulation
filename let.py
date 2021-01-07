import pygame as pg
from game_functions import id_gen
import pygame.gfxdraw


# Просто клетка (без подвида)
class Let(pg.sprite.Sprite):
    def __init__(self, screen, rect):
        super().__init__()
        self.screen = screen
        self.rect = rect
        self.x, self.y = rect.centerx, rect.centery
        self.radius = rect.width//2
        self.id = id_gen()

    def draw_me(self):
        pg.gfxdraw.aacircle(self.screen, int(self.x), int(self.y), self.radius, (0, 200, 0))
        pg.gfxdraw.filled_circle(self.screen, int(self.x), int(self.y), self.radius, (0, 200, 0))
