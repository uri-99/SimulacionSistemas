import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation
import os

dt = 1000 # 1 segundo

dirname = os.path.dirname(__file__)
simulationFile = os.path.join(dirname, './ej.txt')
simulation = open(simulationFile, 'r')

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
    print(particles_x)
    print(particles_y)
    print(particles_type)
    return particles_x, particles_y, particles_type

def parse_file():
    x = []
    y = []
    particle_type = []
    while(True):
        paragraph = read_paragraph()
        print(paragraph)
        if(len(paragraph) == 0):
            break
        particles_x, particles_y, particle_type = parse_paragraph(paragraph)
        x.append(particles_x)
        y.append(particles_y)
        particle_type.append(particle_type)
    return x, y, particle_type

def draw_box():
    plt.plot([0, 20], [0, 0], color="grey") #abajo
    plt.plot([0, 0], [20, 0], color="grey") #izq
    plt.plot([0, 20], [20, 20], color="grey") #arriba
    plt.plot([20, 20], [0, 20], color="grey") #derecha

x, y, types = parse_file()
print(x)
print(y)
print(types)

def animate(frame):
    global d
    d.remove()
    d, = plt.plot(x[frame], y[frame], 'bo', markersize=4)

fig = plt.gcf()
d, = plt.plot(x[0], y[0], 'bo', markersize=4)
frames = len(x)
anim = animation.FuncAnimation(fig, animate, interval=dt, repeat=False, frames=frames)
plt.xlim([0, 20])
plt.ylim([0, 20])
plt.gca().set_aspect('equal')
plt.show()