#
# Electrical and Electronics Engineer
# Ahmet Veysel Altun
#

import random
import matplotlib.pyplot as plt
import numpy as npy
#-------------------------------------
# A class is created to generate people in a room.
# The `Person` class represents a person with an ID and a randomly assigned birthday.
class Person:
    def __init__(self, id):
        self.id = id
        self.birthday = random.randint(1, 365)

    def WriteBirthday(self):
        print(self.birthday)

    def SayBirthday(self):
        return self.birthday
#-------------------------------------

#-------------------------------------
# If at least two people in the room have the same birthday, the room color is "Red"; otherwise, it is "Black".
def at_least_two(Room):
    RoomColor = "B"
    found = False
    population = len(Room)
    for personIndex in range(population):
        if found:
            break
        person = Room[personIndex]
        Birthday = person.SayBirthday()
        for index in range(personIndex + 1, population):
            aPerson = Room[index]
            aBirthday = aPerson.SayBirthday()
            if Birthday == aBirthday:
                RoomColor = "R"
                found = True
                break
    return RoomColor
#-------------------------------------

#-------------------------------------
# The number of people in the room is taken from the user and used as input to the function.
# This function starts with one room and calculates the percentage of red rooms.
# In each iteration, the number of rooms is increased, and the loop breaks when the difference between consecutive iterations is less than the specified error value.
# The final iteration provides the approximate probability that at least two people in a room with the specified number of people will share the same birthday.
def eventIteration(Population):
    TotalRed = 0
    TotalBlack = 0
    ite = 0
    Event = True
    iterationRedPercentArray = []
    iterationBlackPercentArray = []
    while Event:
        Room = []
        for i in range(Population):
            P = Person(id=i)
            Room.append(P)
        if at_least_two(Room) == "R":
            TotalRed += 1
        elif at_least_two(Room) == "B":
            TotalBlack += 1
        Percent = (float(TotalRed/(ite+1)))*100
        iterationRedPercentArray.append(Percent)
        iterationBlackPercentArray.append(100-Percent)
        if ite != 0:
            Error = abs(iterationRedPercentArray[ite]-iterationRedPercentArray[ite-1])
            if Error != 0 and Error < 0.0001:
                Event = False
                print("Repeat :",ite+1,"Error:",Error,"Approximately Red Percent :",iterationRedPercentArray[ite])
        ite += 1
    Total = TotalBlack + TotalRed
    if Total != ite:
        print("there is an error in eventIteration Function")
    else:
        return TotalRed, TotalBlack, iterationRedPercentArray, iterationBlackPercentArray, ite
#-------------------------------------

#-------------------------------------
def Averages(Repeats, RedPercents):
    Average_Repeat = npy.mean(Repeats)
    Average_RedPercents = npy.mean(RedPercents)
    return Average_Repeat, Average_RedPercents
#-------------------------------------

#-------------------------------------
Population = int(input("How many people are in the room? : "))
Exp_number = int(input("What is the number of experiments you want to do? : "))
Average_Red_Array = []
Average_Repeat_Array = []
for i in range(Exp_number):
    TotalRed, TotalBlack ,iterationRedPercent, iterationBlackPercent, ite = eventIteration(Population)
    Average_Red_Array.append(iterationRedPercent[ite-1])
    Average_Repeat_Array.append(ite)
AverageRepeat, AverageRed = Averages(Average_Repeat_Array, Average_Red_Array)
print("After an average of ",AverageRepeat," experiments, the probability value was ",AverageRed,"percent on average.")
#-------------------------------------

#-------------------------------------
# Plotting the occurrence and non-occurrence probabilities with respect to the number of iterations
iterationLabel = []
for label in range(ite):
    label += 1
    iterationLabel.append(label)
plt.plot(iterationLabel, iterationRedPercent, marker='x', linestyle='-', color='r', label='iteration vs Red-Percent (Same Birthday)')
plt.plot(iterationLabel, iterationBlackPercent, marker='o', linestyle='-', color='k', label='iteration vs Black-Percent (No Same Birthday)')
# fig = plt.gcf()
# fig.set_size_inches(19.2, 10.8)
# fig.canvas.manager.window.state('zoomed')
plt.legend()
plt.tight_layout()
plt.show()
#-------------------------------------