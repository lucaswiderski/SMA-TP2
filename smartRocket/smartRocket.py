import random

from pygame.math import Vector2

import core

from rocket import Rocket

def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 600]

    core.memory("target", Vector2(400, 100))
    core.memory("matingpool",[])

    restart()

    print("Setup END-----------")

def selection():
    newPopulation = []
    for i in range(0, core.memory("nbRocket")):
        parentA = core.memory("matingpool")[random.randint(0,len(core.memory("matingpool"))-1)]
        parentB = core.memory("matingpool")[random.randint(0, len(core.memory("matingpool"))-1)]
        child = parentA.crossover(parentB)
        newRocket = Rocket(core.memory("lifetime"))
        newRocket.dna = child
        newRocket.mutation()
        newPopulation.append(newRocket)

    core.memory('rockets',newPopulation)


def evaluate():
    maxFit = 0
    for rocket in core.memory('rockets'):
        rocket.calcFitness(core.memory("target"))
        if rocket.fitness > maxFit:
            maxFit = rocket.fitness



    for rocket in core.memory('rockets'):
        rocket.fitness/=maxFit


    core.memory("matingpool", [])
    for rocket in core.memory('rockets'):
        n = rocket.fitness * 10
        for i in range(0,int(n)):
            core.memory("matingpool").append(rocket)


def run():
    core.memory("time", core.memory("time")+1)
    if core.memory("time") >= core.memory("lifetime"):
        evaluate()
        selection()
        core.memory("time", 0)

    core.cleanScreen()

    for rocket in core.memory('rockets'):
        rocket.update(core.memory("target"))
        rocket.show(core.screen)

    core.Draw.circle((255,0,0),core.memory("target"),20)



def restart():
    core.memory("rockets", [])
    core.memory("nbRocket", 25)
    core.memory("lifetime", 200)
    core.memory("time", 0)


    for i in range(0, core.memory("nbRocket")):
        core.memory('rockets').append(Rocket(core.memory("lifetime")))


core.main(setup, run)
