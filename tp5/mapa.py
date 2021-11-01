import numpy as np

def __init__(self,largo,alto,entrada,salida, cantZombies, cantHumanos, olasHumanos):
    self.largo = largo
    self.alto = alto
    self.entrada = entrada
    self.salida = salida
    self.cantZombies = cantZombies
    self.cantHumanos = cantHumanos
    self.olasHumanos = olasHumanos
    self.olaActual = 1
    self.rondas = 0
    self.zombies = []
    self.humanos = []

def generarSeres(self, cantHumanos, cantZombies):
    for humano in cantHumanos:
        None
        #generarHumano
    for zombie in cantZombies:
        None
        #generarZombies
    return

def generarHumanosExtra(self, cantHumanos):
    
    return

def posicionNoOcupada(x,y,array): # Hay que llamarla para chequear q no existe un humano ahi antes de agregarlo
    for person in array:
        if(person.x == x): # habria que fijarse que no este tampoco muy cerca a uno
            if(person.y == y):
                return False
    return True

def reglas(self):
    if len(self.humanos) == 0:
        return True
    return False

def mover(self):
    self.rondas += 1
    if(self.rondas % 9 == 0) and (self.olaActual < self.olaHumanos):
        generarHumanosExtra(self.cantHumanos)
    for zombie in self.zombies:
        self.zombies[zombie].mover()
    for human in self.humanos:
        self.humanos[human].mover()
    return

def cantZombies():
    return

def cantHumanos():
    return

def zombieAtrapaHumano():
    # Mata al humano y crea un zombie en esa posicion en estado imbecil, es decir, q no se mueve por 7 segundos
    return