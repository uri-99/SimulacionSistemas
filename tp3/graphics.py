from matplotlib import pyplot as plt
from ast import literal_eval as make_tuple
import matplotlib.ticker as mticker
import os
import numpy as np

dirname = os.path.dirname(__file__)

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

def average_arrays(arrays):
    initial_array = np.copy(arrays[0])
    for i in range(1, len(arrays)):
        for j in range(len(arrays[i])):
            if(len(initial_array) <= j):
                np.append(initial_array, arrays[i][j])
            else:
                initial_array[j] = (initial_array[j] + arrays[i][j]) / 2
    return initial_array


def read_params(simulation):
    params = []
    while(True):
        line = simulation.readline()
        if(line == '\n'):
            break
        line = line.rstrip('\n')
        params.append(line)
    return params

def read_paragraph(simulation):
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

def parse_file(simulation):
    differences = []
    times = []
    ids = []
    x = []
    y = []
    while(True):
        paragraph = read_paragraph(simulation)
        if(len(paragraph) == 0):
            break
        difference, time, particles_ids, particles_x, particles_y = parse_paragraph(paragraph)
        differences.append(difference)
        times.append(int(time))
        ids.append(particles_ids)
        x.append(particles_x)
        y.append(particles_y)
    return differences, times, ids, x, y


def calculate_ek(v):
    return pow(v, 2)/2

def linear_func(x):
    return 5103.41*x

def get_first_tuple(tuple):
    return tuple[0]

def to_fraction_100(elem):
    return elem/100

def to_fraction_25(elem):
    return elem/25

