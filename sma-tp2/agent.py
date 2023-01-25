import random

from pygame import Vector2

import core
from body import Body
from item import Item

class Agent(object):
    def __init__(self,param, uuid, predation, body):
        self.predation=predation
        self.body=body
        self.uuid=uuid
        self.param = param

    def perceptionDeco(self):
        nourriture = []
        predateur = []
        symbiose = []
        for i in self.body.fustrum.perceptionList:
            if (not isinstance(i, Item)):
                if (i.etat == 2):
                    nourriture.append(i)
        return nourriture, predateur, symbiose

    def perceptionPred(self):
        nourriture = []
        predateur = []
        symbiose = []
        for i in self.body.fustrum.perceptionList:
            if (not(isinstance(i, Item)) and i.etat != 2):
                if (self.predation == i.predation-1):
                    nourriture.append(i)
                if (self.predation == i.predation+1):
                    predateur.append(i)
                if(self.predation > i.predation+1):
                    symbiose.append(i)
        return nourriture, predateur, symbiose

    def perceptionHerb(self):
        nourriture = []
        predateur = []
        symbiose =[]
        for i in self.body.fustrum.perceptionList:
            if(isinstance(i, Item)):
                nourriture.append(i)
            else:
                if(i.etat!=2):
                    if(self.predation == i.predation+1):
                        predateur.append(i)
                    if(self.predation > i.predation+1):
                        symbiose.append(i)
        return nourriture, predateur, symbiose
    def filtrePerception(self):
        nourriture = []
        predateur = []
        symbiose = []
        if(self.body.etat==0):
            match self.predation:
                case 3:
                    return self.perceptionDeco()
                case 0 | 1:
                    return self.perceptionPred()
                case 2:
                    return self.perceptionHerb()
        return nourriture, predateur, symbiose
    def update(self):
        nourriture, predateur, symbiose=self.filtrePerception()
        target = Vector2(random.randint(-1,1),random.randint(-1,1))*0.35
        for i in nourriture:
            if(self.body.position.distance_to(i.position)<10):
                if(isinstance(i, Item)):
                    i.etat=1
                else:
                    if(self.predation==3):
                        i.etat=3
                    else:
                        if(i.etat==1 or i.etat==0):
                            i.faireMourir()
        if(self.body.etat==0):
            if self.body.jaugeReproduction>=self.body.maxReproduction:
                core.memory('agents').append(Agent(self.param, self.uuid+100, self.predation, Body(
                    self.param,
                    self.predation,
                    self.uuid+100,
                    self.body.tauxJaugeFaim + random.randint(-(min(5, self.body.tauxJaugeFaim)),min(5,(100-self.body.tauxJaugeFaim))),
                    self.body.tauxJaugeFatigue + random.randint(-(min(5, self.body.tauxJaugeFatigue)),min(5,(100-self.body.tauxJaugeFatigue))),
                    self.body.tauxJaugeReproduction + random.randint(-(min(5, self.body.tauxJaugeReproduction)),min(5,(100-self.body.tauxJaugeReproduction))),
                    self.body.tauxVitesse + random.randint(-(min(5, self.body.tauxVitesse)),min(5,(100-self.body.tauxVitesse))),
                    self.body.tauxAcceleration + random.randint(-(min(5, self.body.tauxAcceleration)),min(5,(100-self.body.tauxAcceleration))))))
                self.body.jaugeReproduction=0
        while target.length()==0:
            target = Vector2(random.randint(-1, 1), random.randint(-1, 1))*0.35

        self.body.acc += target

        if len(predateur)>0:
            if len(symbiose)>0:
                target = symbiose[0].position - self.body.position
                target.scale_to_length(target.length() * 1.5)
                self.body.acc += target
            else:
                target = self.body.position - predateur[0].position
                target.scale_to_length(target.length() * 2.5)
                self.body.acc += target
        else:
            if len(nourriture)>0:
                target = nourriture[0].position - self.body.position
                target.scale_to_length(target.length() * 1.5)
                self.body.acc += target
            elif len(symbiose)>0:
                target = symbiose[0].position - self.body.position
                target.scale_to_length(target.length() * 1.5)
                self.body.acc += target


    def show(self):
        self.body.show()

    def score(self):
        vitesse = int((self.body.vMax / self.param['SuperPredateur']['parametres']['vitesseMax'][1])*100)
        faim = int((self.body.maxFaim / self.param['Carnivore']['parametres']['MaxFaim'][1])*100)
        fatigue = int((self.body.maxFatigue / self.param['Herbivore']['parametres']['MaxFatigue'][1])*100)
        reproduction = int((self.param['Herbivore']['parametres']['MaxReproduction'][0]/self.body.vMax)*100)

        return vitesse+faim+fatigue+reproduction
