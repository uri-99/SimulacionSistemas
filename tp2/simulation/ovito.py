from arquitecture.Grid import *

hexagon_size = 5
grid_size = 203

def from_grid_to_ovito(grid):
    aux = []
    grid.generateVectors(500)
    for i in range(203):
        for j in range(203):
            for vector in grid.cellArray[i][j]:
                if(vector == True):
                    aux[i][j] = True
    return aux

grid = Grid(500, 200)
grid.generateMovements()
ovito_grid = from_grid_to_ovito(grid)

#un flag para saber si esta en equilibrio?
while(not grid.equilibrium):
    grid.generateMovements()
    grid.calculateCollisions()
    ovito_grid = from_grid_to_ovito(grid)
    print(ovito_grid)