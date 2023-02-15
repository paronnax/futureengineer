# 13/20
from robot import *
for loop in range(4):
    droite()
for super_loop in range(4,0,-1):
    for loop in range(3):
        prendre()
        for loop in range(super_loop):
            droite()
        poser()
        for loop in range(super_loop):
            gauche()
    gauche()
            