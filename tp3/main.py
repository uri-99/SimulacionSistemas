# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Table import Table

table = Table(10)
table.fly()
print(table.left_right())
print("after fly 1, acá iría el save state\n", table)
table.collide()
table.calculateTC()
table.fly()
print(table.left_right())
print(table)
table.collide()



for i in range(500):
    table.calculateTC()
    table.fly()
    print(table.left_right())
    print(table)
    table.collide()