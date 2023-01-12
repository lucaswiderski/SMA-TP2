import random
import core
from point2d import Point2d
from quadtree import QuadTree
from rectangle import Rectangle


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 800]
    core.memory("capacity",4)
    core.memory("found", [])
    core.memory("quadtree",QuadTree(Rectangle(0,0,core.WINDOW_SIZE[0],core.WINDOW_SIZE[1]),core.memory("capacity")))
    core.memory("query",{"point":Point2d(245,300),'r':150})

    for i in range(0, 5):
        core.memory("quadtree").insert(Point2d(random.randint(0, core.WINDOW_SIZE[0]),random.randint(0, core.WINDOW_SIZE[1])))



    print("Setup END-----------")


def run():
    core.cleanScreen()
    if core.getKeyPressList("r"):
        reset()
    core.memory("quadtree").show()
    core.Draw.circle((0,0,255),core.memory("query")['point'].toArray(),core.memory("query")['r'],1)

    if core.getMouseLeftClick():
        print(core.getMouseLeftClick())
        core.memory("quadtree").insert(Point2d(core.getMouseLeftClick()[0],core.getMouseLeftClick()[1]))

    if core.getMouseRightClick():
        core.memory("query", {"point": Point2d(core.getMouseRightClick()[0],core.getMouseRightClick()[1]), 'r': 150})
        f = core.memory("quadtree").query(core.memory("query")['point'],core.memory("query")['r'])
        core.memory("found", f)

    for p in core.memory("found"):
        p.show((255,0,255))




def reset():
    core.memory("quadtree",
                QuadTree(Rectangle(0, 0, core.WINDOW_SIZE[0], core.WINDOW_SIZE[1]), core.memory("capacity")))
    core.memory("found", [])

core.main(setup, run)
