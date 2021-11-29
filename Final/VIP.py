#stats fijos siempre

class VIP:

    VIPspeed = 1

    def __init__(self, x, y, size, mass):
        self.x = x
        self.y = y
        self.size = size
        self.mass = mass
        self.isDead = False
        self.hasEscaped = False

    def move(self, dt):
        self.x += self.VIPspeed * dt
        if self.x >= 20:
            self.hasEscaped = True

