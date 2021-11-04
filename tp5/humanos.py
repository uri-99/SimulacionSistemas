import math

import numpy


class Humano:
    def __init__(self,x,y,size):
        self.x = x
        self.y = y

        self.v = 1.6
        self.vx = 0
        self.vy = 0
        self.angle = 0 #se setean en la primera iter antes de moverse los wachos

        self.gone = False
        self.size = size

    def direccionDeseada(self, targetX, targetY):
        difX = targetX - self.x
        difY = targetY - self.y
        a = math.atan(difY/difX)

        self.vx = self.v * math.cos(a)
        self.vy = self.v * math.sin(a)

        self.angle = a
        return self.vx, self.vy

    def move(self, dt, zombies, humanos): # MOVER HUMANO  #empieza linea recta hasta la puerta
        targetX, targetY = self.findExit()
        self.direccionDeseada(targetX, targetY)
        if not self.gone:
            zombieInSight = self.findZombie(zombies)
            if zombieInSight is not None:
                self.findTemporalTarget(zombies, zombieInSight, humanos)

            if self.x < 20 and self.y < 20:
                self.x += self.vx * dt
                self.y += self.vy * dt


    def findTemporalTarget(self, zombies, closestZ, humanos):
        exitX, exitY = self.findExit()
        angle_exit = self.angleTo(exitX, exitY)
        angle = self.angleTo(closestZ.x, closestZ.y)


        if abs(angle - angle_exit) > 45:
            self.angle = angle_exit
        else:
            if angle > 0 and self.angle > 0:
                if angle > self.angle:
                    self.angle -= math.pi/4
                else:
                    self.angle += math.pi / 4
            elif angle < 0 and self.angle < 0:
                if angle > self.angle:
                    self.angle -= math.pi/4
                else:
                    self.angle += math.pi / 4
            else:
                if angle > 0:
                    self.angle -= math.pi/4
                else:
                    self.angle += math.pi / 4

        self.vx = self.v * math.cos(self.angle)
        self.vy = self.v * math.sin(self.angle)


    def angleTo(self, x, y):
        difX = abs(x - self.x)
        difY = y - self.y
        a = math.atan(difY / difX)
        #if self.y > y:
        #    return -a
        return a

    '''
    if numpy.sign(self.angle) != numpy.sign(angle):
        self.angle = angle + math.pi/4 * numpy.sign(angle) * -1
            self.angle + math.pi/4 * -1 * numpy.sign(angle) #sumale 45 para el lado que no esté el zombie
    else:
        self.angle = self.angle + math.pi/4 * -1 * numpy.sign(angle) #sumale 45 para el lado que no esté el zombie

    humansInSight = []
    zombiesInSight = []

    for z in zombies:
        if z.distanciaAHumano(self.x, self.y) <= sight:
            zombiesInSight.append(z)
    for h in humanos:
        if h.distanceTo(self.x, self.y) <= sight:
            humansInSight.append(h)     
    #xp, yp = self.findProm(zombiesInSight, humansInSight)
    
    def findProm(self, zombies, humans):
        for z in zombies:
    '''


    def findZombie(self, zombies):
        sight = 3
        minDist = 3
        zombie = None
        for z in zombies:
            if z.x > self.x:
                if z.distanciaAHumano(self.x, self.y) <= sight:
                    if z.distanciaAHumano(self.x, self.y) <= minDist:
                        minDist = z.distanciaAHumano(self.x, self.y)
                        zombie = z
        return zombie
    
    def findExit(self):
        x = 20
        if self.y > (20 + 3) / 2:
            y = 10+1.5
        elif self.y < (20 - 3)/2:
            y = 10-1.5
        else:
            y = self.y
        return x, y

    def checkIfDie(self, zombies):
        for zombie in zombies:
            if( abs(zombie.x - self.x) < self.size):
                if(abs(zombie.y - self.y) < self.size):
                    return True
        return False

    def checkIfWin(self, largo, alto, salida):
        if self.x >= largo and ((alto-salida)/2) <= self.y <= ((alto + salida)/2):
            self.gone = True
        return self.gone

    def kill(self):
        self.gone = True

    def distanceTo(self, x, y):
        return math.sqrt((self.x - x)**2 + (self.y-y)**2)


    def __repr__(self):
        return "x " + str(self.x) + "; y " + str(self.y)

