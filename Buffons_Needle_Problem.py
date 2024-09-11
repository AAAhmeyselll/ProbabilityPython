import random
import matplotlib.pyplot as plt
import numpy as npy

#-------------------------------------
class Needle:
    def __init__(self, length):
        # Randomly choose a starting point (p1)
        self.p1x = random.uniform(0, 6)
        self.p1y = random.uniform(0, 6)

        while True:
            # Randomly choose an angle
            self.angleD = random.uniform(0, 360)
            self.angleR = npy.deg2rad(self.angleD)

            # Calculate the endpoint (p2) based on the angle and length
            self.p2x = self.p1x + npy.cos(self.angleR) * length
            self.p2y = self.p1y + npy.sin(self.angleR) * length
            
            # Check if both points are within the table limits
            if 0 <= self.p2x <= 6 and 0 <= self.p2y <= 6:
                break

    def features(self):
        print("features:", self.p1x, self.p1y, self.p2x, self.p2y, self.angleD)
#-------------------------------------

#-------------------------------------
def checkInterval(linesX, p1x, p2x):
    min_val, max_val = min(p1x, p2x), max(p1x, p2x)
    for x in linesX:
        # If any line x is between p1 and p2, it means the needle crosses a line
        if min_val < x < max_val:
            return "Cross"
    return "NotCross"
#-------------------------------------

#-------------------------------------
# Monte Carlo Simulation
numberOfExp = int(input("How many times should this experiment be repeated? : ")) 
needleLength = float(input("What is needle's Length? : "))

linesX = [2, 4]  # Lines at x = 2 and x = 4
CrossPercentArray = []
PiArray = []

for repeat in range(1, numberOfExp + 1):
    crossNumber = 0
    for j in range(repeat):
        N = Needle(needleLength)
        if checkInterval(linesX, N.p1x, N.p2x) == "Cross":
            crossNumber += 1 
    crossPercent = (crossNumber / repeat) * 100
    app_pi = 2/(crossNumber / repeat) if crossNumber != 0 else 0
    CrossPercentArray.append(crossPercent)
    PiArray.append(app_pi)

# Get the last 15 values from the arrays
last_15_numbers_cross_percent = CrossPercentArray[-15:]
last_15_numbers_pi_Array = PiArray[-15:]

# Calculate the average
averagePercent = sum(last_15_numbers_cross_percent) / len(last_15_numbers_cross_percent)
averagePi = sum(last_15_numbers_pi_Array) / len(last_15_numbers_pi_Array)

print("Average pi estimation: ", averagePi, "and average percent estimation:", averagePercent)
#-------------------------------------

#-------------------------------------
# Plot the results
Times = npy.arange(1, numberOfExp + 1)
plt.plot(Times, CrossPercentArray, marker='.', linestyle='-', color='k', label='Needle Number and Cross-Percent')
plt.plot(Times, PiArray, marker='.', linestyle='-', color='r', label='Needle Number and approximately')
plt.legend()
plt.tight_layout()
plt.show()
#-------------------------------------
