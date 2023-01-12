import random
from pygame.math import Vector2
import core
from agent import Agent
from body import Body
from creep import Creep
from obstcle import Obstacle





def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 800]
    core.fullscreen=True

    core.memory("agents", [])
    core.memory("obstacles", [])
    core.memory("creeps", [])

    for i in range(0,5):
        core.memory('agents').append(Agent(Body()))

    for i in range(0,3):
        core.memory('obstacles').append(Obstacle())

    for i in range(0,50):
        core.memory('creeps').append(Creep())

    print("Setup END-----------")


def computePerception(agent):
    for a in core.memory('agents'):
        a.body.fustrum.perceptionList=[]
        for b in core.memory('agents'):
            if a.uuid!=b.uuid:
                if a.body.fustrum.inside(b.body):
                    a.body.fustrum.perceptionList.append(b.body)
        for b in core.memory('obstacles'):
            if a.body.fustrum.inside(b):
                a.body.fustrum.perceptionList.append(b)

        for b in core.memory('creeps'):
            if a.body.fustrum.inside(b):
                a.body.fustrum.perceptionList.append(b)




def computeDecision(agent):
    for a in core.memory('agents'):
        a.update()


def applyDecision(agent):
    for a in core.memory('agents'):
        a.body.update()


def updateEnv():
    for a in core.memory("agents"):
        for c in core.memory('creeps'):
            if a.body.position.distance_to(c.position) <= a.body.mass:
                c.position=Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
                c.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                a.body.mass+=1
    for a in core.memory("agents"):
        for c in core.memory('obstacles'):
            if a.body.position.distance_to(c.position) <= a.body.mass:
                core.memory("agents").remove(a)

    for a in core.memory("agents"):
        for c in core.memory('agents'):
            if c.uuid != a.uuid:
                if a.body.position.distance_to(c.body.position) <= a.body.mass+c.body.mass:
                    if a.body.mass < c.body.mass:
                        c.body.mass+=a.body.mass/2
                        core.memory("agents").remove(a)
                    else:
                        a.body.mass += c.body.mass / 2
                        core.memory("agents").remove(c)


def reset():
    core.memory("agents", [])
    core.memory("obstacles", [])
    core.memory("creeps", [])

    for i in range(0, 5):
        core.memory('agents').append(Agent(Body()))

    for i in range(0, 3):
        core.memory('obstacles').append(Obstacle())

    for i in range(0, 50):
        core.memory('creeps').append(Creep())


def run():
    if core.getKeyPressList('r'):
        reset()
    core.cleanScreen()

    # Display
    for agent in core.memory("agents"):
        agent.show()

    for item in core.memory("obstacles"):
        item.show()

    for creep in core.memory("creeps"):
        creep.show()

    for agent in core.memory("agents"):
        computePerception(agent)

    for agent in core.memory("agents"):
        computeDecision(agent)

    for agent in core.memory("agents"):
        applyDecision(agent)

    updateEnv()

core.main(setup, run)