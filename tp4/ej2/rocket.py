import math

class Rocket:

    def __init__(self, size, mass, position, speed, angularSpeed, t, dt, system=[]):
        self.radius = size
        self.mass = mass
        self.position = position
        # self.angularPos = self.angle_to_sun(position) #radianes con respecto al sol
        self.speed = speed
        # self.angularSpeed = angularSpeed #self.speed_components_to_total(speed)
        self.t = t
        self.dt = dt
        # self.distance_to_sun = self.calculate_distance_to_sun(position)
        self.system = system
        a_x = []
        a_y = []
        self.accelerations = [a_x, a_y]

    def reachMars(self, Earth, SpacheShip, Mars):
        # si sale ahora, llego a marte? calcular
        return True