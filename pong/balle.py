import random

from pygame.math import Vector2

import core


class Balle:
    def __init__(self,x=300,y=200):
        self.defautPos=Vector2(x,y)
        self.position=Vector2(x,y)
        self.vel = Vector2(random.uniform(-10,10),random.uniform(-10,10))
        self.acc = Vector2()
        self.couleur =(200,200,200)
        self.rayon=10

    def show(self):
        core.Draw.circle(self.couleur,self.position,self.rayon)

    def update(self):
        self.position+=self.vel

    def out(self,j1,j2):
        if self.position.x < 0:
            j2.score+=1
            self.position=Vector2(self.defautPos)

        if self.position.x > core.WINDOW_SIZE[0]:
            j1.score+=1
            self.position = Vector2(self.defautPos)


    def collision(self,j1,j2):
        if j1.collision(self) or j2.collision(self):
            self.vel.x*=-1

        if self.position.y-self.rayon <= 0:
            self.position.y=self.rayon
            self.vel.y*=-1

        if self.position.y+self.rayon>=core.WINDOW_SIZE[1]:
            self.position.y = core.WINDOW_SIZE[1]- self.rayon-3
            self.vel.y *= -1

