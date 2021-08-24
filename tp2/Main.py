from arquitecture.Cell import Cell
from arquitecture.Grid import Grid
import timeit

# INICIO PROGRAMA

# CREO EL MAPA/GRID

grid = Grid(5,5)

# EMPIEZA EL JUEGO


fin_de_juego = False
laps = 0
data_particles = []
left_right = [3]

left_right[0] = grid.amountLeft()
left_right[1] = grid.amountRight()
left_right[2] = 0
data_particles[laps] = left_right

start = timeit.default_timer()

while fin_de_juego == False:
    #contador de vueltas o etapas
    laps += 1
    #movimientos del juego que hacen que sea una vuelta
    grid.calculateCollisions()
    grid.generateMovements()
    #info recolectada para graficos a futuro, cantidad de particulas a la izq y der del tablero
    left_right[0] = grid.amountLeft()
    left_right[1] = grid.amountRight()
    left_right[2] = timeit.default_timer() - start
    #donde se guarda esa data
    data_particles[laps] = left_right
    #incrementador de vueltas
    fin_de_juego = grid.isFinish()

total_time = timeit.default_timer() - start

# aca ya se termino el juego, aca esta la info

print(laps)
print(total_time)
print(grid.amountLeft())
print(grid.amountRight())
print("\n\n\n")
print(data_particles)