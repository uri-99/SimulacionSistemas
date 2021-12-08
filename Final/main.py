from Map import Map

HEIGHT = 20
WIDTH = 20
DOOR_SIZE = 3

def genericEj():
    qAttackers = 5
    qGuards = 20
    rGuards = 1
    doubleGuards = False
    dt = 0.1
    map = Map(WIDTH, HEIGHT, DOOR_SIZE, DOOR_SIZE, qAttackers, qGuards, rGuards, doubleGuards, dt)

    print("asd")
    f = open("generic.txt", "w")

    while(not map.isFinished()):
        map.move()
        f.write(str(map))

    f.close()

genericEj()