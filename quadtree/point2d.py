from math import sqrt

import core


class Point2d:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def show(self,color=(255,0,0)):
        core.Draw.circle(color,(self.x,self.y),2)

    def distance(self,p):
        return sqrt((p.x-self.x)**2 + (p.y - self.y)**2)

    def toArray(self):
        return [self.x,self.y]