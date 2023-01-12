class FakeActionneur(object):
    def __init__(self,e,c):
        self.consigne = c
        self.environemnt=e

    def chauffe(self):
        if self.environemnt.temperature < self.consigne-5:
            self.environemnt.temperature = self.environemnt.temperature+5


