import core
from player import Player
from balle import Balle


def setup():
    core.WINDOW_SIZE = [600,400]
    core.fps = 30
    core.memory("j1",Player("J1",10,200))
    core.memory("j2", Player("J2", 580, 200))

    core.memory("balle", Balle())


def edge(j):
    if j.position.y<0:
        j.position.y=0
    if j.position.y+j.hauteur>core.WINDOW_SIZE[1]:
        j.position.y = core.WINDOW_SIZE[1]-j.hauteur


def run():
    core.cleanScreen()
    if core.getKeyPressList("r"):
        core.memory("j1", Player("J1", 10, 200))
        core.memory("j2", Player("J2", 580, 200))

        core.memory("balle", Balle())

    core.memory("j1").show(100)
    core.memory("j2").show(400)

    core.memory("balle").show()

    core.memory("balle").update()
    core.memory("balle").collision(core.memory("j1"),core.memory("j2"))
    core.memory("balle").out(core.memory("j1"),core.memory("j2"))



    if core.getKeyPressList("a"):
        core.memory("j1").up()
    if core.getKeyPressList("q"):
        core.memory("j1").down()

    if core.getKeyPressList("p"):
        core.memory("j2").up()
    if core.getKeyPressList("m"):
        core.memory("j2").down()

    edge(core.memory("j2"))
    edge(core.memory("j1"))


core.main(setup,run)