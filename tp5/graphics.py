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
    plt.errorbar(zombies, escapeHumans, ecolor="grey", fmt='-o', ms=2, yerr=deviations )
    plt.show()

ejb()