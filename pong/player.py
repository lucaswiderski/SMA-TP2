from pygame import Rect
from pygame.math import Vector2

import core


class Player:
    def __init__(self,j="J0",x=10,y=300):
        self.position = Vector2(x,y)
        self.largeur = 10
        self.hauteur = 50
        self.couleur = (255,255,255)
        self.score = 0
        self.name = j

    def up(self):
        self.position.y=self.position.y-10

    def down(self):
        self.position.y = self.position.y + 10

    def collision(self,b):
        r = Rect(self.position.x,self.position.y,self.largeur,self.hauteur)
        return r.collidepoint(b.position.x,b.position.y)

    def show(self,xScore):
        core.Draw.rect(self.couleur,(self.position.x,self.position.y,self.largeur,self.hauteur))

        core.Draw.text(self.couleur,self.name+": "+str(self.score),(xScore,10))