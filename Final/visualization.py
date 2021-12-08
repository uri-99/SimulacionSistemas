import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter
import os

dt = 90 # 1000 = 1 segundo

dirname = os.path.dirname(__file__)
simulationFile = os.path.join(dirname, 'data/generic.txt')
simulation = open(simulationFile, 'r')

def separate(particles_x, particles_y, particles_type): #type 0 guards, type1 attackers, type2 vip, typ3 dead
    guards_x = []
    guards_y = []
    attackers_x = []
    attackers_y = []
    dead_x = []
    dead_y = []
    vip_x = 0
    vip_y = 0
    for i in range(0, len(particles_x)):
        if(particles_type[i] == 0):
            guards_x.append(particles_x[i])
            guards_y.append(particles_y[i])
        elif(particles_type[i] == 1):
            attackers_x.append(particles_x[i])
            attackers_y.append(particles_y[i])
        elif(particles_type[i] == 3):
            dead_x.append(particles_x[i])
            dead_y.append(particles_y[i])
        else:
            vip_x = particles_x[i]
            vip_y = particles_y[i]
    return guards_x, guards_y, attackers_x, attackers_y, vip_x, vip_y, dead_x, dead_y

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
    global guards_plot
    global attackers_plot
    global vip_plot
    global dead_plot
    guards_plot.remove()
    attackers_plot.remove()
    vip_plot.remove()
    dead_plot.remove()
    guards_x, guards_y, attackers_x, attackers_y, vip_x, vip_y, dead_x, dead_y = separate(x[frame], y[frame], types[frame])
    guards_plot, = plt.plot(guards_x, guards_y, 'bo', markersize=3)
    attackers_plot, = plt.plot(attackers_x, attackers_y, 'go', markersize=3)
    vip_plot, = plt.plot(vip_x, vip_y, 'yo', markersize=3)
    dead_plot, = plt.plot(dead_x, dead_y, 'ro', markersize=3)

fig = plt.gcf()
guards_x_0, guards_y_0, attackers_x_0, attackers_y_0, vip_x_0, vip_y_0, dead_x_0, dead_y_0 = separate(x[0], y[0], types[0])
guards_plot, = plt.plot(guards_x_0, guards_y_0, 'bo', markersize=3)
attackers_plot, = plt.plot(attackers_x_0, attackers_y_0, 'go', markersize=3)
vip_plot, = plt.plot(vip_x_0, vip_y_0, 'yo', markersize=3)
dead_plot, = plt.plot(dead_x_0, dead_y_0, 'ro', markersize=3)
frames = len(x)
anim = animation.FuncAnimation(fig, animate, interval=dt, repeat=False, frames=frames)
draw_box()
plt.xlim([-3, 23])
plt.ylim([-3, 23])
plt.gca().set_aspect('equal')
#plt.show()
anim.save("./animations/15_1.gif", writer=PillowWriter(fps=33))
