# 41/50
from robot import *

placerMarqueur("base")
gauche()
while hauteurColonne() != 0:
    gauche()
droite()
placerMarqueur("start")
placerMarqueur("next")
allerAuMarqueur("base")
while hauteurColonne() < 6:
    allerAuMarqueur("next")
    prendre()
    allerAuMarqueur("start")
    while briqueDuDessus() != briqueTransportee()-1:
        droite()
    placerMarqueur("next")
    allerAuMarqueur("base")
    poser()
allerAuMarqueur("next") 
prendre()
allerAuMarqueur("base")
poser() 

