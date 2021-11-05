from mapa import Mapa

# TODO EN METROS

LARGO = 20
ALTO = 20
PUERTA_ENTRADA = 3
PUERTA_SALIDA = 3

velocidadZombies = 1 #m/s
cantZombies = 10
cantHumanos = 20
cantOlas = 5

dt = 0.05

#CREO MAPA

mapa = Mapa(LARGO,ALTO,PUERTA_ENTRADA,PUERTA_SALIDA, cantZombies, cantHumanos, cantOlas, dt, velocidadZombies)

f = open("data.txt", "w")

while(not mapa.isFinished()):
    mapa.move()
    f.write(str(mapa))
    #escribir resultados, humanos zombies sus posiciones flag de si es uno o el otro, y el t.

f.close()

#RESULTADOS