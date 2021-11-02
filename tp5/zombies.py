import math

class Zombie:
    def __init__(self,vX,vY,x,y,apagado):
        self.x = x
        self.y = y
        self.vX = vX
        self.vY = vY
        self.apagado = apagado # SI ESTA EN TRUE APAGADO, NO PUEDE MOVERSE NI COMER GENTE
        self.rondasPasadas = 0 #todo zombie quien tenga mas o igual de 7 rondas pasadas SE LE PASA EL APAGADO A FALSE

    def zombieDespierta(self):
        if(self.rondasPasadas >= 7):
            self.apagado = False
        return

    def move(self, humanos):
        # MOVER ZOMBIE
        humano = self.perseguirHumano(humanos)
        self.rondasPasadas += 1
        if humano != None:
            if not self.apagado:
                # mover en la direccion de ese humano
            return
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
