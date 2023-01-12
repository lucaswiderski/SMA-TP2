import core
import random
from pygame import Vector2
from Agent import Agent
from Body import Body
from Creep import Creep

def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    core.fullscreen = True

    core.memory("agents", [])
    core.memory("creeps", [])

    for a in range(0, 3):
        core.memory('agents').append(Agent(a, Body()))

    for c in range(0, 50):
        core.memory('creeps').append(Creep(c))

    print("Setup END-----------")


def computePerception(agent):
    agent.body.fustrum.perseptionList = []
    for b in core.memory('agents'):
        if(agent.uuid != b.uuid):
            if agent.body.fustrum.inside(b):
                agent.body.fustrum.perseptionList.append(b)
    for c in core.memory('creeps'):
        if agent.body.fustrum.inside(c):
            agent.body.fustrum.perseptionList.append(c)



def computeDecision(agent):
        agent.update()


def applyDecision(agent):
        agent.body.update()

def updateEnv():
    for a in core.memory("agents"):
        for c in core.memory('creeps'):
            if a.body.position.distance_to(c.position) <= a.body.masse:
                c.position=Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
                a.body.masse+=1
    for a in core.memory("agents"):
        for c in core.memory('agents'):
            if c.uuid != a.uuid:
                if a.body.position.distance_to(c.body.position) <= a.body.masse+c.body.masse:
                    if a.body.masse < c.body.masse:
                        c.body.masse+=a.body.masse/2
                        core.memory("agents").remove(a)
                    else:
                        a.body.masse += c.body.masse / 2
                        core.memory("agents").remove(c)
def run():
    core.cleanScreen()
    
    #Display
    for agent in core.memory("agents"):
        agent.show()
    
    for item in core.memory("creeps"):
        item.show()
        
    for agent in core.memory("agents"):
        computePerception(agent)
        
    for agent in core.memory("agents"):
        computeDecision(agent)
    
    for agent in core.memory("agents"):
        applyDecision(agent)
    
    updateEnv()
    
    
     
core.main(setup, run)
