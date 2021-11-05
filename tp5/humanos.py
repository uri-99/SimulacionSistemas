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

            if 20 > self.x > 0 and 20 > self.y > 0:
                self.x += self.vx * dt
                self.y += self.vy * dt


    def findTemporalTarget(self, zombies, closestZ, humanos):
        exitX, exitY = self.findExit()
        angle_exit = self.angleTo(exitX, exitY)
        angle = self.angleTo(closestZ.x, closestZ.y)
        ordered_zombies = sorted(zombies, key=lambda dist:self.distanceTo(dist.x, dist.y))

        eit = numpy.array([self.vx, self.vy])

        x = closestZ.x - self.x
        y = closestZ.y - self.y
        size = math.sqrt(x**2 + y**2)

        magnitude = self.distanceTo(closestZ.x, closestZ.y)
        nc = numpy.array([-x/size, -y/size])
        nc *= 2/magnitude

        V = self.v * ((eit + nc) / numpy.linalg.norm(eit + nc))

        self.vx = V[0]
        self.vy = V[1]
        print(math.sqrt(self.vx**2 + self.vy**2))



    def angleTo(self, x, y):
        difX = abs(x - self.x)
        difY = y - self.y
        a = math.atan(difY / difX)

        #if self.y > y:
        #    return -a
        return a


    def findZombie(self, zombies):
        sight = math.inf
        minDist = math.inf
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
                    if not zombie.apagado:
                        zombie.freeze()
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

