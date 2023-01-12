from pygame import Vector2
import random
import core
from fustrum import Fustrum

class Body(object):
    def __init__(self):
        self.masse = 5
        self.Vmax = 5
        self.Amax = 5
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.vitesse = Vector2()
        self.acc = Vector2()
        self.fustrum = Fustrum(150, self)

    def update(self):
        return
    def show(self):
        core.Draw.circle((125,255,0), self.position, self.masse)