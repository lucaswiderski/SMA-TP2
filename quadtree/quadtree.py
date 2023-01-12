import core
from rectangle import Rectangle


class QuadTree:
    def __init__(self,boundary,capacity=5):
        self.boundary = boundary
        self.capacity=capacity
        self.points = []
        self.divided = False

    def insert(self,point):
        if not self.boundary.contains(point):
            return
        for p in self.points:
            if p.x == point.x and p.y == point.y:
                return

        if not self.divided:
            if len(self.points) < self.capacity:
                self.points.append(point)
            else:
                self.subdivide()
                self.points.append(point)
                for p in self.points:
                    self.northest.insert(p)
                    self.northwest.insert(p)
                    self.southest.insert(p)
                    self.southwest.insert(p)
                self.points = []
        else:
            self.northest.insert(point)
            self.northwest.insert(point)
            self.southest.insert(point)
            self.southwest.insert(point)

    def subdivide(self):

        x = self.boundary.x
        y = self.boundary.y
        h = self.boundary.h
        w = self.boundary.w

        self.northest = QuadTree(Rectangle(x+w/2,y,w/2,h/2),self.capacity)
        self.northwest= QuadTree(Rectangle(x,y,w/2,h/2),self.capacity)
        self.southest = QuadTree(Rectangle(x+w/2,y+w/2,w/2,h/2),self.capacity)
        self.southwest = QuadTree(Rectangle(x,y+w/2,w/2,h/2),self.capacity)
        self.divided = True
        print("sub")

    def show(self):
        x = self.boundary.x
        y = self.boundary.y
        h = self.boundary.h
        w = self.boundary.w
        core.Draw.rect((255,255,255),(x,y,w,h),1)


        for p in self.points:
            p.show()

        if self.divided:
            self.northest.show()
            self.northwest.show()
            self.southest.show()
            self.southwest.show()


    def query(self, point, radius):

        if not self.boundary.intersection(point,radius):
            return []
        else:

            if not self.divided:
                found = []
                for p in self.points:
                    if p.distance(point) <= radius:
                        found.append(p)
                return found
            else:
                found=self.northest.query(point, radius)
                found=found+self.northwest.query(point, radius)
                found=found+self.southest.query(point, radius)
                found=found+self.southwest.query(point, radius)

                return found





