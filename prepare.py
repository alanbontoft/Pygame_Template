import os
import pygame as pg
import tools

import appdefs

DIRECT_DICT = {"UP"    : ( 0,-1),
               "RIGHT" : ( 1, 0),               
               "DOWN"  : ( 0, 1),
               "LEFT"  : (-1, 0)}


DIRECTIONS = ("UP", "RIGHT", "DOWN", "LEFT")


CONTROLS = {pg.K_UP    : "UP",
            pg.K_RIGHT : "RIGHT",
            pg.K_DOWN  : "DOWN",
            pg.K_LEFT  : "LEFT"}


# Set up environment.
os.environ['SDL_VIDEO_CENTERED'] = '1'
pg.init()
pg.mixer.init()
pg.font.init()
pg.display.set_caption(appdefs.CAPTION)
pg.display.set_mode(appdefs.SCREEN_SIZE)

# Load all graphics.
GFX = tools.load_all_gfx("rpgsprites")
