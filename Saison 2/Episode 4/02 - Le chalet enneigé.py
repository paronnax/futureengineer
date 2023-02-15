from robot import *
for loop in range(14):
    droite()
    while briqueDuDessus() == 1 and hauteurColonne() > 4:
        lacher()
        prendre()