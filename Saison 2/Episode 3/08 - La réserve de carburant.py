# 43/50
from robot import *
placerMarqueur("BEN")
while hauteurColonne() < 2:
    droite()
    
while hauteurColonne() != 0:
    placerMarqueur("WORK")
    while hauteurColonne() != 1:
        prendre()
        gauche()
        poser()
        droite()
    prendre()
    allerAuMarqueur("BEN")
    poser()
    allerAuMarqueur("WORK")
    droite()
    
gauche()
gauche()
while hauteurColonne() != 0:
    while hauteurColonne() != 0:
        prendre()
        droite()
        poser()
        gauche()
    gauche()