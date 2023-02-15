# 19/25
from robot import *

for loop in range(9):
    droite()
while hauteurColonne() != 7:
    gauche()
    while hauteurColonne() < 1:
        gauche()
    prendre()
    while briqueAttendue() == 0:
        droite()
    poser()
    

