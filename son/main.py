import random
from pygame.math import Vector2
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

    core.memory("son",core.Sound("son.mp3"))
    print("Setup END-----------")


def run():
    core.cleanScreen()

    if core.getKeyPressList("s"):
        core.memory("son").start()

    if core.getKeyPressList("r"):
        core.memory("son").rewind()

    if core.getKeyReleaseList("p"):
        core.memory("son").pause()

core.main(setup, run)
