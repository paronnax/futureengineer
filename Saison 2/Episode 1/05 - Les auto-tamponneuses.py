# 30/35
from robot import *
placerMarqueur("START")
droite()
placerMarqueur("Ye")
for loop in range(5):
    droite()
placerMarqueur("Ro")

for loop in range(10):
    allerAuMarqueur("START")
    prendre()
    if briqueTransportee() == 1:
        allerAuMarqueur("Ye")
        poser()
        droite()
        placerMarqueur("Ye")
    else:
        allerAuMarqueur("Ro")
        poser()
        droite()
        placerMarqueur("Ro")
        