import random
from pygame.math import Vector2, Vector3
import core
from fakeCPS.faker.fakeactionneur import FakeActionneur
from fakeCPS.faker.fakecapteur import FakeCapteur
from fakeCPS.faker.fakeenvironement import FakeEnvironment




def setup():
    print("Setup START---------")
    core.fps = 3
    core.WINDOW_SIZE = [800, 600]

    core.memory("environement", FakeEnvironment())
    core.memory("capteurTemperature", FakeCapteur(core.memory("environement")))
    core.memory("actionneurChauffage", FakeActionneur(core.memory("environement"),20))

    core.memory('historique',[])

    print("Setup END-----------")




def run():
    core.cleanScreen()
    core.memory("environement").update()

    core.memory("actionneurChauffage").chauffe()

    print(core.memory("capteurTemperature").mesure())


    #DESSIN
    core.Draw.circle((255,0,0),(5,core.Math.map(core.memory("capteurTemperature").mesure(),10,50,600,0)),10)
    core.Draw.circle((0,0,255),(5,core.Math.map(core.memory("actionneurChauffage").consigne,10,50,600,0)),10)


core.main(setup, run)
