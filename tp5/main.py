from mapa import mapa

# TODO EN METROS

LARGO = 20
ALTO = 20
PUERTA_ENTRADA = 3
PUERTA_SALIDA = 3

cantZombies = 1
cantHumanos = 20
cantOlas = 5

dt = 0.01

#CREO MAPA

mapa = mapa(LARGO,ALTO,PUERTA_ENTRADA,PUERTA_SALIDA, cantZombies, cantHumanos, cantOlas, dt)
mapa.generarSeres()
distribucion = [0,0]

while(mapa.reglas):
    mapa.move()
    distribucion[rondas][0] = mapa.cantZombies
    distribucion[rondas][1] = mapa.cantHumanos
    #escribir resultados, humanos zombies sus posiciones flag de si es uno o el otro, y el t.

#RESULTADOS