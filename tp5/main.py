from mapa import Mapa

# TODO EN METROS

LARGO = 20
ALTO = 20
PUERTA_ENTRADA = 3
PUERTA_SALIDA = 3

velocidadZombies = 1 #m/s
cantZombies = 20
cantHumanos = 20
cantOlas = 5

dt = 0.01

#CREO MAPA

mapa = Mapa(LARGO,ALTO,PUERTA_ENTRADA,PUERTA_SALIDA, cantZombies, cantHumanos, cantOlas, dt, velocidadZombies)

'''
mapa.generarSeres()
distribucion = [0,0]

while(not mapa.isFinished()):
    mapa.move()
    distribucion[rondas][0] = mapa.cantZombies
    distribucion[rondas][1] = mapa.cantHumanos
    #escribir resultados, humanos zombies sus posiciones flag de si es uno o el otro, y el t.

#RESULTADOS
'''