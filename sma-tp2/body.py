import random

import pygame.time
from pygame import Vector2

import core
from fustrum import Fustrum


class Body(object):
    # faire des pourcentage de vitesse, sommeil et faim et reproduction pour faire facilement la reproduction
    def __init__(self,param, predation, uuid, tauxJaugeFaim, tauxJaugeFatigue, tauxJaugeReproduction, tauxVitesse,
                 tauxAcceleration):
        # json
        self.param = param

        self.predation = predation
        self.uuid = uuid
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.vitesse = Vector2()
        self.acc = Vector2()
        self.vMax = 0.25
        self.AMax = 1
        self.color = (125, 125, 125)
        self.tauxJaugeFaim = tauxJaugeFaim
        self.tauxJaugeFatigue = tauxJaugeFatigue
        self.tauxJaugeReproduction = tauxJaugeReproduction
        self.tauxVitesse = tauxVitesse
        self.tauxAcceleration = tauxAcceleration
        match predation:
            case 0:
                self.color = (255, 0, 0)
                self.typeAgent = 'SuperPredateur'
            case 1:
                self.color = (0, 0, 255)
                self.typeAgent = 'Carnivore'
            case 2:
                self.color = (0, 255, 0)
                self.typeAgent = 'Herbivore'
            case 3:
                self.color = (0, 125, 125)
                self.typeAgent = 'Decompositeur'

        self.maxFatigue = self.param[self.typeAgent]['parametres']['MaxFatigue'][0] + int((self.param[self.typeAgent]['parametres']['MaxFatigue'][1] - self.param[self.typeAgent]['parametres']['MaxFatigue'][0]) * (tauxJaugeFatigue / 100))
        self.maxReproduction = self.param[self.typeAgent]['parametres']['MaxReproduction'][0] + int((self.param[self.typeAgent]['parametres']['MaxReproduction'][1] - self.param[self.typeAgent]['parametres']['MaxReproduction'][0]) * (tauxJaugeReproduction / 100))
        self.maxFaim = self.param[self.typeAgent]['parametres']['MaxFaim'][0] + int((self.param[self.typeAgent]['parametres']['MaxFaim'][1] - self.param[self.typeAgent]['parametres']['MaxFaim'][0]) * (tauxJaugeFaim / 100))
        self.vMax = self.param[self.typeAgent]['parametres']['vitesseMax'][0] + int((self.param[self.typeAgent]['parametres']['vitesseMax'][1] - self.param[self.typeAgent]['parametres']['vitesseMax'][0]) * (tauxVitesse / 100))
        self.AMax = self.param[self.typeAgent]['parametres']['accelerationMax'][0] + int((self.param[self.typeAgent]['parametres']['accelerationMax'][1] - self.param[self.typeAgent]['parametres']['accelerationMax'][0]) * (tauxAcceleration / 100))

        self.fustrum = Fustrum(self.param[self.typeAgent]['vision'], self)
        self.jaugeFaim = 0
        self.jaugeFatigue = 0
        self.jaugeReproduction = 0
        self.dateNaissance = pygame.time.get_ticks()

        # 0 en vie, 1 dors, 2 mort, 3 mort et mangé
        self.esperanceVie = self.param[self.typeAgent]['esperanceVie']
        self.etat = 0
        self.dors = 0


    def update(self):
        if (pygame.time.get_ticks() - self.dateNaissance >= self.esperanceVie):
            self.faireMourir()
        if (self.etat == 0 or self.etat == 1):
            if self.jaugeFaim >= self.maxFaim:
                self.faireMourir()
        if (self.etat == 0 and self.jaugeFatigue >= self.maxFatigue):
            self.etat = 1
            self.jaugeFatigue = 0
        if (self.etat == 1 and self.dors >= 3):
            self.etat = 0
            self.dors = 0
        if (self.etat == 0):
            if self.acc.length() > self.AMax / 5:
                self.acc.scale_to_length(self.AMax / 5)

            self.vitesse = self.vitesse + self.acc

            if self.vitesse.length() > self.vMax:
                self.vitesse.scale_to_length(self.vMax)

            self.position = self.position + self.vitesse

            self.acc = Vector2()

            self.edge()
        self.jaugeReproduction += 0.01
        self.jaugeFaim += 0.01
        self.jaugeFatigue += 0.01
        if (self.etat == 1):
            self.dors += 0.01


    def show(self):
        core.Draw.circle(self.color, self.position, 5)


    def edge(self):
        if self.position.x <= 5:
            self.vitesse.x *= -1
        if self.position.x + 5 >= core.WINDOW_SIZE[0]:
            self.vitesse.x *= -1
        if self.position.y <= 5:
            self.vitesse.y *= -1
        if self.position.y + 5 >= core.WINDOW_SIZE[1]:
            self.vitesse.y *= -1


    def faireMourir(self):
        self.etat = 2
        self.color = (125, 125, 125)