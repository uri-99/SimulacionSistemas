import os
import matplotlib.pyplot as plt
from matplotlib import animation


dirname = os.path.dirname(__file__)
simulationFile = os.path.join(dirname, 'data.txt')
simulation = open(simulationFile, 'r')

earth_position = []
mars_position = []
ship_position = []

def read_line(line):
    parsed_line = line.rstrip('\n')
    return list(map(float, parsed_line.split(' ')))

def parse_positions():
    line = simulation.readline()
    while(line != ''):
        earth_position.append(read_line(line))
        line = simulation.readline()
        mars_position.append(read_line(line))
        line = simulation.readline()
        ship_position.append(read_line(line))
        line = simulation.readline()
        line = simulation.readline()
parse_positions()

def get_coordinates(index):
    x = [earth_position[index][0], mars_position[index][0], ship_position[index][0]]
    y = [earth_position[index][1], mars_position[index][1], ship_position[index][1]]
    return x, y

def animate(frame):
    global earth 
    global mars
    global ship
    earth.remove()
    mars.remove()
    ship.remove()
    x, y = get_coordinates(frame)
    ship = plt.Circle((x[2], y[2]), 3390, color = 'green')
    earth = plt.Circle((x[0], y[0]), 63710, color = 'blue')
    mars = plt.Circle((x[1], y[1]), 339000, color = 'red')
    plt.gca().add_patch(mars)
    plt.gca().add_patch(earth)
    plt.gca().add_patch(ship)

fig = plt.gcf()
x, y = get_coordinates(0)
plt.xlim([-300000000, 300000000])
plt.ylim([-300000000, 300000000])
global earth 
global mars
global ship
sun = plt.Circle((0,0), 69600000, color = 'yellow')
ship = plt.Circle((x[2], y[2]), 3390, color = 'green')
earth = plt.Circle((x[0], y[0]), 63710, color = 'blue')
mars = plt.Circle((x[1], y[1]), 339000, color = 'red')
plt.gca().add_patch(sun)
plt.gca().add_patch(earth)
plt.gca().add_patch(mars)
plt.gca().add_patch(ship)
plt.gca().set_aspect('equal')
anim = animation.FuncAnimation(fig, animate, interval=1, repeat=False, frames=len(earth_position))
plt.show()