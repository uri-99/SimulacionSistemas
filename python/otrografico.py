from matplotlib import pyplot as plt
import os
import math
import numpy as np

dirname = os.path.dirname(__file__)
data_file = os.path.join(dirname, 'n')

data = open(data_file, 'r')

x_array = []
y_array_sim = []
y_array_brute_force = []

# ignores first iteration outlier
for k in range(10):
    data.readline()

for i in range(1, 49):
    brute_force_accum = 0
    sim_accum = 0
    size = 0
    for j in range(10):
        line = data.readline().rsplit(' ')
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
    x_array.append(size)

plt.xlabel('cantidad de celdas')
plt.ylabel('tiempo[µs]')
box_props = dict(facecolor='none', edgecolor='grey')
plt.text(37, 1500, 'N = 1000\nL = 100\nRc = 1', style='italic', bbox=box_props)
plt.ticklabel_format(useOffset=False, style='plain', axis='y')

plt.plot(x_array, y_array_brute_force, color='r', label='fuerza bruta')
plt.plot(x_array, y_array_sim, color='g', label='cim')

plt.legend()

print(y_array_brute_force)

plt.title('CIM vs Fuerza bruta')

plt.show()