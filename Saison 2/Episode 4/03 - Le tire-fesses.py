from robot import *
for loop in range(14):
    droite()
    if loop == 0:
        placerMarqueur("B")
    if loop == 13:
        placerMarqueur("R")
allerAuMarqueur("B")
for loop in range(13):
    for inner_loop in range(0,loop):
        droite()
    prendre()
    if briqueTransportee() >= 3:
        allerAuMarqueur("R")
        poser()
    elif briqueTransportee() <= 2:
        allerAuMarqueur("B")
        poser()
    allerAuMarqueur("B")