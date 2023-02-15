# 31/50
from robot import *
placerMarqueur(0)
droite()
placerMarqueur(2)
droite()
placerMarqueur(3)
droite()
placerMarqueur(1)

def contruire():
    placerMarqueur("WORK")
    for loop in range(4):
        allerAuMarqueur(loop)
        prendre()
        allerAuMarqueur("WORK")
        poser()
    droite()

droite()
droite()
contruire()
droite()
contruire()
droite()
droite()
contruire()
contruire()