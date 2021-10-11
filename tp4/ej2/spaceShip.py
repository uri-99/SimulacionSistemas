import math
from planet import Planet

class SpaceShip:

    G = 6.67384 * 10**-11 #N m**2 kg**-2   #m**3 kg**-1 s**-2

    def __init__(self, mass, position, speed, takeoffSpeed, distance_to_earth, t, dt, system):
        self.mass = mass
        self.position = position
        # self.angularPos = self.angle_to_earth(position) #radianes con respecto a la tierra #DUDA tengo que pasarle siempre la tierra o no?
        self.speed = speed
        orbit_length = 2*math.pi*(distance_to_earth)
        period = orbit_length / speed
        self.angularSpeed = (2*math.pi)/period #self.speed_components_to_total(speed)
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
        self.has_launched = False
        self.angular_to_earth = 0
        self.distance_to_earth = distance_to_earth
        self.velocity = self.decompose_speed_earth()
        self.takeoffSpeed = takeoffSpeed
        self.minDistanceToMars = self.distance_to(system[2])


    def decompose_speed_earth(self):
        angle = self.earth.angle_to_sun()
        angle = angle + math.pi/2

        return [self.speed * math.cos(angle), self.speed * math.sin(angle)]

    def compose_velocity(self):
        return math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)

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
        if not self.has_launched:
            self.angular_to_earth += self.dt * self.angularSpeed
            self.angular_to_earth = self.angular_to_earth % (2 * math.pi)
            self.position = [math.cos(self.angular_to_earth) * self.distance_to_earth + self.earth.position[0],
                             math.sin(self.angular_to_earth) * self.distance_to_earth + self.earth.position[1]]
            self.velocity = self.decompose_speed_earth()
            # print("aa", self.distance_to(self.earth))
        else:
            # print("new acc: ", self.calculate_new_acceleration())
            self.calculate_new_acceleration()
            self.Gear("x")
            self.Gear("y")
            self.speed = self.compose_velocity()
            # print("dd", self.distance_to(self.earth))
        if self.distance_to(self.system[2]) < self.minDistanceToMars:
            self.minDistanceToMars = self.distance_to(self.system[2])

    def Gear(self, coord):
        # print("Old sped before gear: ", self.velocity, self.acceleration)
        if coord == "x":
            a = 0
        elif coord == "y":
            a = 1
        else:
            a = None
            exit("Wrong coord gear")

        dt = self.dt
        r0p = self.position[a] + self.velocity[a] * dt + self.acceleration[a] * (dt ** 2 / math.factorial(2)) #+ self.r3() * (dt ** 3 / math.factorial(3)) + self.r4() * (dt ** 4 / math.factorial(4)) + self.r5() * (dt ** 5 / math.factorial(5))
        r1p = self.velocity[a] + self.acceleration[a] * dt #+ self.r3() * (dt ** 2 / math.factorial(2)) + self.r4() * (dt ** 3 / math.factorial(3)) + self.r5() * (dt ** 4 / math.factorial(4))
        r2p = self.acceleration[a] #+ self.r3() * dt + self.r4() * (dt ** 2 / math.factorial(2)) + self.r5() * (dt ** 3 / math.factorial(3))
        r3p = 0#self.r3() + self.r4() * dt + self.r5() * (dt ** 2 / math.factorial(2))
        r4p = 0#self.r4() + self.r5() * dt
        r5p = 0#self.r5()
        # print("predicted sped", r1p)

        self.position[a] = r0p
        self.velocity[a] = r1p
        self.acceleration[a] = r2p
        new_a = self.calculate_new_acceleration_middle()
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
        self.velocity[a] = r1c
        self.velocities[a].append(r1c)
        self.acceleration[a] = r2c
        self.accelerations[a].append(r2c)
        # print("New sped after gear: ", self.velocity, self.acceleration)

        return r0c

    def r3(self):
        return 0

    def r4(self):
        return 0

    def r5(self):
        return 0


    def F(self, other):
        return self.G * ((self.mass * other.mass) / (self.distance_to(other)*1000)**2)

    def Fxy(self, other):
        f = self.F(other)
        # angle = self.angle_to_object(other)
        x = self.position[0] - other.position[0]
        y = self.position[1] - other.position[1]
        angle = math.atan(abs(x)/abs(y))
        # angle = angle % (math.pi/2)
        fy = f * math.cos(angle)
        fx = f * math.sin(angle)

        if self.position[0] > other.position[0]:
            fx *= -1
        if self.position[1] > other.position[1]:
            fy *= -1
        return fx, fy

    def calculate_new_acceleration(self):
        fx = 0
        fy = 0
        for planet in self.system:
            fxx, fyy = self.Fxy(planet)
            fx += fxx
            fy += fyy
        ax = (fx / self.mass) / 1000
        ay = (fy / self.mass) / 1000
        self.accelerations[0].append(ax)
        self.accelerations[1].append(ay)
        self.acceleration = [ax, ay]
        return self.acceleration

    def calculate_new_acceleration_middle(self):
        fx = 0
        fy = 0
        for planet in self.system:
            fxx, fyy = self.Fxy(planet)
            fx += fxx
            fy += fyy
        ax = (fx / self.mass) / 1000
        ay = (fy / self.mass) / 1000
        return [ax, ay]

    def distance_to(self, other):
        return math.sqrt( (self.position[0]-other.position[0])**2 + (self.position[1]-other.position[1])**2 )

    def print_position(self):
        return '' + str(self.position[0]) + ' ' + str(self.position[1])
    def angle_to_object(self, other):
        x = self.position[0] - other.position[0]
        y = self.position[1] - other.position[1]
        relative_angle = abs(math.atan(abs(y)/abs(x)))

        if (x >= 0 and y >= 0):
            return relative_angle
        elif (x <= 0 and y >= 0):
            return math.pi - relative_angle
        elif (x <= 0 and y <= 0):
            return math.pi + relative_angle
        else:
            return 2 * math.pi - relative_angle

    def launch(self):
        if self.has_launched:
            print("SHIP ALREADY HAS LAUNCHED")
        else:
            print()
            self.has_launched = True
            self.speed += self.earth.orbitalSpeed + self.takeoffSpeed
            self.velocity = self.decompose_speed_earth()
            # print("Launch speed ", self.speed, self.velocity, "  position: ", self.position, self.angular_to_earth)
            # print("launch eart pos", self.earth.position, self.earth.angle_to_sun())



