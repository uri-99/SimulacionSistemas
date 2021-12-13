import os
from matplotlib import pyplot as plt
import numpy as np

dirname = os.path.dirname(__file__)
# 
#



# def ejb():
#     dataFile = os.path.join(dirname, './ej1.txt')
#     data = open(dataFile, 'r')
#     zombies = []
#     escapeHumans = []
#     deviations = []
#     while(True):
#         line = data.readline()
#         line = line.rstrip('\n')
#         if(line == '\n' or line == ''):
#             break
#         values = line.split(' ')
#         zombies.append(float(values[0]))
#         escapeHumans.append(float(values[1]))
#         deviations.append(float(values[2]))
#     plt.xlabel('Cantidad de zombies', fontsize=20)
#     plt.ylabel('Fracción de personas que lograron escapar(u.a)', fontsize=20)
#     plt.yticks(fontsize=20)
#     plt.xticks(fontsize=20)
#     plt.errorbar(zombies, escapeHumans, ecolor="grey", fmt='-o', ms=2, yerr=deviations )
#     plt.show()
#
# def ejc():
#     dataFile = os.path.join(dirname, './data/ejc.txt')
#     data = open(dataFile, 'r')
#     velocities = []
#     escapeHumans = []
#     deviations = []
#     while(True):
#         line = data.readline()
#         line = line.rstrip('\n')
#         if(line == '\n' or line == ''):
#             break
#         values = line.split(' ')
#         velocities.append(float(values[0]))
#         escapeHumans.append(float(values[1]))
#         deviations.append(float(values[2]))
#     plt.xlabel('Velocidad máxima de los zombies(m/s)', fontsize=20)
#     plt.ylabel('Fracción de personas que lograron escapar(u.a)', fontsize=20)
#     plt.xticks(fontsize=20)
#     plt.yticks(fontsize=20)
#     plt.errorbar(velocities, escapeHumans, ecolor="grey", fmt='-o', ms=2, yerr=deviations )
#     plt.show()
#
# def caudal():
#     dataFile = os.path.join(dirname, './data/caudal.txt')
#     data = open(dataFile, 'rb')
#     scapeTimes = np.load(data)
#     print(scapeTimes)
#     plt.figure(figsize=(15,1))
#     plt.plot(scapeTimes, len(scapeTimes) * [1], "x")
#     plt.yticks([])
#     plt.xlabel('Tiempo (s)', fontsize=20)
#     plt.ylabel('Humano saliendo', fontsize=20)
#     plt.xlim([0, 42])
#     plt.xticks(fontsize=20)
#     plt.show()
#     # plt.errorbar(zombies, escapeHumans, ecolor="grey", fmt='-o', ms=2)
#
# caudal()

standardVariation = [0, 0.3, 0.4, 0.4583, 0.4899, 0.5, 0.4899, 0.4583, 0.4, 0.3, 0]

def successToStandarVariation(success_array):
    result = []
    for i in range(0, len(success_array)):
        result.append(standardVariation[success_array[i]])
    return result

def part1(data, variation, variationString):
    plt.xlabel(variationString, fontsize=20)
    plt.ylabel('Cantidad de intentos que sobrevivió el VIP', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.errorbar(variation, data, yerr=successToStandarVariation(data),  ecolor="grey", fmt='o', ms=2)
    plt.show()

attackersVariationWithoutKill = [10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 10, 10, 9, 8, 7, 10, 6, 10, 9, 9, 7, 9, 7, 9, 9, 6, 8, 7, 10, 9, 5, 6, 5, 7, 5, 3, 5, 4, 6, 3, 4, 1, 4, 3, 1, 3, 2, 3, 2, 2]
attackersVariationWithKill = [10, 10, 10, 10, 10, 10, 10, 9, 10, 10, 9, 10, 9, 8, 8, 10, 7, 7, 7, 9, 6, 4, 0, 3, 1, 2, 1, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
guardsVariationWithoutKill = [0,0,0,0,0,0,0,0,0,0,0,1,3,5,4,4,8,7,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
guardsVariationWithKill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 2, 3, 4, 2, 7, 7, 8, 7, 8, 9, 7, 8, 8, 9, 6, 7, 9, 8, 8, 10, 9, 8, 8, 7, 6, 9, 10, 9, 9, 8, 10, 6, 10, 9]
doubleGuardsAttackersVariationWithoutKill = [9, 10, 9, 10, 10, 10, 9, 8, 10, 9, 7, 9, 10, 6, 8, 8, 7, 7, 5, 7, 9, 7, 9, 6, 7, 6, 6, 6, 8, 3, 7, 3, 4, 7, 3, 6, 5, 3, 2, 4, 5, 3, 7, 2, 3, 2, 5, 4, 2, 1]
doubleGuardsAttackersVariationWithKill = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 10, 10, 10, 8, 10, 9, 9, 10, 10, 7, 8, 9, 8, 8, 6, 7, 8, 9, 5, 6, 2, 5, 5, 6, 5, 3, 3, 3, 3, 1, 1, 0, 1, 0, 0, 0, 1, 0]
trainingLevelVariationWithKill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 3, 2, 3, 2, 2, 2, 2, 3, 2, 1, 4, 7, 4, 6, 7, 7, 7, 5, 7, 8, 7, 7, 8, 8, 9, 9, 7, 9, 8, 8, 8]
guardsTauVariation = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 5, 6, 6, 9, 9, 10, 9, 10, 10, 10, 10, 10, 10, 10, 10, 9, 10, 9, 10, 10, 10, 9, 9, 9, 10, 10, 10, 9, 10, 10, 10]
attackersVariationShoot = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 10, 10, 9, 10, 8, 9, 9, 7, 8, 7, 8, 9, 5, 6, 8, 5, 7, 6, 4, 5, 2, 2, 1, 4, 1, 1, 0, 2, 0, 1, 0, 0, 1, 0]

attackersVariation = range(0, 50)
attackersString = "Cantidad de atacantes"
guardsVariation = range(0, 50)
guardsString = "Cantidad de guardias"
trainingLevelVariation = np.arange(0, 1, 1/len(trainingLevelVariationWithKill))
trainingString = "Nivel de entrenamiento"
tauVariation = np.arange(0.0002, 0.01, (0.01-0.0002)/len(guardsTauVariation))
tauString = "TAU de guardias"

#part1(attackersVariationWithoutKill, attackersVariation, attackersString)
#part1(attackersVariationWithKill, attackersVariation, attackersString)
#part1(guardsVariationWithoutKill, attackersVariation, guardsString)
#part1(guardsVariationWithKill, attackersVariation, guardsString)
#part1(doubleGuardsAttackersVariationWithoutKill, attackersVariation, attackersString)
#part1(doubleGuardsAttackersVariationWithKill, attackersVariation, attackersString)
#part1(trainingLevelVariationWithKill, trainingLevelVariation, trainingString)
#part1(guardsTauVariation, tauVariation, tauString)
#part1(attackersVariationShoot, attackersVariation, attackersString)

def part2():
