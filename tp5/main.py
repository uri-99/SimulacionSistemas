from mapa import Mapa

# TODO EN METROS

LARGO = 20
ALTO = 20
PUERTA_ENTRADA = 3
PUERTA_SALIDA = 3

#CREO MAPA

def genericEj():
    velocidadZombies = 1 #m/s
    cantZombies = 10
    cantHumanos = 20
    cantOlas = 5

    dt = 0.05
    mapa = Mapa(LARGO,ALTO,PUERTA_ENTRADA,PUERTA_SALIDA, cantZombies, cantHumanos, cantOlas, dt, velocidadZombies)

    f = open("data/generic.txt", "w")

    while(not mapa.isFinished()):
        mapa.move()
        f.write(str(mapa))
        #escribir resultados, humanos zombies sus posiciones flag de si es uno o el otro, y el t.

    f.close()

def ejb():
    velocidadZombies = 1 #m/s
    cantZombies = [2, 5, 10, 15, 20, 25, 30, 35]
    cantHumanos = 20
    cantOlas = 5
    dt = 0.05
    reps = 10

    for i in range(0, len(cantZombies)):
        for j in range(0, reps):
            mapa = Mapa(LARGO,ALTO,PUERTA_ENTRADA,PUERTA_SALIDA, cantZombies[i], cantHumanos, cantOlas, dt, velocidadZombies)
            f = open("data/ejb_" + str(cantZombies[i]) + "_" + str(j) +".txt", "w")
            while(not mapa.isFinished()):
                mapa.move()
                f.write(str(mapa))
                #escribir resultados, humanos zombies sus posiciones flag de si es uno o el otro, y el t.
            f.close()

def ejc():
    velocidadZombies = [0.4, 0.8, 1.2, 1.6, 2, 2.4]
    cantZombies = 10
    cantHumanos = 20
    cantOlas = 5
    dt = 0.05
    reps = 10

    for i in range(0, len(cantZombies)):
        for j in range(0, reps):
            mapa = Mapa(LARGO,ALTO,PUERTA_ENTRADA,PUERTA_SALIDA, cantZombies, cantHumanos, cantOlas, dt, velocidadZombies[i])
            f = open("data/ejc_" + str(cantZombies[i]) + "_" + str(j) +".txt", "w")
            while(not mapa.isFinished()):
                mapa.move()
                f.write(str(mapa))
                #escribir resultados, humanos zombies sus posiciones flag de si es uno o el otro, y el t.
            f.close()

ejb()

#RESULTADOS
