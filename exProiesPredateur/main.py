import pygame

import core
from exProiesPredateur.predateur import Predateur
from exProiesPredateur.proie import Proie


def setup():
    print('SetUp :')
    core.WINDOW_SIZE=[400,400]
    core.fps=30

    core.memory("proies",[])
    core.memory("predateurs",[])

    core.memory("nbProies",100)
    core.memory("nbPredateurs",10)

    for i in range(0,core.memory("nbProies")):
        core.memory("proies").append(Proie())

    for i in range(0,core.memory("nbPredateurs")):
        core.memory("predateurs").append(Predateur())



def run():
    core.cleanScreen()

    #CONTROL
    if core.getKeyPressList("q"):
        pygame.quit()
    if core.getKeyPressList("r"):
        core.memory("proies",[])
        core.memory("predateurs", [])
        for i in range(0, core.memory("nbProies")):
            core.memory("proies").append(Proie())
        for i in range(0, core.memory("nbPredateurs")):
            core.memory("predateurs").append(Predateur())

    #AFFICHAGE
    for p in core.memory("proies"):
        p.afficher()
    for p in core.memory("predateurs"):
        p.afficher()

    #MISE A JOUR DES POSITIONS
    for p in core.memory("proies"):
        p.deplacement()
        p.bordure(core.WINDOW_SIZE)

    for p in core.memory("predateurs"):
        p.deplacement(core.memory("proies"))
        p.bordure(core.WINDOW_SIZE)

    for p in core.memory("predateurs"):
        p.manger(core.memory("proies"))

core.main(setup,run)