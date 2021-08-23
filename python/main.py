from matplotlib import pyplot as plt
import os
import math
import numpy as np


class Particle:
    def __init__(self, id, x, y, r, neighbors):
        self.id = id
        self.x = x
        self.y = y
        self.r = r
        self.neighbors = neighbors

dirname = os.path.dirname(__file__)
simulationFile = os.path.join(dirname, 'simulation')

simulation = open(simulationFile, 'r')

fig, axs = plt.subplots(figsize=(5, 5))

cimp = simulation.readline().rsplit('\n')
print(cimp)
n = int(simulation.readline().rstrip('\n'))
print(n)
l = int(simulation.readline().rstrip('\n'))
m = int(simulation.readline().rstrip('\n'))
rc = float(simulation.readline().rstrip('\n'))

particles = []

for i in range(n):
    line = simulation.readline().rstrip('\n')
    splitedLine = line.split(' ')
    id = int(splitedLine[0])
    x = float(splitedLine[1])
    y = float(splitedLine[2])
    r = float(splitedLine[3])
    neighborsString = splitedLine[4].split(',')
    neighborsString.pop()
    neighbors = []
    for j in range(len(neighborsString)):
        neighbors.append(int(neighborsString[j]))
    particles.append(Particle(id, x, y, r, neighbors))

axs.set_title("Particles")
axs.set_xlabel("X")
axs.set_ylabel("Y")

plt.grid(markevery=l/m, c="black", linewidth=0.5)

particlesX = []
particlesY = []
particlesR = []
particlesNeighbors = []

circleArray = []

rcCircle = []

for particle in particles:
    circle = plt.Circle((particle.x, particle.y), particle.r, color="blue", picker=5)
    circleArray.append(circle)
    particlesX.append(particle.x)
    particlesY.append(particle.y)
    particlesR.append(particle.r)
    particlesNeighbors.append(particle.neighbors)
    axs.add_artist(circle)

#graph = axs.scatter(particlesX, particlesY, particlesR, picker=5)

def on_click(event):
    print("entre")
    x = event.xdata
    y = event.ydata

    selectedParticle = None

    for particle in particles:
        if(particle.r**2 - ((particle.x-x)**2 + (particle.y-y)**2) > 0):
            selectedParticle = particle
            
    for c in circleArray:
        c.set_color('blue')
           
            
    if (selectedParticle):
        if(len(rcCircle) > 0):
            for circle in rcCircle:
                circle.remove()
        rcCircle.clear()
        selectedCircle = circleArray[selectedParticle.id - 1]
        selectedCircle.set_color('red')
        for neighborId in selectedParticle.neighbors:
            circleArray[neighborId-1].set_color('green')
            
        rcCircle.append(plt.Circle((selectedParticle.x, selectedParticle.y), selectedParticle.r + rc, color='yellow', fill=False))
        if cimp[0] == "true":
            posX = selectedParticle.x + selectedParticle.r + rc
            minusX = selectedParticle.x - selectedParticle.r - rc
            posY = selectedParticle.y + selectedParticle.r + rc
            minusY = selectedParticle.y - selectedParticle.r - rc
            if(posX > l):
                rcCircle.append(plt.Circle((selectedParticle.x - l, selectedParticle.y), selectedParticle.r + rc, color='yellow', fill=False))
            if(minusX < 0):
                rcCircle.append(plt.Circle((selectedParticle.x + l, selectedParticle.y), selectedParticle.r + rc, color='yellow', fill=False))
            if(posY > l):
                rcCircle.append(plt.Circle((selectedParticle.x, selectedParticle.y - l), selectedParticle.r + rc, color='yellow', fill=False))
            if(minusY < 0):
                rcCircle.append(plt.Circle((selectedParticle.x, selectedParticle.y + l), selectedParticle.r + rc, color='yellow', fill=False))
            if(posX > l and posY > l):
                rcCircle.append(plt.Circle((selectedParticle.x - l, selectedParticle.y - l), selectedParticle.r + rc, color='yellow', fill=False))
            if(minusX < 0 and minusY < 0):
                rcCircle.append(plt.Circle((selectedParticle.x + l, selectedParticle.y + l), selectedParticle.r + rc, color='yellow', fill=False))
            if(posX > l and minusY < 0):
                rcCircle.append(plt.Circle((selectedParticle.x - l, selectedParticle.y + l), selectedParticle.r + rc, color='yellow', fill=False))
            if(minusX < 0 and posY > l):
                rcCircle.append(plt.Circle((selectedParticle.x + l , selectedParticle.y - l), selectedParticle.r + rc, color='yellow', fill=False))
        for circle in rcCircle:
            axs.add_artist(circle)
        fig.canvas.draw()

plt.xlim(0, l)
plt.ylim(0, l)
fig.canvas.mpl_connect("button_press_event", on_click)
plt.show()