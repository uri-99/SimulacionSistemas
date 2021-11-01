from mapa import mapa

# TODO EN METROS

LARGO = 20
ALTO = 20
PUERTA_ENTRADA = 3
PUERTA_SALIDA = 3

#CREO MAPA

mapa = mapa(LARGO,ALTO,PUERTA_ENTRADA,PUERTA_SALIDA)
mapa.generarSeres()
rondas = 0
distribucion = [0,0]

while(mapa.reglas):
    mapa.mover
    rondas += 1
    distribucion[rondas][0] = mapa.cantZombies
    distribucion[rondas][1] = mapa.cantHumanos

#RESULTADOS