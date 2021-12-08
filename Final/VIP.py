#stats fijos siempre
import random
import math
from utils import distanceBetween

class VIP:

    VIPspeed = 1

    def __init__(self, x, y, size, mass):
        self.x = x
        self.y = y
        self.vx = self.VIPspeed
        self.vy = 0
        self.size = size
        self.mass = mass
        self.isDead = False
        self.hasEscaped = False
        self.dieChance = 0.5
        self.A = 2000 #N
        self.B = 0.8 #m
        self.tau = 0.05 #s

    def move(self, dt, attackers):
        if self.x >= 20:
            self.hasEscaped = True

        granular = [0, 0]
        social = [0, 0]
        drive = [0, 0]

        for person in attackers:
            dist = distanceBetween(self, person)
            difx = math.abs(self.x - person.x)
            dify = math.abs(self.y - person.y)
            if dist <= (self.size/2) + (person.size/2):#un atacker toca al vip
                self.isDead = self.hasDied()

            angle = math.atan(dify / difx)
            # todo angle 4 casos, que vaya de 0 a 2pi
            social[0] += ( self.A ** (dist/self.B) ) * math.cos(-angle)
            social[1] += ( self.A ** (dist/self.B) ) * math.sin(-angle)

            targetX , targetY = self.findDoor()
            angle = math.atan(targetY / targetX)
            drive[0] = self.mass * (self.VIPspeed*math.cos(angle) - self.vx/self.tau)
            drive[1] = self.mass * (self.VIPspeed*math.sin(angle) - self.vy/self.tau)

        F_total = granular + social + drive
        acc = [0,0]
        acc[0] = F_total[0] / self.mass
        acc[1] = F_total[1] / self.mass
        self.vx += acc[0] * dt
        self.vy += acc[1] * dt

        self.x += self.vx * dt
        self.y += self.vy * dt

    def hasDied(self):
        p = random.uniform(0,1)
        if p < self.dieChance:
            return True
        return False

    def findDoor(self): #darle ancho a la puerta
        return 20,10

