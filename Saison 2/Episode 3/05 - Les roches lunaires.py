# 29/40
from robot import *
while hauteurColonne() != 0:
    prendre()
    while hauteurColonne() != 0:
        droite()
    while hauteurColonne() != 1:
        droite()
    poser()
    
    gauche()
    while hauteurColonne() != 0:
        gauche()
    gauche()
    while hauteurColonne() == 2:
        gauche()
    droite()