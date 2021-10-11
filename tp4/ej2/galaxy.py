from planet import Planet
from spaceShip import SpaceShip
from rocket import Rocket
import math


G = 6.67384 * 10**-11 #N m**2 kg**-2
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
Ship = SpaceShip(2*10**5, shipCoords, 7.12, 8, 1500+Earth.radius, t, dt, system) #1500km de la superficie y 7.12 km/s


    # V0 = 8 km/s (sumada a las velocidad orbital total que ya tiene la nave antes del despegue, dada por la velocidad de la tierra mas la velocidad de la estación espacial)

def advance():
    Earth.changePosition()
    Mars.changePosition()
    Ship.changePosition()
    # if(shipTimeToTakeOff()):
    #     # cambiar speed de ship ya que despega
    #     pass

 # calcular si estan alineados

def shipTimeToTakeOff():
    ship_angle = Ship.angle_to_object(Earth)
    earth_angle = Earth.angle_to_sun()
    print(ship_angle, earth_angle, abs(ship_angle - earth_angle))

    if(abs(ship_angle - earth_angle) <= alignment_condition):
        return True
    return False

# for planet in system:
#     print(planet.name, planet.angularPos, planet.position)
#     print(planet.distance_to_sun)
# advance()
# for planet in system:
#     print(planet.name, planet.angularPos, planet.position)
#     print(planet.distance_to_sun)
export = open("data.txt", "w")

for i in range(325):
    advance()
    export.write(Earth.print_position())
    export.write("\n")
    export.write(str(Mars.print_position()))
    export.write("\n")
    export.write(str(Ship.print_position()))
    export.write("\n")
    export.write("\n")

Ship.launch()
while not Ship.has_launched:
    if shipTimeToTakeOff():
        Ship.launch()
    advance()
    export.write(Earth.print_position())
    export.write("\n")
    export.write(str(Mars.print_position()))
    export.write("\n")
    export.write(str(Ship.print_position()))
    export.write("\n")
    export.write("\n")

#
for i in range(2000):
    advance()
    export.write(Earth.print_position())
    export.write("\n")
    export.write(str(Mars.print_position()))
    export.write("\n")
    export.write(str(Ship.print_position()))
    export.write("\n")
    export.write("\n")
#
#
#
# for i in range(1000):
#     advance()
#     export.write(Earth.print_position())
#     export.write("\n")
#     export.write(str(Mars.print_position()))
#     export.write("\n")
#     export.write(str(Ship.print_position()))
#     export.write("\n")
#     export.write("\n")
#     # print("earth ", Earth.angularPos, Earth.position)
#     # print("ship ", Ship.angular_to_earth, Ship.position)