#
# Electrical and Electronics Engineer
# Ahmet Veysel Altun
#

import random

#-------------------------------------
class Door:
    # Constructor to initialize a door with a default "Goat" behind it
    def __init__(self, id):
        self.id = id
        self.BehindIt = "Goat"  # Default prize behind the door is a Goat
        

class Contestant:
    # Constructor to initialize a contestant's choice and strategy
    def __init__(self, ChangeMind):
        self.choice = random.randint(1,3)  # Contestant randomly chooses a door
        self.ChangeMind = ChangeMind  # Strategy: whether to change the choice after a door is revealed
#-------------------------------------

#-------------------------------------
# Function to create doors and randomly assign a car behind one of them
def CreateDoors():
    Doors = []  # List to store the doors
    for i in range(3):
        D = Door(id=i+1)  # Create a door with a unique ID
        Doors.append(D)  # Add the door to the list
    
    # Randomly choose a door to hide the car behind
    CarDoor = random.randint(1, 3)
    for D in Doors:
        if D.id == CarDoor:
            D.BehindIt = "Car"  # Place a car behind the randomly chosen door
    return Doors
#-------------------------------------

#-------------------------------------
# Function to reveal a door with a Goat behind it (that is not the contestant's choice)
def OpenGoatDoor(Doors, Cont):
    NewDoors = Doors.copy()  # Copy the list of doors
    ChoiceDoor = None  # The door chosen by the contestant

    # Find the door chosen by the contestant
    for D in Doors:
        if D.id == Cont.choice:
            ChoiceDoor = D
            NewDoors.remove(D)  # Remove the contestant's chosen door temporarily

    # Remove one of the remaining doors with a Goat behind it
    for D in NewDoors:
        if D.BehindIt == "Goat":
            NewDoors.remove(D)  # Remove the Goat door to reveal it
            break

    # Add the contestant's chosen door back to the list
    NewDoors.append(ChoiceDoor)
    return NewDoors
#-------------------------------------

#-------------------------------------
# Function to run a single competition round with the given strategy
def Competition(ChangeMind):
    # Create a contestant and the doors
    C = Contestant(ChangeMind)
    NewDoors = OpenGoatDoor(CreateDoors(), C)

    # If contestant decides to change their initial choice
    if C.ChangeMind:
        for D in NewDoors:
            if D.id != C.choice:
                C.choice = D.id  # Change choice to the remaining door
                break

    # Check if the contestant's final choice is the car
    for D in NewDoors:
        if C.choice == D.id:
            if D.BehindIt == "Car":
                return 1  # Contestant wins a car
            else:
                return 0  # Contestant wins a goat
#-------------------------------------

#-------------------------------------
# User inputs for the number of experiments and repetitions for averaging
numberOfExp = int(input("How many times should this experiment be repeated? : "))
ForAverage = int(input("How many times should I repeat this for an average calculation? : "))

# Initialize counters for average win percentages
TotalCWPercent = 0  # Total percentage of wins when changing the choice
TotalNCWPercent = 0  # Total percentage of wins when not changing the choice

# Repeat the experiment for averaging
for iteration in range(ForAverage):
    NCWonNumber = 0  # Counter for wins when not changing the choice
    CWonNumber = 0  # Counter for wins when changing the choice

    # Run the experiment for the given number of times
    for i in range(numberOfExp):
        NCWonNumber += Competition(False)  # Contestant does not change choice
        CWonNumber += Competition(True)  # Contestant changes choice

    # Calculate win percentages for both strategies
    NCWPercent = (NCWonNumber / numberOfExp) * 100
    CWPercent = (CWonNumber / numberOfExp) * 100

    # Add the percentages to the total for averaging later
    TotalCWPercent += CWPercent
    TotalNCWPercent += NCWPercent

    # Print the results for this iteration
    print("Number of Experiment:", numberOfExp, "\n",
          NCWPercent, "percent of the winning percentage if the idea is not changed.\n",
          CWPercent, "percent of the winning percentage if the idea is changed.")

# Calculate average win percentages
AverageCWPercent = TotalCWPercent / ForAverage
AverageNCWPercent = TotalNCWPercent / ForAverage

# Print the final average results
print("Probability mean if there is a change:", AverageCWPercent, "Probability mean if no change:", AverageNCWPercent)
#-------------------------------------