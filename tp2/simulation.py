import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation
from arquitecture.Grid import Grid
from matplotlib.animation import FuncAnimation, PillowWriter
matplotlib.use('QT5Agg')

offset_pair = 0.5
offset_odd = 0.5

grid = Grid(50,25)
fig = plt.gcf()

def calculate_position(matrix_index):
    if(matrix_index % 2 == 0):
        return matrix_index*2 + 1.5
    return matrix_index*2

def grid_to_particle(grid):
    particles_x = []
    particles_y = []
    for i in range(203):
        for j in range(203):
            for vector in grid.cellArray[i][j].newVectors:
                if(vector == True):
                    particles_x.append(i*2)
                    particles_y.append(calculate_position(j))
    return particles_x, particles_y

def animate(frame_number):
    global d  # need it to remove old plot
    # old_particles_x, old_particles_y = grid_to_particle(grid)
    grid.generateMovements()
    grid.calculateCollisions()
    d.remove()
    new_particles_x, new_particles_y = grid_to_particle(grid)
    d, = plt.plot(new_particles_x, new_particles_y, 'go')

particles_x, particles_y = grid_to_particle(grid)
d,  = plt.plot(particles_x, particles_y, 'go', markersize=1)
anim = animation.FuncAnimation(fig, animate, frames=200, interval=5000, repeat=True)
#anim.save("movie.gif", writer=PillowWriter(fps=5))
plt.xlim([0, 406])
plt.ylim([0, 406])
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
