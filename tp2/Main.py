from arquitecture.Cell import Cell
from arquitecture.Grid import Grid
import timeit
import sys
import numpy as np


# INICIO PROGRAMA

# py main.py 1000 51 2 1
# ejecutar main con 1000 particulas, 51 de abertura, 2 iteraciones y guardandolo

particles = int(sys.argv[1])
opening = int(sys.argv[2])
iterations = int(sys.argv[3])
save = int(sys.argv[4])

for i in range (1, iterations+1):
    print("Iteracion " + str(i))
    
    # CREO EL MAPA/GRID
    grid = Grid(particles, opening) #N particulas, D tamaño apertura

    # EMPIEZA EL JUEGO


    fin_de_juego = False
    laps = 0
    data_particles = []
    left_right = [0,0,0]

    left_right[0] = grid.amountLeft()
    left_right[1] = grid.amountRight()
    left_right[2] = 0
    data_particles.append(left_right)

    start = timeit.default_timer()
    particles_matrix = []

    while (fin_de_juego == False):
        #contador de vueltas o etapas
        particles_matrix.append(grid.grid_to_matrix())
        laps += 1
        #movimientos del juego que hacen que sea una vuelta
        grid.generateMovements()
        left_right[0] = grid.amountLeft()
        left_right[1] = grid.amountRight()
        fin_de_juego = grid.isFinish()
        grid.calculateCollisions()
        #info recolectada para graficos a futuro, cantidad de particulas a la izq y der del tablero
        left_right[2] = timeit.default_timer() - start
        #donde se guarda esa data
        data_particles.append(left_right)
        #incrementador de vueltas
        
        if laps%10 == 0:
            print("Vuelta: " + str(laps))
            print(str(left_right[0]) + " - " + str(left_right[1]))

    np.save('./simulation/data_'+str(particles)+'-'+str(opening)+'_'+str(i), particles_matrix)
    total_time = timeit.default_timer() - start

    print("Vuelta: " + str(laps))
    print(str(left_right[0]) + " - " + str(left_right[1]))

    print("listo")

# print("Resultados: ")
# print("Vueltas" + laps)
# print("Tiempo:" + total_time)
# print(data_particles)

# grid.printGrid()

# print("\nt1:\n")
# grid.generateMovements() #se mueven al old apropiado
# grid.printGrid()
# print(grid.amountLeft())
# print(grid.amountRight())
# print("left: ", grid.amountLeft())
# print("right: ", grid.amountRight())


# print("\nt1.5:\n")
# grid.calculateCollisions() #los paso a new
# grid.printGrid()

# print("\nt2:\n")
# grid.generateMovements() #se mueven al old apropiado
# grid.printGrid()
# print("left: ", grid.amountLeft())
# print("right: ", grid.amountRight())


# print("\nt2.5:\n")
# grid.calculateCollisions() #los paso a new
# grid.printGrid()


# print("\nt3:\n")
# grid.generateMovements() #se mueven al old apropiado
# grid.printGrid()
# print("left: ", grid.amountLeft())
# print("right: ", grid.amountRight())


# print("\nt3.5:\n")
# grid.calculateCollisions() #los paso a new
# grid.printGrid()

# print("\nt4:\n")
# grid.generateMovements() #se mueven al old apropiado
# grid.printGrid()
# print("left: ", grid.amountLeft())
# print("right: ", grid.amountRight())


# print("\nt4.5:\n")
# grid.calculateCollisions() #los paso a new
# grid.printGrid()

# print("\nt5:\n")
# grid.generateMovements() #se mueven al old apropiado
# grid.printGrid()
# print("left: ", grid.amountLeft())
# print("right: ", grid.amountRight())

# # aca ya se termino el juego, aca esta la info

# print(laps)
# print(total_time)
# print(grid.amountLeft())
# print(grid.amountRight())
# print("\n\n\n")
# print(data_particles)
# print("\n\n\n")
# print("\n\n\n")
# print("\n\n\n")