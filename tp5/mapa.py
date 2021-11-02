import numpy as np

class Mapa:

    humanSize = 0.3#m


    def __init__(self,largo,alto,entrada,salida, cantZombies, cantHumanos, olasHumanosm, dt):
        self.largo = largo
        self.alto = alto
        self.entrada = entrada
        self.salida = salida
        self.cantZombies = cantZombies
        self.cantHumanos = cantHumanos
        self.olasHumanos = olasHumanos
        self.olaActual = 0
        self.rondas = 0
        self.zombies = []
        self.humanos = []
        self.t = 0
        self.dt = dt
        self.humanosEscapados = 0


    def generarSeres(self, cantHumanos, cantZombies):

        generarHumanos(cantHumanos)

        for zombie in cantZombies:
            None
            #generarZombies
        return

    def generarHumanos(self, cantHumanos):
        for i in range(cantHumanos):
            # generarHumano
            self.humanos.append(Humano())
        self.olaActual += 1
        return

    def posicionNoOcupada(self,x,y,array): # Hay que llamarla para chequear q no existe un humano ahi antes de agregarlo
        for person in array:
            if(person.x == x): # habria que fijarse que no este tampoco muy cerca a uno
                if(person.y == y):
                    return False
        return True

    def reglas(self): #condicion de terminacion, ola actual = olas humanos, y hay 0 humanos no escapados
        if len(self.humanos) == 0:
            return True
        return False

    def move(self):
        self.rondas += 1
        self.t += self.dt
        if(self.t % 9 == 0) and (self.olaActual < self.olaHumanos):
            self.generarHumanos(self.cantHumanos)
        for zombie in self.zombies:
            zombie.move()
        for human in self.humanos:
            human.move()
            if human.checkIfDie():
                human.kill()
                zombies.append(Zombie(datos del human que acaba de morir))
        return

    def cantZombies(self):
        return len(self.zombies)

    def cantHumanos(self):
        return len(self.humanos)

    def zombieAtrapaHumano():
        # Mata al humano y crea un zombie en esa posicion en estado imbecil, es decir, q no se mueve por 7 segundos
        return