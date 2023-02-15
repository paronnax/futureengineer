from robot import *
prendre()
for loop in range(14):
    droite()
    if briqueDuDessusCassee():
        lacher()
        prendre()