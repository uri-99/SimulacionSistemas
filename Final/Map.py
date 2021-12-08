#Parametros fijos. 20x20.
import math
import random
from VIP import VIP
from Attacker import Attacker
from Guard import Guard


class Map:

    attackerSize = 0.35#m
    guardSize = 0.5

    def __init__(self, width, height, enter, exit, qAttackers, qGuards, rGuards, doubleGuards, dt):
        self.width = width
        self.height = height
        self.enter = enter
        self.exit = exit
        self.qAttackers = qAttackers
        self.qGuards = qGuards #quantity
        self.rGuards = rGuards #radius of circle surrounding VIP
        self.doubleGuards = doubleGuards #Double layer of guards?
        self.attackers = []
        self.guards = []
        self.VIP = None
        self.t = 0
        self.dt = dt
        self.generateBeings()

    def generateBeings(self):
        self.VIP = VIP(2, 10, self.attackerSize, 70)
        self.generateGuards()

        Zadded = 0
        while Zadded < self.qAttackers: #generarAttackers
            auxX = random.uniform(0, self.width)
            auxY = random.uniform(0, self.height)
            if self.positionIsFree(auxX, auxY):
                mass = random.uniform(60,80)
                self.attackers.append(Attacker(auxX, auxY, self.attackerSize, mass))
                Zadded += 1
        return

    def generateGuards(self):
        angle = (2*math.pi) / self.qGuards
        for i in range(self.qGuards):
            mass = random.uniform(80,100)
            #calcular x e y para cada guardia a ser creado. tengo qGuards, self.VIP.x y self.VIP.y
            #todo meter un guardia en cada angulo respecto al VIP apropiadamente
            return

    def positionIsFree(self, x, y):
        array = self.attackers + self.guards
        for person in array:
            if abs(person.x - x) < person.size:
                if abs(person.y - y) < person.size:
                    if abs(self.VIP.x - x) < self.rGuards or abs(self.VIP.y - y) < self.rGuards: #not spawn between VIP and Guards
                        return False
        return True

    def isFinished(self):
        if self.t > 100:
            return True
        if self.VIP.isDead or self.VIP.hasEscaped:
            return True
        return False

    def move(self):
        self.t += self.dt #dt = 0.1
        self.t = round(self.t, 1)
        self.VIP.move(self.dt, self.attackers)
        for guard in self.guards:
            if not guard.isDead:
                guard.move(self.dt, self.VIP, self.guards, self.attackers)
        for attacker in self.attackers:
            if not attacker.isDead:
                attacker.move(self.dt, self.VIP, self.guards, self.attackers)

    def __repr__(self):
        s = ""
        s += str(self.VIP.x) + " " + str(self.VIP.y) + " 2\n"
        for i in self.guards:
            s += str(i.x) + " " + str(i.y) + " 0\n"
        for j in self.attackers:
            s += str(j.x) + " " + str(j.y) + " 1\n"
        s += "\n"
        return s


