# 16/30
from robot import *
for super_loop in range(2):
    droite()
    for loop in range(5):
        prendre()
        for loop in range(3-super_loop):
            droite()
        if briqueTransportee() == briqueDuDessus():
            poser()
        else:
            droite()
            poser()
            gauche()
        for loop in range(3-super_loop):
            gauche()