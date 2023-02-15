# 21/25
from robot import *
for loop in range(9):
    droite()
    placerMarqueur("WORKING")
    for loop in range(4):
        prendre()
        if briqueTransporteeCassee():
            allerAuMarqueur("A")
            poser()
        else:
            gauche()
            poser()
        allerAuMarqueur("WORKING")
    for loop in range(3):
        gauche()
        prendre()
        droite()
        poser()