def original_case():
    simulationFile = os.path.join(dirname, './data/tp3_variacion_N/100_0.01_1.txt')
    simulation = open(simulationFile, 'r')
    N, opening = read_params(simulation)
    differences, times, ids, x, y = parse_file(simulation)
    differences_parsed = list(map(get_first_tuple, differences))
    differences_fractions = list(map(to_fraction_100, differences_parsed))
    plt.plot(times, differences_fractions, 'bo', markersize=1)
    plt.xlabel('tiempo[s]', fontsize=20)
    plt.ylabel('fracción de partículas[u.a]', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.show()

def variable_n():
    simulation_file_25 = os.path.join(dirname, './data/tp3_variacion_N/25_0.01_2.txt')
    simulation_25 = open(simulation_file_25, 'r')
    N_25, opening_25 = read_params(simulation_25)
    differences_25, times_25, ids_25, x_25, y_25 = parse_file(simulation_25)
    print(differences_25)
    differences_25_parsed = list(map(get_first_tuple, differences_25))
    differences_25_fractions = list(map(to_fraction_25, differences_25_parsed))
    simulation_file_100 = os.path.join(dirname, './data/tp3_variacion_N/100_0.01_1.txt')
    simulation_100 = open(simulation_file_100, 'r')
    N_100, opening_100 = read_params(simulation_100)
    differences_100, times_100, ids_100, x_100, y_100 = parse_file(simulation_100)
    differences_100_parsed = list(map(get_first_tuple, differences_100))
    differences_100_fractions = list(map(to_fraction_100, differences_100_parsed))
    plt.plot(times_25, differences_25_fractions, 'bo', markersize=1, label='N=25')
    plt.plot(times_100, differences_100_fractions, 'go', markersize=1, label='N=100')
    plt.xlabel('tiempo[s]', fontsize=20)
    plt.ylabel('fracción de partículas[u.a]', fontsize=20)
    x_ticks = [0, 100, 200, times_100[len(times_100)-1], 300, 400, times_25[len(times_25)-1]]
    plt.xticks(x_ticks, fontsize=20)
    plt.yticks(fontsize=20)
    plt.legend()
    plt.show()

def variable_d():
    simulation_file_1 = os.path.join(dirname, './data/tp3_variacion_D/100_0.01_1.txt')
    simulation_1 = open(simulation_file_1, 'r')
    N_1, opening_1 = read_params(simulation_1)
    differences_1, times_1, ids_1, x_1, y_1 = parse_file(simulation_1)
    print(differences_1)
    differences_1_parsed = list(map(get_first_tuple, differences_1))
    differences_1_fractions = list(map(to_fraction_100, differences_1_parsed))
    simulation_file_7 = os.path.join(dirname, './data/tp3_variacion_D/100_0.07_2.txt')
    simulation_7 = open(simulation_file_7, 'r')
    N_100, opening_7 = read_params(simulation_7)
    differences_7, times_7, ids_7, x_7, y_7 = parse_file(simulation_7)
    differences_7_parsed = list(map(get_first_tuple, differences_7))
    differences_7_fractions = list(map(to_fraction_100, differences_7_parsed))
    plt.plot(times_1, differences_1_fractions, 'bo', markersize=1, label='D=0.01')
    plt.plot(times_7, differences_7_fractions, 'go', markersize=1, label='D=0.07')
    plt.xlabel('tiempo[s]', fontsize=20)
    plt.ylabel('fracción de partículas[u.a]', fontsize=20)
    x_ticks = [0, times_1[len(times_1)-1], 100, 200, times_7[len(times_7)-1]]
    plt.xticks(x_ticks, fontsize=20)
    plt.yticks(fontsize=20)
    plt.legend()
    plt.show()

def variable_v():
    simulation_file_1 = os.path.join(dirname, './data/tp3_variacion_V/100_0.01_V0.005_2.txt')
    simulation_1 = open(simulation_file_1, 'r')
    N_1, opening_1 = read_params(simulation_1)
    differences_1, times_1, ids_1, x_1, y_1 = parse_file(simulation_1)
    print(differences_1)
    differences_1_parsed = list(map(get_first_tuple, differences_1))
    differences_1_fractions = list(map(to_fraction_100, differences_1_parsed))
    simulation_file_7 = os.path.join(dirname, './data/tp3_variacion_V/100_0.01_V0.02_2.txt')
    simulation_7 = open(simulation_file_7, 'r')
    N_100, opening_7 = read_params(simulation_7)
    differences_7, times_7, ids_7, x_7, y_7 = parse_file(simulation_7)
    differences_7_parsed = list(map(get_first_tuple, differences_7))
    differences_7_fractions = list(map(to_fraction_100, differences_7_parsed))
    plt.plot(times_1, differences_1_fractions, 'bo', markersize=1, label='V=0.005')
    plt.plot(times_7, differences_7_fractions, 'go', markersize=1, label='V=0.02')
    plt.xlabel('tiempo[s]', fontsize=20)
    plt.ylabel('fracción de partículas[u.a]', fontsize=20)
    x_ticks = [0, 100,times_1[len(times_1)-1], 300, 400, times_7[len(times_7)-1]]
    plt.xticks(x_ticks, fontsize=20)
    plt.yticks(fontsize=20)
    plt.legend()
    plt.show()

def n_vs_t():
    N = [25, 50, 75, 100]
    T_25 = [567, 490, 450]
    T_50 = [502, 467, 430]
    T_75 = [293, 267, 235]
    T_100 = [257, 234, 207]
    # average
    T = [502, 466, 265, 232]
    y_err_max = [65, 35, 26, 23]
    y_err_min = [40, 37, 32, 27]
    plt.errorbar(N, T, ecolor="grey", fmt='-o', ms=2, yerr=[y_err_max, y_err_min] )
    x_ticks = [0, 25, 75, 50, 100]
    plt.xticks(x_ticks, fontsize=20)
    plt.yticks(fontsize=20)
    plt.ylabel('tiempo[s]', fontsize=20)
    plt.xlabel('partículas', fontsize=20)
    plt.show()

def d_vs_t():
    D = [0.01, 0.02, 0.05, 0.07]
    T_1 = [234, 203, 170]
    T_2 = [152, 146, 106]
    T_5 = [50, 35, 28]
    T_7 = [28, 21, 17]
    # average
    T = [202, 134, 37, 22]
    y_err_max = [32, 18, 13, 6]
    y_err_min = [32, 28, 9, 5]
    plt.errorbar(D, T, ecolor="grey", fmt='-o', ms=2, yerr=[y_err_max, y_err_min] )
    x_ticks = [0, 0.01, 0.02, 0.05, 0.07]
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.ylabel('tiempo[s]', fontsize=20)
    plt.xlabel('apertura[m]', fontsize=20)
    plt.show()

def v_vs_t():
    V = [0.005, 0.01, 0.015, 0.02]
    T_05 = [630, 520, 401]
    T_1 = [280, 234, 207]
    T_15 = [231, 218, 192]
    T_2 = [167, 150, 132]
    # average
    T = [517, 240, 213, 149]
    y_err_max = [113, 40, 18, 18]
    y_err_min = [116, 33, 21, 17]
    plt.errorbar(V, T, ecolor="grey", fmt='-o', ms=2, yerr=[y_err_max, y_err_min] )
    x_ticks = [0, 0.01, 0.02, 0.05, 0.07]
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.ylabel('tiempo[s]', fontsize=20)
    plt.xlabel('velocidad[m/s]', fontsize=20)
    plt.show()

def P_vs_Ek():
    V = [0.005, 0.01, 0.015, 0.02]
    Ek = list(map(calculate_ek, V))
    linear_Ek = list(map(linear_func, Ek))
    print(Ek)
    P = [0.06432478245847889, 0.25819076499992144, 0.5796720828451926, 1.0167769649687661]
    sigma = [0.006788893498617811, 0.018015313636519772, 0.02595613320772382, 0.04159377638051669]
    plt.xlabel('Energía cinética media[J]', fontsize=20)
    plt.ylabel('Presión[kg/s^2]', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0), useMathText=True)
    plt.errorbar(Ek, P, fmt='bo', ecolor="grey", ms=3, yerr=sigma)
    #plt.plot(Ek, linear_Ek, ms=3)
    plt.show()

def P_vs_Ek_no_error():
    V = [0.005, 0.01, 0.015, 0.02]
    Ek = list(map(calculate_ek, V))
    linear_Ek = list(map(linear_func, Ek))
    print(Ek)
    P = [0.06432478245847889, 0.25819076499992144, 0.5796720828451926, 1.0167769649687661]
    sigma = [0.006788893498617811, 0.018015313636519772, 0.02595613320772382, 0.04159377638051669]
    plt.xlabel('Energía cinética media[J]', fontsize=20)
    plt.ylabel('Presión[kg/s^2]', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0), useLocale=True, useMathText=True)
    #formatter = mticker.ScalarFormatter(useMathText=True)
    #plt.yaxis.set_major_formatter(formatter)
    plt.plot(Ek, P)
    plt.plot(Ek, linear_Ek, 'bo', ms=3)
    plt.show()

P_vs_Ek()