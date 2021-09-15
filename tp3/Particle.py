import math
import random


class Particle:
    mass = 1
    radius = 0.0015


    def __init__(self, x, y, idd):
        self.pseudoT = 0.0001

        self.speed = math.sqrt(self.pseudoT)
        self.x = x
        self.y = y
        self.id = idd
        self.colliding = False
        self.collidingWith = ""

        self.direction = math.radians(random.uniform(0, 360))
        self.vx = self.speed * math.cos(self.direction)
        self.vy = self.speed * math.sin(self.direction)

    def modSpeed(self):
        self.speed = math.sqrt(self.vx**2 + self.vy**2)
        return self.speed


    def flyX(self, t):
        self.x = self.x + self.vx * t

    def flyY(self, t):
        self.y = self.y + self.vy * t

    def calculateVerticalTC(self, table):
        if self.vx > 0:
            if self.x < table.v[1]: #chocó contra el muro del medio
                tc = (table.v[1] - Particle.radius - self.x) / self.vx
                if ((table.height - table.opening)/2) < self.y+(tc*self.vy) < ((table.height + table.opening)/2):
                    #print(self.id, " CROSSES BRODER in", tc)
                    return
                if table.tc > tc:
                    table.tc = tc
                    table.cleanFlags()
                    self.colliding = True
                    self.collidingWith = "vertical"
                    #print("new tc: ", tc, ", vertical ", self.id)
                    return
            else:
                tc = (table.v[2] - Particle.radius - self.x) / self.vx
                if table.tc > tc:
                    table.tc = tc
                    table.cleanFlags()
                    self.colliding = True
                    self.collidingWith = "vertical"
                    #print("new tc: ", tc, ", vertical ", self.id)
                    return
        elif self.vx < 0:
            if self.x > table.v[1]: #chocó contra el muro del medio
                tc = (table.v[1] + Particle.radius - self.x) / self.vx
                if ((table.height - table.opening)/2) < self.y+(tc*self.vy) < ((table.height + table.opening)/2):
                    #print(self.id, " CROSSES BACK in", tc)
                    return
                if table.tc > tc:
                    table.tc = tc
                    table.cleanFlags()
                    self.colliding = True
                    self.collidingWith = "vertical"
                    #print("new tc: ", tc, ", vertical ", self.id)
                    return
            else:
                tc = (table.v[0] + Particle.radius - self.x) / self.vx
                if table.tc > tc:
                    table.tc = tc
                    table.cleanFlags()
                    self.colliding = True
                    self.collidingWith = "vertical"
                    #print("new tc: ", tc, ", vertical ", self.id)
                    return

    def calculateHorizontalTC(self, table):
        if self.vy > 0:
            tc = (table.h[1] - Particle.radius - self.y) / self.vy
            if table.tc > tc:
                table.tc = tc
                table.cleanFlags()
                self.colliding = True
                self.collidingWith = "horizontal"
                #print("new tc: ", tc, ", horizontal ", self.id)
                return
        elif self.vy < 0:
            tc = (table.h[0] + Particle.radius - self.y) / self.vy
            if table.tc > tc:
                table.tc = tc
                table.cleanFlags()
                self.colliding = True
                self.collidingWith = "horizontal"
                #print("new tc: ", tc, ", horizontal ", self.id)
                return

    def calculateParticleTC(self, table, particle):
        if self.x == particle.x and self.y == particle.y:
            return

        sigma = 2*Particle.radius
        deltaR = [particle.x - self.x, particle.y - self.y]
        deltaV = [particle.vx - self.vx, particle.vy - self.vy]

        escalarR2 = deltaR[0]**2 + deltaR[1]**2
        escalarV2 = deltaV[0]**2 + deltaV[1]**2
        escalarVR = deltaV[0]*deltaR[0] + deltaV[1]*deltaR[1]

        d = escalarVR**2 - escalarV2*(escalarR2 - sigma**2)

        if escalarVR >= 0:
            tc = math.inf
        elif d < 0:
            tc = math.inf
        else:
            tc = -(escalarVR + math.sqrt(d)) / escalarV2
        if table.tc > tc:
            table.tc = tc
            table.cleanFlags()
            self.colliding = True
            particle.colliding = True
            self.collidingWith = "particle"
            particle.collidingWith = "particle"
            #print("new tc: ", tc, ", particles ", self.id, " ", particle.id)
        return


    def __repr__(self):
        #return "id: " + str(self.id) + ", x: " + str(self.x) + ", y: " + str(self.y) + ", vx: " + str(self.vx) + ", vy: " + str(self.vy) + "\n"
        return str(self.id) + " " + str(self.x) + " " + str(self.y) + "\n"

