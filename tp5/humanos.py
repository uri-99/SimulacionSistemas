
class Humano:
    def __init__(self,x,y,v,size):
        self.x = x
        self.y = y
        self.v = v
        self.vX ,self.vY = self.calculateV0()
        self.angle = self.calculateAngle()
        self.gone = False
        self.size = size

    def direccionDeseada(self):
        # FORMULA
        return

    def move(self):
        # MOVER HUMANO
        #empezá linea recta hasta la puerta
        if not self.gone:
            oldPos = newPos()
            if(tengo que esquivar):
                vx, vy, angle = new velocity
        return

    def calculateV0(self):

        return vx, vy

    def calculateAngle(self):

        return alpha

    def checkIfDie(self, zombies):
        for zombie in zombies:
            if( abs(zombie.x - self.x) < self.size):
                if(abs(zombie.y - self.y) < self.size):
                    return True
        return False


    def checkIfWin(self):

        return boolean

    def kill(self):
        # LO ATRAPARON Y TIENE Q DECIRLE AL MAPA DE CREAR UN ZOMBIE EN ESTA POSICION
        self.gone = True
        return

