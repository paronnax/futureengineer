from robot import *
prendre()
droite()
droite()
if hauteurColonne() == 4:
    poser()
else:
    droite()
    droite()
    if hauteurColonne() == 4:
        poser()