# 57/65
from robot import *
for loop in range(4):
    droite()
    placerMarqueur(loop)

for loop in range(3):
    droite()
    

placerMarqueur("WORK")
placerMarqueur("CURRENT")

def fin_ligne():
    allerAuMarqueur("WORK")
    droite()
    placerMarqueur("WORK")
    placerMarqueur("CURRENT")
    
def contruire(mark):
    allerAuMarqueur(mark)
    prendre()
    allerAuMarqueur("CURRENT")
    poser()
    droite()
    placerMarqueur("CURRENT")    
    
for loop in range(7):
    contruire(0)
fin_ligne()

for loop in range(6):
    contruire(1)
fin_ligne()

for loop in range(5):
    contruire(2)
fin_ligne()

for loop in range(4):
    contruire(3)
fin_ligne()

for loop in range(2):
    contruire(2)
contruire(1)
fin_ligne()

for loop in range(2):
    contruire(3)
fin_ligne()

for loop in range(1):
    contruire(3)
    
    
    
    
    
    
    
    
    
    
    
    