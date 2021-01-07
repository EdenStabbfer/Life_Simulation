import pygame as pg
import settings as st
import game_functions as gf
from ball import Ball
from let import Let

clock = pg.time.Clock()


def game_cicle():
    pg.init()
    pg.display.set_caption("Bacteria")
    screen = pg.display.set_mode(st.screen_size)

    moving_balls = pg.sprite.Group()
    for i in range(1):
        ball = Ball(screen, pg.rect.Rect(400, 400, 60, 60), 5)
        moving_balls.add(ball)

    barriers = pg.sprite.Group()
    let = Let(screen, pg.rect.Rect(screen.get_rect().centerx, screen.get_rect().centery, 100, 100))
    barriers.add(let)

    # Главный цикл
    while True:
        screen.fill(st.screen_color)

        gf.game_events()
        moving_balls.update()
        gf.collision_detect(moving_balls, barriers)
        for ball in moving_balls:
            ball.draw_me()
        for let in barriers:
            let.draw_me()

        pg.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    game_cicle()
