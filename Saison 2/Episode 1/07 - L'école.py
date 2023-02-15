# 33/35
from robot import *
for loop in range(5):
    droite()
placerMarqueur("MID")

for loop in range(4):
    for tmp in range(loop+1):
        droite()
    placerMarqueur("MV_d")
    prendre()
    allerAuMarqueur("MID")
    poser()
    for tmp in range(loop+1):
        gauche()
    placerMarqueur("MV_g")
    prendre()
    allerAuMarqueur("MV_d")
    poser()
    allerAuMarqueur("MID")
    prendre()
    allerAuMarqueur("MV_g")
    poser()
    allerAuMarqueur("MID")