from planet import Planet
from spaceShip import SpaceShip
from rocket import Rocket
import math


G = 6.67384 * 10**-11 #N m**2 kg**-2
FACTOR = 1
dt = 86400 #86400 = 1 día
t=0

earth_initial_pos = [1.500619962348151e8, 2.288499248197072e6]
earth_initial_speed = [-9.322979134387409e-1, 2.966365033636722e1]
mars_initial_pos = [-2.426617401833969e8, -3.578836154354768e7]
mars_initial_speed = [4.435907910045917e0, -2.190044178514185e1]
sun_initial_position = [0, 0]
sun_initial_speed = [0, 0]

# angulos de diferencia para que esten alineados la tierra y la nave con respecto al sol
alignment_condition = 0.1

#  Planet = Planet(radius, mass, coords, speed, angularSpeed initT, dt)   #km, kg, [posX, posY], [speedX, speedY], t, dt
Earth = Planet("Earth", 6371, 5.97 * 10 ** 24, earth_initial_pos, earth_initial_speed, 1.99106393e-7, t, dt)
Mars = Planet("Mars", 3390, 6.4171 * 10 ** 23, mars_initial_pos, mars_initial_speed, 1.05865302e-7, t, dt)
Sun = Planet("Sun", 696000, 1988500 * 10 ** 24, [0, 0], [0,0], 0, t, dt)

system=[Sun, Earth, Mars]

shipCoords = [earth_initial_pos[0] + 1500, earth_initial_pos[1]]

fleet = []
Ship = SpaceShip(2 * 10 ** 5, shipCoords, 7.12, 10, 1500 + Earth.radius, t, dt,
                 system)  # 1500km de la superficie y 7.12 km/s

# for i in range(365):
#     fleet.append(SpaceShip(2 * 10 ** 5, shipCoords, 7.12, 8, 1500 + Earth.radius, t, dt,
#                      system))


    # V0 = 8 km/s (sumada a las velocidad orbital total que ya tiene la nave antes del despegue, dada por la velocidad de la tierra mas la velocidad de la estación espacial)
start = False
def advance():
    Earth.changePosition()
    Mars.changePosition()
    if start:
        Ship.changePosition()
    for ship in fleet:
        ship.changePosition()
    # if(shipTimeToTakeOff()):
    #     # cambiar speed de ship ya que despega
    #     pass

# def shipTimeToTakeOff():
#     ship_angle = Ship.angle_to_object(Earth)
#     earth_angle = Earth.angle_to_sun()
#     print(ship_angle, earth_angle, abs(ship_angle - earth_angle))
#
#     if(abs(ship_angle - earth_angle) <= alignment_condition):
#         return True
#     return False

export = open("data.txt", "w")

# for i in range(365):
#     fleet[math.ceil(i)].launch()
#     print(math.ceil(i))
#     advance()
#
# for i in range(365):
#     advance()
#
# for i in range(365):
#     export.write(str(fleet[i].minDistanceToMars))
#     export.write("\n")

start=True
for i in range(328):
    advance()
    export.write(Earth.print_position())
    export.write("\n")
    export.write(str(Mars.print_position()))
    export.write("\n")
    export.write(str(Ship.print_position()))
    export.write("\n")
    export.write("\n")
# advance()
Ship.launch()
for i in range(200):
    advance()
    export.write(Earth.print_position())
    export.write("\n")
    export.write(str(Mars.print_position()))
    export.write("\n")
    export.write(str(Ship.print_position()))
    export.write("\n")
    export.write("\n")
    print(Ship.distance_to(Sun))
#
# Ship.launch()
#
# for i in range(200):
#     advance()
#     export.write(Earth.print_position())
#     export.write("\n")
#     export.write(str(Mars.print_position()))
#     export.write("\n")
#     export.write(str(Ship.print_position()))
#     export.write("\n")
#     export.write("\n")


export1a = open("1a.txt", "w")
export1a2 = open("1a2.txt", "w")
export1b = open("1b.txt", "w")
export1c = open("1c.txt", "w")
export2 = open("2.txt", "w")
export3 = open("3.txt", "w")

## EJ 1.a ##
# print("START 1.a")
# for i in range(365):
#     fleet.append(SpaceShip(2 * 10 ** 5, shipCoords, 7.12, 8, 1500 + Earth.radius, t, dt,
#                      system))
#
# for i in range(365*FACTOR):
#     if i % FACTOR == 0:
#         fleet[math.ceil(i/FACTOR)].launch()
#         print(math.ceil(i/FACTOR))
#     advance()
#
# for i in range(math.ceil((365*FACTOR)/2)):
#     advance()
#
# d_min = math.inf
# t_min = 0
# OPTIMAL_LAUNCH_DATE = math.inf
# for i in range(365):
#     if fleet[i].minDistanceToMars < d_min:
#         d_min = fleet[i].minDistanceToMars
#         OPTIMAL_LAUNCH_DATE = i
#         t_min = fleet[i].T_Dmin
#
#     export1a.write(str(fleet[i].minDistanceToMars))
#     export1a.write("\n")
# fleet = []
# print("END 1.a")
# print("t min ", t_min)
OPTIMAL_LAUNCH_DATE = 324

