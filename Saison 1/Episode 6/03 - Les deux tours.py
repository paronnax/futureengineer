from robot import *
droite()
if briqueDuDessus() != 1:
    prendre()
    droite()
    poser()
    gauche()
droite()
droite()
if briqueDuDessus() != 2:
    prendre()
    gauche()
    poser()
    droite()