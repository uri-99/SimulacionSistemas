import math


class Particle:
    m = 70  # kg
    k = 10 ** 4  # N/m
    gama = 100  # kg/s
    tf = 5  # s

    def __init__(self, dt, r=1):
        self.t = 0
        self.dt = dt

        self.A = r
        self.x = r         # A^(-(g/(2m))t) cos((k/m - g^2/(4m^2))^0.5 t
        self.v = -(self.A * self.gama) / (
                    2 * self.m)  # devrivar y evaluar en 0 r: derivo r en dt evalúo t=0, A es amplitud inicial A=1
        self.acc = self.r2()


    def advance(self):
        self.t += self.dt

    def solucion_analitica(self):
        self.x = self.A ** (-(self.gama / (2 * self.m)) * self.t) * math.cos(
            ((self.k / self.m) - (self.gama ** 2 / (4 * self.m ** 2))) ** 0.5 * self.t)
        return self.x

    def r0(self):
         return self.x
    def r1(self):
        pass #return speed mandé mail
    def r2(self): #acc
        self.acc = (-self.k/self.m)*self.x - (self.gama/self.m) * self.v
        return self.acc
    def f(self):  # fuerza
        return -self.k * self.x - self.gama * self.r1()
        pass


    def Euler_r(self):
        self.x = self.r0() + self.dt*self.r1() + (self.dt**2/(2*self.m))*self.f()
        return self.x
    def Euler_v(self):
        self.v = self.r1() + (self.dt/self.m)*self.f()
        return self.v


    def Verlet_r(self, pastPositions):
        self.x= 2*pastPositions[-1] - pastPositions[-2] + (self.dt**2/self.m) * self.f()
        return self.x
    def Verlet_v(self, pastPositions):
        self.v = (pastPositions[-1] - pastPositions[-3])/(2*self.dt)
        return self.v

    def calculateAcceleration(self, x, v): #acc
        return (-self.k/self.m)*x - (self.gama/self.m) * v



    def Beeman(self, pastPositions, pastAcc):
        #x = self.x+ self.v*self.dt + ((2/3)*self.r2() - (1/6)*pastAcc[-2])*self.dt**2
        x = self.x + self.r1() * self.dt + (2/3)*self.r2()*self.dt**2 - (1/6)*pastAcc[-2]*self.dt**2
        v_predicted = self.r1() + (3/2) * self.r2()*self.dt - (1/2)*pastAcc[-2]*self.dt
        a_calculated = self.calculateAcceleration(x, v_predicted)
        v_corrected = self.v + (1/3)*a_calculated*self.dt + (5/6)*self.r2()*self.dt - (1/6)*pastAcc[-2]*self.dt

        self.x = x
        self.v = v_corrected
        return x, a_calculated

    def calculateForce(self, x, v):
        return -self.k * x - self.gama * v

    def Gear(self):
        dt = self.dt
        r0p = self.r0() + self.r1()*dt + self.r2()*(dt**2/math.factorial(2)) + self.r3()*(dt**3/math.factorial(3)) + self.r4()*(dt**4/math.factorial(4)) + self.r5()*(dt**5/math.factorial(5))
        r1p = self.r1() + self.r2()*dt + self.r3()*(dt**2/math.factorial(2)) + self.r4()*(dt**3/math.factorial(3)) + self.r5()*(dt**4/math.factorial(4))
        r2p = self.r2() + self.r3()*dt+ self.r4() * (dt ** 2 / math.factorial(2)) + self.r5() * (dt ** 3 / math.factorial(3))
        r3p = self.r3() + self.r4()*dt + self.r5() * (dt ** 2 / math.factorial(2))
        r4p = self.r4() + self.r5()*dt
        r5p = self.r5()

        f = self.calculateForce(r0p, r1p)
        a = self.calculateAcceleration(r0p, r1p)
        delta_a = a - r2p
        delta_R2 = (delta_a*dt**2)/2

        r0c = r0p + 3/20 * delta_R2
        r1c = r1p + 251/360 * delta_R2 / dt
        r2c = r2p + 1 * (2*delta_R2)/dt**2
        r3c = r3p + 11/18 * (3*2*delta_R2)/dt**3
        r4c = r4p + 1/6 * (4*3*2*delta_R2)/dt**3
        r5c = r5p + 1/60 * (5*4*3*2*delta_R2)/dt**3

        r2 = (-self.k / self.m) * #esto tiene que ser r - r0 pero no tengo la pos eq
        r3 = (-self.k / self.m) * self.r1()
        r4 = (-self.k / self.m) * r2
        r5 = (-self.k / self.m) * r3


    # def O(self, deltaT):  # Orden, es a lo sumo de orden deltaT al cubo, error como mucho es deltaT al cubo.
    #     # Sin calcular la O, la funcion te va a quedar con ese error de aproximación
    #     return 0
    #     pass


