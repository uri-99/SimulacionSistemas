# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Table import Table

table = Table(10)
table.fly()
print("after fly 1, acá iría el save state\n", table)
table.collide()
print("after collide 1\n", table)
table.calculateTC()
table.fly()
table.collide()
print(table)

for i in range(10):
    table.calculateTC()
    table.fly()
    table.collide()