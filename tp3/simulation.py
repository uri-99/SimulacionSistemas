import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np;
from ast import literal_eval as make_tuple
import sys
import math
import os
import time

dirname = os.path.dirname(__file__)
simulationFile = os.path.join(dirname, './data/tp3_variacion_V/100_0.01_V0.015_1.txt')
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
        times.append(int(time*1000))
        ids.append(particles_ids)
        x.append(particles_x)
        y.append(particles_y)
    return differences, times, ids, x, y

def draw_mid_line(size):
    plt.plot([0.12, 0.12], [0.09, 0.09/2 + size/2 + 0.002], color='grey')
    plt.plot([0.12, 0.12], [0, 0.09/2 - size/2 - 0.002 ], color='grey')

def draw_box():
    plt.plot([0, 0.24], [0, 0], color="grey") #abajo
    plt.plot([0, 0], [0.09, 0], color="grey") #izq
    plt.plot([0, 0.24], [0.09, 0.09], color="grey") #arriba
    plt.plot([0.24, 0.24], [0, 0.09], color="grey") #derecha

N, opening = read_params()
differences, times, ids, x, y = parse_file()

current_index = 1

initial_time_ms = time.time()*1000

def animate(frame):
    global current_index
    global text
    if(frame*20 > times[current_index]):
        current_index = current_index + 1
    global d
    d.remove()
    d, = plt.plot(x[current_index], y[current_index], 'bo', markersize=4)
    text.remove()
    text = fig.text(0.65, 0.7, 
        "Partículas de cada lado:\nIzquierda:"+str(differences[current_index][0])+"\nDerecha:"+str(differences[current_index][1]))
    print(frame)

fig = plt.gcf()
draw_mid_line(float(opening))
d, = plt.plot(x[0], y[0], 'bo', markersize=4)
text = fig.text(0.8, 0.8, 
         "Partículas de cada lado:\nizquierda:"+str(differences[0][0])+"\nderecha:"+str(differences[0][1]))
total_time = times[len(times) - 1]
frames = int(total_time / 20)
print(frames)
anim = animation.FuncAnimation(fig, animate, interval=10, repeat=False, frames=frames)
plt.xlim([0, 0.24])
plt.ylim([0, 0.09])
plt.gca().set_aspect('equal')
#plt.show()
#print(total_frames)
anim.save("./simulation_videos/variacion_V_100_0.01_V0.015_1.gif", writer=PillowWriter(fps=50))