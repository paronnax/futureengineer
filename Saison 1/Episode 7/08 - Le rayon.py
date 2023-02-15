# 26/40
from robot import *
droite()
for loop in range(8):
    for loop in range(4):
        prendre()
        if briqueTransportee() == 1:
            gauche()
            poser()
            droite()
        else:
            droite()
            poser()
            gauche()
    for loop in range(2):
        gauche()
        prendre()
        droite()
        poser()   
    for loop in range(2):
        droite()
        prendre()
        gauche()
        poser()
    droite()