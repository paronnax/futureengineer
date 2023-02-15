from robot import *
for loop in range(14):
    droite()
    if hauteurColonne() == 1 or hauteurColonne() == 3 or hauteurColonne() == 5:
        while hauteurColonne() > 0:
            lacher()
            prendre()