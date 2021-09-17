import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np;
from ast import literal_eval as make_tuple
import sys
import math
import os

dirname = os.path.dirname(__file__)
simulationFile = os.path.join(dirname, 'data.txt')
simulation = open(simulationFile, 'r')

def read_params():
    params = []
    while(True):
        line = simulation.readline()
        if(line == '\n'):
            break
        line = line.rstrip('\n')
        params.append(line)
    return params

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
    left = make_tuple(paragraph[0])
    time = float(paragraph[1])
    particles_ids = []
    particles_x = []
    particles_y = []
    for i in range(2, len(paragraph)):
        line = paragraph[i].split(' ')
        particles_ids.append(int(line[0]))
        particles_x.append(float(line[1]))
        particles_y.append(float(line[2]))
    return left, time, particles_ids, particles_x, particles_y

def parse_file():
    differences = []
    times = []
    ids = []
    x = []
    y = []
    while(True):
        paragraph = read_paragraph()
        if(len(paragraph) == 0):
            break
        difference, time, particles_ids, particles_x, particles_y = parse_paragraph(paragraph)
        differences.append(difference)
        times.append(time*100)
        ids.append(particles_ids)
        x.append(particles_x)
        y.append(particles_y)
    return differences, times, ids, x, y

def draw_mid_line(size):
    plt.plot([0.12, 0.12], [0.09, 0.09/2 + size/2], color='grey')
    plt.plot([0.12, 0.12], [0, 0.09/2 - size/2], color='grey')

def draw_box():
    plt.plot([0, 0.24], [0, 0], color="grey") #abajo
    plt.plot([0, 0], [0.09, 0], color="grey") #izq
    plt.plot([0, 0.24], [0.09, 0.09], color="grey") #arriba
    plt.plot([0.24, 0.24], [0, 0.09], color="grey") #derecha

N, opening = read_params()
differences, times, ids, x, y = parse_file()

current_index = 1

def animate(frame_number):
    global current_index
    if(frame_number > times[current_index]):
        print(times[current_index])
        print(frame_number)
        global d
        d.remove()
        d, = plt.plot(x[current_index], y[current_index], 'bo', markersize=2)
        current_index = current_index + 1

fig = plt.gcf()
draw_mid_line(float(opening))
d, = plt.plot(x[0], y[0], 'bo', markersize=2)
anim = animation.FuncAnimation(fig, animate, frames=int(times[len(times)-1])*1000, interval=1, repeat=False)
plt.xlim([0, 0.24])
plt.ylim([0, 0.09])
plt.gca().set_aspect('equal')
plt.show()