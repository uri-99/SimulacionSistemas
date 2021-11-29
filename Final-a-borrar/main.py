from mapa import Mapa
from utils import standardDeviation
import numpy as np

# TODO EN METROS

LARGO = 20
ALTO = 20
PUERTA_ENTRADA = 3
PUERTA_SALIDA = 3

#CREO MAPA

def genericEj():
    velocidadAttackers = 1.2 #m/s
    cantAttackers = 10
    cantHumanos = 20
    cantOlas = 5

    dt = 0.09
    mapa = Mapa(LARGO,ALTO,PUERTA_ENTRADA,PUERTA_SALIDA, cantAttackers, cantHumanos, cantOlas, dt, velocidadAttackers)

    f = open("data/generic.txt", "w")

    while(not mapa.isFinished()):
        mapa.move()
        f.write(str(mapa))
        #escribir resultados, humanos attackers sus posiciones flag de si es uno o el otro, y el t.

    f.close()
    print(str(mapa.humansEscaped))

def caudal():
    velocidadAttackers = 0.4 #m/s
    cantAttackers = 35
    cantHumanos = 20
    cantOlas = 5

    dt = 0.09
    mapa = Mapa(LARGO,ALTO,PUERTA_ENTRADA,PUERTA_SALIDA, cantAttackers, cantHumanos, cantOlas, dt, velocidadAttackers)

    f = open("data/caudal.txt", "wb")

    while(not mapa.isFinished()):
        mapa.move()
    npArray = np.array(mapa.scapeTime)
    print(mapa.humansEscaped)
    print(mapa.scapeTime)
    np.save(f, npArray)
    f.close()

def ejb():
    velocidadAttackers = 1 #m/s
    cantAttackers = [2, 5, 10, 15, 20, 25, 30, 35]
    cantHumanos = 20
    cantOlas = 5
    dt = 0.05
    reps = 10
    f = open("data/ejb.txt", "w")
    for i in range(0, len(cantAttackers)):
        escapes = []
        for j in range(0, reps):
            print(j)
            mapa = Mapa(LARGO,ALTO,PUERTA_ENTRADA,PUERTA_SALIDA, cantAttackers[i], cantHumanos, cantOlas, dt, velocidadAttackers)
            while(not mapa.isFinished()):
                mapa.move()
            escapes.append(mapa.humansEscaped)
        average = sum(escapes) / len(escapes)
        deviation = standardDeviation(escapes)
        f.write(str(cantAttackers[i]) + ' ' + str(average/(cantHumanos * cantOlas)) + ' ' + str(deviation/(cantHumanos * cantOlas)) )
        f.write('\n')
    f.close()

def ejc():
    velocidadAttackers = [0.4, 0.8, 1.2, 1.6, 2, 2.4]
    cantAttackers = 10
    cantHumanos = 20
    cantOlas = 5
    dt = 0.05
    reps = 10
    f = open("data/ejc.txt", "w")
    for i in range(0, len(velocidadAttackers)):
        escapes = []
        for j in range(0, reps):
            print(j)
            mapa = Mapa(LARGO,ALTO,PUERTA_ENTRADA,PUERTA_SALIDA, cantAttackers, cantHumanos, cantOlas, dt, velocidadAttackers[i])
            while(not mapa.isFinished()):
                mapa.move()
            escapes.append(mapa.humansEscaped)
        average = sum(escapes) / len(escapes)
        deviation = standardDeviation(escapes)
        f.write(str(velocidadAttackers[i]) + ' ' + str(average/(cantHumanos * cantOlas)) + ' ' + str(deviation/(cantHumanos * cantOlas)) )
        f.write('\n')
    f.close()

caudal()

#RESULTADOS
