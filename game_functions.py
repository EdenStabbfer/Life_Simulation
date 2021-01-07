import pygame as pg
from math import atan, cos, sin, pi

cells_numb = 0


def key_down_event(event):
    pass


def key_up_event(event):
    pass


def game_events():
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            quit()
        if e.type == pg.KEYDOWN:
            key_down_event(e)
        if e.type == pg.KEYUP:
            key_up_event(e)


def id_gen():
    global cells_numb
    cells_numb += 1
    return cells_numb - 1


def collision_detect(group1, group2):
    group1 = group1.copy()
    group2 = group2.copy()
    for spr1 in group1:
        for spr2 in group2:
            dist = ((spr2.x - spr1.x) ** 2 + (spr2.y - spr1.y) ** 2) ** 0.5
            collide_dist = spr1.radius + spr2.radius - dist
            if collide_dist >= 0:
                ix = spr2.x - spr1.x
                jy = spr2.y - spr1.y
                spr1.x -= collide_dist * ix / dist
                spr1.y -= collide_dist * jy / dist
