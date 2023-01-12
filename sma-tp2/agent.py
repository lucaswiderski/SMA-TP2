import random

from pygame import Vector2

import core
from body import Body
from item import Item


class Agent(object):
    def __init__(self,uuid, predation, body):
        self.predation=predation
        self.body=body
        self.uuid=uuid


    def filtrePerception(self):
        nourriture=[]
        predateur=[]
        if(self.body.etat==0 and self.predation<3):
            for i in self.body.fustrum.perceptionList:
                if(isinstance(i, Item)):
                    nourriture.append(i)
                else:
                    if(i.etat!=2):
                        if(self.predation<i.predation):
                            nourriture.append(i)
                        if(self.predation>i.predation):
                            predateur.append(i)
        else:
            for i in self.body.fustrum.perceptionList:
                if(not isinstance(i, Item)):
                    if(i.etat==2):
                        nourriture.append(i)
                    if(i.etat!=2 and not(isinstance(i, Item)) and self.predation>i.predation):
                        predateur.append(i)
        return nourriture, predateur
    def update(self):
        nourriture, predateur=self.filtrePerception()
        target = Vector2(random.randint(-1,1),random.randint(-1,1))
        for i in nourriture:
            if(self.body.position.distance_to(i.position)<10):
                if(isinstance(i, Item)):
                    i.etat=1
                else:
                    if(i.etat==1 or i.etat==0):
                        i.faireMourir()
                    else:
                        i.etat=3
        if(self.body.etat==0):
            if self.body.jaugeReproduction>=50:
                core.memory('agents').append(Agent(self.uuid+100, self.predation, Body(self.predation, self.uuid+100)))
                self.body.jaugeReproduction=0
        while target.length()==0:
            target = Vector2(random.randint(-1, 1), random.randint(-1, 1))

        self.body.acc += target

        if len(nourriture)>0:
            target = nourriture[0].position - self.body.position
            target.scale_to_length(target.length() * 1.5)
            self.body.acc += target

        if len(predateur)>0:
            target = self.body.position - predateur[0].position
            target.scale_to_length(target.length() * 2.5)
            self.body.acc +=target


    def show(self):
        self.body.show()