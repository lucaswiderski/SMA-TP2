import random
from math import floor
from pygame.math import Vector2


import core
from dna import DNA


class Rocket:
    def __init__(self,lifetime=200):
        self.pos = Vector2(400,600)
        self.vel = Vector2(random.uniform(-1,1),random.uniform(-1,1)).normalize()
        self.acc = Vector2()
        self.dna = DNA(lifetime)
        self.maxAcc=1
        self.maxVel=4
        self.count=0
        self.fitness = 0
        self.complete=False

    def calcFitness(self,target):
        if self.complete:
            self.fitness =100
        else:
            self.fitness =1 / (pow(target.distance_to(self.pos), 8) + 1)
            #self.fitness = 1 / target.distance_to(self.pos)

    def applyFore(self,force):
        self.acc+=force
        if self.acc.length() > self.maxAcc:
            self.acc.scale_to_length(self.maxAcc)


    def update(self, target):

        if target.distance_to(self.pos) < 20:
            self.complete = True
            self.pos = Vector2(target.x, target.y)

        self.applyFore(self.dna.gene[self.count])
        self.count+=1

        if self.complete == False :
            self.vel+=self.acc
            if self.vel.length() > self.maxVel:
                self.vel.scale_to_length(self.maxVel)
            self.pos+=self.vel
            self.acc = Vector2()

    def mutation(self):
        for i,v in enumerate(self.dna.gene):
            if random.randint(0,100) < 1:
                print("mutation")
                self.dna.gene[i] = Vector2(random.uniform(-1,1),random.uniform(-1,1))

    def crossover(self, partner):
        gene = []
        mid = floor(random.randint(0,len(self.dna.gene)))
        for i in range(0,len(self.dna.gene)):
            if i<mid:
                gene.append(self.dna.gene[i])
            else:
                gene.append(partner.dna.gene[i])
        return DNA(len(gene),gene)

    def show(self,screen):
        a = -self.vel.angle_to(Vector2(0, -1))

        tl = self.pos + Vector2(-2,-50).rotate(a)
        tr = self.pos + Vector2(2,-50).rotate(a)
        bl = self.pos + Vector2(-2,0).rotate(a)
        br = self.pos + Vector2(2,0).rotate(a)

        core.Draw.polygon((255,255,255),(tl,tr,br,bl))