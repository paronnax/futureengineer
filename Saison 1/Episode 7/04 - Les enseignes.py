# 12/15
from robot import *
for loop in range(13):
    droite()
    if hauteurColonne() > 2:
        prendre()
    elif hauteurColonne() < 2:
        poser()