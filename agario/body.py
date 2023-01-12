import random

from pygame import Vector2

import core
from fustrum import Fustrum


class Body(object):
    def __init__(self):
        self.position=Vector2(random.randint(0,core.WINDOW_SIZE[0]),random.randint(0,core.WINDOW_SIZE[1]))
        self.vitesse = Vector2()
        self.vMax=2
        self.accMax=10
        self.mass=10
        self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.fustrum=Fustrum(150,self)
        self.acc=Vector2()


    def update(self):
        if self.acc.length() > self.accMax/self.mass:
            self.acc.scale_to_length(self.accMax/self.mass)



        self.vitesse=self.vitesse+self.acc

        if self.vitesse.length() > self.vMax:
            self.vitesse.scale_to_length(self.vMax)

        self.position=self.position+self.vitesse
        core.Draw.line((255,255,255),self.position,self.position+self.acc*100,10)

        self.acc=Vector2()

        self.edge()


    def show(self):
        core.Draw.circle(self.color,self.position,self.mass)


    def edge(self):
        if self.position.x <=self.mass:
            self.vitesse.x *= -1
        if self.position.x+self.mass >= core.WINDOW_SIZE[0]:
            self.vitesse.x *= -1
        if self.position.y <= self.mass:
            self.vitesse.y *= -1
        if self.position.y +self.mass>= core.WINDOW_SIZE[1]:
            self.vitesse.y *= -1