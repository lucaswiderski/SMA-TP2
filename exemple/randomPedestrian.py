import random
from pygame.math import Vector2, Vector3
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 600]


    core.memory("bobPosition", Vector3(0, 0,0))
    core.memory("origine",Vector2(400,300))
    core.memory("bobHistorique", [])


    print("Setup END-----------")




def run():
    core.cleanScreen()
    if core.getKeyPressList("r"):
        core.memory("bobPosition", Vector3(0, 0, 0))
        core.memory("bobHistorique", [])

    if len(core.memory("bobHistorique"))>1:
        core.Draw.lines((255,255,255),False,core.memory('bobHistorique'),3)

    drawBob()
    moveBob()
    core.printMemory()

def drawBob():
    p1 = Vector2(core.memory("bobPosition").x,core.memory("bobPosition").y) + Vector2(-5, 0).rotate(180-core.memory("bobPosition").z)
    p1.y = -p1.y
    p1 = p1 + core.memory("origine")
    p2 = Vector2(core.memory("bobPosition").x,core.memory("bobPosition").y) + Vector2(0, -15).rotate(180-core.memory("bobPosition").z)
    p2.y = -p2.y
    p2 = p2 + core.memory("origine")
    p3 = Vector2(core.memory("bobPosition").x,core.memory("bobPosition").y) + Vector2(5, 0).rotate(180-core.memory("bobPosition").z)
    p3.y = -p3.y
    p3 = p3 + core.memory("origine")

    core.Draw.polygon((255, 0, 0), ((p1), (p2), (p3)))

def moveBob():
    core.memory("bobHistorique").append(Vector2(core.memory("bobPosition").x,-core.memory("bobPosition").y)+ core.memory("origine"))

    vel = Vector2(random.randint(-10,10),random.randint(-10,10))
    angle =( vel.angle_to(Vector2(0, 1)) + core.memory("bobPosition").z ) % 360
    posx = core.memory("bobPosition").x +vel.x
    posy = core.memory("bobPosition").y + vel.y
    core.memory("bobPosition",Vector3(posx,posy,angle))





core.main(setup, run)
