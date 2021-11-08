import os
from matplotlib import pyplot as plt

dirname = os.path.dirname(__file__)


def ejb():
    dataFile = os.path.join(dirname, './data/ejb.txt')
    data = open(dataFile, 'r')
    zombies = []
    escapeHumans = []
    deviations = []
    while(True):
        line = data.readline()
        line = line.rstrip('\n')
        if(line == '\n' or line == ''):
            break
        values = line.split(' ')
        zombies.append(float(values[0]))
        escapeHumans.append(float(values[1]))
        deviations.append(float(values[2]))
    plt.xlabel('Cantidad de zombies(u.a)', fontsize=20)
    plt.ylabel('Fracción de personas que lograron escapar(u.a)', fontsize=20)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    plt.errorbar(zombies, escapeHumans, ecolor="grey", fmt='-o', ms=2, yerr=deviations )
    plt.show()

def ejc():
    dataFile = os.path.join(dirname, './data/ejc.txt')
    data = open(dataFile, 'r')
    velocities = []
    escapeHumans = []
    deviations = []
    while(True):
        line = data.readline()
        line = line.rstrip('\n')
        if(line == '\n' or line == ''):
            break
        values = line.split(' ')
        velocities.append(float(values[0]))
        escapeHumans.append(float(values[1]))
        deviations.append(float(values[2]))
    plt.xlabel('Velocidad máxima de los zombies(m/s)', fontsize=20)
    plt.ylabel('Fracción de personas que lograron escapar(u.a)', fontsize=20)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.errorbar(velocities, escapeHumans, ecolor="grey", fmt='-o', ms=2, yerr=deviations )
    plt.show()

ejb()