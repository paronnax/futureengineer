# 49/70
from robot import *
for loop in range(4):
    placerMarqueur(loop)
    droite()

def motif_1():
    for loop in range(4):
        allerAuMarqueur(loop)
        prendre()
        allerAuMarqueur("WORK")
        poser()

def motif_2():
    allerAuMarqueur(2)
    prendre()
    allerAuMarqueur("WORK")
    poser()
    allerAuMarqueur(0)
    prendre()
    allerAuMarqueur("WORK")
    poser()
    allerAuMarqueur(3)
    prendre()
    allerAuMarqueur("WORK")
    poser()
    
def marque():
    droite()
    placerMarqueur("WORK")

droite()
marque()
motif_1()
marque()
motif_2()
motif_1()
marque()
motif_2()
motif_2()
marque()
motif_1()
marque()
motif_1()
motif_1()