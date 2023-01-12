import copy
import random
import time
import core
from gameoflife.cell import Cell
from minnesweeper.case import Case


def setup():
    print("Setup START---------")

    core.fps = 120
    core.WINDOW_SIZE = [800, 800]
    core.memory("width", int(800/10))
    core.memory("height", int(800/10))
    core.memory("proba",40) # /100
    core.memory("run", False)

    core.memory("generation", 0)
    core.memory("maxGeneration",1000)
    core.memory("grid", [])
    core.setBgColor((255,255,255))

    reset()


    print("Setup END-----------")


def empty():
    core.memory("grid", [])
    for i in range(0, core.memory("width")):
        line = []
        for j in range(0, core.memory("height")):
            x = 0

            line.append(Cell(i, j, x, core.WINDOW_SIZE[0] / core.memory("width")))
        core.memory("grid").append(line)


def run():
    core.cleanScreen()
    if core.getKeyPressList("r"):
        reset()
    if core.getKeyPressList("e"):
        empty()
    if core.getKeyPressList("SPACE"):
        core.memory("run",not core.memory("run"))
        time.sleep(0.3)


    grid = core.memory("grid")
    grid2 = copy.deepcopy(grid)

    if core.getMouseLeftClick():
        time.sleep(0.1)
        for line in grid:
            for c in line:
                c.inside(core.getMouseLeftClick())

    for line in grid:
        for c in line:
            c.show()

    if core.memory("run"):
        core.memory("generation",core.memory("generation")+1)
        for line in grid:
            for c in line:
                stat = c.update(core.memory("width"), core.memory("height"), grid)
                if stat is not None:
                    grid2[int(c.pos.x)][int(c.pos.y)].occupied = stat
        core.memory('grid',copy.deepcopy(grid2))

    core.setTitle("Generation : "+str(core.memory("generation")))



def reset():
    core.memory("grid", [])


    for i in range(0, core.memory("width")):
        line = []
        for j in range(0, core.memory("height")):
            x = (1 if random.randint(0,100)<core.memory("proba") else 0)

            line.append(Cell(i, j, x , core.WINDOW_SIZE[0]/core.memory("width") ))
        core.memory("grid").append(line)





core.main(setup, run)
