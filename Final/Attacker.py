#stats fijos siempre. Varía su cantidad en caso 1
from utils import *
import Guard


class Attacker:

    attackerSpeed = 1.6 #m/s

    def __init__(self, x, y, size, mass):
        self.x = x
        self.y = y
        self.vx = 0#self.attackerSpeed
        self.vy = 0
        self.angle = 0
        self.size = size
        self.mass = mass
        self.isDead = False
        self.kn = 2 * 10 **3
        self.kt = 0#2 * 10**1
        self.A = 2000 #N
        self.B = 0.08 #m
        self.tau = 0.015 #s
        self.isFighting = False
        self.roundsFighting = 0

    def move(self, dt, VIP, guards, attackers):
        granular = [0, 0]
        social = [0, 0]
        drive = [0, 0]

        for person in attackers + guards:
            dist = distanceBetween(self, person)
            if dist>0:
                angle = angleBetween(self, person)
                if dist <= (self.size/2) + (person.size/2): #si se están tocando
                    #print("touching")
                    dif = dist - (self.size + person.size)
                    granular[0] += dif * self.kn *math.cos(angle)
                    granular[1] += dif * self.kn *math.sin(angle)
                    #print(granular)

                    granular[0] += (self.vx-self.vy)* math.cos(angle + math.pi/2) * dif * self.kt * math.cos(angle + math.pi/2)#vt velocidad relativa tangencial?
                    granular[1] += (self.vx-self.vy)* math.sin(angle + math.pi/2) * dif * self.kt * math.sin(angle + math.pi/2)
                    #print(granular)
                    if person is Guard:
                        #battle here
                        person.transferForce(self.mass, granular[0], granular[1])

                social[0] += ( self.A ** (-dist/self.B) ) * math.cos(angle)
                social[1] += ( self.A ** (-dist/self.B) ) * math.sin(angle)
                #print("social: ", social)


        angle = angleBetween(self, VIP)
        drive[0] = ((self.attackerSpeed*math.cos(angle) - self.vx)/self.tau)
        drive[1] = ((self.attackerSpeed*math.sin(angle) - self.vy)/self.tau)
        #print("drive: ", drive)

        F_total = [0,0]
        F_total[0] = granular[0] + social[0] + drive[0]
        F_total[1] = granular[1] + social[1] + drive[1]
        #print(F_total)

        acc = [0,0]
        acc[0] = F_total[0] / self.mass
        acc[1] = F_total[1] / self.mass


        self.vx += acc[0] * dt
        self.vy += acc[1] * dt
        #print("totalSpeed", totalSpeed(self))

        if 0 < self.x + self.vx * dt < 20:
            self.x += self.vx * dt
        else:
            if 8.5<self.y<11.5:
                self.x += self.vx * dt
                #self.isDead = True
        if 0 < self.y + self.vy * dt < 20:
            self.y += self.vy * dt


        return
