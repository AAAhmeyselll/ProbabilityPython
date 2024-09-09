#
# Electrical and Electronics Engineer
# Ahmet Veysel Altun
#

import random
import matplotlib.pyplot as plt
import numpy as npy

#-------------------------------------
class Gambler:
    # Constructor to initialize the gambler with an initial amount and status
    def __init__(self, account):
        self.account = account
        self.status = "InGame"  # Status can be 'InGame', 'Failure', or 'Winner'

    # Method to update the status of the gambler based on the current account balance
    def changeStatus(self):
        if self.account == 0:
            self.status = "Failure"  # Status is 'Failure' if the account reaches 0
        elif self.account == 20:
            self.status = "Winner"  # Status is 'Winner' if the account reaches 20

    # Method to simulate a single game until the gambler wins or loses
    def Game(self):
        while self.status == "InGame":  # Continue playing until the gambler wins or loses
            gameStatus = random.randint(0, 1)  # Randomly decide to win or lose $1
            if gameStatus == 0:
                self.account -= 1  # Lose $1
            else:
                self.account += 1  # Win $1
            self.changeStatus()  # Update the status based on the new account balance
        return self.status  # Return the final status after the game ends
#-------------------------------------

#-------------------------------------
numberOfExp = int(input("How many times should this experiment be repeated? : "))
initialMoney = int(input("How much money you have initially? : "))

WinPercentArray = []  # Array to store win percentages for each experiment
WinNumber = 0  # Counter for the number of wins

# Run the experiment for the given number of times
for i in range(1, numberOfExp + 1):
    Gamb = Gambler(initialMoney)  # Create a new gambler for each experiment
    if Gamb.Game() == "Winner":
        WinNumber += 1  # Increment win counter if the gambler wins

    # Calculate win percentage up to the current experiment
    WinRate = (WinNumber / i) * 100
    WinPercentArray.append(WinRate)
#-------------------------------------

#-------------------------------------
# Plot the results
Times = npy.arange(1, numberOfExp + 1)  # X-axis: Number of experiments
plt.plot(Times, WinPercentArray, marker='.', linestyle='-', color='k', label='Number of Experiment and Win-Percent')
plt.xlabel('Number of Experiments')  # Label for X-axis
plt.ylabel('Win Percentage')  # Label for Y-axis
plt.title('Gambler\'s Ruin Problem: Winning Probability')  # Title of the plot
plt.legend()
plt.tight_layout()
plt.show()
#-------------------------------------
