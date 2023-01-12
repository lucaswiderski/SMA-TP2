import random

import pygame.time
from pygame import Vector2

import core
from fustrum import Fustrum

import paramVivarium


class Body(object):
    def __init__(self, predation, uuid):
        self.predation=predation
        self.uuid=uuid
        self.position=Vector2(random.randint(0,core.WINDOW_SIZE[0]),random.randint(0,core.WINDOW_SIZE[1]))
        self.vitesse = Vector2()
        self.acc = Vector2()
        self.vMax=0.25
        self.AMax=1
        self.color=(125,125,125)
        match predation:
            case 0:
                self.color = (255,0,0)
                #self.vMax = paramVivarium.paramSuper["VMax"]
                #self.vMin = paramVivarium.paramSuper["VMin"]
                #self.accMax=paramVivarium.paramSuper["AMax"]
                #self.accMin=paramVivarium.paramSuper["AMin"]
                #self.maxFaim=paramVivarium.paramSuper["FaimMax"]
                #self.minFaim=paramVivarium.paramSuper["FaimMin"]
                #self.fustrum=Fustrum(paramVivarium.paramSuper["vision"],self)
                self.maxFatigue = paramVivarium.paramSuper["FatigueMax"]
                #self.minFatigue = paramVivarium.paramSuper["FatigueMin"]
                #self.maxReproduction = paramVivarium.paramSuper["ReproductionMax"]
                #self.minReproduction = paramVivarium.paramSuper["ReproductionMin"]
            case 1:
                self.color = (0, 0, 255)
                self.maxFatigue = paramVivarium.paramCarn["FatigueMax"]
            case 2:
                self.color = (0, 255, 0)
                self.maxFatigue = paramVivarium.paramHerb["FatigueMax"]
            case 3:
                self.color = (0, 125, 125)
                self.maxFatigue = paramVivarium.paramDeco["FatigueMax"]
        self.fustrum=Fustrum(40,self)
        #self.jaugeFaim=self.minFaim
        #self.jaugeFatigue=self.minFatigue
        #self.jaugeReproduction=self.minReproduction
        self.jaugeFaim = 0
        self.jaugeFatigue = 0
        self.jaugeReproduction = 0
        self.dateNaissance=pygame.time.get_ticks()
        #0 en vie, 1 dors, 2 mort, 3 mort et mangé
        self.esperanceVie=30
        self.etat=0
        self.dors=0


    def update(self):
        if(pygame.time.get_ticks()-self.dateNaissance >= self.esperanceVie*1000):
            self.faireMourir()
        if(self.etat==0 or self.etat==1):
            if self.jaugeFaim>=1000:
                self.faireMourir()
        if(self.etat==0 and self.jaugeFatigue>=self.maxFatigue):
            self.etat=1
            self.jaugeFatigue=0
        if(self.etat==1 and self.dors>=3):
            self.etat=0
            self.dors=0
        if(self.etat==0):
            if self.acc.length() > self.AMax/5:
                self.acc.scale_to_length(self.AMax/5)

            self.vitesse=self.vitesse+self.acc

            if self.vitesse.length() > self.vMax:
                self.vitesse.scale_to_length(self.vMax)

            self.position=self.position+self.vitesse

            self.acc=Vector2()

            self.edge()
        self.jaugeReproduction+=0.01
        self.jaugeFaim+=0.01
        self.jaugeFatigue+=0.01
        if(self.etat==1):
            self.dors+=0.01


    def show(self):
        core.Draw.circle(self.color,self.position,5)


    def edge(self):
        if self.position.x <=5:
            self.vitesse.x *= -1
        if self.position.x+5 >= core.WINDOW_SIZE[0]:
            self.vitesse.x *= -1
        if self.position.y <= 5:
            self.vitesse.y *= -1
        if self.position.y +5>= core.WINDOW_SIZE[1]:
            self.vitesse.y *= -1

    def faireMourir(self):
        self.etat=2
        self.color=(125,125,125)