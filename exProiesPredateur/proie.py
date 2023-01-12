import random

from pygame.math import Vector2

import core


class Proie:
    def __init__(self):
        self.position=Vector2(random.randint(0,400),random.randint(0,400))
        self.vitesse = Vector2(0,0)
        self.acceleration = Vector2(0,0)
        self.vivante = True

        self.couleur = (0,255,0)
        self.taille = 5

        self.maxVitesse = 5
        self.maxAcceleration = 1

    def afficher(self):
        if self.vivante:
            core.Draw.circle(self.couleur,self.position,self.taille)
        else:
            core.Draw.circle((0,0,255),self.position,self.taille)


    def deplacement(self):
        if self.vivante:
            self.acceleration = Vector2(random.uniform(-1,1),random.uniform(-1,1))

            if self.acceleration.length() > self.maxAcceleration:
                self.acceleration.scale_to_length(self.maxAcceleration)

            self.vitesse = self.vitesse + self.acceleration

            if self.vitesse.length()>self.maxVitesse:
                self.vitesse.scale_to_length(self.maxVitesse)

            self.position = self.position + self.vitesse

            self.acceleration = Vector2(0,0)

    def bordure(self,fenetre):
        if self.position.y<0:
            self.position.y = fenetre[1]

        if self.position.y > fenetre[1]:
            self.position.y=0

        if self.position.x < 0:
            self.position.x = fenetre[0]

        if self.position.x > fenetre[0]:
            self.position.x = 0