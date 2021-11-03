import math


class Humano:
    def __init__(self,x,y,size):
        self.x = x
        self.y = y

        self.v = 1.6
        self.vx = 0
        self.vy = 0
        self.angle = 0
        self.move(0) #le setea el vx y vy y angle

        self.gone = False
        self.size = size

    def direccionDeseada(self, targetX, targetY):
        difX = targetX - self.x
        difY = (targetY - self.y)
        a = math.tan(difY/difX)
        self.x = self.vx * math.cos(a)
        self.y = self.vy * math.sin(a)
        self.angle = a
        return self.vx, self.vy

    def move(self, dt, zombies): # MOVER HUMANO  #empieza linea recta hasta la puerta
        if not self.gone:
            zombieInSight = self.findZombie(zombies)
            if zombieInSight is None:
                targetX, targetY = self.findExit()
                self.direccionDeseada(targetX, targetY)
                self.x += self.vx * dt
                self.y += self.vy * dt
            else: #tirate un paso bro

            #oldPos = newPos()
            #if(tengo que esquivar):
            #    vx, vy, angle = new velocity


    def findZombie(self, zombies):
        minDist = 3
        zombie = None
        for z in zombies:
            if z.distanciaAHumano(self.x, self.y) <= minDist:
                minDist = z.distanciaAHumano(self.x, self.y)
                zombie = z
        return zombie
    
    def findExit(self):
        x = 20
        if self.y > (20 + 3) / 2:
            y = 20+1.5
        elif self.y < (20-3)/2:
            y = 20-1.5
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


    def __repr__(self):
        return "x " + str(self.x) + "; y " + str(self.y)

