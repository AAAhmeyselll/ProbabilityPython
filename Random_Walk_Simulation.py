#
# Electrical and Electronics Engineer
# Ahmet Veysel Altun
#

import random
import matplotlib.pyplot as plt
import numpy as npy
import time

#-------------------------------------
class Dot:
    # Constructor to initialize the starting position (0, 0)
    def __init__(self):
        self.x = 0
        self.y = 0

    # Method to choose a random path for a given number of steps
    def choosePath(self, nTimes):
        for i in range(nTimes):
            # Randomly choose a direction: Right, Up, Left, or Down
            choose = random.randint(1, 4)
            match choose:
                case 1:
                    self.x += 1  # Move Right
                case 2:
                    self.y += 1  # Move Up
                case 3:
                    self.x -= 1  # Move Left
                case 4:
                    self.y -= 1  # Move Down

#-------------------------------------

#-------------------------------------
# Create a Dot object
D = Dot()

# User input for the number of step intervals and experiments
nInterval = int(input("What is the number of step intervals (1,N)? : "))
numberOfExp = int(input("How many times should this experiment be repeated? : "))

# Start time for performance measurement
start_time = time.time()

# Initialize variables for storing results
percentArray = []  # Array to store return percentages for each step interval
nTimes = 0  # Number of steps
ProcessPercent = 0  # Progress percentage

# Loop through each step interval
for i in range(nInterval):
    Back = 0  # Counter for the number of returns to the origin
    nTimes += 1  # Increment the number of steps

    # Repeat the experiment for the given number of times
    for j in range(numberOfExp):
        # Perform random walk and check if it returns to the origin
        D.choosePath(nTimes)
        if D.x == 0 and D.y == 0:
            Back += 1  # Increment if it returns to the origin
        # Reset position for the next experiment
        D.x, D.y = 0, 0
    
    # Calculate the return percentage for this step interval
    ReturnPercent = (Back / numberOfExp) * 100
    percentArray.append(ReturnPercent)

    # Print progress every 1% of the total intervals
    if (i != 0) and (i % (nInterval // 100) == 0):
        ProcessPercent += 1
        print(ProcessPercent, "Percent Completed")

# End time for performance measurement
end_time = time.time()
elapsed_time = end_time - start_time

# Print the total runtime in seconds and minutes
print("It took ", elapsed_time, " seconds for the code to run.")
print("It took ", elapsed_time / 60, " minutes for the code to run.")
#-------------------------------------

#-------------------------------------
# Plotting the results
Times = npy.arange(1, nInterval + 1)
plt.plot(Times, percentArray, marker='.', linestyle='-', color='k', label='Steps and Return-Percent')
plt.legend()
plt.tight_layout()
plt.show()
#-------------------------------------
