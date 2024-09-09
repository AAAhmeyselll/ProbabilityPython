#
# Electrical and Electronics Engineer
# Ahmet Veysel Altun
#

import random
import matplotlib.pyplot as plt
import numpy as npy

#-------------------------------------
class needle:
    def __init__(self):
        self.p1x = random.uniform(0,10)
        self.p1y = random.uniform(0,10)

        self.angleD = random.uniform(0,360)
        self.angleR = npy.deg2rad(self.angleD)

        self.p2x = self.p1x + npy.cos(self.angleR)
        self.p2y = self.p1y + npy.sin(self.angleR)

#-------------------------------------

#-------------------------------------
def checkInterval(linesX,p1x,p2x):
    min_val, max_val = min(p1x, p2x), max(p1x, p2x)
    for x in linesX:
        status = "Cross" if min_val <= x <= max_val else "NotCross"
    return status
#-------------------------------------

#-------------------------------------
#TODO You have to control this area
numberOfExp = int(input("How many times should this experiment be repeated? : ")) 

linesX = [2,4,6,8]
crossNumber = 0
for i in range(numberOfExp):
    N = needle()
    if checkInterval(linesX,N.p1x,N.p2x) == "Cross":
        crossNumber += 1 
crossPercent = (crossNumber/numberOfExp)*100
print(crossPercent)
#-------------------------------------