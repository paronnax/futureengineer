# 20/25
from robot import *
prendre()
while hauteurColonne() == 0:
    droite()
poser()
gauche()
while hauteurColonne() == 0:
    gauche()
prendre()
while hauteurColonne() == 0:
    droite()
poser()