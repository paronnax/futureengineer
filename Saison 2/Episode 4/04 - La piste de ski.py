from robot import *
droite()
placerMarqueur("START")
while hauteurColonne() >= 2:
    droite()
placerMarqueur("A")

while hauteurColonne() > 0 or briqueAttendue():
    if briqueAttendue():
        placerMarqueur("A")
        droite()
    elif hauteurColonne() > 2:
        prendre()
        allerAuMarqueur("A")
        poser()
        if hauteurColonne() > 2:
            prendre()
            droite()
            placerMarqueur("A")
            poser()
        allerAuMarqueur("START")
    else:
        droite()