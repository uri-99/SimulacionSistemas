import math

class Object:

    G = 6.67384 * 10**-11 #N m**2 kg**-2

    def __init__(self, size, mass, position, speed, angularSpeed, t, dt):
        self.radius = size
        self.mass = mass
        self.position = position
        self.angularPos = self.angle_to_sun() #radianes con respecto al sol
        self.speed = speed
        self.angularSpeed = angularSpeed #self.speed_components_to_total(speed)
        self.t = t
        self.dt = dt
        self.distance_to_sun = self.calculate_distance_to_sun(position)


    def F(self, other):
        return self.G * ((self.mass * other.mass) / self.distance_to(other))

    def distance_to(self, other):
        return math.sqrt( (self.position[0]-other.position[0])**2 + (self.position[1]-other.position[1])**2 )

    def changePosition(self):
        self.t += self.dt
        #hacer la formula basica de movimiento circular uniforme, tan los datos en self.angularSpeed etc


    def calculate_distance_to_sun(self, position):
        x = position[0]
        y = position[1]
        return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

    def angle_to_object(self, other):
        x = self.position[0] - other.position[0]
        y = self.position[1] - other.position[1]
        return math.atan(y/x)
    
    def sun_relative_angle_to_object(self, other): #los angulos de cada uno son desde sol, el sol es el 0,0
        return math.fabs(self.angle_to_sun() - other.angle.to_sun()) #acuerdense q el angulo siempre va desde el eje x en sentido antihorario, asi que con modulo y resta todos los casos estan bien

    def angle_to_sun(self):
        x = self.position[0]
        y = self.position[1]
        relative_angle = math.atan(y/x)
        if(x >= 0 and y>= 0):
            return relative_angle
        elif(x <= 0 and y >= 0):
            return math.pi - relative_angle
        elif(x <= 0 and y <= 0):
            return math.pi + relative_angle
        else:
            return 2*math.pi - relative_angle

    def speed_components_to_total(self, velocity):
        vx = velocity[0]
        vy = velocity[1]
        return math.sqrt(math.pow(vx, 2) + math.pow(vy, 2))
    
    def get_angular_position(self):
        return self.position_to_angle(self.position)


