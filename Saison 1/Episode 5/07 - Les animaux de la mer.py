from robot import *
for loop in range(4):
    droite()
    for loop in range(3):
        prendre()
        for loop in range(5):
            droite()
        poser()
        for loop in range(5):
            gauche()
        prendre()
        for loop in range(6):
            droite()
        poser()
        for loop in range(6):
            gauche()
droite()
droite()
for loop in range(3):
    prendre()
    for loop in range(4):
        droite()
    poser()
    for loop in range(4):
        gauche()