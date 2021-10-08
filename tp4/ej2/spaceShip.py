import math
from ej2.object import Object

class SpaceShip:

    G = 6.67384 * 10**-11 #N m**2 kg**-2

    def __init__(self, mass, position, speed, angularSpeed, t, dt, system):
        self.mass = mass
        self.position = position
        # self.angularPos = self.angle_to_earth(position) #radianes con respecto a la tierra #DUDA tengo que pasarle siempre la tierra o no?
        self.speed = speed
        self.angularSpeed = angularSpeed #self.speed_components_to_total(speed)
        self.t = t
        self.dt = dt
        # self.distance_to_sun = self.calculate_distance_to_sun(position)
        self.system = system
        self.earth = system[1]
        a_x = []
        a_y = []
        self.accelerations = [a_x, a_y]
        self.acceleration = None
        v_x = []
        v_y = []
        self.velocities = [v_x, v_y]
        pos_x = []
        pos_y = []
        self.positions = [pos_x, pos_y]

    def angle_to_earth(self):
        x = self.position[0] - self.earth.position[0]
        y = self.position[1] - self.earth.position[1]
        relative_angle = math.atan(y/x)
        if(x >= 0 and y>= 0):
            return relative_angle
        elif(x <= 0 and y >= 0):
            return math.pi - relative_angle
        elif(x <= 0 and y <= 0):
            return math.pi + relative_angle
        else:
            return 2*math.pi - relative_angle

        # lo que pense es, la velocidad del bicho este es basciamente igual que la tierra mas su velocidad, entonces tengo dos ideas: 1) la velocidad de el es la suya mas la de la tierra y q se mueva sola. 2) Veo lo q se movio la tierra, muevo lo mismo a la nave y despues calculo lo q se movio la nave pero en ese caso necesito saber la posicion actual de la tierra y la anterior y es medio un chino
    def changePosition(self):
        self.t += self.dt
        self.calculate_new_acceleration()
        self.Gear("x")
        self.Gear("y")

    def Gear(self, coord):
        if coord == "x":
            a = 0
        elif coord == "y":
            a = 1
        else:
            a = None
            exit("Wrong coord gear")

        dt = self.dt
        r0p = self.position[a] + self.speed[a] * dt + self.acceleration[a] * (
                    dt ** 2 / math.factorial(2)) + self.r3() * (dt ** 3 / math.factorial(3)) + self.r4() * (
                          dt ** 4 / math.factorial(4)) + self.r5() * (dt ** 5 / math.factorial(5))
        r1p = self.speed[a] + self.acceleration[a] * dt + self.r3() * (dt ** 2 / math.factorial(2)) + self.r4() * (
                    dt ** 3 / math.factorial(3)) + self.r5() * (dt ** 4 / math.factorial(4))
        r2p = self.acceleration[a] + self.r3() * dt + self.r4() * (dt ** 2 / math.factorial(2)) + self.r5() * (
                    dt ** 3 / math.factorial(3))
        r3p = self.r3() + self.r4() * dt + self.r5() * (dt ** 2 / math.factorial(2))
        r4p = self.r4() + self.r5() * dt
        r5p = self.r5()

        self.position[a] = r0p
        new_a = self.calculate_new_acceleration()
        delta_a = new_a[a] - r2p
        delta_R2 = (delta_a * dt ** 2) / 2

        r0c = r0p + 3 / 16 * delta_R2
        r1c = r1p + 251 / 360 * delta_R2 / dt
        r2c = r2p + 1 * (2 * delta_R2) / dt ** 2
        r3c = r3p + 11 / 18 * (3 * 2 * delta_R2) / dt ** 3
        r4c = r4p + 1 / 6 * (4 * 3 * 2 * delta_R2) / dt ** 3
        r5c = r5p + 1 / 60 * (5 * 4 * 3 * 2 * delta_R2) / dt ** 3

        self.position[a] = r0c
        self.positions[a].append(r0c)
        self.speed[a] = r1c
        self.velocities[a].append(r1c)
        self.acceleration[a] = r2c
        self.accelerations[a].append(r2c)

        return r0c

    def r3(self):
        return 0

    def r4(self):
        return 0

    def r5(self):
        return 0


    def F(self, other):
        return self.G * ((self.mass * other.mass) / self.distance_to(other))

    def Fxy(self, other):
        f = self.F(other)
        angle = self.angle_to_object(other)
        fx = f * math.sin(angle)
        fy = f * math.cos(angle)
        if self.position[0] > other.positions[0]:
            fx *= -1
        if self.position[1] > other.positions[1]:
            fy *= -1
        return fx, fy

    def calculate_new_acceleration(self):
        fx = 0
        fy = 0
        for planet in self.system:
            fxx, fyy = self.Fxy(planet)
            fx += fxx
            fy += fyy
        self.accelerations[0].append(fx / self.mass)
        self.accelerations[1].append(fy / self.mass)
        self.acceleration = [fx / self.mass, fy / self.mass]
        return self.acceleration

    def distance_to(self, other):
        return math.sqrt( (self.position[0]-other.position[0])**2 + (self.position[1]-other.position[1])**2 )