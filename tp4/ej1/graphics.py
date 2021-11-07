import os
from matplotlib import pyplot as plt
import numpy as np
from functools import reduce

dirname = os.path.dirname(__file__)
simulationFile = os.path.join(dirname, './data/data_99.txt')
errorsFile = os.path.join(dirname, './data/errors.txt')
errors = open(errorsFile, "rb")
data = open(simulationFile, "rb")

dt = 10**-2

verlet_errors = np.load(errors)
beeman_errors = np.load(errors)
gear_errors = np.load(errors)

print(len(verlet_errors))

print(verlet_errors)

analytic = np.load(data)
verlet = np.load(data)
beeman = np.load(data)
gear = np.load(data)

print(len(verlet))

data.close()

errors.close()

def graphic_func():
    times = np.arange(0, len(analytic)*dt, dt)
    plt.xlabel('Tiempo(s)', fontsize=20)
    plt.ylabel('Posición(m)', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.plot(times, analytic, '--', label = 'Analítica')
    plt.plot(times, verlet, '--', label = 'Verlet')
    plt.plot(times, beeman, '--', label = 'Beeman')
    plt.plot(times, gear, '--', label='Gear')
    plt.legend()
    plt.show()

def graphic_errors():
    times = np.arange(10**-4, 10**-2, 10**-4)
    plt.xlabel('dt(s)', fontsize=20)
    plt.ylabel(r'$ECM(m^2)$', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.plot(times, verlet_errors, 'o', markersize=2, label='Verlet')
    plt.plot(times, beeman_errors, 'o', markersize=2, label='Beeman')
    plt.plot(times, gear_errors, 'o', markersize=2, label='Gear')
    plt.gca().set_yscale('log', base = 10)
    plt.legend()
    plt.show()

print(verlet_errors[98])
print(beeman_errors[98])
print(gear_errors[98])
graphic_errors()