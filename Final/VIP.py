#stats fijos siempre
import random
import math
from utils import *

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
        self.B = 0.08 #m
        self.tau = 0.015 #s

    def move(self, dt, attackers):
        if self.x >= 20:
            self.hasEscaped = True

        granular = [0, 0]
        social = [0, 0]
        drive = [0, 0]

        for person in attackers:
            dist = distanceBetween(self, person)
            difx = abs(self.x - person.x)
            dify = abs(self.y - person.y)
            if dist <= (self.size/2) + (person.size/2):#un atacker toca al vip
                if not person.isDead and not person.isFighting:
                    self.isDead = self.hasDied()

            angle = angleBetween(self, person)
            #social[0] += ( self.A ** (-dist/self.B) ) * math.cos(angle)
            #social[1] += ( self.A ** (-dist/self.B) ) * math.sin(angle)


            angle = angleBetween(self, "exit")
            drive[0] = ((self.VIPspeed*math.cos(angle) - self.vx)/self.tau)
            drive[1] = ((self.VIPspeed*math.sin(angle) - self.vy)/self.tau)

        F_total = [0, 0]
        F_total[0] = granular[0] + social[0] + drive[0]
        F_total[1] = granular[1] + social[1] + drive[1]
        #print("social", social)
        #print("drive", drive)
        #print(F_total)

        acc = [0,0]
        acc[0] = F_total[0] / self.mass
        acc[1] = F_total[1] / self.mass

        self.vx += acc[0] * dt
        self.vy += acc[1] * dt

        self.x += self.vx * dt
        if 0 < self.y + self.vy * dt < 20:
            self.y += self.vy * dt

        #print("vip spd ", totalSpeed(self))


    def hasDied(self):
        p = random.uniform(0,1)
        if p < self.dieChance:
            return True
        return False

    def findDoor(self): #darle ancho a la puerta
        return 20,10

