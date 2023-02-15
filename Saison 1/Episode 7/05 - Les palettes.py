# 24/35
from robot import *
for loop in range(5):
    prendre()
    for loop in range(14):
        droite()
        if briqueDuDessus() == briqueTransportee():
            droite()
            poser()
            gauche()
            prendre()
            for inner_loop in range(13-loop):
                droite()
            poser()
            for inner_loop_retour in range(12-loop):
                gauche() 
            prendre()
            gauche()
            poser()
    for loop in range(14):
        gauche()