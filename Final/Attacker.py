#stats fijos siempre. Varía su cantidad en caso 1
from utils import *


class Attacker:

    attackerSpeed = 1.6 #m/s

    def __init__(self, x, y, size, mass):
        self.x = x
        self.y = y
        self.vx = self.attackerSpeed
        self.vy = 0
        self.angle = 0
        self.size = size
        self.mass = mass
        self.isDead = False
        self.kn = 1.2 * 10 **5
        self.kt = 2.4 * 10**5
        self.A = 2000 #N
        self.B = 0.8 #m
        self.tau = 0.05 #s

    def move(self, dt, VIP, guards, attackers):
        granular = [0, 0]
        social = [0, 0]
        drive = [0, 0]

        for person in guards + attackers:
            dist = distanceBetween(self, person)
            if dist>0:
                difx = math.abs(self.x - person.x)
                dify = math.abs(self.y - person.y)
                if dist <= (self.size/2) + (person.size/2): #si se están tocando
                    dif = dist - (self.size + person.size)
                    angle = math.atan(dify / difx) #between 2 wachines, osea angulo normal
                    #todo angle 4 casos, que vaya de 0 a 2pi
                    granular[0] += -dif * self.kn *math.cos(-angle) #todo formula falopa de granular
                    granular[1] += -dif * self.kn *math.sin(-angle)

                    angle += math.pi/2 #ahora es tangencial? podría ser -=pi/2
                    granular[0] += self.vx * dif * self.kt * cos(-angle)#vt velocidad relativa tangencial?
                    granular[1] += self.vy * dif * self.kt * sin(-angle)
                    #if person is Guard:
                        #battle here

                angle = math.atan(dify / difx)
                social[0] += ( self.A ** (dist/self.B) ) * math.cos(-angle)
                social[1] += ( self.A ** (dist/self.B) ) * math.sin(-angle)

                targetX = self.x - VIP.x
                targetY = self.y - VIP.y
                angle = math.atan(targetY / targetX)
                drive[0] = self.mass * (self.attackerSpeed*math.cos(angle) - self.vx/self.tau)
                drive[1] = self.mass * (self.attackerSpeed*math.sin(angle) - self.vy/self.tau)

        F_total = granular + social + drive
        acc = [0,0]
        acc[0] = F_total[0] / self.mass
        acc[1] = F_total[1] / self.mass
        self.vx += acc[0] * dt
        self.vy += acc[1] * dt

        self.x += self.vx * dt
        self.y += self.vy * dt


        return
