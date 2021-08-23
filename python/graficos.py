from matplotlib import pyplot as plt
import os
import math
import numpy as np

dirname = os.path.dirname(__file__)
data_file = os.path.join(dirname, 'data')
variable_file = os.path.join(dirname, 'n')

data = open(data_file, 'r')
variable = open(variable_file, 'r')

# ignores first iteration outlier
for _ in range(10):
    data.readline()

def analyze_data(file):
    x_array_size = []
    x_array_particles = []
    y_array_sim = []
    y_array_brute_force = []
    for i in range(1, 49):
        brute_force_accum = 0
        sim_accum = 0
        size = 0
        particles = 0
        print(i)
        for j in range(10):
            line = file.readline().rsplit(' ')
            line.pop() # sacando el \n
            particles = int(line[0])
            size = int(line[1])
            brute_force_time = int(line[2])
            sim_time = int(line[3])
            brute_force_accum += brute_force_time
            sim_accum += sim_time
        brute_force_promedy = brute_force_accum/49
        sim_promedy = sim_accum/49
        y_array_brute_force.append(brute_force_promedy/1000) # lo pasamos a micro
        y_array_sim.append(sim_promedy/1000) # lo pasamos a micro
        x_array_size.append(size)
        x_array_particles.append(particles)
    return x_array_size, x_array_particles, y_array_sim, y_array_brute_force

size, particles, sim, brute_force = analyze_data(data)
variable_size, variable_particles, variable_sim, variable_brute_force = analyze_data(variable)

fig, axs = plt.subplots(2)

axs[0].set_title('CIM vs Fuerza bruta variando cantidad de celdas')
axs[0].set(xlabel='cantidad de celdas', ylabel='tiempo[µs]')
axs[0].plot(size, brute_force, color='r', label='fuerza bruta')
axs[0].plot(size, sim, color='g', label='cim')
axs[0].legend()


axs[1].set_title('CIM vs Fuerza bruta variando cantidad de particulas')
axs[1].set(xlabel='cantidad de particulas', ylabel='tiempo[µs]')
axs[1].plot(variable_particles, variable_brute_force, color='r', label='fuerza bruta')
axs[1].plot(variable_particles, variable_sim, color='g', label='cim')
axs[1].legend()

plt.ticklabel_format(useOffset=False, style='plain', axis='y')

plt.show()