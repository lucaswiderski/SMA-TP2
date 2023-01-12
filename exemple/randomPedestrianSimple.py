import random
from pygame.math import Vector2, Vector3
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 600]

    core.memory("bobPosition", Vector2(0, 0))
    core.memory("origine",Vector2(400,300))

    print("Setup END-----------")




def run():
    core.cleanScreen()
    if core.getKeyPressList("r"):
        core.memory("bobPosition", Vector2(0, 0))

    #DESSIN
    core.Draw.circle((255,0,0),core.memory("bobPosition") + core.memory("origine"),10)

    #DEPLACEMENT
    vel = Vector2(random.randint(-10, 10), random.randint(-10, 10))
    posx = core.memory("bobPosition").x + vel.x
    posy = core.memory("bobPosition").y + vel.y
    core.memory("bobPosition", Vector2(posx, posy))

    core.printMemory()





core.main(setup, run)
