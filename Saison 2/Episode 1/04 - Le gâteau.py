# 23/25
from robot import *
placerMarqueur("Choco")
for loop in range(4):
    droite()
placerMarqueur("Creame")
for layer in range(3):
    for cnt in range(1,4):
        allerAuMarqueur("Choco")
        prendre()
        for loop in range(cnt):
            droite()
        poser()
    for cnt in range(1,4):
        allerAuMarqueur("Creame")
        prendre()
        for loop in range(cnt):
            gauche()
        poser()