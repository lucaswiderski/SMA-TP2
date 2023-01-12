import random
from pygame import Vector2
from Creep import Creep
from Body import Body
class Agent(object):
    def __init__(self, uuid, body):
        self.uuid=uuid
        self.body=body

    def filtrePerception(self):
        creeps=[]
        danger=[]
        manger=[]
        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            if isinstance(i,Body):
                if i.masse > self.body.masse:
                    danger.append(i)
                else:
                    manger.append(i)
            if isinstance(i,Creep):
                creeps.append(i)

        creeps.sort(key=lambda x: x.dist, reverse=False)
        danger.sort(key=lambda x: x.dist, reverse=False)

        return creeps,danger,manger
    def update(self):
        creeps, danger, manqer = self.filtrePerception()

        if len(creeps) > 0:
            target = creeps[0].position - self.body.position

        else:

            target = Vector2(random.randint(-1, 1), random.randint(-1, 1))
            while target.length() == 0:
                target = Vector2(random.randint(-1, 1), random.randint(-1, 1))

        target.scale_to_length(target.length() * self.coefCreep)
        self.body.acc += target

        if len(manqer) > 0:
            target = manqer[0].position - self.body.position
            target.scale_to_length(target.length() * self.coefCreep)
            self.body.acc = self.body.acc + target

        if len(danger) > 0:
            target = self.body.position - danger[0].position
            target.scale_to_length(1 / target.length() ** 2)
            target.scale_to_length(target.length() * (self.coefObs + self.body.mass))
            self.body.acc = self.body.acc + target

    def show(self):
        self.body.show()