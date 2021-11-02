import random

import numpy as np

from humanos import Humano
from zombies import Zombie


class Mapa:

    humanSize = 0.3#m


    def __init__(self,largo,alto,entrada,salida, cantZombies, cantHumanos, olasHumanos, dt, velZombies):
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
        self.velZombies = velZombies


    def generarSeres(self, cantHumanos, cantZombies):
        self.generarHumanos(cantHumanos)

        Zadded = 0
        while Zadded < cantZombies: #generarZombies
            auxX = random.uniform(self.largo/2, self.largo)
            auxY = random.uniform(0, self.alto)
            if self.posicionNoOcupada(auxX, auxY):
                self.zombies.append(Zombie(auxX, auxY, self.velZombies))
                Zadded += 1
        return

    def generarHumanos(self, cantHumanos):
        added = 0
        while added < cantHumanos: #generarHumano
            auxX = random.uniform(0, 3)
            auxY = random.uniform((self.alto / 2) + (self.entrada / 2), (self.alto / 2) - (self.entrada / 2))
            if self.posicionNoOcupada(auxX, auxY):
                self.humanos.append(Humano(auxX, auxY))
                added += 1

        self.olaActual += 1
        return

    def posicionNoOcupada(self,x,y): # Hay que llamarla para chequear q no existe un humano ahi antes de agregarlo
        array = self.humanos + self.zombies
        for person in array:
            if( abs(person.x - x) < self.humanSize ): # habria que fijarse que no este tampoco muy cerca a uno
                if(abs(person.y - y) < self.humanSize):
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