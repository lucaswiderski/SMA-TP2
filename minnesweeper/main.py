import random
import time
import core
from minnesweeper.case import Case


def setup():
    print("Setup START---------")

    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    core.memory("width", 10)
    core.memory("height", 10)

    core.memory("mineCount", 10)
    core.memory("grid", [])

    reset()


    print("Setup END-----------")


def revealAll():
    for line in core.memory("grid"):
        for c in line:
            c.revealed=True

def run():
    core.cleanScreen()
    if core.getKeyPressList("r"):
        reset()

    if core.getMouseRightClick():
        for line in core.memory("grid"):
            for c in line:
                c.marked(core.getMouseRightClick())
        time.sleep(0.3)

    if core.getMouseLeftClick():
        for line in core.memory("grid"):
            for c in line:
                bee,neighbor = c.inside(core.getMouseLeftClick())
                if bee:
                    revealAll()
                if neighbor == 0:
                    neighborList=[c]
                    while(len(neighborList)>0):
                        print(neighborList)
                        i = neighborList[0]
                        neighborList.remove(i)
                        neighborList+=i.revealNeighbor(core.memory("width"), core.memory("height"), core.memory("grid"))



    for line in core.memory("grid"):
        for c in line:
            c.show()


def reset():
    core.memory("grid", [])
    for i in range(0, core.memory("width")):
        line = []
        for j in range(0, core.memory("height")):
            line.append(Case(i, j))
        core.memory("grid").append(line)

    mineCpt = 0
    while mineCpt < core.memory("mineCount"):
        x = random.randint(0, core.memory("width") - 1)
        y = random.randint(0, core.memory("height") - 1)

        if not core.memory("grid")[x][y].bee:
            core.memory("grid")[x][y].bee = True
            mineCpt += 1

    for line in core.memory("grid"):
        for c in line:
            c.computeNeighbor(core.memory("width"), core.memory("height"), core.memory("grid"))


core.main(setup, run)
