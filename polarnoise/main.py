import math
import random
import threading
import time
import core

def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step

def setup():
    print("Setup START--------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    core.memory('phase',0)
    core.memory('zoff',0)
    core.memory('maxNoise', 3)




    print("Setup END-----------")


def run():
    core.cleanScreen()
    if core.getKeyPressList("r"):
        reset()

    points=[]
    for i in drange(0,math.pi*2, math.radians(5)):
        x= 0
        y = 0
        r= core.Math.map(random.uniform(0,0.5),0,1,100,200)
        x = r * math.cos(i)
        y = r * math.sin(i)
        points.append([x+200,y+200])
    core.Draw.lines((255,255,255),True,points,1)

    core.memory("phase",core.memory('phase')+0.03)



def reset():
    pass

core.main(setup, run)
