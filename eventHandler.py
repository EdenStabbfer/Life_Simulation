import pygame as pg

class EventHandler:
    def __init__(self, settings):
        self.settings = settings

    def key_down_event(self, event):
        pass

    def key_up_event(self, event):
        pass

    def key_press_event(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                quit()
            if e.type == pg.KEYDOWN:
                self.key_down_event(e)
            if e.type == pg.KEYUP:
                self.key_up_event(e)

    def screen_update(self, screen, cells):
        screen.fill(self.settings.screen_color)
        for cell in cells:
            cell.draw_me()
        pg.display.flip()
