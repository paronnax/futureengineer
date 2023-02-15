# 12/20
from robot import *
for loop in range(6):
    droite()
for loop in range(1,5):
    for count_boite in range(loop):
        for loop in range(4):
            droite()
        prendre()
        for loop in range(4):
            gauche()
        poser()
    gauche()