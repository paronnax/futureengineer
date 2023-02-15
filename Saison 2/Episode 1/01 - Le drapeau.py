from robot import *
for loop in range(9):
    droite()
placerMarqueur("B")

for loop in range(7):
    for inner_loop in range(8-loop):
        gauche()
    prendre()
    allerAuMarqueur("B")
    poser()