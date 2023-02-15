
# 25/25
# from robot import *
droite()
placerMarqueur("START")
for loop in range(9):
    droite()
placerMarqueur("Base") 

for super_loop in range(3):
    for loop in range(3):
        allerAuMarqueur("START")
        for loop in range(loop):
            droite()
        prendre()
        allerAuMarqueur("Base")
        for loop in range(super_loop):
            droite()
        poser()
    allerAuMarqueur("START")
    for loop in range(3):
        droite()
    placerMarqueur("START")