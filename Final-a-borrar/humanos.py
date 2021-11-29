import math

import numpy


class Humano:
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.humano = True
        self.attacker = False
        self.v = 1.6
        self.vx = 0
        self.vy = 0
        self.angle = 0 #se setean en la primera iter antes de moverse los wachos

        self.gone = False
        self.size = size
        self.radius = size

    def direccionDeseada(self, targetX, targetY):
        difX = targetX - self.x
        difY = targetY - self.y
        a = math.atan(difY/difX)

        if self.radius < self.size:
            v = self.v * ((self.radius - 0.2)/(self.size - 0.2))**0.9
        else:
            v = self.v

        self.vx = v * math.cos(a)
        self.vy = v * math.sin(a)

        self.angle = a
        return self.vx, self.vy

    def move(self, dt, attackers, humanos, isCpm): # MOVER HUMANO  #empieza linea recta hasta la puerta
        if not self.gone:
            if not isCpm:
                targetX, targetY = self.findExit()
                self.direccionDeseada(targetX, targetY)
                self.findTemporalTarget(attackers, humanos)

            if (self.x + self.vx * dt >= 20 and 10+1.5 > self.y + self.vy * dt> 10-1.5) or (20 > self.x + self.vx * dt > 0 and 20 > self.y + self.vy * dt> 0):
                self.x += self.vx * dt
                self.y += self.vy * dt
            else:
                self.y += self.vy * dt


        if self.radius < self.size:
            self.radius += self.size/(0.5/dt)
        else:
            self.radius = self.size


    def findTemporalTarget(self, attackers, humanos):
        ordered_attackers = sorted(attackers, key=lambda dist:self.distanceTo(dist.x, dist.y))
        ordered_humans = sorted(humanos, key=lambda dist:self.distanceTo(dist.x, dist.y))
        eit = numpy.array([self.vx, self.vy])

        if self.x > 10:
            xw = 20 - self.x
            d_wall = self.distanceTo(20,self.y)
        else:
            xw = 0 - self.x
            d_wall = self.distanceTo(0, self.y)
        if self.y > 10:
            yw = 20 - self.y
            d_floor = self.distanceTo(self.x, 20)
        else:
            yw = 0 - self.y
            d_floor = self.distanceTo(self.x, 0)

        sizew = math.sqrt(xw ** 2 + yw ** 2)
        if abs(d_floor) < abs(d_wall):
            magnitudew = d_floor
        else:
            magnitudew = d_wall

        ncw = numpy.array([-xw/sizew, -yw/sizew])
        ncw *= 0.2 / magnitudew

        ncholderZ = [0,0]
        attackersQ = 3 if len(attackers) > 3 else len(attackers)
        for i in range(attackersQ):
            ncx = ordered_attackers[i].x - self.x
            ncy = ordered_attackers[i].y - self.y
            ncsize = math.sqrt(ncx**2 + ncy**2)
            ncmagnitude = self.distanceTo(ordered_attackers[i].x, ordered_attackers[i].y)
            aux = numpy.array([-ncx/ncsize, -ncy/ncsize])
            aux *= 1/ncmagnitude
            ncholderZ = ncholderZ + aux

        ncholderH = [0, 0]
        for i in range(attackersQ):
            if len(ordered_humans) > i+1:
                ncx = ordered_humans[i+1].x - self.x
                ncy = ordered_humans[i+1].y - self.y
                ncsize = math.sqrt(ncx**2 + ncy**2)
                ncmagnitude = self.distanceTo(ordered_humans[i+1].x, ordered_humans[i+1].y)
                aux = numpy.array([-ncx/ncsize, -ncy/ncsize])
                aux *= 0.05/ncmagnitude
                ncholderH = ncholderH + aux

        if self.radius < self.size:
            v = self.v * ((self.radius - 0.2)/(self.size - 0.2))**0.9
        else:
            v = self.v

        V = v * ((eit + ncholderZ + ncholderH + ncw) / numpy.linalg.norm(eit + ncholderZ + ncholderH + ncw))
        #V = self.v * ((eit + nc + nc2 + ncw) / numpy.linalg.norm(eit + nc + nc2 + ncw))

        self.vx = V[0]
        self.vy = V[1]
        #print(math.sqrt(self.vx**2 + self.vy**2))


    def angleTo(self, x, y):
        difX = abs(x - self.x)
        difY = y - self.y
        a = math.atan(difY / difX)

        #if self.y > y:
        #    return -a
        return a


    def findAttacker(self, attackers):
        sight = math.inf
        minDist = math.inf
        attacker = None
        for z in attackers:
            if z.x > self.x:
                if z.distanciaAHumano(self.x, self.y) <= sight:
                    if z.distanciaAHumano(self.x, self.y) <= minDist:
                        minDist = z.distanciaAHumano(self.x, self.y)
                        attacker = z
        return attacker
    
    def findExit(self):
        x = 20
        if self.y > (20 + 3) / 2:
            y = 10+1.5
        elif self.y < (20 - 3)/2:
            y = 10-1.5
        else:
            y = self.y
        return x, y

    def checkIfDie(self, attackers):
        for attacker in attackers:
            if( abs(attacker.x - self.x) < self.size):
                if(abs(attacker.y - self.y) < self.size):
                    if not attacker.apagado:
                        attacker.freeze()
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

    def changeDirection(self,x,y):
        a = self.angleTo(x,y)
        a = -a#(a+math.pi) % (2*math.pi) ## seria el angulo opuesto al ser mas cercano que tiene
        self.vx = self.v * math.cos(a)
        self.vy = self.v * math.sin(a)
        return

    def __repr__(self):
        return "x " + str(self.x) + "; y " + str(self.y)
