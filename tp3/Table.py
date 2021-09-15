import math
import random

from Particle import Particle


class Table:
    width = 0.24  # m
    height = 0.09  # m
    opening = 0.02  # m

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
        print("done adding particles")
        #print("t0\n", self)
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
        #print("t=", self.t)
        for particle in self.particles:
            particle.flyX(self.tc)
            particle.flyY(self.tc)
        self.tc = math.inf

    def cleanFlags(self):
        for particle in self.particles:
            if particle.colliding:
                particle.colliding = False
                particle.collidingWith = ""

    def collide(self):
        #calculate new vx and vy for collided particles, se puede hacer para todas las particles o la que colisionó que tenga un flag
        collidingParticles = []
        for particle in self.particles:
            if particle.colliding:
                collidingParticles.append(particle)
        if len(collidingParticles) == 1:
            if collidingParticles[0].collidingWith == "vertical":
                collidingParticles[0].vx *= -1
                #print("vertical", collidingParticles[0])
            elif collidingParticles[0].collidingWith == "horizontal":
                collidingParticles[0].vy *= -1
                #print("horizontal", collidingParticles[0])
            else:
                print(collidingParticles[0], collidingParticles[0].collidingWith)
                exit("error calculating collide of single particle")
        elif len(collidingParticles) == 2:
            particle1 = collidingParticles[0]
            particle2 = collidingParticles[1]
            if particle1.collidingWith != "particle" or particle2.collidingWith != "particle":
                exit("error in collidingWith particles")

            sigma = 2 * Particle.radius
            deltaR = [particle2.x - particle1.x, particle2.y - particle1.y]
            deltaV = [particle2.vx - particle1.vx, particle2.vy - particle1.vy]
            escalarVR = deltaV[0] * deltaR[0] + deltaV[1] * deltaR[1]

            J = (Particle.mass * escalarVR) / sigma
            Jx = J*deltaR[0] / sigma
            Jy = J*deltaR[1] / sigma

            particle1.vx = particle1.vx + Jx/Particle.mass
            particle1.vy = particle1.vy + Jy/Particle.mass

            particle2.vx = particle2.vx - Jx/Particle.mass
            particle2.vy = particle2.vy - Jy/Particle.mass

            #print("p1", collidingParticles[0])
            #print("p2", collidingParticles[1])
        else:
            print("error, too many particles colliding")
            exit()
        return

    def collide2(self):
        #calculate new vx and vy for collided particles, se puede hacer para todas las particles o la que colisionó que tenga un flag
        collidingParticles = []
        for particle in self.particles:
            if particle.colliding:
                collidingParticles.append(particle)
        if len(collidingParticles) == 1:
            if collidingParticles[0].collidingWith == "vertical":
                collidingParticles[0].vx *= -1
                if (collidingParticles[0].vx > 0 and collidingParticles[0].x>Table.v[1]) or (collidingParticles[0].vx < 0 and collidingParticles[0].x<Table.v[1]):
                    return abs(collidingParticles[0].vx)*Particle.mass
                else:
                    return 0
                #print("vertical", collidingParticles[0])
            elif collidingParticles[0].collidingWith == "horizontal":
                collidingParticles[0].vy *= -1
                return abs(collidingParticles[0].vy)*Particle.mass
                #print("horizontal", collidingParticles[0])
            else:
                print(collidingParticles[0], collidingParticles[0].collidingWith)
                exit("error calculating collide of single particle")
        elif len(collidingParticles) == 2:
            particle1 = collidingParticles[0]
            particle2 = collidingParticles[1]
            if particle1.collidingWith != "particle" or particle2.collidingWith != "particle":
                exit("error in collidingWith particles")

            sigma = 2 * Particle.radius
            deltaR = [particle2.x - particle1.x, particle2.y - particle1.y]
            deltaV = [particle2.vx - particle1.vx, particle2.vy - particle1.vy]
            escalarVR = deltaV[0] * deltaR[0] + deltaV[1] * deltaR[1]

            J = (Particle.mass * escalarVR) / sigma
            Jx = J*deltaR[0] / sigma
            Jy = J*deltaR[1] / sigma

            particle1.vx = particle1.vx + Jx/Particle.mass
            particle1.vy = particle1.vy + Jy/Particle.mass

            particle2.vx = particle2.vx - Jx/Particle.mass
            particle2.vy = particle2.vy - Jy/Particle.mass

            #print("p1", collidingParticles[0])
            #print("p2", collidingParticles[1])
        else:
            print("error, too many particles colliding")
            exit()
        return 0

    def calculateV2(self):
        totV2 = 0
        for particle in self.particles:
            totV2 += (particle.modSpeed())**2
        return totV2

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
        leftP = left / len(self.particles)
        rightP = right / len(self.particles)
        return leftP, rightP

    def __repr__(self):
        string = ""
        string += str(self.t) + "\n"
        for particle in self.particles:
            string += str(particle)
        string += "\n"
        return string






