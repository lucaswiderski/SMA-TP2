import random

from pygame import Vector2

import core


class Item(object):
    def __init__(self):
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.etat=0

    def show(self):
        core.Draw.circle((0,255,0), self.position, 5)
