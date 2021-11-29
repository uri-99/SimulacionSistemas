import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter
import os

dt = 90 # 1000 = 1 segundo

dirname = os.path.dirname(__file__)
simulationFile = os.path.join(dirname, 'data/generic.txt')
simulation = open(simulationFile, 'r')

def separate(particles_x, particles_y, particles_type):
    zombies_x = []
    zombies_y = []
    humans_x = []
    humans_y = []
    for i in range(0, len(particles_x)):
        if(particles_type[i] == 0):
            humans_x.append(particles_x[i])
            humans_y.append(particles_y[i])
        else:
            zombies_x.append(particles_x[i])
            zombies_y.append(particles_y[i])
    return humans_x, humans_y, zombies_x, zombies_y

def read_paragraph():
    lines = []
    while(True):
        line = simulation.readline()
        if(line == '\n' or line==''):
            break
        line = line.rstrip('\n')
        lines.append(line)
    return lines

def parse_paragraph(paragraph):
    particles_x = []
    particles_y = []
    particles_type = []
    for i in range(0, len(paragraph)):
        line = paragraph[i].split(' ')
        particles_x.append(float(line[0]))
        particles_y.append(float(line[1]))
        particles_type.append(int(line[2]))
    return particles_x, particles_y, particles_type

def parse_file():
    x = []
    y = []
    type = []
    while(True):
        paragraph = read_paragraph()
        if(len(paragraph) == 0):
            break
        particles_x, particles_y, particle_type = parse_paragraph(paragraph)
        x.append(particles_x)
        y.append(particles_y)
        type.append(particle_type)
    return x, y, type

def draw_box():
    plt.plot([0, 20], [0, 0], color="grey") #abajo
    plt.plot([0, 0], [20, 11.5], color="grey") #izq
    plt.plot([0, 0], [8.5, 0], color="grey") #izq
    plt.plot([0, 20], [20, 20], color="grey") #arriba
    plt.plot([20, 20], [0, 8.5], color="grey") #derecha
    plt.plot([20, 20], [20, 11.5], color="grey") #derecha

x, y, types = parse_file()

def animate(frame):
    global humans_plot
    global zombies_plot
    humans_plot.remove()
    zombies_plot.remove()
    humans_x, humans_y, zombies_x, zombies_y = separate(x[frame], y[frame], types[frame])
    humans_plot, = plt.plot(humans_x, humans_y, 'bo', markersize=3)
    zombies_plot, = plt.plot(zombies_x, zombies_y, 'go', markersize=3)

fig = plt.gcf()
humans_x_0, humans_y_0, zombies_x_0, zombies_y_0 = separate(x[0], y[0], types[0])
humans_plot, = plt.plot(humans_x_0, humans_y_0, 'bo', markersize=3)
zombies_plot, = plt.plot(zombies_x_0, zombies_y_0, 'go', markersize=3)
frames = len(x)
anim = animation.FuncAnimation(fig, animate, interval=dt, repeat=False, frames=frames)
draw_box()
plt.xlim([-3, 23])
plt.ylim([-3, 23])
plt.gca().set_aspect('equal')
#plt.show()
anim.save("./animations/15_1.gif", writer=PillowWriter(fps=33))