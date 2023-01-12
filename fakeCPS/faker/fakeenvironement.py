import random


class FakeEnvironment(object):
    def __init__(self):
        self.temperature = random.randint(10,15)

    def getTemperature(self):
        return self.temperature

    def update(self):
        self.temperature=self.temperature-0.01