## EJ 1.a día 324 ##
# print("START 1.a 324")
# fleet = []
# for i in range(144):
#     fleet.append(SpaceShip(2 * 10 ** 5, shipCoords, 7.12, 8, 1500 + Earth.radius, t, 600,
#                      system))
#
# for i in range(144*OPTIMAL_LAUNCH_DATE):
#     if i%144 == 0:
#         print("day ", i/144)
#     advance()
#
# for i in range(144):
#     print("launch ", i)
#     fleet[i].launch()
#     advance()
#
# for i in range(144*100):
#     if i%144 == 0:
#         print("day ", i/144)
#     advance()
#
# d_min = math.inf
# for i in range(144):
#     if fleet[i].minDistanceToMars < d_min:
#         d_min = fleet[i].minDistanceToMars
#         OPTIMAL_LAUNCH_MINUTE = i*10
#         t_min = fleet[i].T_Dmin
#         print("optimal minute ", OPTIMAL_LAUNCH_MINUTE, i)
#     export1a2.write(str(fleet[i].minDistanceToMars))
#     export1a2.write("\n")
# export1a2.close()






# # ## EJ 1.b ##
# print("START 1.b")
# start = True
#
# OPTIMAL_LAUNCH_DATE = 324
#
# for i in range(400):
#     if Ship.has_launched:
#         export1b.write(str(Ship.speed))
#     else:
#         export1b.write(str(Ship.speed + Earth.speed_components_to_total(Earth.speed)))
#     export1b.write("\n")
#     if i == OPTIMAL_LAUNCH_DATE*FACTOR:
#         print("optimal ", OPTIMAL_LAUNCH_DATE)
#         Ship.launch()
#     advance()
#
# print("END 1.b")

## EJ 1.c ##
# print("START 1.c")
# start = True
# t_min = 34300800
# OPTIMAL_LAUNCH_DATE = 324
# speed_when_closest = 42069
# for i in range(math.ceil(400)):
#     export1c.write(str(Ship.relative_to_mars_speed()))
#     export1c.write("\n")
#     if i == OPTIMAL_LAUNCH_DATE*FACTOR:
#         Ship.launch()
#     if Ship.t == t_min:
#         speed_when_closest = Ship.relative_to_mars_speed()
#     advance()
#     if i%FACTOR == 0:
#         print("1c ", i)
# export1c.write("\nSPEED WHEN CLOSEST: ")
# export1c.write(str(speed_when_closest))
# print("END 1.c")

## EJ 2 ##
# print("START 2")
# for i in range(365):
#     fleet.append(SpaceShip(2 * 10 ** 5, shipCoords, 7.12, 5, 1500 + Earth.radius, t, dt,
#                      system))
#
# for i in range(365*FACTOR):
#     if i % FACTOR == 0:
#         fleet[math.ceil(i/FACTOR)].launch()
#         print(math.ceil(i/FACTOR))
#     advance()
#
# for i in range(math.ceil((365*FACTOR)/2)):
#     advance()
#
# d_min = math.inf
# t_min = 0
# OPTIMAL_LAUNCH_DATE = math.inf
# for i in range(365):
#     if fleet[i].minDistanceToMars < d_min:
#         d_min = fleet[i].minDistanceToMars
#         OPTIMAL_LAUNCH_DATE = i
#         t_min = fleet[i].T_Dmin
#
#     export2.write(str(fleet[i].minDistanceToMars))
#     export2.write("\n")
# export2.write("\n")
# export2.write("Optimal launch day: ")
# export2.write(str(OPTIMAL_LAUNCH_DATE))
# fleet = []
# print("END 2")



## EJ 3 ##
print("START 3")
# for i in range(1500):
#     fleet.append(SpaceShip(2 * 10 ** 5, shipCoords, 7.12, -i/10, 1500 + Earth.radius, t, dt,
#                      system))
# advance()
#
# for i in range(1500):
#     fleet[i].launch()
#     # print(fleet[i].speed)
#
# for i in range(200):
#     advance()
#     # print(fleet[0].minDistanceToMars)
#     # print(fleet[-1].minDistanceToMars)
#
# minn = math.inf
# minn_i = 0
# for i in range(1500):
#     export3.write(str(fleet[i].minDistanceToMars))
#     if fleet[i].minDistanceToMars < minn:
#         minn = fleet[i].minDistanceToMars
#         minn_i = i
#     export3.write("\n")
# export3.write("\n")
# export3.write("Min distance: ")
# export3.write(str(minn))
# export3.write(" iteration: ")
# export3.write(str(minn_i))
# export3.write(" V0: ")
# export3.write(str(fleet[minn_i].takeoffSpeed))
# print("END 3")


export1a.close()
export1b.close()
export1c.close()
export2.close()
export3.close()