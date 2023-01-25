import random
from pygame.math import Vector2
import core
from agent import Agent
from body import Body
from item import Item
import json

def load(path):
    f=open(path)
    return json.load(f)
def setup():
    print("Setup START---------")
    param=load('paramVivarium.json')
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

    core.memory("agents", [])
    core.memory("items", [])

    total=0

    for i in range(0,param['SuperPredateur']['nb']):
        core.memory('agents').append(Agent(param, i,0, Body(param,0,i,random.randint(0,100),random.randint(0,100),random.randint(0,100), random.randint(0,100), random.randint(0,100))))
        total+=1

    for i in range(0,param['Carnivore']['nb']):
        core.memory('agents').append(Agent(param, total+i,1, Body(param, 1,total+i,random.randint(0,100),random.randint(0,100),random.randint(0,100), random.randint(0,100), random.randint(0,100))))
        total+=1

    for i in range(0,param['Herbivore']['nb']):
        core.memory('agents').append(Agent(param, total+i,2, Body(param, 2, total+i,random.randint(0,100),random.randint(0,100),random.randint(0,100), random.randint(0,100), random.randint(0,100))))
        total+=1

    for i in range(0,param['Decompositeur']['nb']):
        core.memory('agents').append(Agent(param, total+i,3, Body(param, 3, total+i,random.randint(0,100),random.randint(0,100),random.randint(0,100), random.randint(0,100), random.randint(0,100))))
        total+=1

    for i in range(0,param['nbPlantes']):
        core.memory('items').append(Item())

    print("Setup END-----------")


def computePerception(agent):
    for a in core.memory('agents'):
        a.body.fustrum.perceptionList=[]
        for b in core.memory('agents'):
            if a.uuid!=b.uuid:
                if a.body.fustrum.inside(b.body):
                    a.body.fustrum.perceptionList.append(b.body)
        for c in core.memory('items'):
            if a.body.fustrum.inside(c):
                a.body.fustrum.perceptionList.append(c)

def computeDecision(agent):
    for a in core.memory('agents'):
        a.update()


def applyDecision(agent):
    for a in core.memory('agents'):
        a.body.update()


def updateEnv():
    for a in core.memory("agents"):
        if a.body.etat==3:
            core.memory("agents").remove(a)
    for b in core.memory("items"):
        if b.etat==1:
            core.memory("items").remove(b)
            core.memory("items").append(Item())

def run():
    core.cleanScreen()

    # Display
    for agent in core.memory("agents"):
        agent.show()

    for item in core.memory("items"):
        item.show()

    for agent in core.memory("agents"):
        computePerception(agent)

    for agent in core.memory("agents"):
        computeDecision(agent)

    for agent in core.memory("agents"):
        applyDecision(agent)

    updateEnv()
    totalpop=len(core.memory('agents'))+len(core.memory('items'))
    super=0
    carn=0
    herb=0
    deco=0
    for a in core.memory('agents'):
        if a.body.etat!=2:
            if a.predation==0:
                super+=1
            if a.predation==1:
                carn+=1
            if a.predation==2:
                herb+=1
            if a.predation==3:
                deco+=1
    print("Super : "+str(int(((super/totalpop)*100)))+"%")
    print("Carnivor : " + str(int(((carn / totalpop) * 100)))+"%")
    print("Herbivor : " + str(int(((herb / totalpop) * 100)))+"%")
    print("Decoposeur : " + str(int(((deco / totalpop) * 100)))+"%")
    print("Vegetaux : " + str(int(((totalpop-super-carn-herb-deco)*100)/totalpop))+"%")
    print("###")

    minScore=0
    typeAgent=""
    for a in core.memory('agents'):
        if(a.body.etat!=2):
            temp=a.score()
            if(temp > minScore):
                meilleurAgent=a
                minScore=a.score()
                typeAgent=a.body.typeAgent
    print("le meilleur agent est de type : "+typeAgent+" et son id est "+str(meilleurAgent.uuid))
    print("###################################################################################")

core.main(setup, run)