# 20/30
from robot import *
droite()
droite()
for loop in range(7):
    prendre()
    if briqueTransporteeCassee():
        droite()
        droite()
        poser()
        gauche()
        gauche()
    else:
        droite()
        poser()
        gauche()
for loop in range(4):
    droite()
    prendre()
    gauche()
    poser()