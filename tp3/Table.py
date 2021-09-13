import math
import random

from Particle import Particle


class Table:
    width = 0.24  # m
    height = 0.09  # m
    opening = 0.01  # m

    v = [0, width/2, width]  #walls
    h = [0, height]  #floor and roof

    tc = math.inf
    t = 0

    def __init__(self, N):
        self.N = N
        self.particles = []
        self.currID = 0
        while self.currID < self.N:
            self.addParticle()
        self.calculateTC()


    def addParticle(self):
        newX = random.uniform(Particle.radius, (self.width / 2) - Particle.radius)
        newY = random.uniform(Particle.radius, self.height - Particle.radius)
        for particle in self.particles:
            if abs(particle.x - newX) < Particle.radius:
                return False
            elif abs(particle.y - newY) < Particle.radius:
                return False

        self.currID += 1
        newParticle = Particle(newX, newY, self.currID)
        self.particles.append(newParticle)
        return True

    def calculateTC(self):
        i = 0
        j = 1
        while i < len(self.particles):
            self.particles[i].calculateHorizontalTC(self)
            self.particles[i].calculateVerticalTC(self)
            while j < len(self.particles):
                self.particles[i].calculateParticleTC(self, self.particles[j])
                j += 1
            i += 1
            j = i+1

    def fly(self):
        self.t += self.tc
        print("t=", self.t)
        for particle in self.particles:
            particle.flyX(self.tc)
            particle.flyY(self.tc)
            print(particle)
        self.tc = math.inf

    def collide(self):
        #calculate new vx and vy for collided particles, se puede hacer para todas las particles o la que colisionó que tenga un flag
        return


    def left_right(self):
        left = 0
        right = 0
        for particle in self.particles:
            if particle.x < self.width / 2:
                left += 1
            elif particle.x > self.width / 2:
                right += 1

        return left, right

    def left_right_percentages(self):
        left, right = self.left_right()
        leftP = left / self.currID
        rightP = right / self.currID
        return leftP, rightP

    def __repr__(self):
        string = ""
        for particle in self.particles:
            string += str(particle)
        return string






