import os
from matplotlib import pyplot as plt
import numpy as np

dirname = os.path.dirname(__file__)


def ejb():
    dataFile = os.path.join(dirname, './data/ejb.txt')
    data = open(dataFile, 'r')
    attackers = []
    escapeHumans = []
    deviations = []
    while(True):
        line = data.readline()
        line = line.rstrip('\n')
        if(line == '\n' or line == ''):
            break
        values = line.split(' ')
        attackers.append(float(values[0]))
        escapeHumans.append(float(values[1]))
        deviations.append(float(values[2]))
    plt.xlabel('Cantidad de attackers', fontsize=20)
    plt.ylabel('Fracción de personas que lograron escapar(u.a)', fontsize=20)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    plt.errorbar(attackers, escapeHumans, ecolor="grey", fmt='-o', ms=2, yerr=deviations )
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
    plt.xlabel('Velocidad máxima de los attackers(m/s)', fontsize=20)
    plt.ylabel('Fracción de personas que lograron escapar(u.a)', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.errorbar(velocities, escapeHumans, ecolor="grey", fmt='-o', ms=2, yerr=deviations )
    plt.show()

def caudal():
    dataFile = os.path.join(dirname, './data/caudal.txt')
    data = open(dataFile, 'rb')
    scapeTimes = np.load(data)
    print(scapeTimes)
    plt.figure(figsize=(15,1))
    plt.plot(scapeTimes, len(scapeTimes) * [1], "x")
    plt.yticks([])
    plt.xlabel('Tiempo (s)', fontsize=20)
    plt.ylabel('Humano saliendo', fontsize=20)
    plt.xlim([0, 42])
    plt.xticks(fontsize=20)
    plt.show()
    # plt.errorbar(attackers, escapeHumans, ecolor="grey", fmt='-o', ms=2)

caudal()