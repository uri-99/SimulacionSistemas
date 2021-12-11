from Map import Map

HEIGHT = 20
WIDTH = 20
DOOR_SIZE = 3

def genericEj(q):
    qAttackers = q
    qGuards = 15
    rGuards = 1
    guardTau = 0.002
    doubleGuards = False
    canKill = False
    canShoot = False

    dt = 0.05
    map = Map(WIDTH, HEIGHT, DOOR_SIZE, DOOR_SIZE, qAttackers, qGuards, rGuards, doubleGuards, dt, guardTau, canShoot, canKill)

    #print("map generated")

    f = open("generic.txt", "w")

    while(not map.isFinished()):
        map.move()
        #f.write(str(map))
    map.move()
    #f.write(str(map))

    f.close()
    return map.result

array = []

for i in range(50):
    num = 0
    for j in range(10):
        num += genericEj(i)
    print(i)
    array.append(num)

print(array)


#genericEj()