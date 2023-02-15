# 27/32
from robot import *
placerMarqueur("T")
for loop in range(15):
    droite()
placerMarqueur("D")
for loop in range(4):
    for loop in range(4):
        allerAuMarqueur("T")
        prendre()
        allerAuMarqueur("D")
        poser()
    for loop in range(3):
        gauche()
        if hauteurColonne() == 0:
            placerMarqueur("D")
    allerAuMarqueur("T")
    droite()
    placerMarqueur("T")