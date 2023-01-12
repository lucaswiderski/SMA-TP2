class FakeCapteur(object):
    def __init__(self,e):
        self.count=0
        self.min=-10
        self.max = 150
        self.name="Temperature"
        self.environment=e

    def mesure(self):
        return self.environment.getTemperature()
