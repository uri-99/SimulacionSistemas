import os
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

dirname = os.path.dirname(__file__)

def distances_to_mars(filename):
    distances = []
    simulationFile = os.path.join(dirname, filename)
    simulation = open(simulationFile, 'r')
    while(True):
        line = simulation.readline()
        if(line==''):
            break
        line = line.rstrip('\n')
        distances.append(float(line))
    return distances

def graphic_distances_to_mars():
    distances = distances_to_mars('./1a.txt')
    days = range(0, 365)
    plt.xlabel('Día de despegue(u.a)', fontsize=20)
    plt.ylabel('Distancia mínima a marte(km)', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useLocale=True, useMathText=True)
    #formatter = mticker.ScalarFormatter(useMathText=True)
    #plt.yaxis.set_major_formatter(formatter)
    plt.plot(days, distances, 'o', markersize=2)
    plt.show()

def eja2():
    distances = distances_to_mars('./1a2.txt')
    minutes = range(0, 1440, 10)
    plt.xlabel('Minuto de despegue(u.a)', fontsize=20)
    plt.ylabel('Distancia mínima a marte(km)', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useLocale=True, useMathText=True)
    #formatter = mticker.ScalarFormatter(useMathText=True)
    #plt.yaxis.set_major_formatter(formatter)
    plt.plot(minutes, distances, 'o', markersize=2)
    plt.show()

def ejb():
    velocities = distances_to_mars('./1b.txt')
    days = range(0, 400)
    plt.xlabel('Tiempo(días)', fontsize=20)
    plt.ylabel('|Velocidad|(km/s)', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    #formatter = mticker.ScalarFormatter(useMathText=True)
    #plt.yaxis.set_major_formatter(formatter)
    plt.plot(days, velocities, 'o', markersize=2)
    plt.show()

def ejc():
    velocities = distances_to_mars('./1c.txt')
    days = range(0, 400)
    plt.xlabel('Tiempo(días)', fontsize=20)
    plt.ylabel('|Velocidad relativa|(km/s)', fontsize=20)
    plt.xticks([0, 100, 200, 324, 397 ], fontsize=20)
    plt.yticks(fontsize=20)
    #formatter = mticker.ScalarFormatter(useMathText=True)
    #plt.yaxis.set_major_formatter(formatter)
    plt.plot(days, velocities, 'o', markersize=2)
    plt.show()

def ej3():
    velocities = distances_to_mars('./3.txt')
    days = np.arange(0, -200, -0.1)
    plt.xlabel('Velocidad inicial (km/h)', fontsize=20)
    plt.ylabel('Distancia a marte(km)', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    #formatter = mticker.ScalarFormatter(useMathText=True)
    #plt.yaxis.set_major_formatter(formatter)
    plt.plot(days, velocities, 'o', markersize=2)
    plt.show()

def ej2():
    velocities = [2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 25, 50, 100, 200, 300]
    days = [329, 327, 329, 330, 329, 328, 324, 328, 328, 327, 323, 316, 309, 301, 298]
    plt.xlabel('Velocidad inicial (km/s)', fontsize=20)
    plt.ylabel('Día de lanzamiento(u.a)', fontsize=20)
    plt.semilogx(velocities, days, 'o', markersize=3)
    plt.xticks([8, 10, 50, 100], fontsize=20)
    plt.axes().get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    plt.yticks(fontsize=20)
    plt.show()
# eja1
#graphic_distances_to_mars()

#eja2()

#ejb()

ej2()

#ejc()

#ej3()