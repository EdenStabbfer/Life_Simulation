import pygame as pg
from bacteria import Bacteria
from settings import Settings

clock = pg.time.Clock()


def game_cicle():
    pg.init()
    pg.display.set_caption("Bacteria")
    settings = Settings()
    screen = pg.display.set_mode(settings.screen_size)

    bact = Bacteria(screen, 3)

    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                quit()

        screen.fill(settings.screen_color)
        bact.update()
        bact.draw_me()
        pg.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    game_cicle()
