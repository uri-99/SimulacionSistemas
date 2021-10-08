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
                    2 * self.m)  # derivar y evaluar en 0 r: derivo r en dt evalúo t=0, A es amplitud inicial A=1

        self.positions = []
        self.positions.append(self.x)
        self.velocities = []
        self.velocities.append(self.v)
        self.accelerations = []
        self.acc = self.r2()


    def advance(self):
        self.t += self.dt

    def solucion_analitica(self):
        self.x = self.A * math.e ** (-(self.gama / (2 * self.m)) * self.t) * math.cos(
            ((self.k / self.m) - (self.gama ** 2 / (4 * (self.m ** 2)))) ** 0.5 * self.t)
        self.positions.append(self.x)
        return self.x

    def r0(self):
         return self.x
    def r1(self):
        return self.velocities[-1]
        # (self.r0(t+dt) - self.r0(t-dt))/(2*self.dt)
    def r2(self): #acc
        self.acc = (-self.k/self.m)*self.x - (self.gama/self.m) * self.v
        self.accelerations.append(self.acc)
        return self.acc
    def f(self):  # fuerza
        return -self.k * self.x - self.gama * self.r1()
        pass
    def f_verlet(self):  # fuerza
        return -self.k * self.x - self.gama * self.Verlet_v()
        pass


    def Euler_r(self):
        self.x = self.r0() + self.dt*self.r1() + (self.dt**2/(2*self.m))*self.f()
        self.positions.append(self.x)
        self.Euler_v()
        return self.x
    def Euler_v(self):
        self.v = self.r1() + (self.dt/self.m)*self.f()
        self.velocities.append(self.v)
        return self.v


    def Verlet_r(self):
        self.x = 2*self.positions[-1] - self.positions[-2] + (self.dt**2/self.m) * self.f()
        self.positions.append(self.x)
        self.Verlet_v()
        return self.x
    def Verlet_v(self):
        self.v = (self.positions[-1] - self.positions[-3])/(2*self.dt)
        self.velocities.append(self.v)
        return self.v

#listo verlet

    def calculateAcceleration(self, x, v): #acc
        return (-self.k/self.m)*x - (self.gama/self.m) * v

    def Beeman(self):
        # if type==1: #ver teorica si queres entender este comentario
        #     x = self.x+ self.v*self.dt + ((2/3)*self.r2() - (1/6)*self.accelerations[-2])*self.dt**2
        #     v = self.v + ((1/3)*self.calculateAcceleration(x, self.v) ...)
        # elif type==2:
        x = self.x + self.r1() * self.dt + (2/3)*self.r2()*self.dt**2 - (1/6)*self.accelerations[-2]*self.dt**2
        v_predicted = self.r1() + (3/2) * self.accelerations[-1]*self.dt - (1/2)*self.accelerations[-2]*self.dt
        a_calculated = self.calculateAcceleration(x, v_predicted)
        v_corrected = self.v + (1/3)*a_calculated*self.dt + (5/6)*self.accelerations[-1]*self.dt - (1/6)*self.accelerations[-2]*self.dt
        # else:
        #     exit("wrong beeman type")

        self.x = x
        self.positions.append(x)
        self.v = v_corrected
        self.velocities.append(v_corrected)
        return x

#listo Beeman

    def calculateForce(self, x, v):
        return -self.k * x - self.gama * v

    def r3(self):
        return (-self.k / self.m) * self.v - (self.gama / self.m) * self.acc

    def r4(self):
        return (-self.k/self.m)* self.acc - (self.gama/self.m) * self.r3()

    def r5(self):
        return (-self.k/self.m)* self.r3() - (self.gama/self.m) * self.r4()

    def Gear(self):
        dt = self.dt
        r0p = self.r0() + self.r1()*dt + self.r2()*(dt**2/math.factorial(2)) + self.r3()*(dt**3/math.factorial(3)) + self.r4()*(dt**4/math.factorial(4)) + self.r5()*(dt**5/math.factorial(5))
        r1p = self.r1() + self.accelerations[-1]*dt + self.r3()*(dt**2/math.factorial(2)) + self.r4()*(dt**3/math.factorial(3)) + self.r5()*(dt**4/math.factorial(4))
        r2p = self.accelerations[-1] + self.r3()*dt+ self.r4() * (dt ** 2 / math.factorial(2)) + self.r5() * (dt ** 3 / math.factorial(3))
        r3p = self.r3() + self.r4()*dt + self.r5() * (dt ** 2 / math.factorial(2))
        r4p = self.r4() + self.r5()*dt
        r5p = self.r5()

        f = self.calculateForce(r0p, r1p)
        a = self.calculateAcceleration(r0p, r1p)
        delta_a = a - r2p
        delta_R2 = (delta_a*dt**2)/2

        r0c = r0p + 3/16 * delta_R2
        r1c = r1p + 251/360 * delta_R2 / dt
        r2c = r2p + 1 * (2*delta_R2)/dt**2
        r3c = r3p + 11/18 * (3*2*delta_R2)/dt**3
        r4c = r4p + 1/6 * (4*3*2*delta_R2)/dt**3
        r5c = r5p + 1/60 * (5*4*3*2*delta_R2)/dt**3

        self.x = r0c
        self.positions.append(self.x)
        self.v = r1c
        self.velocities.append(self.v)
        self.acc = r2c
        self.accelerations.append(self.acc)

        r2 = (-self.k / self.m) * self.x
        r3 = (-self.k / self.m) * self.r1()
        r4 = (-self.k / self.m) * r2
        r5 = (-self.k / self.m) * r3

        return r0c

    #listo Gear 5


    # def O(self, deltaT):  # Orden, es a lo sumo de orden deltaT al cubo, error como mucho es deltaT al cubo.
    #     # Sin calcular la O, la funcion te va a quedar con ese error de aproximación
    #     return 0
    #     pass


