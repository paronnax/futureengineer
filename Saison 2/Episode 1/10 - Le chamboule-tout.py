# 28/50
from robot import *
placerMarqueur("WORKING")
for loop in range(5):
    droite()
placerMarqueur("START")
allerAuMarqueur("WORKING")

for loop in range(4):
    for inner_loop in range(4):
        allerAuMarqueur("WORKING")
        prendre()
        allerAuMarqueur("START")
        for loop in range(inner_loop):
            droite()
        poser()
    allerAuMarqueur("START")
    droite()
    placerMarqueur("START") 
    allerAuMarqueur("WORKING")
    droite()
    placerMarqueur("WORKING")