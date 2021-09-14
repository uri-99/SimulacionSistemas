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

for i in range(500):
    table.calculateTC()
    table.fly()
    export.write("\n")
    export.write(str(table))
    table.collide()

export.close()