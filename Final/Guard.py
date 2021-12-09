#Tau y KillProbability variable como variación de su training (caso 3).
#Se varía su cantidad en el caso 2. Caso 5 doble corona
#caso 4 matan de lejos
from utils import *
import math

class Guard:
    guardSpeed = 2 #m/s
    def __init__(self, size, mass, angle, VIP, guards, guardTau, canShoot, second=False):
        self.VIP = VIP
        if not second:
            self.x = VIP.x + math.cos(angle)
            self.y = VIP.y + math.sin(angle)
            self.angle = angle
        else:
            self.x = VIP.x + 1.5*math.cos(angle)
            self.y = VIP.y + 1.5*math.sin(angle)
            self.angle = angle + math.pi/12
        self.second = second
        self.vx = 0#self.attackerSpeed
        self.vy = 0
        self.size = size
        self.mass = mass
        self.isDead = False
        self.trainingLevel = 0.8
        self.guards = guards
        self.kn = 2 * 10 **3
        self.kt = 0#2 * 10**1
        self.tau = guardTau #0.002 #s
        self.isFighting = False
        self.roundsFighting = 0
        self.amountOfRivals = 0
        self.canShoot = canShoot
        self.shootTimer = 1/0.05 #1/dt

    def move(self, dt, VIP, guards, attackers):
        granular = [0, 0]
        social = [0, 0]
        drive = [0, 0]

        closestPersonDist = math.inf
        closestPerson = None

        for person in attackers:
            dist = distanceBetween(self, person)
            if dist < closestPersonDist:# and not person.isDead:
                closestPerson = person
                closestPersonDist = dist
            angle = angleBetween(self, person)
            if dist <= (self.size / 2) + (person.size / 2):
                dif = dist - (self.size + person.size)
                granular[0] += dif * self.kn * math.cos(angle)
                granular[1] += dif * self.kn * math.sin(angle)

            #self.x = VIP.x + math.cos(self.angle)
            #self.y = VIP.y + math.sin(self.angle)

        if self.shootTimer == 0:
            if closestPerson is not None:
                closestPerson.isDead = True
            self.shootTimer = 2/dt
        else:
            self.shootTimer -= 1


        if not self.second:
            angle = angleBetween(self, Position(VIP.x + math.cos(self.angle), VIP.y + math.sin(self.angle)))
        else:
            angle = angleBetween(self, Position(VIP.x + 1.2*math.cos(self.angle), VIP.y + 1.2*math.sin(self.angle)))
        drive[0] = ((self.guardSpeed * math.cos(angle) - self.vx) / self.tau)
        drive[1] = ((self.guardSpeed * math.sin(angle) - self.vy) / self.tau)

        F_total = [0,0]
        F_total[0] = granular[0] + social[0] + drive[0]
        F_total[1] = granular[1] + social[1] + drive[1]

        acc = [0,0]
        acc[0] = F_total[0] / self.mass
        acc[1] = F_total[1] / self.mass

        self.vx += acc[0] * dt
        self.vy += acc[1] * dt
        #print("totalSpeed", totalSpeed(self))

        #if 0 < self.x + self.vx * dt < 20:
        self.x += self.vx * dt
        if 0 < self.y + self.vy * dt < 20:
            self.y += self.vy * dt


        return

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
