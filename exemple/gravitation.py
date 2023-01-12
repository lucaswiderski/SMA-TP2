import random
from pygame.math import Vector2
import core


class Paricule:
    def __init__(self):
        self.pos = Vector2(random.randint(0,200),random.randint(0,200))
        self.vel = Vector2(random.uniform(10,15),0)
        self.acc = Vector2(0,0)
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.mass = 10
        self.maxAcc=0.5

    def applyforce(self,force):
        self.acc += force
        if self.acc.length() > self.maxAcc:
            self.acc.scale_to_length(self.maxAcc)

    def update(self):
        self.vel+=self.acc
        self.acc=Vector2(0,0)
        self.pos+=self.vel

    def show(self,screen):
        core.Draw.circle(self.color,self.pos,5)


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

    core.memory("Centre", Vector2(200,200))
    core.memory("rayon", 10)
    core.memory("mass", 10000)

    core.memory("particules",[])
    core.memory("particulesNb", 10)
    for i in range(0,core.memory("particulesNb")):
        core.memory("particules").append(Paricule())


    print("Setup END-----------")


def reset():
    core.memory("particules", [])
    for i in range(0, core.memory("particulesNb")):
        core.memory("particules").append(Paricule())


def run():
    core.cleanScreen()
    if core.getKeyPressList("r"):
        reset()
    if core.getMouseLeftClick():
        core.memory("Centre",Vector2(core.getMouseLeftClick()))


    for p in core.memory("particules"):
        u = core.memory("Centre")
        u = u - p.pos
        u = u.normalize()
        u=u*9.8*(p.mass*core.memory("mass"))/p.pos.distance_to(core.memory("Centre"))**2
        p.applyforce(u)
        p.update()
        core.Draw.line((255,0,0),p.pos,p.pos+u,1)

    for p in core.memory("particules"):
        p.show(core.screen)
    core.Draw.circle((255,255,255),core.memory("Centre"),core.memory("rayon"))

core.main(setup, run)
