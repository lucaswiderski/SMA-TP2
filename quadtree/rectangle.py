

class Rectangle:
    def __init__(self,x=0,y=0,w=1,h=1):
        self.x=x
        self.y=y
        self.w=w
        self.h=h

    def contains(self,point):
        return self.x < point.x < self.x + self.w  and self.y < point.y < self.y + self.h

    def intersection(self, point, r):
        DeltaX = point.x - max(self.x, min(point.x, self.x + self.w));
        DeltaY = point.y - max(self.y, min(point.y, self.y + self.h));
        return (DeltaX * DeltaX + DeltaY * DeltaY) < (r * r);
