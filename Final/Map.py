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
        if self.qGuards > 0:
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
        print(self.qGuards)
        for i in range(self.qGuards):
            mass = random.uniform(80,100)
            new_angle = i*angle
            self.guards.append(Guard(self.guardSize, mass, new_angle, self.VIP, self.guards))
            #calcular x e y para cada guardia a ser creado. tengo qGuards, self.VIP.x y self.VIP.y
            #todo meter un guardia en cada angulo respecto al VIP apropiadamente

    def guardsOrder(self):
        notFighting = 0
        for guard in self.guards:
            if (not guard.isFighting) and (not guard.isDead):
                notFighting += 1
        angle = (2*math.pi) / notFighting
        i = 1
        for guard in self.guards:
            if (not guard.isFighting) and (not guard.isDead):
                new_angle = i*angle
                i += 1
                # TODO ya esta el angulo segun cuantos hay, solo habria q saber decirle como ir ahi
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
            checkGuard(guard)
            if (not guard.isDead) and (not guard.isFighting):
                guard.move(self.dt, self.VIP, self.guards, self.attackers)
        for attacker in self.attackers:
            checkAttacker(attacker)
            if (not attacker.isDead) and (not attacker.isFighting):
                attacker.move(self.dt, self.VIP, self.guards, self.attackers)
        for guard in self.guards:
            checkFight(guard)

    def checkFight(self, guard): #se fija si el guardia esta peleando y calcula posibilidades
        if not guard.isDead:
            for attacker in self.attackers:
                if not attacker.isDead:
                    # FIGHT STARTER
                    if dist <= (guard.size/2) + (attacker.size/2): # entra solo cuando ambos estan vivos
                        guard.isFighting = True
                        attacker.isFighting = True
                        guard.amountOfRivals += 1
                        if random.uniform(0,1) >= guard.trainingLevel/guard.amountOfRivals #segun la cantidad de rivales la prob de ganar es mas baja
                            guard.isDead = True
                        else
                            attacker.isDead = True

    def checkGuard(self, guard):
        if (not guard.isDead) and guard.isFighting:
            # FIGHT ENDER
            guard.roundsFighting += 1

            if guard.roundsFighting != 0 and guard.roundsFighting%2 == 0:
                guard.roundsFighting -= 2
                guard.amountOfRivals -= 1
                if guard.amountOfRivals == 0:
                    guard.isFighting = False

    def checkAttacker(self, attacker):
        if not attacker.isDead and attacker.isFighting:
            # FIGHT ENDER
            attacker.roundsFighting += 1

            if attacker.roundsFighting != 0 and attacker.roundsFighting%2 == 0:
                attacker.roundsFighting = 0
                attacker.isFighting = False


    def __repr__(self):
        s = ""
        s += str(self.VIP.x) + " " + str(self.VIP.y) + " 2\n"
        for i in self.guards:
            s += str(i.x) + " " + str(i.y) + " 0\n"
        for j in self.attackers:
            s += str(j.x) + " " + str(j.y) + " 1\n"
        s += "\n"
        return s
