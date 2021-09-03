import os
from matplotlib import pyplot as plt
import numpy as np
import sys

particles = int(sys.argv[1])
opening = int(sys.argv[2])
iterations_arg = int(sys.argv[3])

def initialize_empty_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append([])
    return matrix

def file_to_array(name, params_quantity):
    dirname = os.path.dirname(__file__)
    simulationFile = os.path.join(dirname, name)
    data = open(simulationFile, 'r')
    line = data.readline().rstrip('\n')
    data_array = initialize_empty_matrix(params_quantity)
    while(line != '' and line!= '\n'):
        array_line = line.split(' ')
        array_line.pop()
        for j in range(params_quantity):
            data_array[j].append(int(array_line[j]))
        line = data.readline().rstrip('\n')
    return data_array

def filename(particles, size, iteration):
    return 'data/data_'+str(particles)+'-'+str(size)+'_'+str(iteration)+'.txt'

def promedy_max_min(iterations):
    iterations_data = initialize_empty_matrix(3)
    for i in range(iterations):
        data = file_to_array(filename(particles, opening, i+1), 3)
        for j in range(len(data)):
            iterations_data[j].append(data[j])
    return iterations_data

def max_array_index(arrays):
    max_array_index = 0
    for i in range(1, len(arrays)):
        if(len(arrays[i]) > max_array_index):
            max_array_index = i
    return max_array_index

def average_arrays(arrays):
    initial_array = np.copy(arrays[0])
    for i in range(1, len(arrays)):
        for j in range(len(arrays[i])):
            if(len(initial_array) <= j):
                np.append(initial_array, arrays[i][j])
            else:
                initial_array[j] = (initial_array[j] + arrays[i][j]) / 2
    return initial_array

def max_arrays(arrays):
    initial_array = np.copy(arrays[0])
    for i in range(1, len(arrays)):
        for j in range(len(arrays[i])):
            if(len(initial_array) <= j):
                np.append(initial_array, arrays[i][j])
            else:
                if (initial_array[j] < arrays[i][j]):
                    initial_array[j] = arrays[i][j]
    return initial_array

def min_arrays(arrays):
    initial_array = arrays[0]
    for i in range(1, len(arrays)):
        for j in range(len(arrays[i])):
            if(len(initial_array) <= j):
                np.append(initial_array, arrays[i][j])
            else:
                if (initial_array[j] > arrays[i][j]):
                    initial_array[j] = arrays[i][j]
    return initial_array

frame_array, left_particles_array, right_particles_array = promedy_max_min(iterations_arg)

average_frame = average_arrays(frame_array)
average_left_particles = average_arrays(left_particles_array)
average_right_particles = average_arrays(right_particles_array)
max_left_particles = max_arrays(left_particles_array)
min_left_particles = min_arrays(left_particles_array)
max_right_particles = max_arrays(right_particles_array)
min_right_particles = min_arrays(right_particles_array)

plt.errorbar(average_frame, average_left_particles, ecolor="grey", fmt='o', ms=2, yerr=[np.subtract(average_left_particles, min_left_particles), np.subtract(max_left_particles, average_left_particles)])
plt.errorbar(average_frame, average_right_particles, ecolor='grey', fmt='o', ms=2,  yerr=[np.subtract(average_right_particles, min_right_particles), np.subtract(max_right_particles, average_right_particles)])
plt.xlabel('iteraciones', fontsize=20)
plt.ylabel('partículas', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

# plt.title(str(particles) + " partículas, " + str(opening) + " de apertura, " + str(iterations_arg) + " iteraciones")

plt.legend()
plt.show()
