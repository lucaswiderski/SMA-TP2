import random
from pygame.math import Vector2


class DNA:
    def __init__(self,size,gene=None):
        self.gene = []
        if gene is None:
            for i in range(0,size):
                self.gene.append(Vector2(random.uniform(-1,1),random.uniform(-1,1)).normalize())
        else:
            self.gene = gene
