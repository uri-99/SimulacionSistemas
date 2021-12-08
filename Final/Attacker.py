#stats fijos siempre. Varía su cantidad en caso 1
from utils import *


class Attacker:

    attackerSpeed = 1.6 #m/s

    def __init__(self, x, y, size, mass):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.angle = 0
        self.size = size
        self.mass = mass
        self.isDead = False
        self.kn = 1.2 * 10 **5
        self.kt = 2.4 * 10**5
        self.A = 2000 #N
        self.B = 0.08 #m
        self.tau = 0.05 #s

    def move(self, dt, VIP, guards, attackers):
        granular = [0, 0]
        social = [0, 0]
        drive = [0, 0]

        for person in guards + attackers:
            dist = distanceBetween(self, person)
            difx = self.x - person.x
            dify = self.y - person.y
            if dist <= (self.size/2) + (person.size/2):
                dif = dist - (self.size + person.size)
                angle = math.atan(dify / difx) #between 2 wachines, osea angulo normal
                granular[0] += -dif * self.kn *math.cos(-angle) #todo formula falopa de granular
                granular[1] += -dif * self.kn *math.sin(-angle)

                angle += math.pi/2 #ahora es tangencial? podría ser -=pi/2
                granular[0] += vt * dif * self.kt * cos(-angle)#vt velocidad relativa tangencial?
                granular[1] += vt * dif * self.kt * sin(-angle)
                if person is Attacker:
                    #battle here

            angle = math.atan(dify / difx)
            social[0] += ( self.A ** (dist/self.B) ) * math.cos(-angle)
            social[1] += ( self.A ** (dist/self.B) ) * math.sin(-angle)

            targetX = VIP.x
            targetY = VIP.y
            drive[0] = self.mass * (self.vx*targetX - self.vx/self.tau)
            drive[1] = self.mass * (self.vy*targetY - self.vy/self.tau)

        return
