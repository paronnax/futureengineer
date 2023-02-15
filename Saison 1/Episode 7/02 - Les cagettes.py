# 19/25
from robot import *
for loop in range(3):
    droite()
for loop in range(8):
    prendre()
    if briqueTransportee() == 1:
        gauche()
        gauche()
        poser()
        droite()
        droite() 
    else:
        droite()
        droite() 
        poser()
        gauche()
        gauche()