import random
from pygame import Vector2
import core
class Creep(object):
    def __init__(self, c):
        self.uuid = c
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.masse = 1

    def show(self):
        core.Draw.circle((0,125,255), self.position, self.masse)