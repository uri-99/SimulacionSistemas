import math

class Zombie:
    def __init__(self,x,y,v,wasBit):
        self.v = v
        self.x = x
        self.y = y
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
        self.secondsSinceBit += 1
        if humano is not None:
            if not self.apagado:
                self.direccionDeseada(humano.x, humano.y)
                self.x += self.vx * dt
                self.y += self.vy * dt
                # mover en la direccion de ese humano
        self.secondsSinceBit += dt
        self.zombieDespierta()

    def direccionDeseada(self, targetX, targetY):
        difX = targetX - self.x
        difY = (targetY - self.y)
        a = math.tan(difY/difX)
        self.x = self.vx * math.cos(a)
        self.y = self.vy * math.sin(a)
        self.angle = a
        return self.vx, self.vy

    def elegirHumano(self, humanos): #Se fija quien tiene dentro de un radio de 5 metros
        distancia = math.inf
        humano = None
        for human in humanos:
            aux = self.distanciaAHumano(human.hx, human.hy)
            if aux < distancia:
                distancia = aux
                humano = human
        if distancia <= 5:
            return humano
        else:
            return None

    def distanciaAHumano(self,hx,hy): # Se fija la distancia entre el y el humano

        return math.sqrt((hx-self.x)**2 + (hy-self.y)**2)

    def __repr__(self):
        return "x " + str(self.x) + "; y " + str(self.y)
