import random
from pygame.math import Vector2
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

    core.memory("centredecercle", Vector2(100,200))
    core.memory("rayonducercle", 100)
    core.memory("couleurducercle", (255, 0, 0, 127))

    core.memory("direction" ,Vector2(0,0))

    print("Setup END-----------")


def run():
    core.cleanScreen()
    #core.Draw.circle(core.memory("couleurducercle"), core.memory("centredecercle"), core.memory("rayonducercle"),10)
    #core.Draw.circle((255, 0, 0),(100,100), core.memory("rayonducercle"),10)

    core.Draw.rect((255,0,0,125),(100,100,10,10))
    core.Draw.rect((255,0,0),(110,100,10,10))

    core.Draw.ellipse((255,255,0,127),(100,100,100,100))
    core.Draw.ellipse((255,255,0),(300,100,100,100))


    if core.getKeyPressList("r") :
        core.memory("direction", Vector2(0, 0))

    if core.getKeyPressList("z") :
        core.memory("direction", Vector2(core.memory("direction").x, -1))
    if core.getKeyPressList("s") :
        core.memory("direction", Vector2(core.memory("direction").x, 1))
    if core.getKeyPressList("q") :
        core.memory("direction", Vector2(-1,core.memory("direction").y))
    if core.getKeyPressList("d") :
        core.memory("direction", Vector2(1,core.memory("direction").y))

    if core.memory("centredecercle").y  < 0  or core.memory("centredecercle").y > core.WINDOW_SIZE[1] :
        core.memory("direction", Vector2(core.memory("direction").x, core.memory("direction").y*-1))
        core.memory("couleurducercle", (random.randint(0,255),random.randint(0,255), random.randint(0,255)))

    if core.memory("centredecercle").x < 0 or core.memory("centredecercle").x > core.WINDOW_SIZE[0]:
        core.memory("direction", Vector2(core.memory("direction").x*-1, core.memory("direction").y ))
        core.memory("couleurducercle", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    core.memory("centredecercle" , core.memory("direction")+core.memory("centredecercle"))

    print(core.memory("direction").length())
core.main(setup, run)
