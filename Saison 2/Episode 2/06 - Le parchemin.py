# 50/70
from robot import *

def transport(mark):
    allerAuMarqueur("WORK")
    prendre()
    allerAuMarqueur(mark)
    poser()
def gestion_infini():
    transport(0)
def gestion_musique():
    transport(1)
def gestion_oisseau():
    transport(2)
def fin_colonne():
    allerAuMarqueur("WORK")
    droite()
    placerMarqueur("WORK")

 
placerMarqueur("WORK")
for loop in range(4):
    droite()
for loop in range(3):
    droite()
    placerMarqueur(loop)

gestion_musique()
gestion_infini()
gestion_musique()
gestion_oisseau()
gestion_infini()
gestion_oisseau()
gestion_infini()
fin_colonne()
gestion_oisseau()
gestion_musique()
gestion_oisseau()
for loop in range(4):
    gestion_musique()
fin_colonne()
gestion_infini()
gestion_oisseau()
gestion_infini()
for loop in range(2):
    gestion_infini()
    gestion_oisseau()