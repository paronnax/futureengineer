# 36/45
from robot import *
placerMarqueur("Orange")
droite()
placerMarqueur("Violet")
droite()
placerMarqueur("Yellow")
for loop in range(3):
    droite()
placerMarqueur("Luggage")

for loop in range(4):
    for loop in range(3):
        prendre()
        if briqueTransportee() == 1:
            allerAuMarqueur("Orange")
        elif briqueTransportee() == 2:
            allerAuMarqueur("Violet")
        else:
            allerAuMarqueur("Yellow")
        poser()
        allerAuMarqueur("Luggage")
    droite()
    placerMarqueur("Luggage")
        