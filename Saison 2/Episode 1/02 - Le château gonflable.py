from robot import *
for loop in range(12):
    droite()
placerMarqueur("B")
for loop in range(1,6):
    for inner_loop in range(2*loop):
        gauche()
    prendre()
    allerAuMarqueur("B")
    poser()