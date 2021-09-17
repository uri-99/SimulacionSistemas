# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import statistics

from Particle import Particle
from Table import Table

export = open("data.txt", "w")

table = Table(10)
export.write(str(table.N))
export.write("\n")
export.write(str(Table.opening))
export.write("\n")
export.write("\n")
export.write("(" + str(table.N) +", 0)")
export.write("\n")
export.write(str(table))

old = table.left_right_percentages()[0]
while table.left_right_percentages()[0] > 0.55:
    table.calculateTC()
    table.fly()
    export.write(str(table.left_right()))
    export.write("\n")
    export.write(str(table))
    table.collide()
    print(table.t)
    if table.left_right_percentages()[0] != old:
        print(table.left_right())
        old = table.left_right_percentages()[0]
print("eq in T: ", table.t)

'''
for i in range(500):
    table.calculateTC()
    table.fly()
    export.write(str(table.left_right()))
    export.write("\n")
    export.write(str(table))
    table.collide()
    '''

print("v2: ", table.calculateV2())

L = 2*table.height + 2*table.width

iniT = table.t
totalMomentum = 0
deltaTforDeviation = 1
valuesArray = []
tempMomentum = 0
iter = 1

while table.t < iniT + 100*deltaTforDeviation:
    table.calculateTC()
    table.fly()
    if table.t < iniT + iter*deltaTforDeviation:
        tempMomentum += table.collide2()
    else:
        valuesArray.append(tempMomentum / (5*L))
        totalMomentum += tempMomentum

        tempMomentum = 0
        iter += 1


finT = table.t
transT = finT - iniT

pressure = totalMomentum / (transT * L)
print("Presion: ", pressure, "[kg/(m*s^2)]")
export.write(str(Particle.initSpeed))
export.write("\n")
export.write(str(pressure))
export.write("\n")

deviation = statistics.stdev(valuesArray)
print("deviation: ", statistics.stdev(valuesArray))
export.write(str(deviation))


print(len(valuesArray), valuesArray)
print(table.t)


export.close()
