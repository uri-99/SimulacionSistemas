from Map import Map

HEIGHT = 20
WIDTH = 20
DOOR_SIZE = 3

def genericEj():
    qAttackers = 25
    qGuards = 15
    rGuards = 1
    guardTau = 0.002
    doubleGuards = True
    canShoot = False
    dt = 0.05
    map = Map(WIDTH, HEIGHT, DOOR_SIZE, DOOR_SIZE, qAttackers, qGuards, rGuards, doubleGuards, dt, guardTau, canShoot)

    print("map generated")

    f = open("generic.txt", "w")

    while(not map.isFinished()):
        map.move()
        f.write(str(map))

    f.close()

genericEj()