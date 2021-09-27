import math


class Particle:
    m = 70  # kg
    k = 10 ** 4  # N/m
    gama = 100  # kg/s
    tf = 5  # s
    dt = 10 ** -4

    def __init__(self, r=1):
        self.A = r
        self.r = r  # check integrity
        self.v = -(self.A * self.gama) / (
                    2 * self.m)  # devrivar y evaluar en 0 r: derivo r en dt evalúo t=0, A es amplitud inicial A=1
        self.t = 0

    def solucion_analitica(self):
        self.r = self.A ** (-(self.gama / (2 * self.m)) * self.t) * math.cos(
            ((self.k / self.m) - (self.gama ** 2 / (4 * self.m ** 2))) ** 0.5 * self.t)

    def ri(self, t):  # pocizión
        return self.A ** (-(self.gama / (2 * self.m)) * self.t) * math.cos(
            ((self.k / self.m) - (self.gama ** 2 / (4 * self.m ** 2))) ** 0.5 * self.t)

    def fi(self, t):  # fuerza
        return -self.k*self.r - self.gama*self.vi
        pass

    def gear(self):  # predictor-corrector orden 5
        pass

    def Beeman(self):
        pass

    def Verlet(self):  # original
        # r(t + deltaT)
        self.r = self.verlet_r(self.t, self.dt)
        # v(t)
        self.v = self.verlet_v(self.t)

        pass

    def verlet_r(self, t, deltaT):
        return 2 * self.ri(t) - self.ri(t - deltaT) + (deltaT ** 2 / self.m) * self.fi(t) + self.O(deltaT ** 4)

    def verlet_v(self, t):
        return ( (self.ri(t+self.dt) - self.ri(t-self.dt)) / (2*self.dt) ) + self.O(self.dt**3)

    def O(self, deltaT):  # Orden, es a lo sumo de orden deltaT al cubo, error como mucho es deltaT al cubo.
        # Sin calcular la O, la funcion te va a quedar con ese error de aproximación
        return 0
        pass


