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
        self.humansEscaped = 0
        self.velZombies = velZombies
        self.generarSeres()
        print("humanos: ", self.humanos, "\nzombies: ", self.zombies)

    def generarSeres(self):
        self.generarHumanos()

        Zadded = 0
        while Zadded < self.cantZombies: #generarZombies
            auxX = random.uniform(self.largo/2, self.largo)
            auxY = random.uniform(0, self.alto)

            #auxX = 10 #test
            #auxY = 10 #test
            if self.posicionNoOcupada(auxX, auxY):
                self.zombies.append(Zombie(auxX, auxY, self.velZombies, False))
                Zadded += 1
        return

    def generarHumanos(self):
        if self.olaActual == self.olasHumanos:
            print("Todas las olas ya fueron generadas")
            return

        added = 0
        while added < self.cantHumanos: #generarHumano
            auxX = random.uniform(0, 1)
            auxY = random.uniform((self.alto / 2) + (self.entrada / 2), (self.alto / 2) - (self.entrada / 2))
            if self.posicionNoOcupada(auxX, auxY):
                self.humanos.append(Humano(auxX, auxY, self.humanSize))
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

    def isFinished(self): #condicion de terminacion, ola actual = olas humanos, y hay 0 humanos no escapados
        if self.olaActual == self.olasHumanos:
            for humano in self.humanos:
                if humano.gone == False:
                    return False #queda algun humano vivo
            return True
        if self.t > 100:
            return True
        return False #quedan oleadas por mandar

    def move(self):
        self.t += 0.1
        self.t = round(self.t, 1)
        if(self.t % 9 == 0) and (self.olaActual < self.olasHumanos):
            self.generarHumanos()
        for zombie in self.zombies:
            self.cpm(zombie)
            zombie.move(self.dt, self.humanos)
        for human in self.humanos:
            self.cpm(human)
            human.move(self.dt, self.zombies, self.humanos)
            if human.checkIfDie(self.zombies):
                print("dead")
                human.kill()
                self.humanos.remove(human)
                self.zombies.append(Zombie(human.x, human.y, self.velZombies, True))
            elif human.checkIfWin(self.largo, self.alto, self.salida):
                print("win")
                human.kill()
                self.humanos.remove(human)
                self.humansEscaped += 1
        return

    def cantZombies(self):
        return len(self.zombies)

    def cantHumanos(self):
        return len(self.humanos)

    # def cpm(self,ser):
    #     ## AVERIGUAR SI ESTA EN CONTACTO
    #     for human in self.humanos:
    #         if ser.distanceTo(human.x,human.y) <= 0.50 and ser.humano: ##0.3 es el radio de las personas
    #             ## EN CONTACTO HUMANO - HUMANO, CAMBIAR DIRECCION
    #             ser.changeDirection(human.x,human.y) ## LA DEL HUMAN NO HACE FALTA CAMBIAR DIRECCINO (SOLO SELF) XQ DESP EL FOR VA A OCUPARE DE ESE HUMAN EN CPM
    #             return
    #         ##CASO ZOMBIE - HUMANO, SOLO HUMANO CAMBIA DIRECCION, YA QUE ZOMBIE QUIERE IR HACIA EL. PERO SELF ES ZOMBIE ASI Q LISTO
                
        
    #     for zombie in self.zombies:
    #         if ser.distanceTo(zombie.x,zombie.y) <= 0.50: ##0.3 es el radio de las personas
    #             ser.changeDirection(zombie.x,zombie.y) ## sea SER zombie o humano en ambos caso el SER debe cambiar direccion
    #             return

    #     return ##todos estan separados si llega este punto

    #     ### LEER ESTO LEER ESTO LEER
    #     ### SI LA RELACION ZOMBIE - HUMANO YA SE TIENE EN CUENTA ENTONCES SOLO HABRIA QUE HACER ZOMBIE - ZOMBIE y HUMANO - HUMANO, SI ES ASI SERIA ASI
    #     ###

    def cpm(self,ser):
        ## AVERIGUAR SI ESTA CERCA
        if ser.humano:
            for human in self.humanos:
                if(ser.x != human.x and ser.y != human.y):
                    if ser.distanceTo(human.x,human.y) <= 0.50: ##0.3 es el radio de las personas
                    ## EN CONTACTO HUMANO - HUMANO, CAMBIAR DIRECCION
                        ser.changeDirection(human.x,human.y) ## LA DEL HUMAN NO HACE FALTA CAMBIAR DIRECCINO (SOLO SELF) XQ DESP EL FOR VA A OCUPARE DE ESE HUMAN EN CPM
                        return
                
        else:
            for zombie in self.zombies:
                if(ser.x != zombie.x and ser.y != zombie.y):
                    if ser.distanceTo(zombie.x,zombie.y) <= 0.50: ##0.3 es el radio de las personas
                        ser.changeDirection(zombie.x,zombie.y) ## sea SER zombie 
                        return

        return ##todos estan separados si llega este punto

    def __repr__(self):
        s = ""
        for i in self.humanos:
            s += str(i.x) + " " + str(i.y) + " 0\n"
        for j in self.zombies:
            s += str(j.x) + " " + str(j.y) + " 1\n"
        s += "\n"
        return s