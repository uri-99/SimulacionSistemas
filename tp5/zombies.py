import math

class Zombie:
    def __init__(self,x,y,v,wasBit):
        self.v = v
        self.x = x
        self.y = y
        self.vX = 0
        self.vY = 0
        self.apagado = wasBit # SI ESTA EN TRUE APAGADO, NO PUEDE MOVERSE NI COMER GENTE
        self.secondsSinceBit = 0 #Todo zombie quien tenga mas o igual de 7 segundos pasados SE LE PASA EL APAGADO A FALSE

    def zombieDespierta(self):
        if(self.secondsSinceBit >= 7):
            self.apagado = False
        return

    def move(self, humanos):
        '''
        # MOVER ZOMBIE
        humano = self.perseguirHumano(humanos)
        self.secondsSinceBit += 1
        if humano != None:
            if not self.apagado:
                # mover en la direccion de ese humano
            return
            '''
        return #None es que no hay humano a quien perseguir por ende Velocidad es 0

    def perseguirHumano(self, humanos):
        # Se fija quien tiene dentro de un radio de 5 metros
        distancia = 6 #metros
        humano = None
        for human in humanos:
            aux = self.distanciaAHumano(human.hx, human.hy)
            if aux < distancia:
                distancia = aux
                humano = human
        if distancia < 5:
            return humano
        return

    def distanciaAHumano(self,hx,hy):
        # Se fija la distancia entre el y el humano
        return math.sqrt((hx-self.x)**2 + (hy-self.y)**2)

    def __repr__(self):
        return "x " + str(self.x) + "; y " + str(self.y)
