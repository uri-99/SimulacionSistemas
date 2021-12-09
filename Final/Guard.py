#Tau y KillProbability variable como variación de su training (caso 3).
#Se varía su cantidad en el caso 2. Caso 5 doble corona
#caso 4 matan de lejos
from utils import *
import math

class Guard:
    def __init__(self, size, mass, angle, VIP, guards):
        self.VIP = VIP
        self.x = VIP.x + math.cos(angle)
        self.y = VIP.y + math.sin(angle)
        self.size = size
        self.mass = mass
        self.isDead = False
        self.angle = angle
        self.trainingLevel = 0.8
        self.guards = guards
        self.isFighting = False
        self.roundsFighting = 0
        self.amountOfRivals = 0

    def move(self, dt, VIP, guards, attackers):
        for person in attackers:
            dist = distanceBetween(self, person)
            difx = self.x - person.x
            dify = self.y - person.y
            self.x = VIP.x + math.cos(self.angle)
            self.y = VIP.y + math.sin(self.angle)
            #if dist <= (self.size/2) + (person.size/2):
                #battle, hasta que puede quedar mejor en attacker.py
                #if random.uniform(0,1) > self.trainingLevel:
                    #person.isDead = True
                #else
                    #self.isDead = True

        #posición respectiva al vip nada mas, él tiene el social force
        return
