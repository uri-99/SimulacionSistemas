# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Table import Table

export = open("data.txt", "w")

table = Table(10)
export.write(str(table.N))
export.write("\n")
export.write(str(Table.opening))
export.write("\n")
export.write(str(table))

while table.left_right_percentages()[0] > 0.55:
    table.calculateTC()
    table.fly()
    export.write("\n")
    export.write(str(table.left_right()))
    export.write("\n")
    export.write(str(table))
    table.collide()
print("eq in T: ", table.t)

'''
for i in range(500):
    table.calculateTC()
    table.fly()
    export.write("\n")
    export.write(str(table.left_right()))
    export.write("\n")
    export.write(str(table))
    table.collide()
    '''

print("v2: ", table.calculateV2())

iniT = table.t
momentum = 0
for i in range(500):
    table.calculateTC()
    table.fly()
    momentum += table.collide2()

finT = table.t
transT = finT - iniT
L = 2*table.height + 2*table.width
pressure = momentum/(transT * L)
print("Presion: ", pressure, "[kg/(m*s^2)]")


export.close()
