# 21/40
from robot import *
droite()
placerMarqueur("WORK")
while hauteurColonne() < 9:
    allerAuMarqueur("WORK")
    while briqueDuDessus() != 2:
        droite()
    prendre()
    while briqueAttendue() !=2:
        droite()
    poser()