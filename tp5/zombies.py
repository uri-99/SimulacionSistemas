import math

class Zombie:
    def __init__(self,x,y,v,wasBit):
        self.v = v
        self.x = x
        self.y = y
        self.humano = False
        self.zombie = True
        self.vx = 0
        self.vy = 0
        self.angle = 0
        self.apagado = wasBit # SI ESTA EN TRUE APAGADO, NO PUEDE MOVERSE NI COMER GENTE
        self.secondsSinceBit = 0 #Todo zombie quien tenga mas o igual de 7 segundos pasados SE LE PASA EL APAGADO A FALSE

    def zombieDespierta(self):
        if(self.secondsSinceBit >= 7):
            self.apagado = False
        return

    def move(self, dt, humanos): # MOVER ZOMBIE
        humano = self.elegirHumano(humanos)
        if humano is not None:
            if not self.apagado:
                self.direccionDeseada(humano.x, humano.y)
                self.x += self.vx * dt
                self.y += self.vy * dt
                # mover en la direccion de ese humano
        self.secondsSinceBit += dt
        self.zombieDespierta()

    def direccionDeseada(self, targetX, targetY):
        difX = abs(targetX - self.x)
        difY = abs(targetY - self.y)
        a = math.atan(difY/difX)
        if self.x > targetX:
            self.vx = self.v * math.cos(a) *-1
        elif self.x < targetX:
            self.vx = self.v * math.cos(a)
        else:
            self.vx = 0

        if self.y > targetY:
            self.vy = self.v * math.sin(a) *-1
        elif self.y < targetY:
            self.vy = self.v * math.sin(a)
        else:
            self.vy = 0

        self.angle = a
        return self.vx, self.vy

    def elegirHumano(self, humanos): #Se fija quien tiene dentro de un radio de 5 metros
        distancia = math.inf
        humano = None
        for human in humanos:
            aux = self.distanciaAHumano(human.x, human.y)
            if aux < distancia:
                distancia = aux
                humano = human
        if distancia < 5:
            return humano
        else:
            return None

    def distanciaAHumano(self,hx,hy): # Se fija la distancia entre el y el humano
        return math.sqrt((hx-self.x)**2 + (hy-self.y)**2)

    def freeze(self):
        self.apagado = True
        self.secondsSinceBit = 5

    def distanceTo(self, x, y):
        return math.sqrt((self.x - x)**2 + (self.y-y)**2)

    def changeDirection(self,x,y):
        a = self.angleTo(x,y)
        a = (a+180) % 360 ## seria el angulo opuesto al ser mas cercano que tiene
        self.vx = self.v * math.cos(a)
        self.vy = self.v * math.sin(a)
        return

    def __repr__(self):
        return "x " + str(self.x) + "; y " + str(self.y)
