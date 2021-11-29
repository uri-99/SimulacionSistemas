import random

import numpy as np

from humanos import Humano
from attackers import Attacker


class Mapa:

    humanSize = 0.4#m


    def __init__(self,largo,alto,entrada,salida, cantAttackers, cantHumanos, olasHumanos, dt, velAttackers):
        self.largo = largo
        self.alto = alto
        self.entrada = entrada
        self.salida = salida
        self.cantAttackers = cantAttackers
        self.cantHumanos = cantHumanos
        self.olasHumanos = olasHumanos
        self.olaActual = 0
        self.rondas = 0
        self.attackers = []
        self.humanos = []
        self.t = 0
        self.dt = dt
        self.humansEscaped = 0
        self.scapeTime = []
        self.velAttackers = velAttackers
        self.generarSeres()
        # print("humanos: ", self.humanos, "\nattackers: ", self.attackers)

    def generarSeres(self):
        self.generarHumanos()

        Zadded = 0
        while Zadded < self.cantAttackers: #generarAttackers
            auxX = random.uniform(self.largo/2, self.largo)
            auxY = random.uniform(0, self.alto)
            if self.posicionNoOcupada(auxX, auxY):
                self.attackers.append(Attacker(auxX, auxY, self.velAttackers, False))
                Zadded += 1
        return

    def generarHumanos(self):
        if self.olaActual == self.olasHumanos:
            #print("Todas las olas ya fueron generadas")
            return

        added = 0
        while added < self.cantHumanos: #generarHumano
            auxX = random.uniform(0, 2.5)
            auxY = random.uniform((self.alto / 2) + (self.entrada / 2), (self.alto / 2) - (self.entrada / 2))
            if self.posicionNoOcupada(auxX, auxY):
                self.humanos.append(Humano(auxX, auxY, self.humanSize))
                added += 1

        self.olaActual += 1
        return

    def posicionNoOcupada(self,x,y): # Hay que llamarla para chequear q no existe un humano ahi antes de agregarlo
        array = self.humanos + self.attackers
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
        for attacker in self.attackers:
            isCpm = self.cpm(attacker)
            attacker.move(self.dt, self.humanos, isCpm)
        for human in self.humanos:
            isCpm = self.cpm(human)
            human.move(self.dt, self.attackers, self.humanos, isCpm)
            if human.checkIfDie(self.attackers):
                #print("dead")
                human.kill()
                self.humanos.remove(human)
                self.attackers.append(Attacker(human.x, human.y, self.velAttackers, True))
            elif human.checkIfWin(self.largo, self.alto, self.salida):
                #print("win")
                human.kill()
                self.humanos.remove(human)
                self.humansEscaped += 1
                self.scapeTime.append(self.t)
        return

    def cantAttackers(self):
        return len(self.attackers)

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
                
        
    #     for attacker in self.attackers:
    #         if ser.distanceTo(attacker.x,attacker.y) <= 0.50: ##0.3 es el radio de las personas
    #             ser.changeDirection(attacker.x,attacker.y) ## sea SER attacker o humano en ambos caso el SER debe cambiar direccion
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
                    if ser.distanceTo(human.x,human.y) <= 0.2: ##radio min de las personas
                    ## EN CONTACTO HUMANO - HUMANO, CAMBIAR DIRECCION
                        ser.changeDirection(human.x,human.y) ## LA DEL HUMAN NO HACE FALTA CAMBIAR DIRECCINO (SOLO SELF) XQ DESP EL FOR VA A OCUPARE DE ESE HUMAN EN CPM
                        #ser.direccionDeseada(-human.x, -human.y)
                        return True
            for attacker in self.attackers:
                if attacker.apagado and attacker.x != ser.x and attacker.y != ser.y:
                    if ser.distanceTo(attacker.x,attacker.y) <= 0.2: ## radio min de las personas
                    ## EN CONTACTO HUMANO - HUMANO, CAMBIAR DIRECCION
                        ser.changeDirection(attacker.x,attacker.y) ## LA DEL HUMAN NO HACE FALTA CAMBIAR DIRECCINO (SOLO SELF) XQ DESP EL FOR VA A OCUPARE DE ESE HUMAN EN CPM
                        ser.radius = 0.2
                        #ser.direccionDeseada(-human.x, -human.y)

                
        else:
            for attacker in self.attackers:
                if(ser.x != attacker.x and ser.y != attacker.y):
                    if ser.distanceTo(attacker.x,attacker.y) <= 0.4: ##0.3 es el radio de las personas
                        ser.changeDirection(attacker.x,attacker.y) ## sea SER attacker 
                        return True

        return False ##todos estan separados si llega este punto

    def __repr__(self):
        s = ""
        for i in self.humanos:
            s += str(i.x) + " " + str(i.y) + " 0\n"
        for j in self.attackers:
            s += str(j.x) + " " + str(j.y) + " 1\n"
        s += "\n"
        return s