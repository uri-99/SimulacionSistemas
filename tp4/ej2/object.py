import math

class Object:

    G = 6.67384 * 10**-11 #N m**2 kg**-2

    def __init__(self, size, mass, position, speed, t, dt, system=[]):
        self.size = size
        self.mass = mass
        self.position = position
        self.angularPos = self.angle_to_sun(position) #radianes con respecto al sol
        self.speed = speed
        self.angularSpeed = self.speed_to_angular_speed(speed)
        self.t = t
        self.dt = dt
        self.distance_to_sun = self.calculate_distance_to_sun(position)
        self.system = system
        a_x = []
        a_y = []
        self.accelerations = [a_x, a_y]

    def F(self, other):
        return self.G * ((self.mass * other.mass) / self.distance_to(other))

    def distance_to(self, other):
        return math.sqrt( (self.position[0]-other.position[0])**2 + (self.position[1]-other.position[1])**2 )
        
        '''      
    def Beeman(self, coord):
        if coord == "x":
            x=self.position[0]
            v = self.speed[0]
            acc = self.accelerations[0]
        elif coord == "y":
            x = self.position[1]
            v = self.speed[1]
            acc = self.accelerations[1]
        else:
            exit("Wrong Beeman coord param")

        x = x + v*self.dt + ((2/3)*acc[-1] - (1/6)*acc[-2])*self.dt**2
        v = v + ((1/3)*self.calculateAcceleration(x, self.v) ...)*self.dt + (5/6)*acc[-1]self.dt - (1/6)*acc[-2]*self.dt
        
        ''''''
        new_x = x + v*self.dt + (2/3)*acc[-1]*self.dt**2 - (1/6)*acc[-2]*self.dt**2
        v_predicted = self.r1() + (3/2) * acc[-1]*self.dt - (1/2)*acc[-2]*self.dt
        a_calculated = self.calculateAcceleration(x, v_predicted)
        v_corrected = self.v + (1/3)*a_calculated*self.dt + (5/6)*acc[-1]*self.dt - (1/6)*acc[-2]*self.dt

        self.x = x
        self.positions.append(x)
        self.v = v_corrected
        self.velocities.append(v_corrected)
        return x
    '''
        

        
    def changePosition(self):
        self.t += self.dt
        self.calculate_new_acceleration()
        self.Beeman("x")
        self.Beeman("y")

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
        self.accelerations[0].append(self.mass*fx)
        self.accelerations[1].append(self.mass*fy)

    def calculate_distance_to_sun(self, position):
        x = position[0]
        y = position[1]
        return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

    def angle_to_object(self, other):
        self.angle_to_sun()
        other.angle.to_sun()
        return
    

    def angle_to_sun(self):
        x = self.position[0]
        y = self.position[1]
        relative_angle = math.atan(y/x)
        if(x >= 0 and y>= 0)
            return relative_angle
        else if(x =< 0 and y >= 0)
            return 180 - relative_angle
        else if(x =< 0 and y =< 0)
            return 180 + relative_angle
        return 360 - relative_angle

    def speed_to_angular_speed(self, velocity):
        vx = velocity[0]
        vy = velocity[1]
        return math.sqrt(math.pow(vx, 2) + math.pow(vy, 2))
    
    def get_angular_position(self):
        return position_to_angle(self.position)