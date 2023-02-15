# 20/20
from robot import *
for loop in range(13):
    poser()
    droite()
    prendre()
    if briqueDuDessus() != briqueTransportee():
        poser()
        gauche()
        prendre()
        droite()
        for loop in range(3):
            lacher()
            prendre()
    else:
        poser()
        gauche()
        prendre()
        droite()