import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation
from arquitecture.Grid import Grid
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np;
import sys
import math

offset_pair = 0.5
offset_odd = 0.5

particles = int(sys.argv[1])
opening = int(sys.argv[2])
iteration = int(sys.argv[3])

fig = plt.gcf()
matrix = np.load('./simulation/data_'+str(particles)+'-'+str(opening)+'_'+str(iteration) + '.npy')


def calculate_position(i, j):
    i_offset = i #y
    j_offset = j #x
    if(i % 2 == 0):
       j_offset -= 0.5 #0.5
    return i_offset, j_offset

def matrix_to_particles(matrix):
    particles_x = []
    particles_y = []
    for i in range(203):
        for j in range(203):
            if(matrix[i][j] == 1):
                i_offset, j_offset = calculate_position(i, j)
                particles_y.append(i_offset)
                particles_x.append(j_offset)
    return particles_x, particles_y

def draw_mid_line(size):
    plt.plot([101, 101], [0, 203/2 - size/2], color='grey')
    plt.plot([101, 101], [203, 203/2 + size/2], color='grey')

def separate_particles(particles_x, particles_y, old_particles_x):
    new_particles_x_left = []
    new_particles_x_right = []
    new_particles_y_left = []
    new_particles_y_right = []
    for i in range(len(particles_x)):
        if(particles_x[i] < 101 or (particles_x[i] == 101)):
            new_particles_x_left.append(particles_x[i])
            new_particles_y_left.append(particles_y[i])
        else:
            new_particles_x_right.append(particles_x[i])
            new_particles_y_right.append(particles_y[i])
    return new_particles_x_left, new_particles_x_right, new_particles_y_left, new_particles_y_right

def animate(frame_number):
    global d  # need it to remove old plot
    global d1
    d.remove()
    d1.remove()
    old_particles_x = matrix_to_particles(matrix[frame_number])
    new_particles_x, new_particles_y = matrix_to_particles(matrix[frame_number + 1])
    new_particles_x_left, new_particles_x_right, new_particles_y_left, new_particles_y_right = separate_particles(new_particles_x, new_particles_y, old_particles_x)
    print(len(new_particles_x_left))
    d, = plt.plot(new_particles_x_left, new_particles_y_left, 'bo', color=(0, 1, (len(new_particles_x_right)*2/particles)), markersize=2)
    d1, = plt.plot(new_particles_x_right, new_particles_y_right, 'bo', color=(0, (len(new_particles_x_right)*2/particles), 1), markersize=2)
    #d, = plt.plot(new_particles_x, new_particles_y, 'go', markersize=2)
    

particles_x, particles_y = matrix_to_particles(matrix[0])
new_particles_x_left, new_particles_x_right, new_particles_y_left, new_particles_y_right = separate_particles(particles_x, particles_y, particles_x)
d, = plt.plot(new_particles_x_left, new_particles_y_left, 'bo', color=(0, 1, 0), markersize=2)
d1, = plt.plot(new_particles_x_right, new_particles_y_right, 'bo', color=(0, 0, 1), markersize=2)
draw_mid_line(opening)
plt.plot([0, 203], [0, 0], color="grey") #abajo
plt.plot([0, 0], [203, 0], color="grey") #izq
plt.plot([0, 203], [203, 203], color="grey") #arriba
plt.plot([203, 203], [0, 203], color="grey") #derecha
anim = animation.FuncAnimation(fig, animate, frames=1000, interval=1, repeat=False)
anim.save("./simulation_videos/2000_25.gif", writer=PillowWriter(fps=30))
plt.xlim([0, 203])
plt.ylim([0, 203])
plt.gca().set_aspect('equal', adjustable='box')
#plt.show()
