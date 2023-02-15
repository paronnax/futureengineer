# 29/50
from robot import *
placerMarqueur(0)
droite()
placerMarqueur(2)
droite()
placerMarqueur(1)
droite()
placerMarqueur(4)
droite()
placerMarqueur(3)
droite()
droite()

def contruire():
    placerMarqueur("WORK")
    for loop in range(5):
        allerAuMarqueur(loop)
        prendre()
        allerAuMarqueur("WORK")
        poser()
    droite()

for loop in range(5):
    contruire() 